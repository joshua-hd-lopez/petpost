from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, FormView
# from .forms import Forms

from .utils import load, save, upload




class ListView(TemplateView):
    
    
    
    template_name = 'petlist.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pets'] = load()
        context['forms'] = Forms()
        return context




class AddView(FormView):
    template_name = 'petlist.html'
    form_class = Forms
    success_url= reverse_lazy('pets:list')

    def form_valid(self, form):
        photo = self.request.FILES['photo']
        img = upload_to_s3(photo, photo.name)

        pet = {
            "name": form.cleaned_data['name'],
            "age": form.cleaned_data['age'],
            "breed": form.cleaned_data['breed'],
            "image": img
        }
        pets = load()
        pets.append(pet)
        save_pets(pets)

        return super().form_valid(form)

