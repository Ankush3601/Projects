from django.shortcuts import render
from.forms import ContactForm
from.models import Contact
from.functions import handle_fileupload
from django.http import HttpResponse
# Create your views here.
def cnt(request):

    if request.method == "POST":
        frm = ContactForm(request.POST,request.FILES)
        if frm.is_valid():
            t = Contact()
            t.name = frm.cleaned_data["name"]
            t.email = frm.cleaned_data["email"]
            t.password = frm.cleaned_data["password"]
            t.age = frm.cleaned_data["age"]
            t.income = frm.cleaned_data["income"]
            t.dateofbirth = frm.cleaned_data["dateofbirth"]
            t.is_married = frm.cleaned_data["is_married"]
            t.memberships = frm.cleaned_data["memberships"]
            t.photo = request.FILES["photo"]
            t.save()
            handle_fileupload(request.FILES["photo"])
            return HttpResponse("Data Saved")
    else:
        frm=ContactForm()
        return render(request, "Contact.html", {"form":frm})