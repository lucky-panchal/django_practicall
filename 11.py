"""
Steps to create a base template and extend it:

1. blog/templates/base.html  — base layout with {% block title %} and {% block content %}
2. blog/templates/home.html  — extends base.html, fills in Home content
3. blog/templates/about.html — extends base.html, fills in About content

4. In blog/views.py:
       def home(request):
           return render(request, 'home.html')

       def about(request):
           return render(request, 'about.html')

5. In MyWebsite/urls.py:
       path('home/', home),
       path('about/', about),

6. Run the server and visit:
       http://127.0.0.1:8000/home/
       http://127.0.0.1:8000/about/
"""

import os
import subprocess

project_path = os.path.join(os.path.dirname(__file__), "MyWebsite")
subprocess.run(["python", "manage.py", "runserver"], cwd=project_path)
