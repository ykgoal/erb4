from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


# Create your views here.


def contact(request):

    if request.method == 'POST':

        listing_id = request.POST['listing_id']
        listing_title = request.POST['listing_title']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']


        if request.user.is_authenticated:
            user_id = request.user.id 
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You made an inquiry for this listing !')
                return redirect('/listings/' + listing_id)
            
        contact = Contact(listing=listing_title, 
                        listing_id=listing_id, 
                        name=name, 
                        email=email, 
                        phone=phone, 
                        message=message, 
                        user_id=user_id
                    )
        contact.save()
        '''
        send_mail(
            'Listing Inquiry',
            'Inquiry for ' + listing_title + '.Sign into admin for more info',
            '123@abc.com',
            [realtor_email, 'admin@bcre.com'],
            fail_silently=False,
        )
        '''
        messages.success(request, 'Your request submitted, realtor will get back to you soon.')

    return redirect('/listings/'+listing_id)

