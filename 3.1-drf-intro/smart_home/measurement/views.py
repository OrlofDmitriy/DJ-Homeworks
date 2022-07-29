# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, SensorSerializer


class SensorsList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def put(self, request, pk):
        sensor = self.get_object()
        serializer = MeasurementSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(sensor.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        sensor = self.get_object()
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeasurementDetail(RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def put(self, request, pk=None):
        measurement = self.get_object()
        serializer = MeasurementSerializer(measurement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        measurement = self.get_object()
        measurement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)