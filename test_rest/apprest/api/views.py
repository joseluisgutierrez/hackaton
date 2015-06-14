from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apprest.models import Hijo,Padre
from django.shortcuts import get_object_or_404
from apprest.api.serializers import HijoSerializer,PadreSerializer,PadreHyperSerializer
# Create your views here.

class HijoVista(APIView):
	serializer_class = HijoSerializer
	def get(self,request,id=None,format=None):
		if id != None:
			hijos = get_object_or_404(Hijo,pk=id)
			many=False
		else:
			hijos = Hijo.objects.all()
			many = True
		response = self.serializer_class(hijos, many=many)
		return Response(response.data)

hijos = HijoVista.as_view()

class PadreVista(APIView):

	serializer_class = PadreSerializer

	def get(self,request,id=None,format=None):
		if id != None:
			padres = get_object_or_404(Padre,pk=id)
			many=False
		else:
			padres = Padre.objects.all()
			many = True
		response = self.serializer_class(padres,many=many)
		return Response(response.data)

padres = PadreVista.as_view()