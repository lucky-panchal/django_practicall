"""
Steps to create an HTML page using Django templates:

1. Create blog/templates/profile.html:
       <!DOCTYPE html>
       <html>
       <head><title>My Profile</title></head>
       <body>
           <h1>Name: {{ name }}</h1>
           <p>Profession: {{ profession }}</p>
       </body>
       </html>

2. In blog/views.py add:
       def profile(request):
           return render(request, 'profile.html', {'name': 'Lucky', 'profession': 'Python Developer'})

3. In MyWebsite/urls.py add:
       path('profile/', profile),

4. Run the server:
       cd MyWebsite
       python manage.py runserver

5. Visit: http://127.0.0.1:8000/profile/
"""

import os
import subprocess

project_path = os.path.join(os.path.dirname(__file__), "MyWebsite")
subprocess.run(["python", "manage.py", "runserver"], cwd=project_path)
