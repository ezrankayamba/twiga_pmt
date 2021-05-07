class MenuAuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.menus = [
            {'privilege': 'view.dashboard', 'name': 'Dashboard', 'url_name': 'dashboard-home'},
            {'privilege': 'view.map', 'name': 'Map', 'url_name': 'dashboard-map'},
            {'privilege': 'view.projects', 'name': 'Projects', 'url_name': 'projects-home'},
            {'privilege': 'view.setups', 'name': 'Setups', 'url_name': 'setups-home'},
            {'privilege': 'view.users', 'name': 'Users', 'url_name': 'users-list'},
            {'privilege': 'view.roles', 'name': 'Roles', 'url_name': 'role-list'},
            {'privilege': 'change.mypassword', 'name': 'Change My Password', 'url_name': 'users-change-password'},
        ]

    def __call__(self, request):
        self.path = request.path
        if not self.path.startswith('/static') and not request.user.is_anonymous and request.user.profile.role:
            privileges = []
            for p in request.user.profile.role.privileges.all():
                privileges.append(p.privilege)
            request.allowed_menus = list(filter(lambda x: x['privilege'] in privileges, self.menus))
        else:
            request.allowed_menus = []
        response = self.get_response(request)
        return response
