from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView
from mainapp.tasks import send_sms_to_users_collections
from mainapp.models import *
from mainapp.forms import *
# from mainapp.task import send_sms_to_users_collections


def url_dispatch(request):
    if request.user.is_authenticated:
        return redirect('home_view')
    return redirect('login_view')


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    # login_url = redirect('login_view')
    model = Contact
    form_class = ContactModelForm
    template_name = 'contact/contact_update.html'
    success_url = reverse_lazy('contact_list_view')
    context_object_name = 'contact'


class ContactCreateView(LoginRequiredMixin, CreateView):
    # login_url = redirect('login_view')
    model = Contact
    form_class = ContactModelForm
    success_url = reverse_lazy('contact_list_view')


class ContactListView(LoginRequiredMixin, ListView):
    # login_url = redirect('login_view')
    model = Contact
    template_name = 'contact/contact.html'
    context_object_name = 'contact'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ContactListView, self).get_context_data(**kwargs)
        context['contact_form'] = ContactModelForm
        return context


class DealerDeleteView(LoginRequiredMixin, DeleteView):
    # login_url = redirect('login_view')
    model = Dealer
    success_url = reverse_lazy('dealer_list_view')


class DealerCreateView(LoginRequiredMixin, CreateView):
    # login_url = redirect('login_view')
    model = Dealer
    form_class = DealersModelForm
    success_url = reverse_lazy('dealer_list_view')


class DealerUpdateView(LoginRequiredMixin, UpdateView):
    # login_url = redirect('login_view')
    model = Dealer
    form_class = DealersModelForm
    template_name = 'dealers/dealer_update.html'
    success_url = reverse_lazy('dealer_list_view')
    context_object_name = 'dealer'


class DealerListView(LoginRequiredMixin, ListView):
    # login_url = redirect('login_view')
    model = Dealer
    template_name = 'dealers/dealer_list.html'
    context_object_name = 'dealers'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DealerListView, self).get_context_data(**kwargs)
        context['dealer_form'] = DealersModelForm
        return context


class CityListView(LoginRequiredMixin, ListView):
    # login_url = redirect('login_view')
    model = City
    template_name = 'cities/city_list.html'
    context_object_name = 'cities'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CityListView, self).get_context_data(**kwargs)
        context['city_form'] = CityModelForm
        return context


class CityDeleteView(LoginRequiredMixin, DeleteView):
    # login_url = redirect('login_view')
    model = City
    success_url = reverse_lazy('city_list_view')


class CityUpdateView(LoginRequiredMixin, UpdateView):
    # login_url = redirect('login_view')
    model = City
    form_class = CityModelForm
    template_name = 'cities/city_update.html'
    success_url = reverse_lazy('city_list_view')
    context_object_name = 'city'


class CityCreateView(LoginRequiredMixin, CreateView):
    # login_url = redirect('login_view')
    model = City
    form_class = CityModelForm
    success_url = reverse_lazy('city_list_view')


class HomeView(LoginRequiredMixin, ListView):
    model = Collection
    login_url = reverse_lazy('login_view')
    template_name = 'home.html'
    context_object_name = 'collections'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['collection_form'] = CollectionModelForm
        context['collection_title'] = self.request.GET.get('title')
        return context

    def get_queryset(self):
        queryset = Collection.objects.all()
        if self.request.GET.get('title'):
            queryset = queryset.filter(name__icontains=self.request.GET.get('title'))
        return queryset


class CollectionCreateView(LoginRequiredMixin, CreateView):
    # login_url = redirect('login_view')
    model = Collection
    form_class = CollectionModelForm
    success_url = reverse_lazy('home_view')


class SubCollectionUpdateView(LoginRequiredMixin, UpdateView):
    # login_url = redirect('login_view')
    model = SubCollection
    fields = ('name', 'link')
    template_name = 'collections/sub_collection_update.html'
    context_object_name = 'sub_collection'

    def get_success_url(self):
        return reverse_lazy('collection_detail_view', kwargs={'pk': self.object.collection_id})


class CollectionUpdateView(LoginRequiredMixin, UpdateView):
    # login_url = redirect('login_view')
    model = Collection
    form_class = CollectionModelForm
    template_name = 'collections/sub_collection_update.html'
    context_object_name = 'collection'

    def get_success_url(self):
        return reverse_lazy('collection_detail_view', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(CollectionUpdateView, self).get_context_data(**kwargs)
        context['updater'] = "1"
        return context


class CollectionDeleteView(LoginRequiredMixin, DeleteView):
    # login_url = redirect('login_view')
    model = Collection

    def get_success_url(self):
        return reverse_lazy('home_view')


class SubCollectionDeleteView(LoginRequiredMixin, DeleteView):
    # login_url = redirect('login_view')
    model = SubCollection

    def get_success_url(self):
        return reverse_lazy('collection_detail_view', kwargs={'pk': self.object.collection_id})


@login_required
def sub_collection_create_view(request, pk):
    obj = SubCollection.objects.create(
        collection_id=pk,
        name=request.POST.get('name'),
        link=request.POST.get('link')
    )
    send_sms_to_users_collections.delay(obj.id)
    return redirect('collection_detail_view', pk=pk)


class CollectionDetail(LoginRequiredMixin, DetailView):
    # login_url = redirect('login_view')
    model = Collection
    template_name = 'collections/collection_detail.html'
    context_object_name = 'collection'

    def get_context_data(self, **kwargs):
        context = super(CollectionDetail, self).get_context_data(**kwargs)
        context['collection_form'] = CollectionModelForm
        context['sub_collection_form'] = SubCollectionModelForm
        context['sub_collections'] = SubCollection.objects.filter(collection_id=self.kwargs['pk'])
        return context


class UserLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home_view')
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            context = {
                'login_error': "Неверный логин или пароль"
            }
            return render(request, 'login.html', context)
        login(request, user)
        return redirect('home_view')


class UserLogoutView(LoginRequiredMixin, View):
    # login_url = redirect('login_view')

    def get(self, request):
        logout(request)
        return redirect('login_view')