from django.conf.urls import url

from .views import ChildSiteAddView


urlpatterns = [
    url(
        r'^new/$',
        ChildSiteAddView.as_view(),
        name='add_child_site'
    ),
]
