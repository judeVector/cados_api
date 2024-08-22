from django.urls import path

from .views import *

urlpatterns = [
    path("", endpoints, name="endpoint"),
    path("advocates/", advocates_list, name="advocates"),
    # path("advocates/<str:username>", advocate_detail),
    path("advocates/<str:username>", AdvocateDetail.as_view()),
    path("companies/", companies_list, name="companies"),
]
