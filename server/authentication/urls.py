from django.conf.urls import url

from .views import ProfileView, ProfileRegister, ProfileLogin

urlpatterns = [
    url(r'^auth/$', ProfileView.as_view(), name='Crud'),
    url(r'^auth/register?$', ProfileRegister.as_view()),
    url(r'^auth/login?$', ProfileLogin.as_view()),
]

