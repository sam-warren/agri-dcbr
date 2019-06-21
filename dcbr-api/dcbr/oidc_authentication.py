from mozilla_django_oidc.auth import OIDCAuthenticationBackend


class AdminOIDCAB(OIDCAuthenticationBackend):
    """
    Custom authentication class for django-admin.
    """

    def verify_claims(self, claims):
        verified = super(AdminOIDCAB, self).verify_claims(claims)
        is_admin = "admin" in claims.get("roles", [])
        return verified and is_admin

    def create_user(self, claims):
        user = super(AdminOIDCAB, self).create_user(claims)

        old_username = user.username
        user.username = claims.get("sub", old_username)
        user.first_name = claims.get("given_name", "")
        user.last_name = claims.get("family_name", "")
        user.email_address = claims.get("email", "")
        user.is_staff = True
        user.save()

        return user

    def update_user(self, user, claims):
        user.first_name = claims.get("given_name", "")
        user.last_name = claims.get("family_name", "")
        user.email_address = claims.get("email", "")
        user.save()

        return user
