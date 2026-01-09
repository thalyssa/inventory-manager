from django.urls import path
from inventory import views

urlpatterns = [
    path('items/', views.itemList.as_view(), name='items_list'),
    path('item/<int:pk>', views.itemDetail.as_view(), name='item_detail'),
    path('item/create', views.newItem.as_view(), name='create_item'),
    path('item/<int:pk>/update',views.updateItem.as_view(), name='update_item'),
    path('item/<int:pk>/delete',views.deleteItem.as_view(), name='delete_item')
]
