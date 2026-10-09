from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book

def hello(request):
    return HttpResponse("Hello, Django!")

def profile(request):
    return render(request, 'profile.html', {'name': 'Lucky', 'profession': 'Python Developer'})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Q13 - Display all book titles
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Q13 - Contact form
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request, 'thankyou.html', {'name': name, 'email': email})
    return render(request, 'contact.html')

# Q14 - Login
def login_view(request):
    error = ''
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('/books/')
        error = 'Invalid credentials'
    return render(request, 'login.html', {'error': error})

# Q14 - Logout
def logout_view(request):
    logout(request)
    return redirect('/login/')
