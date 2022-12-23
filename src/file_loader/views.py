from django.shortcuts import render
from .loader import upload_files
from .constants import (
    pareto_front_file_name,
    requirements_file_name,
    stakeholders_file_name
)

# Create your views here.
def upload_view(request):
    if request.method == "POST":
        files = request.FILES.getlist("files")
        upload_files(files)
        
    return render(request, 'file_loader/upload.html', {
        "pareto_front_file_name": pareto_front_file_name,
        "requirements_file_name": requirements_file_name,
        "stakeholders_file_name": stakeholders_file_name
    })
