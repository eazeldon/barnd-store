# TEST-from django.http import HttpResponse

# TEST-def home(request):
# TEST- return HttpResponse('WELCOME AGAIN LOL!!!')

# -set up home page here -go to templates home.html
from django.shortcuts import render
from store.models import Product, ReviewRating


def home(request):
    products = Product.objects.all().filter(is_available=True)

    # Get the reviews to home page
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(
            product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)
