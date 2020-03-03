from django.core.exceptions import PermissionDenied
import functools


class ViewAuthorizedMixin(object):

    def has_permissions(self):
        exist = {x: False for x in self.permissions}
        for rp in self.request.user.profile.role.privileges.filter(privilege__in=self.permissions):
            exist[rp.privilege] = True
        return functools.reduce(lambda a, b: a and b, exist.values())

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise PermissionDenied(f"{request.method} {request.path}")
        return super(ViewAuthorizedMixin, self).dispatch(request, *args, **kwargs)
