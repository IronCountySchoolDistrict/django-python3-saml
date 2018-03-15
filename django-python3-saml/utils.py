from django.conf import settings
from .saml_settings import SAMLServiceProviderSettings

# Mixin to load saml_settings.py and pass to the view.
# Will create .env to populate these fields dynamically
# and to protect security of the information.
class SAMLSettingsMixin(object):
    def get_saml_settings(self):
        with open(settings.SAML['X509CERT']) as cert:
            x509cert = cert.read()

            return SAMLServiceProviderSettings(
                        # SP settings
                        sp_metadata_url=settings.SAML['SP']['METADATA_URL'],
                        sp_login_url=settings.SAML['SP']['LOGIN_URL'],
                        sp_logout_url=settings.SAML['SP']['LOGOUT_URL'],
                        sp_x509cert=settings.SAML['SP']['X509CERT'],
                        sp_private_key=settings.SAML['SP']['PRIVATE_KEY'],

                        # Idp settings
                        idp_metadata_url=settings.SAML['IDP']['METADATA_URL'],
                        idp_sso_url=settings.SAML['IDP']['SSO_URL'],
                        idp_slo_url=settings.SAML['IDP']['SLO_URL'],
                        idp_x509cert=x509cert,
                        idp_x509_fingerprint=settings.SAML['IDP']['X509_FINGERPRINT'],

                        # Django settings detection
                        debug=settings.DEBUG,
                        strict=settings.DEBUG,

                    ).settings

    # Function that formats the saml request for Django.
    def prepare_from_django_request(self, request):
        saml_request = {
            'https': settings.SAML['HTTPS'],
            'http_host': request.META['HTTP_HOST'],
            'script_name': request.META['PATH_INFO'],
            'get_data': request.GET.copy(),
            'post_data': request.POST.copy()
        }
        if settings.DEBUG:
            saml_request['server_port'] = request.META.get('HTTP_X_FORWARDED_PORT',request.META['SERVER_PORT'])
        return saml_request
