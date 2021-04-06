from rest_framework import viewsets
from .serializers import ccsSerializer
# from .models import Book
from .models import ccsFormData
# from .models import Child
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ccsViewSet(viewsets.ModelViewSet):
    serializer_class = ccsSerializer
    queryset = ccsFormData.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

# class ChildViewSet(viewsets.ModelViewSet):
#         serializer_class = childSerializer
#         queryset = Child.objects.all()
#         authentication_classes = (TokenAuthentication,)
#         permission_classes = (IsAuthenticated,)