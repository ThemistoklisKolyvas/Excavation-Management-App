from rest_framework import serializers
from .models import Excavation, Grave

class ExcavationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excavation
        fields = ['user', 'ditch_number', 'pottery', 'jewellery', 'bones', 'tools', 
                  'small_findings', 'samples', 'east_dimension', 'north_dimension', 
                  'depth', 'graves_found']

class GraveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grave
        fields = ['grave_number', 'comments', 'east_dimension', 'north_dimension', 'depth']
