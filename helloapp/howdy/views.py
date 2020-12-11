from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from howdy.models import Exam

from rest_framework import generics
from .serializers import ShortExamSerializer
from .models import ShortExam


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ShortExam.objects.all()
    serializer_class = ShortExamSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


def home(request):
    result = Exam.objects.all()

    return render(request, 'index.html', {"res":result})


def nav_view(request):
    # return response
    short_data = ShortExam.objects.all()
    return render(request, "short_ans.html", {"sdata":short_data})


