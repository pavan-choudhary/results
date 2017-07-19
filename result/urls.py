from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name="batchs"),
    url(r'^(?P<batch_id>[0-9]+)/$',views.getsems,name="getsems"),
    url(r'^view_result/$',views.result,name="result"),
]