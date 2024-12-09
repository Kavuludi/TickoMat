from django.shortcuts import render, redirect

from TickoApp.forms import ContactForm,BookingForm
from TickoApp.models import Client, Admin, Contact, Booking


# Create your views here.
def base(request):
    return render(request,'base.html')
def index(request):
    return render(request,'index.html')

def fleet(request):
    return render(request,'fleet-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def routes(request):
    return render(request,'routes.html')

def adminlogin(request):
    return render(request,'adminlogin.html')

def contact(request):
    if request.method == "POST":
        mycontact=Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],

        )
        mycontact.save()
        return redirect('/showcontact')
    else:
        return render(request,'contact.html')

def showcontact(request):
    customercontacts=Contact.objects.all()
    return render(request,'showcontact.html',{'contacts':customercontacts})

def delete1(request,id):
    customcontacts=Contact.objects.get(id=id)
    customcontacts.delete()
    return redirect('/showcontact')

def edit1(request,id):
    editcontacts=Contact.objects.get(id=id)
    return render(request,'editcontact.html',{'contacts':editcontacts})

def update1(request,id):
    updatecontact=Contact.objects.get(id=id)
    myform=ContactForm(request.POST,instance=updatecontact)
    if myform.is_valid():
        myform.save()
        return redirect('/showcontact')
    else:
        return render(request,'editcontact.html')
def gallery(request):
    return render(request,'gallery.html')

def buses(request):
    return render(request,'buses.html')

def register(request):
    if request.method == 'POST':
        clients=Client(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password']
        )
        clients.save()
        return redirect('login')
    else:
        return render(request,'register.html')



def login(request):
    return render(request,'login.html')

def logout(request):
    logout(request)
    return redirect('login')

def clientbookings(request):
    if request.method == 'POST':
        if Admin.objects.filter(
                username=request.POST['username'],
                password=request.POST['password']
        ).exists():
            return render(request,'showbooking.html')
        else:
            return render(request,'adminlogin.html')
    else:
        return render(request,'adminlogin.html')

def booking(request):
    if request.method == "POST":
        customerbooking=Booking(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            depart=request.POST['depart'],
            destination=request.POST['destination'],
            bus=request.POST['bus'],
            seatno=request.POST['seatno']
        )
        customerbooking.save()
        return redirect('/showbooking')
    else:
        return render(request, 'booking.html')

def mybookings(request):
    allbookings=Booking.objects.all()
    return render (request,'showbooking.html',{'bookings':allbookings})

def delete(request,id):
    delbooking=Booking.objects.get(id=id)
    delbooking.delete()
    return redirect('/showbooking')

def trips(request):
    return render(request,'trips.html')

def managetrips(request):
    return render(request,'managetrips.html')

def editbooking(request,id):
    edityourbooking=Booking.objects.get(id=id)
    return render(request,'editbooking.html',{'yourbooking':edityourbooking})

def updatebooking(request,id):
    updatebookinginfo=Booking.objects.get(id=id)
    bookingform=BookingForm(request.POST,instance=updatebookinginfo)
    if bookingform.is_valid():
        bookingform.save()
        return redirect('/showbooking')
    else:
        return render(request,'editbooking.html')