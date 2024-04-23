from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from catalog.models import Product, Contact

# class ProductListView(ListView):
#     model = Product
#     template_name = 'catalog/home.html'
#     extra_context = {
#         'title': 'Best Store Ever'
#     }


class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Best Store Ever'
    }
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        all_products = Product.objects.all()
        context_data['prod_to_display'] = all_products
        return context_data

def home(request):
    all_products = Product.objects.all()
    content = {
        'prod_to_display': all_products,
        'title': 'Best Store Ever'
    }
    return render(request, "catalog/home.html", content)



def contacts(request):
    company_info = Contact.objects.all()
    info_content = {
        'info_list': company_info,
        'title': 'Контакты'
    }
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, "catalog/contacts.html", info_content)

class ProductListView(ListView):
    model = Product
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        one_product = Product.objects.filter(id=self.kwargs.get('pk'))
        context_data['prod_to_display'] = one_product,
        context_data['title'] ='Детальная информация о товаре'

        return context_data

class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description',)
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog)
            new_blog.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description',)
    success_url = reverse_lazy('catalog:home')



class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    extra_context = {
        'title': 'Детальная информация о товаре'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


# def product_detail(request, pk):
#     one_product = Product.objects.filter(id=pk)
#     content = {
#         'prod_to_display': one_product,
#         'title': 'Детальная информация о товаре'
#     }
#     return render(request, "catalog/product_detail1.html", content)


# class ProductsCreateView(CreateView):
#     """
#     класс контроллер приложения каталог
#     шаблон форма добавить продукт
#     """
#     model = Product
#     fields = ('product_name', 'product_description', 'product_image', 'product_category', 'product_price')
#     success_url = reverse_lazy('catalog:list')
#
#
# class ProductsListView(ListView):
#     """
#     Класс контроллер приложения каталог
#     шаблон продукты
#     """
#     model = Product
#     template_name = 'catalog/products_list.html'
#
#
# class ProductsDetailView(DetailView):
#     """
#     Класс контроллер приложения каталог
#     шаблон продукта
#     """
#     model = Product
#     template_name = 'catalog/products_detail.html'
#
# class ProductsUpdateView(UpdateView):
#     """
#     класс контроллер приложения каталог
#     шаблон форма изменить продукт
#     """
#     model = Product
#     fields = ('product_name', 'product_description', 'product_image', 'product_category', 'product_price')
#     success_url = reverse_lazy('catalog:list')
#
#     def get_success_url(self):
#         return reverse('products:detail', args=[self.kwargs.get('pk')])
#
#
# class ProductsDeleteView(DeleteView):
#     """
#     класс контроллер приложения каталог
#     шаблон форма удалить продукт
#     """
#     model = Product
#     success_url = reverse_lazy('catalog:list')
