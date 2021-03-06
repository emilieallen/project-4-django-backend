from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied

import jwt

User = get_user_model()

class JWTAuthentication(BasicAuthentication):

    def authenticate(self, request):
        header = request.headers.get('Authorization')

        if not header:
            return None
        if not header.startswith('Bearer'):
            raise PermissionDenied({'detail': 'Invalid Authentication Header'})
        
        token = header.replace('Bearer ', '')

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            print(settings.JWT_SECRET_KEY)
            user = User.objects.get(pk=payload.get('sub'))

        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied({'detail': 'Invalid Token'})
        except User.DoesNotExist:
            raise PermissionDenied({'detail': 'User Not Found'})

        return (user, token)