"""codesnipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import include, path
from core import views
from core.views import SearchResultsView 
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.index, name='home'),
    path('developer/<int:pk>/profile', views.developer_profile, name="developer-profile"),
    path('snippet/<int:pk>/edit', views.edit_snippet, name="edit-snippet"),
    path('snippet/new', views.add_snippet, name="add-snippet"),
    path('snippet/<int:pk>/delete', views.delete_snippet, name="delete-snippet"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # path('accounts/logout/', views.LogoutView, name="logout"),
    path('snippet/<int:pk>/copy', views.copy_snippet, name="copy-snippet"),
    path('profile/<int:pk>/edit', views.edit_profile, name="edit-profile"),
]

if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
