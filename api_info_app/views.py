from ipaddress import ip_address
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from api_info_app.utils.api_info import get_api_info
from history_app.models import History
from drf_yasg.utils import swagger_auto_schema
from api_info_app.utils.safe_to_history import safe_to_history
from history_app.serializers import HistorySerializer


class ForeignApiInfoView(APIView):

    def post(self, request):
        user_id = request.user.id
        ip_adr = request.data.get("ip")
        answer = get_api_info(ip_adr)
        status = safe_to_history(ip_adr, user_id)
        return Response({"id": user_id, "ip": ip_adr, "answer": answer, "status": status})


class SelfIpApiInfoView(APIView):
    def get(self, request):
        user_id = request.user.id
        self_ip = request.META.get("HTTP_X_FORWARDED_FOR")
        answer = get_api_info(self_ip)
        status = safe_to_history(self_ip, user_id)
        return Response({"ip": self_ip, "answer": answer, "status": status, })


# @method_decorator(csrf_exempt, name="dispatch")
class HistoryInfoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Получение истории",
        responses={200: HistorySerializer(many=True)},
        tags=["История"],
    )
    def get(self, request):
        serialized_history = cache.get("serialized_history")
        if serialized_history is None:
            history = History.objects.all()
            serialized_history = HistorySerializer(history, many=True).data
            cache.set("serialized_history", serialized_history)
        return Response({"history": serialized_history.data})

    @swagger_auto_schema(
        operation_description="Создание записи в истории",
        request_body=HistorySerializer,
        responses={201: HistorySerializer()},
        tags=["История"],
    )
    def post(self, request):
        """
        Создает новую запись в истории
        """
        serializer = HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# class UserProfileView(generics.RetrieveAPIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         user_id = request.user.id
#         return Response({"user_id": user_id, "username": request.user.username})
