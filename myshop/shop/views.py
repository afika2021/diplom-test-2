from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Category, Product, Comment
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, SearchForm
import difflib
from orders.models import Order


def product_list(request, category_slug=None):
    form_s = SearchForm() 
    query = None 
    category = None
    categories_b = Category.objects.all()
    products_b = Product.objects.filter(available=True).order_by('-created')[:4]
    categories = Category.objects.all()
    product = Product.objects.filter(available=True).order_by('slug')
    if 'query' in request.GET: 
        form_s = SearchForm(request.GET) 
        if form_s.is_valid(): 
            query = form_s.cleaned_data['query']
            product = Product.objects.filter(name__contains=query) 
    paginator = Paginator(product, 30)
    page = request.GET.get('page') 
    product_add = ""
    try:  
        products = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        products = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        products = paginator.page(paginator.num_pages)    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = product.filter(category=category)
        paginator = Paginator(product, 30)
        page = request.GET.get('page') 
        try:  
          products = paginator.page(page)  
        except PageNotAnInteger:  
            # Если страница не является целым числом, поставим первую страницу  
          products = paginator.page(1)  
        except EmptyPage:  
            # Если страница больше максимальной, доставить последнюю страницу результатов  
          products = paginator.page(paginator.num_pages)

    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'page': page,
                   'categories': categories,
                   'products': products,
                    'categories_b': categories_b,
                   'products_b': products_b,
                    'cart_product_form': cart_product_form,
                    'form_s': form_s, 
                   'query': query
                     })




def product_base(request):
    category = None
    categories_b = Category.objects.all()
    products_b = Product.objects.filter(created=timezone.now()).order_by('-created')[:4]

    return render(request,
                  'shop/base.html',
                  {
                   'categories_b': categories_b,
                   'products_b': products_b
                  })




def product_detail(request, id, slug):
    category = None
    categories_b = Category.objects.all()
    products_b = Product.objects.filter(available=True).order_by('-created')[:4]
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.product = product
            form.save()
        
    comments = Comment.objects.filter()
    form = CommentForm()
    cart_product_form = CartAddProductForm()
    
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form,
                                                        'categories_b': categories_b,
                   'products_b': products_b,
                   'comments': comments,
                   'form': form
                   })


def product_main(request, category_slug=None):
    category = None
    categories_b = Category.objects.all()
    products_b = Product.objects.filter(available=True).order_by('-created')[:4]
    
    categories = Category.objects.all()
    product = Product.objects.filter(available=True).order_by('-created')
    paginator = Paginator(product, 6)
    page = request.GET.get('page') 
    try:  
        products = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        products = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        products = paginator.page(paginator.num_pages)    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/main.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'categories_b': categories_b,
                   'products_b': products_b})

def product_new(request, category_slug=None):
    
    category = None
    categories_b = Category.objects.all()
    products_b = Product.objects.filter(available=True).order_by('-created')[:4]
    categories = Category.objects.all()
    product = Product.objects.filter(available=True).order_by('-created')
    paginator = Paginator(product, 30)
    page = request.GET.get('page') 
    product_add = ""
    try:  
        products = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        products = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        products = paginator.page(paginator.num_pages)    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = product.filter(category=category)
        paginator = Paginator(product, 30)
        page = request.GET.get('page') 
        try:  
          products = paginator.page(page)  
        except PageNotAnInteger:  
            # Если страница не является целым числом, поставим первую страницу  
          products = paginator.page(1)  
        except EmptyPage:  
            # Если страница больше максимальной, доставить последнюю страницу результатов  
          products = paginator.page(paginator.num_pages)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/new.html',
                  {'category': category,
                   'page': page,
                   'categories': categories,
                   'products': products,
                    'categories_b': categories_b,
                   'products_b': products_b,
                    'cart_product_form': cart_product_form
                                                       
                     })


def product_delivery(request):
  category = None
  categories_b = Category.objects.all()
  products_b = Product.objects.filter(available=True).order_by('-created')[:4]
  return render(request,
                'shop/product/delivery.html',
                {
                'category':category,
                 'categories_b': categories_b,
                   'products_b': products_b,
                })

def product_inform(request):
  product = Product.objects.all()
  return render(request,
                'shop/product/inform.html',
                {
                'product':product
                })

def product_shop_i(request):
  product = Product.objects.all()
  return render(request,
                'shop/product/shop_i.html',
                {
                'product':product
                })