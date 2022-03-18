from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import UpdateView, DeleteView

from Restauracja_app.forms import Add_CategoryModelForm, Add_MenuModelForm
from Restauracja_app.models import Category, Menu


class IndexView(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'Index.html', {'category': category})

class Add_CategoryView(View):
    def get(self, request):
        form = Add_CategoryModelForm
        return render(request, 'form_category.html', {'form': form})

    def post(self, request):
        form = Add_CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
        return render(request, 'form_category.html', {'form': form})


class CategoryView(View):
    def get(self, request):
        category = Category.objects.all()
        menu = Menu.objects.all()
        return render(request, 'category.html', {'category': category, 'menu': menu})


class UpdateCategoryView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'edit_form.html'
    success_url = reverse_lazy('category')

class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_form.html'
    success_url = reverse_lazy('category')



class Menu_AddView(View):
    def get(self, request):
        form = Add_MenuModelForm
        return render(request, 'form_menu.html', {'form': form})

    def post(self, request):
        form = Add_MenuModelForm(request.POST)
        if form.is_valid():
            save = form.save()
            return redirect(reverse('menu_list', args=(save.category.slug,)))
        return render(request, 'form_menu.html', {'form': form})


class Menu_listView(View):
    def get(self, request, slug):
        menu = Menu.objects.filter(category__slug=slug)
        return render(request, 'menu_list.html', {'menu': menu})


class Menu_Details(View):
    def get(self, request, id):
        menu = Menu.objects.get(id=id)
        return render(request, 'menu_details.html', {'menu': menu})
#
    def post(self, request, id):
        if 'vote' in request.POST:
            menu = Menu.objects.get(id=id)
            votes = int(request.POST.get('vote'))
            menu.votes += votes
            menu.save()
            return render(request, 'menu_details.html', {'menu': menu})
#         if 'dodaj' in request.POST:
#             form = CommentForm(request.POST or None)
#             if form.is_valid():
#                 form.save()
#
#             return render(request, 'menu_details.html', {'form': form})




class UpdateMenuView(UpdateView):
    model = Menu
    template_name = 'edit_form.html'
    form_class = Add_MenuModelForm
    def get_success_url(self):
        menu = self.object
        return reverse_lazy('menu_list', kwargs={'slug': menu.category.slug})

class DeleteMenuView(DeleteView):
    model = Menu
    template_name = 'delete_form.html'
    def get_success_url(self):
        menu = self.object
        return reverse_lazy('menu_list', kwargs={'slug': menu.category.slug})