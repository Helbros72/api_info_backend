from django.urls import path

from about_app.views import AboutApiView
from api_info_app.views import ForeignApiInfoView, SelfIpApiInfoView, HistoryInfoView

urlpatterns = [
    path("foreign/", ForeignApiInfoView.as_view()),
    path("self/", SelfIpApiInfoView.as_view()),
    path("history/", HistoryInfoView.as_view(), name="history"),
    # path("history/<int:user_id>/", HistoryInfoView.as_view(), name="history")
]
