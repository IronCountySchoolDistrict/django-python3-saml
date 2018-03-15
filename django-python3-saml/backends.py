from django.conf import settings
from django.contrib.auth.models import User

class SAMLServiceProviderBackend(object):

    def authenticate(self, request, saml_authentication=None):
        if not saml_authentication:  # Using another authentication method
            return None

        if saml_authentication.is_authenticated():
            attributes = saml_authentication.get_attributes()
            try:
                user = User.objects.get(username=saml_authentication.get_nameid())
            except User.DoesNotExist:
                groups = settings.SAML['NEW_USER']['GROUPS']
                user = User(username=saml_authentication.get_nameid())
                user.set_unusable_password()
                user.first_name = attributes['first_name'][0]
                user.last_name = attributes['last_name'][0]
                user.email = attributes['email'][0]
                user.save()
                if groups:
                    for item in groups:
                        user.groups.add(item)
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
