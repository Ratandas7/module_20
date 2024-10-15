from django.shortcuts import render, redirect
from django.views.generic import DetailView
from car.models import Car, Order
from django.contrib import messages
from car.forms import ReviewForm
# Create your views here.
class CarDetailView(DetailView):
    model = Car
    template_name = 'car/car_details.html'
    slug_field = 'model__slug'
    slug_url_kwarg = 'model_slug'
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        review_form = ReviewForm(data = self.request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.car = self.object
            new_review.save()
            messages.success(self.request, "Your Feedback Added Successfully!")
            return redirect('car_details', model_slug=self.object.model.slug, pk=self.object.pk)
        else:
            return self.get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        reviews = car.reviews.all()
        review_form = ReviewForm()
        context['reviews'] = reviews
        context['review_form'] = review_form        
        return context


def order_now(request, model_slug, id):
    if request.method == 'POST':
        car = Car.objects.get(slug = model_slug, pk = id)
        if car.quantity > 0:
            Order.objects.create(customer = request.user, car = car)
            car.quantity -= 1
            car.save()
            messages.success(request, f"{car.model} purchased successfully!")
            return redirect('order_history')
        else:
            messages.error(request, f"Sorry, {car.model} is out of stock!")
            return redirect('car_details', model_slug = car.model.slug, pk = id)
    else:
        return redirect('home')
    