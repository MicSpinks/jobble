def user_template(request):
    """
    Injects the correct base template depending on the user.
    """
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return {"base_template": "baseA.html"}   # special admin template
        elif getattr(request.user, "role", "").lower() == "recruiter":
            return {"base_template": "baseR.html"}   # recruiter template
        else:
            return {"base_template": "base.html"}    # regular user
    return {"base_template": "base.html"}           # default for anonymous users