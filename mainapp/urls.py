from django.urls import path
from .views import *


urlpatterns = [
    path('', url_dispatch, name="url_dispatcher"),
    path('login/', UserLoginView.as_view(), name="login_view"),
    path('logout/', UserLogoutView.as_view(), name="logout_view"),
    path('home/', HomeView.as_view(), name="home_view"),
    path('contact/', ContactListView.as_view(), name="contact_list_view"),
    path('contact/create/', ContactCreateView.as_view(), name="contact_create_view"),
    path('contact/update/<int:pk>/', ContactUpdateView.as_view(), name="contact_update_view"),
    path('dealer/list_view/', DealerListView.as_view(), name="dealer_list_view"),
    path('dealer/create/', DealerCreateView.as_view(), name="dealer_create_view"),
    path('dealer/update/<int:pk>/', DealerUpdateView.as_view(), name="dealer_update_view"),
    path('dealer/delete/<int:pk>/', DealerDeleteView.as_view(), name="dealer_delete_view"),
    path('city/list_view', CityListView.as_view(), name="city_list_view"),
    path('city/create/', CityCreateView.as_view(), name="city_create_view"),
    path('city/delete/<int:pk>/', CityDeleteView.as_view(), name="city_delete_view"),
    path('city/update/<int:pk>/', CityUpdateView.as_view(), name="city_update_view"),
    path('collection/create/', CollectionCreateView.as_view(), name="collection_create_view"),
    path('collection/update/<int:pk>/', CollectionUpdateView.as_view(), name="collection_update_view"),
    path('collection/delete/<int:pk>/', CollectionDeleteView.as_view(), name="collection_delete_view"),
    path('collection/detail/<int:pk>/', CollectionDetail.as_view(), name="collection_detail_view"),
    path('sub_collection/create/<int:pk>/', sub_collection_create_view, name="sub_collection_create_view"),
    path('sub_collection/update/<int:pk>/', SubCollectionUpdateView.as_view(), name="sub_collection_update_view"),
    path('sub_collection/delete/<int:pk>/', SubCollectionDeleteView.as_view(), name="sub_collection_delete_view"),
]
