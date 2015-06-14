from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from apprest.models import Hijo,Padre
from rest_framework import serializers

class HijoSerializer(ModelSerializer):
	class Meta:
		model = Hijo
		fields = ('dni', 'nombre', 'apellido','genero','direccion','fechaNaci')

class PadreSerializer(ModelSerializer):
	Shijos = HijoSerializer(many = False, read_only = True)
	class Meta:
		model = Padre
		fields = ('dni', 'nombres', 'apellidos','Shijos')
		

class PadreHyperSerializer(HyperlinkedModelSerializer):
	Shijos = serializers.HyperlinkedRelatedField(
		view_name = 'padres',
		lookup_field = 'id',
		
		read_only = True,

		)
	class Meta:
		model = Padre
		fields = ('dni', 'nombres', 'apellidos','Shijos')
		

