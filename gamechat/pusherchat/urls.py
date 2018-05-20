from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^Overwatch/', views.index1, name='Overwatch.html'),
    url(r'^CallofDutyWW2/', views.index4, name='CallofDutyWW2.html'),
    url(r'^TeamFortress2/', views.index2, name='TeamFortress2.html'),
    url(r'^Dota2/', views.index3, name='Dota2.html'),
    url(r'^Fortnite/', views.index5, name='Fortnite.html'),
    url(r'^chat/',views.index6, name='chat.html'),
]