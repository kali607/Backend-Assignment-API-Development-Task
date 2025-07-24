from rest_framework import generics
from .models import BogieChecksheetForm, WheelSpecificationForm
from .serializers import BogieChecksheetFormSerializer, WheelSpecificationFormSerializer


class BogieChecksheetFormAPIView(generics.CreateAPIView):
    """
    API endpoint to submit a new Bogie Checksheet form (POST).
    """
    queryset = BogieChecksheetForm.objects.all()
    serializer_class = BogieChecksheetFormSerializer


class WheelSpecificationFormAPIView(generics.CreateAPIView):
    """
    API endpoint to submit a new Wheel Specification form (POST).
    """
    queryset = WheelSpecificationForm.objects.all()
    serializer_class = WheelSpecificationFormSerializer


class BogieFormListView(generics.ListAPIView):
    """
    API endpoint to list all Bogie Checksheet form entries (GET).
    """
    queryset = BogieChecksheetForm.objects.all()
    serializer_class = BogieChecksheetFormSerializer


class WheelFormListView(generics.ListAPIView):
    """
    API endpoint to list all Wheel Specification form entries (GET).
    """
    queryset = WheelSpecificationForm.objects.all()
    serializer_class = WheelSpecificationFormSerializer
