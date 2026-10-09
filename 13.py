"""
Q13: Add books via admin and display all book titles. Create a contact form.

1. Register Book in blog/admin.py:
       admin.site.register(Book)

2. blog/views.py - book_list view fetches all books using ORM:
       def book_list(request):
           books = Book.objects.all()
           return render(request, 'book_list.html', {'books': books})

3. blog/views.py - contact view handles form POST:
       def contact(request):
           if request.method == 'POST':
               name = request.POST.get('name')
               email = request.POST.get('email')
               return render(request, 'thankyou.html', {'name': name, 'email': email})
           return render(request, 'contact.html')

4. Templates: book_list.html, contact.html, thankyou.html

URLs:
   /books/   -> displays all book titles
   /contact/ -> contact form -> thank you page

Steps to test:
   1. Run server: python manage.py runserver
   2. Go to http://127.0.0.1:8000/admin/ -> add books
   3. Go to http://127.0.0.1:8000/books/ -> see book titles
   4. Go to http://127.0.0.1:8000/contact/ -> submit form
"""

import os
import subprocess

project_path = os.path.join(os.path.dirname(__file__), "MyWebsite")
subprocess.run(["python", "manage.py", "runserver"], cwd=project_path)
