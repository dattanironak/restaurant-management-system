from django.shortcuts import render,redirect
from .models import feedback
from django.utils import timezone



# Create your views here.
def displayfeedback(request):
    fd = feedback.objects.all()
    return render(request, 'displayfeedback.html', {'fd': fd})


def newfeedback(request):
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



