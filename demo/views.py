from rest_framework import viewsets
from .serializers import ccsSerializer, childrenSerializer, parentSerializer, eceSerializer
# from .models import Book
from .models import ccsFormData, children, parent,ece
# from .models import Child
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ccsViewSet(viewsets.ModelViewSet):
    serializer_class = ccsSerializer
    queryset = ccsFormData.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class childrenViewSet(viewsets.ModelViewSet):
        serializer_class = childrenSerializer
        queryset = children.objects.all()
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)


class parentViewSet(viewsets.ModelViewSet):
    serializer_class = parentSerializer
    queryset = parent.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class eceViewSet(viewsets.ModelViewSet):
    serializer_class = eceSerializer
    queryset = ece.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)