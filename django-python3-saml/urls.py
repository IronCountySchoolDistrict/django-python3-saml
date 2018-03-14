from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views
from .views import MetadataView, CompleteAuthenticationView, InitiateAuthenticationView

urlpatterns = [
    url(r'^initiate-login/$', InitiateAuthenticationView.as_view(), name="saml_login_initiate"),
    url(r'^complete-login/$', csrf_exempt(CompleteAuthenticationView.as_view()), name="saml_login_complete"),
    url(r'^metadata/$', MetadataView.as_view(), name="saml_metadata"),
]
