from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/', views.index, name='index'),
    path('single-product/<slug>/', views.single_product, name='single_product'),
    path('toys/', views.toys, name='toys'),
    path('about-us/', views.about, name='about'),
    path('gift-items/', views.gift_items, name='gift_items'),
    path('electric-items/', views.electric_items, name='electric_items'),
    path('household-items/', views.household_items, name='household_items'),
    path('furniture-items/', views.furniture_items, name='furniture_items'),
    path('stationary_items/', views.stationary_items, name='stationary_items'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
