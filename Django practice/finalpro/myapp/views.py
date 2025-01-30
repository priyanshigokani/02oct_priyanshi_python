from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from finalpro import settings
import random

# Create your views here.
def index(request):
    msg=""
    user=request.session.get('user')
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']  

        user=userSignup.objects.filter(username=unm,password=pas)
        userid=userSignup.objects.get(username=unm)
        print("user ID: ",userid.id)
        if user:
            print("Login successful!")
            request.session['user']=unm
            request.session['userid']=userid.id
            return redirect('notes')
        else:
            print("Error! Login failed!")
            msg="Error! Login failed!"

    return render(request,'index.html',{'msg':msg ,'user':user})

def about(request):
    user=request.session.get("user") 
    return render(request,'about.html', {'user':user})

def contact(request):
    user=request.session.get('user')
    if request.method=='POST':
        newcontact=contactForm(request.POST)
        if newcontact.is_valid():
            newcontact.save()
            print("Your data has been submitted!")

            send_mail(
                subject="Thankyou!",
                message=f"Hello User!\n\nThank you for connecting with us!\nWe will contact you.\n\n\Thanks & Regards!\nminji min",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.POST["email"]],
            )

        else:
            print(newcontact.errors)
    return render(request,'contact.html' , {'user':user})

def notes(request):
    msg2 = ''
    user = request.session.get('user')
    userid = request.session.get('userid')
    username = ''
    
    print("User ID from session: ", userid)

    if userid and userSignup.objects.filter(id=userid).exists():
        username = userSignup.objects.get(id=userid).username
        print("Username fetched: ", username)
    else:
        print("User ID not found or invalid!")

    if request.method == 'POST':
        newNote = NotesForm(request.POST, request.FILES)
        if newNote.is_valid():
            newNote.save()
            msg2 = "Your notes have been submitted!"
        else:
            print(newNote.errors)
            msg2 = "Error! Something went wrong..."
    
    return render(request, 'notes.html', {'user': user, 'msg2': msg2, 'username': username})

def profile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    cid=userSignup.objects.get(id=userid)
    print("Current User ID:",cid)
    if request.method=='POST':
        updateReq=updForm(request.POST,instance=cid)
        if updateReq.is_valid():
            updateReq.save()
            request.session.delete()
            return redirect('/')
        else:
            print(updateReq.errors)
            msg="Error!Something went wrong...."
    return render(request,'profile.html',{'user':user,'cid':cid})

def signup(request):
    msg=""
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            global otp
            otp=random.randint(111111,999999)

            sub="Your one time password!"
            msg=f"Hello User!\n\nThanks for registration with us!\n\nFor account verification, Your one time password is :{otp}.\n\nThanks & Regards!\nNotesApp\nPriyanshi Gokani"
            from_email=settings.EMAIL_HOST_USER
            to_email=[request.POST['username']]

            send_mail(subject=sub, message=msg, from_email=from_email, recipient_list=to_email
            )

            newuser.save()
            return redirect('otpverify')
        
        else:
            print(newuser.errors)
            msg="error!Something went wrong... "
            return render(request, 'signup.html',{'msg':msg})

    return render(request,'signup.html')

def userlogout(request):
    logout(request)
    return redirect('/')

def otpverify(request):
    msg=""
    global otp
    if request.method=="POST":
        if request.POST["otp"]==str(otp):
            print("Verification done!")
            return redirect("/")
        else:
            print("Error! Invalid OTP")
            msg="Error!Invalid OTP"
    return render(request,"otpverify.html",{"msg":msg})


