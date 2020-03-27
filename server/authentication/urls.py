from django.conf.urls import url

from .views import ProfileView, ProfileRegister, ProfileLogin

urlpatterns = [
    url(r'^profiles/$', ProfileView.as_view(), name='Crud'),
    url(r'^profile/?$', ProfileRegister.as_view()),
    url(r'^profile/login?$', ProfileLogin.as_view()),
]
