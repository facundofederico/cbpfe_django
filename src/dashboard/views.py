from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'dashboard/home.html', {})