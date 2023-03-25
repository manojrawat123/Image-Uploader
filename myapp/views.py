from django.shortcuts import render,  HttpResponseRedirect
from myapp.models import Image
from myapp.forms import ImageForm

# Create your views here.
def home_page(request):
    if request.method == "POST":
        forms = ImageForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect("/")
    forms = ImageForm()
    img = Image.objects.all()
    return render(request, "myapp/index.html", {"forms": forms, "img": img})

def delete_page(request, pk):
    if request.method == "POST":
        delImg = Image.objects.get(id = pk)
        delImg.delete()
        return HttpResponseRedirect("/")
    return HttpResponseRedirect("/")
