from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from pytils.translit import slugify

from catalog.models import Product, Contact


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
        context_data['title'] = 'Детальная информация о товаре'

        return context_data


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description',)
    success_url = reverse_lazy('catalog:home.html')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog)
            new_blog.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description',)
    success_url = reverse_lazy('catalog:home.html')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('catalog:home.html', kwargs={'pk': self.object.pk})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    extra_context = {
        'title': 'Детальная информация о товаре'
    }

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        product_item = self.get_object()
        context['blogpost_item'] = product_item
        context['title'] = 'Детальная информация о товаре'
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home.html')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
