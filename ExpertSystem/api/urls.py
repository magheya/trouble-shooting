from django.urls import path
from .views import ProblemView

urlpatterns=[
    path('problem/<int:pk>/',ProblemView.as_view())
]


