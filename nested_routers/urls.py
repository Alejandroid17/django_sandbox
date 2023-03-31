from atexit import register
from rest_framework_nested import routers
from .api import DomainViewSet, NameserverViewSet, ExtensionDomainViewSet, ExtensionNameserverViewSet
from django.urls import include, path
from rest_framework_extensions.routers import ExtendedSimpleRouter


router = routers.SimpleRouter()
router.register(r'domains', DomainViewSet)

domains_router = routers.NestedSimpleRouter(router, r'domains', lookup='domain')
domains_router.register(r'nameservers', NameserverViewSet, basename='domain-nameservers')

extension_router = ExtendedSimpleRouter()
extension_router.register(r'domains', ExtensionDomainViewSet, basename='domain').register(r'nameservers', ExtensionNameserverViewSet, basename='domains-nameserver', parents_query_lookups=['domain'])

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(domains_router.urls)),
    path('extension/', include(extension_router.urls)),
]