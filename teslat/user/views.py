from django.shortcuts import render, redirect
from django.views.generic import FormView, UpdateView, TemplateView
from user.forms import SignupForm, ChangeUserForm, ChangePasswordForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from car.models import Order
# Create your views here.
class UserSignupView(FormView):
    form_class = SignupForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account created successfully!')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Sign up'
        return context
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)
    

class UserLoginView(LoginView):
    template_name = 'user/signup.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully!')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Log in'
        return context
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(self.request, 'Logged out successfully!')
        else:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class UserProfileView(UpdateView):
    form_class = ChangeUserForm
    template_name = 'user/profile.html'
    def get_object(self):
        return self.request.user
    

@method_decorator(login_required, name='dispatch')
class UserEditProfileView(UpdateView):
    form_class = ChangeUserForm
    template_name = 'user/edit_profile.html'
    success_url = reverse_lazy('edit_profile')
    def get_object(self):
        return self.request.user
    def form_valid(self, form):
        messages.success(self.request, 'Updated profile successfully!')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update profile'
        return context


@method_decorator(login_required, name='dispatch')
class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'user/change_password.html'
    success_url = reverse_lazy('change_password')
    def form_valid(self, form):
        messages.success(self.request, 'Password changed successfully!')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Change Password'
        return context
    
@method_decorator(login_required, name='dispatch')
class OrderHistoryView(TemplateView):
    template_name = 'user/order_history.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.filter(customer = self.request.user)
        context['orders'] = orders
        return context
