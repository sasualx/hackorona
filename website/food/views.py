from django.shortcuts import render
from django.views.generic import TemplateView
from website.food.models import Food
# Create your views here.

class FoodView(TemplateView):
    title = "Food"
    template  = 'main_page.html'

    def get(self, request):
        context = {
            'items': Food.objects.all()
        }

        return render(request, self.template, context)
