from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
from BookHaven import settings
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'index.html')


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
        if user:
            print("Login successfully!")
            msg="Login successfully!"

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

        elif newuser.is_valid():
                newuser.save()
                
                send_mail(
                    subject="Thankyou",
                    message=f"Hello User! \n \n thank you for connecting with us.You have successfully signed up. \n\n Thanks & Regards! \n minji min",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[request.POST['email']],
                )


                msg="signup successfully! "
                print("signup successfully!")
        else:
                print(newuser.errors)
                msg="Error! Somethong went wrong..."
                print("Error! Somethong went wrong...")
    return render(request,'sign_up.html',{'msg':msg})

def showbook(request, genre):
    #genre = genre.replace('_', ' ')
    #print(f"Genre received: {genre}")
    books = Book.objects.filter(genre__icontains=genre)
    print(f"Books found: {books.count()}")
    #print(f"All genres in database: {list(all_genres)}") 
    return render(request,'showbook.html',{"books": books, "selected_genre": genre})

def search(request):
    query = request.GET.get('query', '').strip()
    results = Book.objects.filter(booktitle__icontains=query) if query else Book.objects.none()
    
    return render(request,'search.html',{'query':query, 'results':results})

def author_apply(request):
    msg=''
    if request.method == 'POST':
         au = au_ap(request.POST) 
         if au.is_valid():  # Check if form data is valid
            author = au.save(commit=False)  # Create author instance but don't save yet
            author.user = request.user
            author.approval_status = 'Pending'  # Set approval status
            author.save()  # Save to the database
            msg='Applied successfully!'
            print('Applied successfully!')
            return redirect('/')
         else:
            print(au.errors)
            msg='Error! Something went wrong...'
            print("Error! Something went wrong...")
    return render(request,'author_apply.html',{'msg':msg})



