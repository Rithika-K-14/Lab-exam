from django.shortcuts import render
from .models import trainticket
from django.http import HttpResponseRedirect 
# Create your views here.
def index(request):
    return render(request, 'index.html')

def trainappView(request): #getting entire data from model and passing it to html file
    all_bookings = trainticket.objects.all()
    return render(request, 'booking.html',  {'all_bookings':all_bookings})


def addbooking(request):
    new_booking= trainticket()
    new_booking.Name = request.POST.get('Name')
    new_booking.from1 = request.POST.get('from1')
    new_booking.to1=request.POST.get('to1') 
    new_booking_train_no=request.POST.get('train_no')
    new_booking.save()
    return HttpResponseRedirect('/booking/') 

# Create your views here.
