from django.db import models
from django.urls import reverse

class Service(models.Model):
    img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    title= models.CharField(max_length=150)
    content= models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True)
    #category=models.ForeignKey('Category' , on_delete=models.PROTECT,  verbose_name='Kategori')


    def get_absolute_url(self):
        return reverse('view_service', kwargs={'pk':self.pk})



    def __str__(self):
        return self.title



    class Meta:
        ordering=['-create_at']



class Gallery(models.Model):
    img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    title = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse('view_gallery', kwargs={'pk':self.pk})



    def __str__(self):
        return self.title






class Faq(models.Model):
    title = models.CharField(max_length=150)
    content= models.TextField()


    def get_absolute_url(self):
        return reverse('view_faq', kwargs={'pk':self.pk})



    def __str__(self):
        return self.title




class Company(models.Model):
    title = models.CharField(max_length=150)
    content= models.TextField()
    img = models.ImageField(upload_to='photos/%Y/%m/%d/')


    def get_absolute_url(self):
        return reverse('view_company', kwargs={'pk':self.pk})



    def __str__(self):
        return self.title