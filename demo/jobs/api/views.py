
from rest_framework.views import APIView
from  jobs.models import *
from jobs.api.serializers import jobofferSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

class jobofferListCreateAPIView(APIView):
    def get(self,request):
        job=joboffer.objects.all()
        serial=jobofferSerializer(job,many=True)
        return Response(serial.data)

    def post(self,request):
        add=jobofferSerializer(data=request.data)
        if add.is_valid():
            add.save()
            return Response(add.data,status=status.HTTP_200_OK)
        return Response(add.errors,status=status.HTTP_404_NOT_FOUND)

class jobofferDetailAPIView(APIView):
    def getobject(self,pk):
        job=get_object_or_404(joboffer,pk=pk)
        return  job

    def get(self,request,pk):
        job=get_object_or_404(joboffer,pk=pk)
        serial=jobofferSerializer(job)
        return Response(serial.data)

    def put(self,request,pk):
        job=self.getobject(pk)
        serial=jobofferSerializer(job,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors,status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        job=self.getobject(pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



