from django.shortcuts import render, redirect

from .models import Car
from .forms import CarForm

from django.contrib import messages

def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
    form = CarForm()
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Form is created")

            return redirect('car-list')
        else:
            print (form.errors)
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)


def car_update(request, car_id):

    car_obj = Car.objects.get(id=car_id)
    form = CarForm(instance=car_obj)
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES or None, instance=car_obj)
        if form.is_valid():
            form.save()

            messages.success(request, "Form is Updated")
            return redirect('car-list')
        else:
            print (form.errors)
    context = {
        "car_obj": car_obj,
        "form": form,
    }
    return render(request, 'update.html', context)


def car_delete(request, car_id):
    car_obj = Car.objects.get(id=car_id)
    car_obj.delete()
    messages.success(request, "Form is deleted")
    return redirect('car-list')
