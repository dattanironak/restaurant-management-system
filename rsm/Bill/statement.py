from django.utils.datetime_safe import datetime

from .models import Bill
from django.shortcuts import render, redirect
from django.utils import timezone


def statement(request) :
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == 'POST' :
<<<<<<< HEAD
                print(request.POST['from_time'], type(request.POST['from_time']))
                from_time = datetime.strptime(request.POST['from_time'], '%Y-%m-%dT%H:%M')
                to_time = datetime.strptime(request.POST['to_time'], '%Y-%m-%dT%H:%M')
                bills = Bill.objects.filter(is_active=False)
                bills_to_send = []
                total = 0
                tz_info = from_time.tzinfo
                print(bills[0].bill_date, type(bills[0].bill_date))
                for bill in bills:
                     if bill.bill_date > from_time and bill.bill_date<to_time:
                         bills_to_send.append(bill)
                         total = total + bill.total
                return render(request, 'displaystatement.html',  {'bills': bills_to_send, 'total': total})
=======
                #print(request.POST['from_time'], type(request.POST['from_time']))
                #from_time = datetime.strptime(request.POST['from_time'], '%y-%m-%dT%H:%M')
                #to_time = datetime.strptime(request.POST['to_time'])
                bills = Bill.objects.filter(is_active=False)
                print(bills[0].bill_date, type(bills[0].bill_date))
                # for bill in bills:
                #     if bill.bill_date:
                #         pass
                return render(request, 'displaystatement.html',  {'bills': bills})
>>>>>>> 673f329fd7fcf909a38534e4fb7b8022537e44f1

            return render(request, 'statement.html')
        else:
            return redirect('/')
    else:
        return redirect('/login')


                # from_time = datetime.strptime('190321 0603', '%d%m%y %H%M')
                # to_time = datetime.strptime('310321 0605', '%d%m%y %H%M')
                #drange= (datetime.datetime.combine(from_time, datetime.time.min), datetime.datetime.combine(to_time, datetime.time.max))

                 #bills = Bill.objects.filter(bill_date=drange)