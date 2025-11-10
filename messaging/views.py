from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def recruiter_messages(request):
    if request.user.role != "recruiter":
        return redirect("home")  # block users from recruiter page

    inbox = Message.objects.filter(receiver=request.user).order_by('-sent_at')
    sent = Message.objects.filter(sender=request.user).order_by('-sent_at')
    form = MessageForm(request.POST or None, user=request.user)

    if request.method == "POST" and form.is_valid():
        msg = form.save(commit=False)
        msg.sender = request.user
        msg.save()
        return redirect('messaging:recruiter_inbox')

    return render(request, "messaging/recruiter_messages.html", {
        "inbox": inbox, "sent": sent, "form": form
    })


@login_required
def user_messages(request):
    if request.user.role != "user":
        return redirect("home")  # block recruiters from user page

    inbox = Message.objects.filter(receiver=request.user).order_by('-sent_at')
    sent = Message.objects.filter(sender=request.user).order_by('-sent_at')
    form = MessageForm(request.POST or None, user=request.user)

    if request.method == "POST" and form.is_valid():
        msg = form.save(commit=False)
        msg.sender = request.user
        msg.save()
        return redirect('messaging:user_inbox')

    return render(request, "messaging/user_messages.html", {
        "inbox": inbox, "sent": sent, "form": form
    })
