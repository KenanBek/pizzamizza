"""pizzamizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.utils.translation import ugettext as _

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from pizza import views as pizza_api_views

router = routers.DefaultRouter()
router.register(r'pizzas', pizza_api_views.PizzaViewSet)
router.register(r'orders', pizza_api_views.OrderViewSet)

urlpatterns = [
    # Static home page with links (see settings.TEMPLATES conf)
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    # Link to administration
    url(r'^admin/', admin.site.urls),
    # Link to docs
    url(r'^docs/', include_docs_urls(
        title=_('Pizza Mizza API'),  # Title for the doc website
        description=_('RESTful API for Pizza Mizza')  # Desc for the doc website
    )),
    # Link to API itself
    url(r'^api/', include(router.urls)),
]
