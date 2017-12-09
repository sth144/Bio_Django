from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import form.views
import reversecomplement.views

# Examples:
# url(r'^$', 'engine.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', include('data.urls')),
    url(r'^form', form.views.HomeView.as_view(), name='form'),
    url(r'^reversecomplement', reversecomplement.views.HomeView.as_view(), name='form'),
    url(r'^admin/', include(admin.site.urls)),
]
