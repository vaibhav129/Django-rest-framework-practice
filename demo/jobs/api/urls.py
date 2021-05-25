from django.urls import path
from jobs.api.views import jobofferListCreateAPIView,jobofferDetailAPIView

urlpatterns=[
    path("jobs/",jobofferListCreateAPIView.as_view(),name="joblist"),
    path("jobs/<int:pk>",jobofferDetailAPIView.as_view(),name="jobdetail"),
]