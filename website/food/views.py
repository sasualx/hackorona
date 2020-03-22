from django.views.generic import TemplateView
from website.food.forms import FoodForm
from website.food.models import Food
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from website.user.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


# Create your views here.

class FoodView(TemplateView):
    title = "Food"
    template  = 'main_page.html'

    def get(self, request):
        context = {
            'items': request.user.food_set.all(),
            'form': FoodForm()
        }

        if (request.GET.get('DeleteButton')):
            request.user.food_set.filter(id = request.GET.get('DeleteButton')).delete()

        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):

        form_data = {
            'name': request.POST.get('name'),
            'number': request.POST.get('number'),
            'unit': request.POST.get('unit'),
            'date_purchased': request.POST.get('date_purchased'),
            'date_expiry': request.POST.get('date_expiry'),
            'status': request.POST.get('status'),
            'use_before': request.POST.get('use_before'),
        }

        if request.method == 'POST':
            form = FoodForm(form_data)
            if form.is_valid():
                request.user.food_set.create(
                    name=form_data['name'],
                    number=form_data['number'],
                    unit=form_data['unit'],
                    date_purchased=form_data['date_purchased'],
                    date_expiry=form_data['date_expiry'],
                    status=form_data['status'],
                    use_before=form_data['use_before'],
                    )

        context = {
            'items': request.user.food_set.all(),
            'form': FoodForm()
        }

        return render(request, self.template, context)

class DeleteFood(DeleteView):
    model = Food
    success_url = reverse_lazy('main_page')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def main_page(request):
    return render(request, 'main_page.html')