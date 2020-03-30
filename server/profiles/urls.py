from django.conf.urls import url

from .views import PropietarioView, PropietarioRUD, InquilinoView, InquilinoRUD

urlpatterns = [
    url(r'^propietarios/$', PropietarioView.as_view(), name='users_crud'),
    url(r'^propietario/(?P<pk>[-\w]+)$', PropietarioRUD.as_view(), name='users_crud'),
    url(r'^inquilinos/$', InquilinoView.as_view(), name='users_crud'),
    url(r'^inquilino/(?P<pk>[-\w]+)$', InquilinoRUD.as_view(), name='users_crud'),
]

