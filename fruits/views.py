from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fruits
from .forms import FruitForm


def index(request):
    fruits = Fruits.objects.all()
    return render(request, 'fruits.html', {'fruits': fruits})


def create(request):
    if request.method == 'GET':
        form = FruitForm()
        data = {
            'form': form
        }

        return render(request, 'create.html', data)
    if request.method == 'POST':

        form = FruitForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            print('ok')
        return redirect('index')
