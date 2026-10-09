"""
Steps to create and run a Django project:

1. Install Django:
       pip install django

2. Create the project:
       django-admin startproject MyWebsite

3. Run the development server:
       cd MyWebsite
       python manage.py runserver
"""

import os
import subprocess

project_path = os.path.join(os.path.dirname(__file__), "MyWebsite")

subprocess.run(["python", "manage.py", "runserver"], cwd=project_path)
