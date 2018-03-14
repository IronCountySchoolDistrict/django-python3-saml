from django.conf import settings

class SAMLServiceProviderSettings(object):
    contact_info = {
        # Contact information template, it is recommended to suply a
        # technical and support contacts.
        "technical": {
            "givenName": settings.SAML['CONTACT_INFO']['TECHNICAL']['GIVEN_NAME'],
            "emailAddress": settings.SAML['CONTACT_INFO']['TECHNICAL']['EMAIL'],
        },
        "support": {
            "givenName": settings.SAML['CONTACT_INFO']['SUPPORT']['GIVEN_NAME'],
            "emailAddress": settings.SAML['CONTACT_INFO']['SUPPORT']['EMAIL'],
        }
    }

    organization_info = {
        # Organization information template, the info in en_US lang is
        # recommended, add more if required.
        "en-US": {
            "name": settings.SAML['ORGANIZATION_INFO']['EN_US']['NAME'],
            "displayname": settings.SAML['ORGANIZATION_INFO']['EN_US']['DISPLAY_NAME'],
            "url": settings.SAML['ORGANIZATION_INFO']['EN_US']['URL'],
        }
    }

    def __init__(self,
                 debug=False,
                 strict=True,
                 sp_metadata_url=None, sp_login_url=None, sp_logout_url=None, sp_x509cert=None, sp_private_key=None,  # Service provider settings (e.g. us)
                 idp_metadata_url=None, idp_sso_url=None, idp_slo_url=None, idp_x509cert=None, idp_x509_fingerprint=None,  # Identify provider settings (e.g. onelogin)

    ):
        super(SAMLServiceProviderSettings, self).__init__()
        self.settings = default_settings = {
            # If strict is True, then the Python Toolkit will reject unsigned
            # or unencrypted messages if it expects them to be signed or encrypted.
            # Also it will reject the messages if the SAML standard is not strictly
            # followed. Destination, NameId, Conditions ... are validated too.
            "strict": strict,

            # Enable debug mode (outputs errors).
            "debug": debug,

            # Service Provider Data that we are deploying.
            "sp": {
                # Identifier of the SP entity  (must be a URI)
                "entityId": sp_metadata_url,
                # Specifies info about where and how the <AuthnResponse> message MUST be
                # returned to the requester, in this case our SP.
                "assertionConsumerService": {
                    # URL Location where the <Response> from the IdP will be returned
                    "url": sp_login_url,
                    # SAML protocol binding to be used when returning the <Response>
                    # message. OneLogin Toolkit supports this endpoint for the
                    # HTTP-POST binding only.
                    "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
                },
                # Specifies info about where and how the <Logout Response> message MUST be
                # returned to the requester, in this case our SP.
                "singleLogoutService": {
                    # URL Location where the <Response> from the IdP will be returned
                    "url": sp_logout_url,
                    # SAML protocol binding to be used when returning the <Response>
                    # message. OneLogin Toolkit supports the HTTP-Redirect binding
                    # only for this endpoint.
                    "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"
                },
                # Specifies the constraints on the name identifier to be used to
                # represent the requested subject.
                # Take a look on src/onelogin/saml2/constants.py to see the NameIdFormat that are supported.
                "NameIDFormat": "urn:oasis:names:tc:SAML:2.0:nameid-format:unspecified",
                # Usually x509cert and privateKey of the SP are provided by files placed at
                # the certs folder. But we can also provide them with the following parameters
                'x509cert': sp_x509cert,
                'privateKey': sp_private_key
            },

            # Identity Provider Data that we want connected with our SP.
            "idp": {
                # Identifier of the IdP entity  (must be a URI)
                "entityId": idp_metadata_url,
                # SSO endpoint info of the IdP. (Authentication Request protocol)
                "singleSignOnService": {
                    # URL Target of the IdP where the Authentication Request Message
                    # will be sent.
                    "url": idp_sso_url,
                    # SAML protocol binding to be used when returning the <Response>
                    # message. OneLogin Toolkit supports the HTTP-Redirect binding
                    # only for this endpoint.
                    "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"
                },
                # SLO endpoint info of the IdP.
                "singleLogoutService": {
                    # URL Location of the IdP where SLO Request will be sent.
                    "url": idp_slo_url,
                    # SAML protocol binding to be used when returning the <Response>
                    # message. OneLogin Toolkit supports the HTTP-Redirect binding
                    # only for this endpoint.
                    "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"
                },
                # Public x509 certificate of the IdP
                "x509cert": idp_x509cert,
                #   Instead of use the whole x509cert you can use a fingerprint
                #   (openssl x509 -noout -fingerprint -in "idp.crt" to generate it)
                "certFingerprint": idp_x509_fingerprint

            },
            "organization": self.organization_info,
            'contactPerson': self.contact_info,
        }
        if not idp_x509cert:
            del self.settings['idp']['x509cert']
        if not idp_x509_fingerprint:
            del self.settings['idp']['certFingerprint']
