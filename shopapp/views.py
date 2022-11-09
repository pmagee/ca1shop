from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Product, Shop

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'plist.html'
    context_object_name = 'all_ps_list'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'p_detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'p_create.html'
    fields = ['name', 'exp_date', 'shop']

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'p_edit.html'
    fields = ['name']

class SSListView(ListView):
    model = Shop
    template_name = 'ss_list.html'
    context_object_name = 'all_s_list'