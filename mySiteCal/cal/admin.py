from django.contrib import admin
from .models import Service,Gallery,Faq,Company


# Register your models here.

 

class ServiceAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'img', 'create_at', 'updated_at', 'is_published','price')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class GalleryAdmin (admin.ModelAdmin):
    list_display = ('id', 'title','img')
    list_display_links = ('id', 'title')
    
class FaqAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class CompanyAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'content','img')
    list_display_links = ('id', 'title','img')
    search_fields = ('title', 'content')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Faq,FaqAdmin)
admin.site.register(Company,CompanyAdmin)
