# Copy SAML setting variable into settings
# Set up django-environ by the instructions
# https://github.com/joke2k/django-environ


import os
import sys
import environ

# Three folder back (/a/b/c/ - 3 = /)
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
