from django.urls import path

from measurement.views import SensorsList, SensorView, MeasurementView, MeasurementDetail

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsList.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('measurements/<pk>/', MeasurementDetail.as_view()),
]
