"""
Q14: Login/Logout using Django built-in auth + CSS with {% static %} tag.

1. blog/views.py - login/logout views:
       def login_view(request):
           if request.method == 'POST':
               user = authenticate(request, username=..., password=...)
               if user:
                   login(request, user)
                   return redirect('/books/')
           return render(request, 'login.html', {'error': error})

       def logout_view(request):
           logout(request)
           return redirect('/login/')

2. Protect book_list with @login_required decorator.

3. base.html uses {% load static %} and links CSS:
       <link rel="stylesheet" href="{% static 'style.css' %}">

4. CSS file at blog/static/style.css

5. settings.py:
       LOGIN_URL = '/login/'

URLs:
   /login/  -> login page
   /logout/ -> logs out and redirects to login

Steps to test:
   1. Run server: python manage.py runserver
   2. Go to http://127.0.0.1:8000/login/
   3. Login with admin / admin123
   4. Visit /books/ (protected page)
   5. Click Logout
"""

import os
import subprocess

project_path = os.path.join(os.path.dirname(__file__), "MyWebsite")
subprocess.run(["python", "manage.py", "runserver"], cwd=project_path)
