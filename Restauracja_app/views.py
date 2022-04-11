import datetime
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import UpdateView, DeleteView
from Restauracja_app.forms import Add_CategoryModelForm,\
    Add_MenuModelForm, TableModelForm, CommentsForm, ContactForm
from Restauracja_app.models import Category, Menu, Table, Reserve, Comments, Order
from django.core.mail import send_mail, BadHeaderError

class IndexView(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'Index.html', {'category': category})

class Add_CategoryView(View):
    def get(self, request):
        form = Add_CategoryModelForm()
        return render(request, 'form_category.html', {'form': form})

    def post(self, request):
        form = Add_CategoryModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category')
        else:
            form = Add_CategoryModelForm()
        return render(request, 'form_category.html', {'form': form})


class CategoryView(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'category.html', {'category': category})


class UpdateCategoryView(UpdateView):
    model = Category
    template_name = 'edit_form.html'
    form_class = Add_CategoryModelForm
    success_url = reverse_lazy('category')

class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_form.html'
    success_url = reverse_lazy('category')



class Menu_AddView(View):
    def get(self, request):
        form = Add_MenuModelForm()
        return render(request, 'form_menu.html', {'form': form})

    def post(self, request):
        form = Add_MenuModelForm(request.POST, request.FILES)
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
        comment = Comments.objects.filter(meal=menu)
        form = CommentsForm(initial={'meal': menu})
        return render(request, 'menu_details.html', {'menu': menu, 'comment': comment, 'form': form})
#
    def post(self, request, id):
        menu = Menu.objects.get(id=id)
        comment = Comments.objects.filter(meal=menu)
        form = CommentsForm(initial={'meal': menu})
        if 'vote' in request.POST:
            votes = int(request.POST.get('vote'))
            menu.votes += votes
            menu.save()
            return render(request, 'menu_details.html', {'menu': menu, 'comment': comment, 'form': form})
        if 'dodaj' in request.POST:
            form = CommentsForm(data=request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.menu = menu
                new_comment.save()
                form = CommentsForm(initial={'meal': menu})
            return render(request, 'menu_details.html', {'menu': menu, 'comment': comment, 'form': form})
        return render(request, 'menu_details.html', {'menu': menu, 'comment': comment, 'form': form})


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


class TableListView(View):
    def get(self, request):
        date = datetime.date.today()
        table = Table.objects.all().order_by('number_of_seats')
        for tab in table:
            reservation_dates = [reservation.date for reservation in tab.reserve_set.all()] #dla każdego stolika, wyciągamy listę dat, w których stolik jest zajęty.
            tab.reserved = datetime.date.today() in reservation_dates #sprawdzamy, czy dzisiaj stolik jest zarezerwowany i dodajemy tę informację do obiektu stolika.
        return render(request, 'table_list.html', {'table': table, 'date': date})


class ReserveView(View):
    def get(self, request, id):
        date = datetime.date.today()
        table = Table.objects.get(id=id)
        reservations = table.reserve_set.filter(date__gte=str(datetime.date.today())).order_by('date') #Bierzemy date przyszłych rezerwacji
        return render(request, 'reserve.html', {'table': table, 'reservations': reservations, 'date': date})

    def post(self, request, id):
        table = Table.objects.get(id=id)
        reservations = table.reserve_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        last_name = request.POST.get('last_name')
        date = request.POST.get('date')
        time = request.POST.get('time')

        if Reserve.objects.filter(tables=table, date=date):
            return render(request, 'reserve.html', {'error': 'Stolik jest już zarezerwowany', 'table': table, 'reservations': reservations})

        if date < str(datetime.date.today()):
            return render(request, 'reserve.html', {'error': 'Podana data jest nieprawidłowa', 'table': table, 'reservations': reservations})


        reserve = Reserve()
        reserve.tables = table
        reserve.last_name = last_name
        reserve.date = date
        reserve.time = time
        reserve.save()
        return redirect('table_list')


class Contact_View(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Kontakt"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message']
                }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                    return HttpResponse('Znaleziono nieprawidłowy nagłówek.')
            return redirect("index")
        else:
            form = ContactForm()
            return render(request, "contact.html", {'form': form})

class ReserveList(View):
    def get(self, request):
        reserve = Reserve.objects.all().order_by('time')
        return render(request, 'reserve_list.html', {'reserve': reserve})

class Reserve_realized(UpdateView):
    model = Reserve
    template_name = 'edit_form.html'
    fields = 'realized',
    success_url = reverse_lazy('reserve_list')


class UpdateTableView(UpdateView):
    model = Table
    template_name = 'edit_form.html'
    form_class = TableModelForm
    success_url =  reverse_lazy('table_list')

class DeleteTableView(DeleteView):
    model = Table
    template_name = 'delete_form.html'
    success_url = reverse_lazy('table_list')




class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')





class Order_Details_View(LoginRequiredMixin, View):
    def get(self, request):
        try:
            order = Order.objects.get(user=request.user)
            return render(request, 'order_card.html', {'order': order})
        except ObjectDoesNotExist:
            return redirect("/")

