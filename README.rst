===================
Django-python3-saml
===================

Django-python3-saml is a Django app designed to allow plug & play SAML authentication setup for any Python 3 enabled Django instance.

Setup
-----------

1. Create .env file in the same folder as settings.py if one does not already exist.
2. Copy the template below into the .env::

    # Fill out all that apply.
    # On True or False pick the one that applies.

    # Redirect URL passed to the next parameter.
    LOGIN_REDIRECT_URL=""

    # Absolute Path to X509CERT file location.
    X509CERT=""

    # HTTPS setting
    HTTPS=True or False

    # Service Provider Information
    SP_METADATA_URL=""
    SP_LOGIN_URL=""
    SP_LOGOUT_URL=""
    SP_X509CERT=""
    SP_PRIVATE_KEY=""

    # Identity Provider Information
    IDP_METADATA_URL=""
    IDP_SSO_URL=""
    IDP_SLO_URL=""
    IDP_X509_FINGERPRINT=""

    # New User Groups expects a list.
    # The list must contain a string with the Group Name.
    # If no groups to be assigned leave list blank.
    NEW_USER_GROUPS=[]

    # New Users setup
    ACTIVE_STATUS=True or False
    STAFF_STATUS=True or False

    # Contact Information Technical
    CI_TECH_GIVEN_NAME=""
    CI_TECH_EMAIL=""

    # Contact Information Support
    CI_SUPPORT_GIVEN_NAME=""
    CI_SUPPORT_EMAIL=""

    # Organizational Information EN_US
    ORG_NAME=""
    ORG_DISPLAY_NAME=""
    ORG_HOME_URL=""

3. Copy the template below into settings.py::

    # Set up django-environ by the instructions
    # https://github.com/joke2k/django-environ
    # if the project has a different .env package
    # simply change the env("variable") to package format

    import os
    import sys
    import environ

    # Three folder back (/config/settings/.env - 3 = /)
    # This should be walked back to the project's root (e.g. where manage.py exists)
    root = environ.Path(__file__) - 3

    # Initialize root function
    PROJECT_ROOT = root()

    # Initialize Env function
    env = environ.Env()

    # Reads the .env file
    env.read_env()

    # Set the system path to the base application folder
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

    # SAML variable houses all .env variables in a single location.
    # All variable requests in the module will pull from these settings.
    # The .env file is used for security and should not be committed.
    SAML = {
        'LOGIN_REDIRECT': env("LOGIN_REDIRECT_URL"),
        'X509CERT': env("X509CERT"),
        'HTTPS': 'on' if env("HTTPS") else 'off',
        'SP': {
            'METADATA_URL': env("SP_METADATA_URL"),
            'LOGIN_URL': env("SP_LOGIN_URL"),
            'LOGOUT_URL': env("SP_LOGOUT_URL"),
            'X509CERT': env("SP_X509CERT"),
            'PRIVATE_KEY': env("SP_PRIVATE_KEY"),
        },
        'IDP': {
            'METADATA_URL': env("IDP_METADATA_URL"),
            'SSO_URL': env("IDP_SSO_URL"),
            'SLO_URL': env("IDP_SLO_URL"),
            'X509_FINGERPRINT': env("IDP_X509_FINGERPRINT"),
        },
        'NEW_USER': {
            'GROUPS': env("NEW_USER_GROUPS"),
            'ACTIVE': env("ACTIVE_STATUS"),
            'STAFF': env("STAFF_STATUS"),
        },
        'CONTACT_INFO': {
            'TECHNICAL': {
                'GIVEN_NAME': env("CI_TECH_GIVEN_NAME"),
                'EMAIL': env("CI_TECH_EMAIL"),
            },
            'SUPPORT': {
                'GIVEN_NAME': env("CI_SUPPORT_GIVEN_NAME"),
                'EMAIL': env("CI_SUPPORT_EMAIL"),
            }
        },
        'ORGANIZATION_INFO': {
            'EN-US': {
                'NAME': env("ORG_NAME"),
                'DISPLAY_NAME': env("ORG_DISPLAY_NAME"),
                'URL': env("ORG_HOME_URL"),
            }
        }
    }

4. Add 'django-python3-saml' to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django-python3-saml',
    ]

5. Include the dango-python3-saml URLconf into project urls.py like this::

    url(r'^saml/', include('django-python-3-saml.urls')),

6. Once the urls have been included as above the SP url paths should be as the following example::

    https://example.com/saml/initiate-login/
    https://example.com/saml/complete-login/
    https://example.com/saml/metadata/

7. Add 'django-python3-saml.backends.SAMLServiceProviderBackend' to AUTHENTICATION_BACKENDS like this::

    AUTHENTICATION_BACKENDS = [
        'django-python3-saml.backends.SAMLServiceProviderBackend',
        ...
    ]

8. Install chosen Identity Provider (IDP) api::

    Example Google api: pip install --upgrade google-api-python-client

Special Thanks
==============

OneLogin's SAML Python Toolkit --> `<https://github.com/onelogin/python3-saml>`
Django-environ --> `<https://github.com/joke2k/django-environ>`
