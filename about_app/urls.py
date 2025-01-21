from django.urls import path


from about_app.views import AboutApiView

urlpatterns = [
    path("", AboutApiView.as_view()),
]


