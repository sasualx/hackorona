from django.shortcuts import render
from django.views.generic import TemplateView
from website.food.models import Food
from website.food.forms import FoodForm
from django.http import JsonResponse
from website.food.models import Food
# Create your views here.

class FoodView(TemplateView):
    title = "Food"
    template  = 'main_page.html'

    def get(self, request):
        context = {
            'items': request.user.food_set.all()
        }

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
            request.user.food_set.create(
                    name=form_data['name'],
                    number=form_data['number'],
                    unit=form_data['unit'],
                    date_purchased=form_data['date_purchased'],
                    date_expiry=form_data['date_expiry'],
                    status=form_data['status'],
                    use_before=form_data['use_before'],
                    )


        return render(request, self.template)