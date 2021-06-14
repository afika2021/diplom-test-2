from .models import Category, Product

def category_bar(request):
	categories_b = Category.objects.all()
	products_b = Product.objects.filter(available=True).order_by('-created')[:4]
	return('categories_b': categories_b,
		   'products_b': products_b,)
	