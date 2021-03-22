from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Bill, BillMenu
from menu.models import Menu
from django.utils import timezone

# Create your views here.

def bills(request):
    if request.user.is_authenticated :
        if request.user.is_staff:
            try:
                active_tables = Bill.objects.filter(is_active=True)
                active_table_no = {bill.table_no for bill in active_tables}
            except ObjectDoesNotExist :
                active_tables = None

            for table in active_tables:
                table.is_active = False

            rang = range(0,18)
            return render(request, 'bills.html', {'active_tables' : active_tables, 'rang': rang, 'active_table_no':active_table_no})
        else :
            return redirect('/')
    else :
        return redirect('/login')


def newbill(request, table_no = 0) :
    if request.user.is_authenticated :
        if request.user.is_staff :
                try:
                    bill=Bill.objects.get(table_no=table_no, is_active=True)
                except ObjectDoesNotExist:
                    bill = Bill()
                    bill.table_no = table_no
                    bill.bill_date = timezone.now()
                    bill.save()

                except MultipleObjectsReturned:
                    messages.info("Something seriosly went Wrong. Connnect ASAP.")
                    return redirect("/")

                return redirect("/bill/updatebill/" + str(bill.table_no))
        else :
            return redirect('/')
    else :
        return redirect('/login')


def updatebill(request, table_no=0, update_id=None) :  # update_id is ID of BillMenu model if particular item
    if request.user.is_authenticated :
        if request.user.is_staff :
            if request.method == 'POST':

                #-------------------------------------------------------------------------------------------------------
                #           If request is post means it is coming from update bill and coming for update item in bill
                #-------------------------------------------------------------------------------------------------------

                try:
                    bill = Bill.objects.get(table_no=table_no, is_active =True)
                except ObjectDoesNotExist:
                    bill = None
                    messages.info(request, "Something went wrong. line 65")
                    return redirect('/bill')

                if 'update_from_web_id' in request.POST :
                    up_id = request.POST['update_from_web_id']
                    item = BillMenu.objects.get(id=up_id)
                else :
                    item = BillMenu()
                    item.bill_id = bill
                try :
                    item_for_instance = Menu.objects.get(item_id=request.POST['item_id'])
                except ObjectDoesNotExist :
                    messages.info(request, "Something went wrong. line 77")
                    return redirect('/bill')
                except MultipleObjectsReturned:
                    messages.info(request, "Something went wrong.line 80")
                    return redirect('/bill')

                item.item_id = item_for_instance
                item.item_name = item_for_instance.item_name
                item.item_price = request.POST['price']
                item.quantity = request.POST['quantity']
                item.item_total = int(item.item_price) * int(item.quantity)
                item.save()
            else:
                bill = None

            # -------------------------------------------------------------------------------------------------------
            #   Either request is post or no request, we have to return update bill page. This Part is doing returning.
            # -------------------------------------------------------------------------------------------------------
            if not bill:

                try:
                    bill = Bill.objects.get(table_no=table_no, is_active =True)

                except ObjectDoesNotExist:
                    bill = None
                    messages.info(request, "Something went wrong. line 102")
                    return redirect('/bill')
                except MultipleObjectsReturned:
                    messages.info(request, 'Something seriosly went wrong.')
                    return redirect('/bill')

            try :
                items = BillMenu.objects.filter(bill_id=bill.id)
                bill.total = 0
                for item in items :
                    bill.total = bill.total + item.item_total
                bill.save()

            except ObjectDoesNotExist :
                items = None
            try :
                to_update_item = BillMenu.objects.get(id=update_id)
            except ObjectDoesNotExist :
                to_update_item = None


            menu = Menu.objects.filter(is_available=True)

            return render(request, 'updatebill.html',
                          {'bill' : bill, 'items' : items, 'menu' : menu, 'to_update_item' : to_update_item})

        else :
            return redirect('/')
    else :
        return redirect('/login')


def deleteitem(request, delete_id, bill_id) :
    if request.user.is_authenticated :
        if request.user.is_staff :
            item = BillMenu.objects.get(id=delete_id)
            item.delete()

            #
            #
            #
            # Have to check how to impliment this url
            #

            return redirect('/bill/updatebill' + str(bill_id))
        else :
            return redirect('/')
    else :
        return redirect('/login')


def print(request, bid) :
    if request.user.is_authenticated :
        if request.user.is_staff :
            bill = Bill.objects.get(id=bid)
            bill.is_printed = True

            ### Print Function will be placed here

            bill.save()
            return redirect('/bill/updatebill' + str(bill.table_no))
        else :
            return redirect('/')
    else :
        return redirect('/login')


def finish(request, bid) :
    if request.user.is_authenticated :
        if request.user.is_staff :
            bill = Bill.objects.get(id=bid)
            bill.is_active = False
            bill.save()
            return redirect('/bill')
        else :
            return redirect('/')
    else :
        return redirect('/login')
