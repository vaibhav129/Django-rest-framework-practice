from quotes.models import quote
from quotes.api.serializers import quoteSerializer
from rest_framework import generics,permissions
from quotes.api.permissions import *

class quoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = quote.objects.all().order_by("id")
    serializer_class = quoteSerializer
    permission_classes = [adminuser]

class quoteDetailsCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = quote.objects.all().order_by("id")
    serializer_class = quoteSerializer
    permission_classes = [adminuser]
