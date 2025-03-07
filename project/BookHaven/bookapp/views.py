from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
from BookHaven import settings
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def index(request):
  user=request.session.get("user")
  query = request.GET.get('query', '').strip()
  results = Book.objects.filter(booktitle__icontains=query) if query else Book.objects.none()
  if user:
        try:
            isapp = Author.objects.get(email=user)
            approved = isapp.is_approved  # Assuming 'is_approved' is a field in Author model
        except Author.DoesNotExist:
            approved = False
  else:
        approved = False
  return render(request,'index.html',{'user':user,'approved':approved,'query':query,'results':results})


def addbook(request):
    msg = ""
    if request.method == 'POST':
        newbook = adddbookform(request.POST, request.FILES)
        if newbook.is_valid():
            book_instance = newbook.save(commit=False)  # Save book without committing to the database
            book_instance.save()  # Now save the book instance
            
            newbook.save_m2m()  # Save ManyToMany field data
            
            msg = "Added book successfully!"
            print("Added book successfully!")
            return redirect('/')
        else:
            print(newbook.errors)
            msg = "Error: Something went wrong. Please ensure all fields are filled correctly."
    
    return render(request, 'addbook.html', {'msg': msg})

def log_in(request):
    msg=''
    if request.method == 'POST':
        unm=request.POST['email']
        password=request.POST['pas']

        user=signup.objects.filter(email=unm,pas=password)
        #isapp=Author.objects.get(email=unm)
        #print("Current User:",isapp)
        if user:
            print("Login successfully!")
            request.session['user']=unm
            msg="Login successfully!"
            return redirect('/')
        else:
            print("Login failed...")
            msg='Login failed.. Try again...'
    return render(request,'log_in.html',{'msg':msg})

def sign_up(request):
    msg=''
    if request.method =='POST':
        newuser=signupForm(request.POST)

        password=request.POST['pas']
        confirm_password=request.POST['cpas']

        if password != confirm_password:
            msg="Your Password doesn't match Try again..."
            print("Your Password doesn't match Try again...")

        elif newuser.is_valid():
                newuser.save()
                
                send_mail(
                    subject="Thankyou",
                    message=f"Hello User! \n \n thank you for connecting with us.You have successfully signed up. \n\n Thanks & Regards! \n BookHeaven",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[request.POST['email']],
                )


                msg="signup successfully! "
                print("signup successfully!")
                return redirect('log_in')
        else:
                print(newuser.errors)
                msg="Error! Somethong went wrong..."
                print("Error! Somethong went wrong...")
    return render(request,'sign_up.html',{'msg':msg})

def showbook(request, genre):
    user=request.session.get("user")
    #genre = genre.replace('_', ' ')
    #print(f"Genre received: {genre}")
    books = Book.objects.filter(genre__icontains=genre)
    print(f"Books found: {books.count()}")
    query = request.GET.get('query', '').strip()
    results = Book.objects.filter(booktitle__icontains=query) if query else Book.objects.none()
    #print(f"All genres in database: {list(all_genres)}") 
    if user:
        try:
            isapp = Author.objects.get(email=user)
            approved = isapp.is_approved  # Assuming 'is_approved' is a field in Author model
        except Author.DoesNotExist:
            approved = False
    else:
        approved = False
    return render(request,'showbook.html',{"books": books,'user':user, "selected_genre": genre,'approved':approved,'query':query,'results':results})

def search(request):
    user = request.session.get("user")
    
    if user:
        try:
            isapp = Author.objects.get(email=user)
            approved = isapp.is_approved
        except Author.DoesNotExist:
            approved = False
    else:
        approved = False

    query = request.GET.get('query', '').strip()
    print(f"Search query: {query}")  # Debugging line to check if query is received

    results = Book.objects.filter(booktitle__icontains=query) if query else None
    
    return render(request, 'search.html', {'query': query, 'user': user, 'approved': approved, 'results': results})


def author_apply(request):
    msg=''
   
    if request.method == 'POST':
         au = au_ap(request.POST) 
         if au.is_valid(): 
            author = au.save(commit=False)  
            author.user = request.user
            author.approval_status = 'Pending' 
            author.save()  
            msg='Applied successfully!'
            print('Applied successfully!')
            return redirect('/')
         else:
            print(au.errors)
            msg='Error! Something went wrong...'
            print("Error! Something went wrong...")
    return render(request,'author_apply.html',{'msg':msg})

def userlogout(request):
    logout(request)
    return redirect('/')