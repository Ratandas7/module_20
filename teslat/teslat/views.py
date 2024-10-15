from django.shortcuts import render
from car.models import Car, Brand, Model

def home(request, model_slug = None, brand_slug = None):
    data = Car.objects.all()
    models = None
    brands = None
    if brand_slug is not None:
        brands = Brand.objects.get(slug = brand_slug)
        data = Car.objects.filter(model__brand = brands)
    if model_slug is not None:
        models = Model.objects.get(slug = model_slug)
        data = Car.objects.filter(model = models)
    

    models = Model.objects.all()
    brands = Brand.objects.all()
    return render(request, 'home.html', {'cars' : data, 'models' : models, 'brands' : brands})