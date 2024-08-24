from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *

urlpatterns = [
    path("healthcheck/", status, name="status"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("advocates/", advocates_list, name="advocates"),
    # path("advocates/<str:username>", advocate_detail),
    path("advocates/<str:username>", AdvocateDetail.as_view()),
    path("companies/", companies_list, name="companies"),
]
