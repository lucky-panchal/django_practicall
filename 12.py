"""
Steps to define a Book model and run migrations:

1. In blog/models.py:
       from django.db import models

       class Book(models.Model):
           title = models.CharField(max_length=200)
           author = models.CharField(max_length=100)
           published_date = models.DateField()

           def __str__(self):
               return self.title

2. Create migration file:
       python manage.py makemigrations

3. Apply migrations to the database:
       python manage.py migrate
"""

import os
import subprocess

project_path = os.path.join(os.path.dirname(__file__), "MyWebsite")
migrations_dir = os.path.join(project_path, "blog", "migrations")
db_path = os.path.join(project_path, "db.sqlite3")

# Remove old migration files (keep __init__.py)
for f in os.listdir(migrations_dir):
    if f != "__init__.py" and f.endswith(".py"):
        os.remove(os.path.join(migrations_dir, f))

# Remove old database
if os.path.exists(db_path):
    os.remove(db_path)

print("Creating migrations...")
subprocess.run(["python", "manage.py", "makemigrations"], cwd=project_path)

print("\nApplying migrations...")
subprocess.run(["python", "manage.py", "migrate"], cwd=project_path)
