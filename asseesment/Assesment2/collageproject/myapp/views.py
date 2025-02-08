from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from collageproject import settings

# Create your views here.
def index(request):
    return render(request, 'index.html')

def usersignup(request):
    msg=''
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()

            sub="Thank you!"
            msg= f"Hi !\n\nThank you for registering with StudyMate We're delighted to have you join us.\n\nIf you need assistance, feel free to contact us at +91 12345 67890 \nBest regards,\nStudy Mate college\n+91 12345 67890 "
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
            

            print('User Created Successfully')
            msg='User Created Successfully'
            return redirect('/')
        else:
            msg='Something went wrong...'
            print(newuser.errors)
    return render(request, 'signup.html', {'msg':msg})

def signin(request):
    msg = ""

    if request.method == 'POST':
        role = request.POST.get('role')
        email = request.POST.get('email')
        pas = request.POST.get('password')

        if not email or not pas or not role:
            msg = "Please fill all the fields"
            print("Please fill all the fields")
        else:
            # Debugging role and credentials
            print(f"Role from form: {role}")
            user = signup.objects.filter(email=email, password=pas, role=role).first()

            if user:
                # Debugging user role from database
                print(f"User role in database: {user.role}")
                
                # Set session variables upon successful login
                request.session['user'] = user.email
                request.session['role'] = user.role

                # Redirect user based on role
                if user.role.lower() == 'student':
                    return redirect('/student')
                elif user.role.lower() == 'teacher':
                    return redirect('/teacher')
                elif user.role.lower() == 'admin':
                    return redirect('/adminn')
                else:
                    msg = "Invalid Role"
                    print("Invalid Role")
            else:
                msg = "Invalid Credentials"
                print("Invalid Credentials")
          
    return render(request, 'signin.html', {'msg': msg})

def student(request):
    user=request.session.get('user')
    sdt=addStu.objects.all()
    return render(request, 'student.html',{'sdt':sdt,'user':user})

def teacher(request):
    user=request.session.get('user')
    tdt=addTea.objects.all()
    return render(request, 'teacher.html',{'tdt':tdt,'user':user})

def base(request):
    return render(request, 'base.html')

def addTEA(request):
    msg=""
    if request.method=='POST':
        newTea=addTeaForm(request.POST)
        if newTea.is_valid():
            newTea.save()
            print('Teacher Added Successfully')
            msg='Teacher Added Successfully'
            return redirect('/teacher')
        else:
            print(newTea.errors)
            msg='Something went wrong...'
    return render(request, 'addTea.html', {'msg':msg})

def addStud(request):
    msg=""
    if request.method=='POST':
        newStu=addStuForm(request.POST)
        if newStu.is_valid():
            newStu.save()
            print('Student Added Successfully')
            msg="Student Added Successfully"
            return redirect('/student')
        else:
            print(newStu.errors)
            msg='Something went wrong...'
    return render(request, 'addStu.html', {'msg':msg})

def adminn(request):
    user=request.session.get('user')
    return render (request, "adminn.html",{'user':user})

def library(request):
    user=request.session.get('user')
    books=addB.objects.all()
    return render (request, "library.html",{'books':books,'user':user})

def addBooks(request):
    msg=""
    if request.method=="POST":
        NBook=aBooks(request.POST,request.FILES)
        if NBook.is_valid():
            NBook.save()
            print("Your book uploaded successfully!")
            msg="Your book uploaded successfully!"
        else:
            print(NBook.errors)
            msg="Error!Something went Wrong.. Please try again"
    return render (request, "addBooks.html",{'msg':msg})

def addEvent(request):
    msg=""
    if request.method=="POST":
        NEve=aEve(request.POST,request.FILES)
        if NEve.is_valid():
            NEve.save()
            print("Your Event uploaded successfully!")
            msg="Your event uploaded successfully!"
        else:
            print(NEve.errors)
            msg="Error!Something went Wrong.. Please try again"
    
    return render (request,'addEvent.html',{'msg':msg})

def upd(request):
    msg=""
    user=request.session.get('user')
    userR=request.session.get('role')
    
    ur=signup.objects.filter(role=userR,email=user).first()
    print("current ID: ",ur)
    if request.method=='POST':
        upr=updData(request.POST,instance=ur)
        if upr.is_valid():
            upr.save()
            print("Update successfully!")
            msg="Update successfully!"
            #request.session.delete()
            return redirect('/')
        else:
            print(upr.errors)
            msg="Error!Something went Wrong.. Please try again"
    return render(request,'upd.html',{'user':user,'ur':ur,'msg':msg})

'''def event_list(request):
    events = addEve.objects.all()  # Fetch all events
    return render(request, 'event_list.html', {'events': events})'''


def event(request):
    user=request.session.get('user')
    eid=addEve.objects.all()
    return render(request,'event.html',{'eid':eid,'user':user})


def deleteTea(request,id):
    tid=addTea.objects.get(id=id)
    addTea.delete(tid)
    return redirect('teacher')




def deleteStu(request,id):
    sid=addStu.objects.get(id=id)
    addStu.delete(sid)
    return redirect('student')

def deleteEv(request,id):
    eid=addEve.objects.get(id=id)
    addEve.delete(eid)
    return redirect('event')

def userlogout(request):
    logout(request)
    return redirect("/")

def forgotPass(request):    
    user=request.session.get('user')
    userR=request.session.get('role')

    np=signup.objects.filter(role=userR,email=user).first()
    print("current ID: ",np)
    if request.method=='POST':
        ups=pas(request.POST,instance=np)
        if ups.is_valid():
            ups.save()
            print("password changed successfully!")
            msg="password changed successfully!"
            #request.session.delete()
            return redirect('/')
        else:
            print(ups.errors)
            msg="Error!Something went Wrong.. Please try again"

    return render(request, 'forgotPass.html',{'user':user,'np':np,})

