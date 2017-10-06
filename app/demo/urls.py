from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView
from .views import UserView
from .views import UserDetailsView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls',  # ADD THIS URL
                           namespace='rest_framework')),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),

    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token),

    url(r'^docs/', include_docs_urls(title='Youtube'))
}

urlpatterns = format_suffix_patterns(urlpatterns)
