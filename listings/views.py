from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def index(request):

    #listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)                  #get how many pages
    page = request.GET.get('page')                      #currency page
    Paged_listings = paginator.get_page(page)           #currency qs

    context = {
        'listings' : Paged_listings,
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):

    return render(request, 'listings/listing.html')


def search(request):

    return render(request, 'listings/search.html')


