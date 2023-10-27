from django.urls import path, include
from .views import *
from .models import *


urlpatterns = [
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('categories/<slug:cat_name>', CategoryView, name='category'),
    path('create_category/', CreateCategoryView.as_view(), name='createcategory'),
    path('product/<slug:prod_id>', DetailProductView , name='product'),
    path('create_product', CreateProductView.as_view(), name='createproduct')
]
