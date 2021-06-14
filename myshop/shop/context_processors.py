from .models import Category, Product
from .forms import SearchForm


def categories_processor(request):
	categories_b = Category.objects.all()
	return {
	'categories_b': categories_b,
	}


def product_processor(request):
	products_b = Product.objects.filter(available=True).order_by('-created')[:4]
	return {
	'products_b': products_b,
	}

def search_form(request):
	form_s = SearchForm() 
	return{
	'form_ss': form_s,
	}