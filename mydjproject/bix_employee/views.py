from django.core.mail import EmailMessage
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

from .forms import empfom
from .models import Employee
# Create your views here.
def display(request):
    return HttpResponse('hello everyone')

def empview(request):
    if request.method == 'POST':
        form = empfom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/created/')
        else:
            print("not valid")
    form = empfom
    return render(request, 'bix_employee.html', {'form': form})


def created(request):
    return HttpResponse("data created")

def search(request):
    if request.method == 'POST':
        your_name = request.POST.get('searchs')
        print(your_name)
        record = {'studentInfo': Employee.objects.all().filter(name=your_name)}
        print(record)
        return render(request, 'register.html', record)

    return render(request, 'search.html', {})

# Today,s day two
def send_mail(request):
    form_class = empfom  # class not a instance
    context = {'form': form_class}

    # POST REQUEST
    if request.method == 'POST':
        form = empfom(request.POST)

        your_name = request.POST['your_name']
        phno = request.POST['your_mobile_no']
        contact_email = request.POST['your_email']
        course = request.POST['your_course']

        subject = "A new contact or lead - {}".format(your_name)
        content = your_name + '\n' + contact_email + '\n' + str(
            phno) + '\n' + course
        email = EmailMessage(subject, content, to=['bix5learning@gmail.com'])
        email.send()
        return HttpResponseRedirect('/submit/')

    return render(request, 'mail.html', context)


def submit(request):
    return HttpResponse("Thank you and Have a great day!!!,I will inform soon")