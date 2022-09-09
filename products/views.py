from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from users.models import User

# Create your views here.
def product_detail_view(request, *args, **kwargs):
	product_object = Product.objects.get(id=request.GET['id'])
	# print(f"request.GET.get('id') - {request.GET.get('id')}")
	# product_object = Product.objects.get(id=request.GET.get('id'))
	print(f'product_detail_view - {product_object}')
	context = {
		'object': product_object
	}
	# print(request.GET['id'])
	return render(request, "products_detail.html", context)


def product_search_view(request, *args, **kwargst):
	if request.GET == {}:
		product_object = Product.objects.get(id=1)
		print(product_object)
	else:
		try:
			product_object = Product.objects.get(id=request.GET['id'])
			product_detail_view(request, product_object)
		except:
			product_object = Product.objects.get(id=1)
		print(product_object)
	context = {
		'object': product_object
	}
	return render(request, "products_search.html", context)

def product_detail_all_view(request):
	product_objects = list(Product.objects.all())
	user_objects	= User.objects.all()
	print(product_objects)
	context = {
		'product': product_objects,
		'user': user_objects
	}
	return render(request, "products_detail_all.html", context)