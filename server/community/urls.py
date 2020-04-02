from django.conf.urls import url

from .views import (
    CommunityView
)

urlpatterns = [
    url(r'^comunidades/$', CommunityView.as_view(), name='List')
]