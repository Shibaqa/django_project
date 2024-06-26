from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contact, Version


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_formset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = version_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = version_formset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


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

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object
