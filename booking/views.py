from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from hotel.models import Hotel,HotelFaqs,HotelGallery,HotelFeatures,RoomType,Room,Booking,ActivityLog,StaffOnDuty

# Create your views here.

def check_room_availability(request):
    if request.method == "POST":
        id= request.POST.get('hotel-id')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        adult = request.POST.get('adult')
        children = request.POST.get('children')
        type = request.POST.get('room-type')

        hotel = Hotel.objects.get(id=id)
        room_type= RoomType.objects.get(hotel=hotel, slug=type)
        print("Room type",room_type)
        print("id =====",id)
        print("checkin =====",checkin)
        print("checkout =====",checkout)

        url = reverse("hotel:room_type_detail", args=(hotel.slug, room_type.slug))
        url_with_params= f"{url}?hotel-id={id}&checkin={checkin}&checkout={checkout}&children={children}&room_type={room_type}&adult={adult}"

        return HttpResponseRedirect(url_with_params)