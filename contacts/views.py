from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Contact
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'contacts/index.html', {
        'contacts': Contact.objects.all()
    })

def view_contact(request,id):
    contact = Contact.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_id = form.cleaned_data['id']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_specialty = form.cleaned_data['specialty']
            new_publication = form.cleaned_data['publication']
            new_email = form.cleaned_data['email']
            new_phone = form.cleaned_data['phone']

            new_contact = Contact(
                id = new_id,
                first_name = new_first_name,
                last_name = new_last_name,
                specialty = new_specialty,
                publication = new_publication,
                email = new_email,
                phone = new_phone,
            )

            new_contact.save()
            return render(request, 'contacts/add.html', {
                'form': ContactForm(),
                'success': True
            })
    else:
        form = ContactForm()
    return render(request, 'contacts/add.html', {
        'form': ContactForm()
    })

def edit(request, id):
    if request.method == 'POST':
        contact = Contact.objects.get(pk=id)
        form = ContactForm(request.POST, instance = contact)
        if form.is_valid():
            form.save()
            return render(request, 'contacts/edit.html', {
                'form': form,
                'success': True
            })
    else:
        contact = Contact.objects.get(pk=id)
        form = ContactForm(instance=contact)
    return render(request, 'contacts/edit.html', {
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        contact = Contact.objects.get(pk=id)
        contact.delete()
    return HttpResponseRedirect(reverse('index'))