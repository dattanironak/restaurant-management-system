from django.shortcuts import render, redirect
from .models import Menu
from django.contrib import messages


# Create your views here.
def menu(request):
    fullmenu = Menu.objects.filter(is_available=True).order_by('category')
    return render(request, 'menu.html', {'Menu': fullmenu})


def updateMenu(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            fullmenu = Menu.objects.order_by('is_available', 'category', 'item_name')
            return render(request, 'updatemenu.html', {'Menu': fullmenu})
        else:
            return redirect('/menu')
    else:
        return redirect('/login')


def additem(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == 'POST':
                item = Menu()
                item.item_id = request.POST['item_id']
                item.item_name = request.POST['item_name']
                item.category = request.POST['categories']
                item.price = request.POST['price']
                if 'is_available' in request.POST:
                    item.is_available = True
                else:
                    item.is_available = False

                if Menu.objects.filter(item_id=item.item_id).exists():
                    messages.info(request, 'ID Exists.')
                    categories = Menu.categories
                    return render(request, 'additem.html', {'categories': categories})
                if Menu.objects.filter(item_name=item.item_name).exists():
                    messages.info(request, 'Item Exists.')
                    return redirect('/menu/update')
                item.save()

                return redirect('/menu/update')

            else:
                categories = Menu.categories
                return render(request, 'additem.html', {'categories': categories})
        else:
            return redirect('/menu')
    else:
        return redirect('/login')


def updateitem(request, uid):
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == 'POST':
                item = Menu.objects.get(item_id=uid)
                try:
                    check_item = Menu.objects.get(item_name=request.POST['item_name'])
                except Menu.DoesNotExist:
                    check_item = None
                if check_item:
                    if check_item.item_id != uid:
                        messages.info(request, 'Item Name Exists.')
                        return redirect('/menu/update')



                item.item_name = request.POST['item_name']
                item.category = request.POST['categories']
                item.price = request.POST['price']
                if 'is_available' in request.POST:
                    item.is_available = True
                else:
                     item.is_available = False
                item.save()

                return redirect('/menu/update')

            else:
                item = Menu.objects.get(item_id=uid)
                categories = Menu.categories
                name = item.item_name
                return render(request, 'updateitem.html', {'item': item, 'categories': categories})
        else:
            return redirect('/menu/update')

    else:
        return redirect('/login')


def deleteitem(request, did):
    if request.user.is_authenticated:
        if request.user.is_staff:
            item = Menu.objects.get(item_id=did)
            if item:
                item.delete()
            return redirect("/menu/update")
        else:
            return redirect('/menu')
    else:
        return redirect("/login")



def changeavailable(request, cid):
    if request.user.is_authenticated :
        if request.user.is_staff:
            item = Menu.objects.get(item_id=cid)
            if item.is_available:
                item.is_available = False
            else:
                item.is_available = True
            item.save()
            return redirect('/menu/update')
        else:
            return redirect('/menu')
    else:
        return redirect('/login')
