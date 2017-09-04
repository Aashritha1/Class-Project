from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from onlineapp import views
from onlineapp.classviews import Createcollege,Create,Delete,Update,CreateDetail
from rest_framework_jwt.views import obtain_jwt_token

app_name='onlineapp'
urlpatterns = [
    url(r'^testsession', views.testsession),
    url(r'^testcookies', views.testcookies),
    url(r'^collegeinfo1',views.collegeinfo),
    url(r'collegeinfo/$', Createcollege.as_view(), name='collegeinfo'),
    url(r'^Create/$',Create.as_view()),
    url(r'^CreateDetail/(?P<pk>[0-9]+)/$',CreateDetail.as_view()),
    url(r'^Update/(?P<pk>[0-9]+)/$', Update.as_view()),
    url(r'^Delete/(?P<pk>[0-9]+)/$', Delete.as_view()),
    url(r'^marksinfo/(?P<c_id>[0-9]+)/$',views.marksinfo,name="marksinfo"),
    url(r'^$', views.index),
    url(r'^collegelist/$', views.college_list,name="collegelist"),
    url(r'^collegelist/(?P<pk>[0-9]+)/$', views.college_detail),
    url(r'^collegelist/(?P<pk>[0-9]+)/students/$', views.college_stud_detail),
    url(r'^studentlist/$', views.student_list),
    url(r'^studentlist/(?P<pk>[0-9]+)/$', views.student_detail),
    url(r'^studentlist/(?P<pk>[0-9]+)/marks/$', views.student_marks_detail),
    url(r'^login/', obtain_jwt_token),
]
