from django.urls import path
from .views import display,empview,created,search,send_mail,submit


urlpatterns = [
    path('display001/',display),
    path('empview/',empview),
    path('created/',created),
    path('search/',search),
    path('send_mail/',send_mail),
    path('submit/',submit),
]