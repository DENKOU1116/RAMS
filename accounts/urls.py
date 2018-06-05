from django.conf.urls import url
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/$', login,
        {'template_name': 'accounts/login.html'},
        name='login'),
    url(r'^logout/$', logout,
        {'template_name': 'accounts/logged_out.html'},
        name='logout')
]

