from django.conf.urls import url
from template_project import views

app_name = 'template_project'

urlpatterns = [
    url(r'^relative/$',views.relative, name = 'relative'),
    url(r'^other/$',views.other, name = 'other'),
]
