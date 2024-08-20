from django.contrib import admin
from hotel.models import Hotel,HotelFaqs,HotelGallery,HotelFeatures,RoomType,Room,Booking,ActivityLog,StaffOnDuty

# Register your models here.

class HotelGalleryInline(admin.TabularInline):
    model = HotelGallery

class HotelFeauturesInline(admin.TabularInline):
    model= HotelFeatures

class HotelAdmin (admin.ModelAdmin):
    inlines = [HotelGalleryInline,HotelFeauturesInline]
    list_display=['thumbnail','name','user','status']
    prepopulated_fields= {"slug":("name",)}

admin.site.register(Hotel,HotelAdmin)
admin.site.register(HotelFaqs)
admin.site.register(HotelGallery)
admin.site.register(HotelFeatures)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(ActivityLog)
admin.site.register(StaffOnDuty)