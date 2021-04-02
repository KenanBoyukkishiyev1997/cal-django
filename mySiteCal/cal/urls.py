from django.urls import path

from .views import *


urlpatterns =[
    # path('',index,name='home'),
    path('', ServiceCal.as_view()),
    path('',GalleryCal.as_view()),
    path('',FaqCal.as_view()),
    path('',CompanyCal.as_view()),
    # path('category/<int:category_id>/', CategoryNews.as_view(),name='category'),
    # path('news/<int:pk>/', ViewsNews.as_view(), name='view_news'),
    # path('news/add_news/', AddNews.as_view(), name='add_news'),
]