from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_of_post, name='list_of_post'),
    url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.list_of_post_by_category, name='list_of_post_by_category'),
    url(r'^(?P<slug>[-\w]+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^blog/references/social_net/Twitter.html$', views.twitter_reference, name='twitter_reference'),
    url(r'^blog/references/social_net/RSS.html$', views.rss_reference, name='rss_reference'),
    url(r'^blog/references/archives.html$', views.archives_reference, name='archives_reference'),
    url(r'^blog/references/contact.html$', views.contact_reference, name='contact_reference'),
    url(r'^blog/references/about.html$', views.about_reference, name='about_reference'),
]
