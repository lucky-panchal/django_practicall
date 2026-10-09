"""
Steps to create a Django app named 'blog' and register it:

1. Navigate to the project directory:
       cd MyWebsite

2. Create the app:
       python manage.py startapp blog

3. Register the app in MyWebsite/settings.py under INSTALLED_APPS:

       INSTALLED_APPS = [
           ...
           'blog',
       ]
"""

import os
import subprocess

project_path = os.path.join(os.path.dirname(__file__), "MyWebsite")

# Create the blog app only if it doesn't already exist
blog_path = os.path.join(project_path, "blog")
if not os.path.exists(blog_path):
    subprocess.run(["python", "manage.py", "startapp", "blog"], cwd=project_path)
    print("Blog app created successfully.")
else:
    print("Blog app already exists.")

# Verify registration in settings.py
settings_path = os.path.join(project_path, "MyWebsite", "settings.py")
with open(settings_path) as f:
    content = f.read()

if "'blog'" in content:
    print("'blog' is registered in INSTALLED_APPS.")
else:
    print("'blog' is NOT registered. Please add it manually to INSTALLED_APPS.")
