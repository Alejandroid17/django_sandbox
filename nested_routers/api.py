from cgitb import lookup
from dataclasses import fields
from rest_framework import viewsets
from .models import Domain, Nameservers
from rest_framework import serializers
from rest_framework_extensions.mixins import NestedViewSetMixin


class DomainSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Domain
        fields = ['pk', 'host']

class NameserversSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nameservers
        fields = ['pk', 'label']



class DomainViewSet(viewsets.ModelViewSet):
    serializer_class = DomainSerializer
    queryset = Domain.objects.all()

    lookup_field = 'pk'

class NameserverViewSet(viewsets.ModelViewSet):
    serializer_class = NameserversSerializer
    
    def get_queryset(self):
        return Nameservers.objects.filter(domain=self.kwargs['domain_pk'])


class ExtensionDomainViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = DomainSerializer
    queryset = Domain.objects.all()

    lookup_field = 'pk'

class ExtensionNameserverViewSet(ExtensionDomainViewSet):
    serializer_class = NameserversSerializer
    
    def get_queryset(self):
        return Nameservers.objects.all()
    