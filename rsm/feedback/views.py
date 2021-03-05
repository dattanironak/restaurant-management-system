from django.shortcuts import render,redirect
from .models import feedback
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages



# Create your views here.
def displayfeedback(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            fd = feedback.objects.all()
            return render(request, 'displayfeedback.html', {'fd': fd})
        else:
            return redirect('/feedback')
    else:
        return redirect('/login')



def newfeedback(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('feedback_desc') and request.POST.get('ratings'):
                fd = feedback()
                fd.feedback_desc = request.POST['feedback_desc']
                fd.ratings = request.POST['ratings']
                now = timezone.now()
                fd.date = now
                fd.save()

            return redirect('/')

        else:
            return render(request, 'feedback.html')
    else:
        messages.info(request, 'Please log in to give feedback.')
        return redirect('/login')


