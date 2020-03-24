from django.shortcuts import render, redirect
from .models import Oas
from .forms import OasCreate
from django.http import HttpResponse

# Create your views here.
def index(request):

    shelf = Oas.objects.all()
    return render(request, 'Oas/oas.html', {'shelf': shelf})

def upload(request):
    upload = OasCreate()
    if request.method == 'POST':
        upload = OasCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'Oas/upload_form.html', {'upload_form':upload})


def update_oas(request, oas_id):
    oas_id = int(oas_id)
    try:
        oas_sel = Oas.objects.get(id = oas_id)
    except Oas.DoesNotExist:
        return redirect('index')
    oas_form = OasCreate(request.POST or None, instance = oas_sel)
    if oas_form.is_valid():
       oas_form.save()
       return redirect('index')
    return render(request, 'oas/upload_form.html', {'upload_form':oas_form})


def delete_oas(request, oas_id):
    oas_id = int(oas_id)
    try:
        oas_sel = Oas.objects.get(id = oas_id)
    except Oas.DoesNotExist:
        return redirect('index')
    oas_sel.delete()
    return redirect('index')

