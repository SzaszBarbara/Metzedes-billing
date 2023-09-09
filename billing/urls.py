from django.urls import path

from billing import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='homepage'),

    path('create_bill/', views.BillCreateView.as_view(), name='create-bill'),
    path('list_of_bills/', views.BillListView.as_view(), name='list-of-bills'),
    path('update_bill/<int:pk>/', views.BillUpdateView.as_view(), name='update-bill'),
    path('delete_bill/<int:pk>/', views.BillDeleteView.as_view(), name='delete-bill'),
    path('details_bill/<int:pk>/', views.BillDetailView.as_view(), name='details-bill'),

    path('create_product_bill/', views.ProductBillCreateView.as_view(), name='create-product-bill'),
    path('list_of_product_bills/', views.ProductBillListView.as_view(), name='list-of-product-bills'),
    path('update_product_bill/<int:pk>/', views.ProductBillUpdateView.as_view(), name='update-product_bill'),
    path('delete_product_bill/<int:pk>/', views.ProductBillDeleteView.as_view(), name='delete-product-bill'),
    path('details_product_bill/<int:pk>/', views.ProductBillDetailView.as_view(), name='details-product-bill'),

    path('create_client/', views.ClientCreateView.as_view(), name='create-client'),
    path('list_of_clients/', views.ClientListView.as_view(), name='list-of-clients'),
    path('update_client/<int:pk>/', views.ClientUpdateView.as_view(), name='update-client'),
    # path('delete_client/<int:pk>/', views.ClientDeleteView.as_view(), name='delete-client'),
    path('details_client/<int:pk>/', views.ClientDetailView.as_view(), name='details-client'),
    path('delete_client/<int:pk>/', views.delete_client, name='delete-client'),

    path('create_product/', views.ProductCreateView.as_view(), name='create-product'),
    path('list_of_products/', views.ProductListView.as_view(), name='list-of-products'),
    path('update_product/<int:pk>/', views.ProductUpdateView.as_view(), name='update-product'),
    # path('delete_product/<int:pk>/', views.ProductDeleteView.as_view(), name='delete-product'),
    path('details_product/<int:pk>/', views.ProductDetailView.as_view(), name='details-product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete-product'),

    path('create_car/', views.CarCreateView.as_view(), name='create-car'),
    path('list_of_cars/', views.CarListView.as_view(), name='list-of-cars'),
    path('update_car/<int:pk>/', views.CarUpdateView.as_view(), name='update-car'),
    path('delete_car/<int:pk>/', views.CarDeleteView.as_view(), name='delete-car'),
    path('details_car/<int:pk>/', views.CarDetailView.as_view(), name='details-car')


]