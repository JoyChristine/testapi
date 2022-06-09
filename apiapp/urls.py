from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('api/merch/',  views.MerchList.as_view()),
    path('api/merch/merch-id/<pk>',views.MerchDescription.as_view())
]