from django.http import HttpResponse

def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, 'role') and request.user.role == role:
                return view_func(request, *args, **kwargs)
            return HttpResponse('Forbidden', status=403)
        return _wrapped_view
    return decorator
