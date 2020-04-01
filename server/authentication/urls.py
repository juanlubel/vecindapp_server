from django.conf.urls import url

from .views import ProfileView, ProfileRUD, ProfileRegister, ProfileLogin

urlpatterns = [
    url(r'^users/$', ProfileView.as_view(), name='List'),
    url(r'^user/(?P<pk>[-\w]+)$', ProfileRUD.as_view(), name='Retrieve_Update_Delete'),
    url(r'^auth/register?$', ProfileRegister.as_view(), name='Create'),
    url(r'^auth/login?$', ProfileLogin.as_view(), name='Authorized_token'),
]

