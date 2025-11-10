from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db import models
from .models import SavedSearch
from messaging.models import Message

User = get_user_model()

@receiver(post_save, sender=User)
def notify_matching_saved_searches(sender, instance, created, **kwargs):
    if instance.role != 'user':
        return
    
    saved_searches = SavedSearch.objects.all()
    
    for search in saved_searches:
        if search.user == instance:
            continue
            
        query = search.query.strip()
        if not query:
            continue
        
        matches = User.objects.filter(
            models.Q(id=instance.id),
            models.Q(role='user')
        ).filter(
            models.Q(username__icontains=query) |
            models.Q(headline__icontains=query) |
            models.Q(skills__icontains=query) |
            models.Q(location__icontains=query)
        ).exists()
        
        if matches:
            # Check for duplicate
            existing = Message.objects.filter(
                sender=instance,
                receiver=search.user,
                content__contains=f"matches your saved search: '{search.name or search.query}'"
            ).exists()
            
            if not existing:
                message_content = f"New match! {instance.username} matches your saved search: '{search.name or search.query}'"
                
                Message.objects.create(
                    sender=instance,
                    receiver=search.user,
                    content=message_content
                )