from django.urls import include, path

from .import views 
 

urlpatterns = [
    path('latest-products/', views.LatestProductList.as_view(), name='latest-product'),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view(), name='product-detail'),

]