from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',

	# common views
	url(r'^$', 'dashboard.views.home', name='home'),
	url(r'^welcome/$', 'dashboard.views.welcome', name='welcome'),
	url(r'^help/$', 'dashboard.views.help', name='help'),
	url(r'^security/$', 'dashboard.views.security', name='security'),

	# userprofile / account
	url(r'^login/$', 'userprofile.views.auth', name='login'),
	url(r'^register/$', 'userprofile.views.register', name='login'),
	url(r'^logout/$', 'userprofile.views.user_logout', name='logout'),
	url(r'^account/settings/$', 'userprofile.views.account_settings', name='account_settings'),
	url(r'^account/password/$', 'userprofile.views.change_password', name='change_password'),
	url(r'^lock/$', 'userprofile.views.lock', name='lock'),
	url(r'^goodbye/$', 'userprofile.views.goodbye', name='goodbye'),

	# support
	url(r'^support/$', 'support.views.support', name='support'),
	#url(r'^support/new/$', 'support.views.support_add_new', name='support_add_new'),
	#url(r'^support/ticket/(?P<ticket_id>\d+)/$', 'support.views.support_view_ticket', name='support_view_ticket'),

	# invoices
	url(r'^invoices/$', 'invoices.views.invoices', name='invoices'),
	#url(r'^invoice/177212(?P<id>\d+)s/$', 'invoices.views.invoice', name='invoice'),

	# private servers
	url(r'^private/servers/$', 'private_servers.views.servers', name='servers'),
	url(r'^private/server/(?P<uuid>[\w\-\.]+)/$', 'private_servers.views.server_detail', name='server_detail'),
	url(r'^server/add/new/$', 'private_servers.views.server_add', name='server_add'),	
	# private storage
	url(r'^private/storage/$', 'private_storage.views.private_storage', name='private_storage'),
	
	# cloud stuff
	url(r'^cloud/software/$', 'cloud_software.views.cloud_software', name='cloud_software'),
	url(r'^cloud/software/add/new/$', 'cloud_software.views.cloud_software_add_new', name='cloud_software_add_new'),
	url(r'^cloud/software/tag/(?P<tag_slug>[\w\-\.]+)/$', 'cloud_software.views.cloud_software_view_tag', name='cloud_software_view_tag'),
	url(r'^cloud/backups/$', 'cloud_backup.views.cloud_backups', name='cloud_backups'),
	url(r'^cloud/storage/$', 'cloud_storage.views.cloud_storage', name='cloud_storage'),
	url(r'^cloud/settings/$', 'userprofile.views.cloud_settings', name='cloud_settings'),

	# TODO URLs from/refferenced in /cloud/storage/
	#
	#/cloud/storage/files/
	#/cloud/storage/dropzone/
	#/cloud/storage/s3/enable/

	# devel
	url(r'^devel/$', 'devel.views.devel', name='devel'),	
	url(r'^devel/(?P<dev>[\w\-\.]+)/$', 'devel.views.devel', name='devel'),
)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.MEDIA_ROOT, #'show_indexes': True,
	}),
)
