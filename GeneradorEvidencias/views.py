from django.shortcuts import render, redirect  # puedes importar render_to_response
from .forms import UploadForm
from .models import  Cliente


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/GeneradorEvidencias/')
    else:
        form = UploadForm()
    return render(request, 'GeneradorEvidencias/upload.html', {'form': form})
'''
def selec_fase(request):
    if request.method == 'POST':
        form = FaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(selec_fase)
    else:
        form = FaseForm()
    return render(request, 'GeneradorEvidencias/upload.html', {'form': form})
'''






