from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, About, Contact
from .forms import ContactForm
# Create your views here.

def home(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'home.html', context)



def single_product(request, slug):
    item = get_object_or_404(Item, slug=slug)
    context = {'item': item}
    return render(request, 'single_product.html', context)


def toys(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'toys.html', context)


def about(request):
    about = About.objects.all()
    context = {'about': about}
    return render(request, 'about.html', context)

def gift_items(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'gift.html', context)

def electric_items(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'electric.html', context)

def household_items(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'household.html', context)

def furniture_items(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'furniture.html', context)

def stationary_items(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'stationary.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
        context = {'form': form}
        return render(request, 'contact.html', context)
    return redirect('contact')
