from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import ProductCategory, Product, Basket
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'products/index.html'                                                                           #Передается страница для рендеринга(отображение)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()                                                          #Выполняется код, возвращается словарь, который мы можем дополнить своим контекстом
        context['title'] = 'Store - Каталог'
        return context


class ProductsListView(ListView):
    model = Product                                                                                                 #автоматически создает product_list, в котором все объекты Product
    template_name = "products/products.html"
    paginate_by = 3
    def get_queryset(self):                                                                                         # переопределяем функцию, изначально возвращает Product.objects.all()

        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')

        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super(ProductsListView,self).get_context_data()
        context['title'] = "Store - Каталог"
        context['categories'] = ProductCategory.objects.all()

        return context
#

@login_required
def basket_add(request, product_id):

    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, products=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, products=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
