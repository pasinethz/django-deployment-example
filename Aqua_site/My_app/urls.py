from django.conf.urls import url
from My_app import views

app_name='My_app'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'about/',views.about,name='about'),
    url(r'contact/',views.contact,name='contact'),
]