from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .favorit import Favorit
from .forms import FavoritAddProductForm


@require_POST
def favorit_add(request, product_id):
    favorit = Favorit(request)
    product = get_object_or_404(Product, id=product_id)
    form = FavoritAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        favorit.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('favorit:favorit_detail')

def favorit_remove(request, product_id):
    favorit = Favorit(request)
    product = get_object_or_404(Product, id=product_id)
    favorit.remove(product)
    return redirect('favorit:favorit_detail')

def favorit_detail(request):
    favorit = Favorit(request)
    return render(request, 'favorit/detail.html', {'favorit': favorit})