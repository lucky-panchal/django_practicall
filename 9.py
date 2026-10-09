"""
Steps to create a view and map it to a URL:

1. In blog/views.py:
       from django.http import HttpResponse

       def hello(request):
           return HttpResponse("Hello, Django!")

2. In MyWebsite/urls.py:
       from blog.views import hello

       urlpatterns = [
           path('admin/', admin.site.urls),
           path('hello/', hello),
       ]

3. Run the server:
       cd MyWebsite
       python manage.py runserver

4. Visit: http://127.0.0.1:8000/hello/
"""

import os
import subprocess

project_path = os.path.join(os.path.dirname(__file__), "MyWebsite")
subprocess.run(["python", "manage.py", "runserver"], cwd=project_path)
