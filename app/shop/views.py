from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.views.generic import CreateView,DetailView, ListView
from .models import *
from django.contrib.auth.mixins import PermissionRequiredMixin

class CategoriesListView(ListView):
    model = Category
    template_name = 'shop/categories.html'
    context_object_name = 'cats'
    page_title_name = 'Category'
    


def CategoryView(request,cat_name):
    category = Category.objects.get(name = cat_name)
    try:   
        products = Product.objects.filter(category_id = category.pk)
    except:
        print('error')
        products = None
    return render(request, 'shop/category.html',{'title':cat_name,'products': products} )



class CreateCategoryView(PermissionRequiredMixin, CreateView):
    permission_required = 'category.add_category'
    model = Category
    fields = ['name']
    template_name= 'shop/createcategory.html' 
    success_url = '/'


def DetailProductView(request, prod_id):
    template_name = 'shop/product.html'
    product = get_object_or_404(Product, pk=prod_id)
    comments = ProductComent.objects.filter(product_id = prod_id)
    new_comment = None
    comments_form = ProductCommentForm()
    if request.method == 'POST':
        comments_form = ProductCommentForm(data=(request.POST or None))
        if comments_form.is_valid():   
            data = request.POST.get('comment')
            new_comment = ProductComent.objects.create(product = product, writer = request.user, comment = data)
            return redirect(product.get_absolute_url())
        else:
            comments_form = ProductCommentForm()
    context = {
        'comment_form': comments_form,
        'comments':comments,
        'product': product
    }
    return render(request, template_name, context)

class CreateProductView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_product'
    model = Product
    fields = ['name','price','content','category']
    template_name= 'shop/createproduct.html' 
    success_url = '/'