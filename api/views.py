from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'Hello World'
	})

class Sale(APIView):
	
	def get(self, request, transactionKey, format=None):
		return Response({
			'Hello World'
		})
	
	def post(self, request, format=None):
		pass

	def put(self, request, pk, format=None):
		pass