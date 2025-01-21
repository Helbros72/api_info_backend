from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics

class AboutApiView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        user = request.user
        user_id = request.user.id

        # Determine the username
        if user.is_authenticated:
            username = user.username
            user_id = user.id
        else:
            username = "Anonimus"

        # Return a consistent and meaningful response
        # return Response({"greeting": f"Hello, {username}, UserID: {user_id}"})
        return Response({"greeting": {
                                     "message": "Hello",
                                     "username": username,
                                     "user_id": user_id}
                        })


