from quotes.api.views import *
from django.urls import path
urlpatterns = [
    path("quotes",quoteListCreateAPIView.as_view(),name="list"),
    path("quotes/<int:pk>",quoteDetailsCreateAPIView.as_view(),name="list"),
]