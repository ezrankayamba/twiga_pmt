from functools import wraps
from django.http import HttpResponseRedirect
import functools
from django.core.exceptions import PermissionDenied


def view_authorized(permissions=None):

    def has_permissions(request):
        perms = []
        if permissions is not None:
            perms = permissions
        exist = {x: False for x in perms}
        for rp in request.user.profile.role.privileges.filter(privilege__in=perms):
            exist[rp.privilege] = True
        return functools.reduce(lambda a, b: a and b, exist.values())

    def wrapper(fun):

        def wrapped(request, *args, **kwargs):
            if has_permissions(request):
                return fun(request, *args, **kwargs)
            else:
                raise PermissionDenied(f"{request.method} {request.path}")
        return wrapped
    return wrapper
