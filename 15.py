"""
Q15: REST API using Django REST Framework for CRUD on Product model.

1. Install DRF:
       pip install djangorestframework

2. Add to INSTALLED_APPS in settings.py:
       'rest_framework'

3. blog/models.py - Product model:
       class Product(models.Model):
           name = models.CharField(max_length=200)
           price = models.DecimalField(max_digits=10, decimal_places=2)
           stock = models.IntegerField()

4. blog/serializers.py:
       class ProductSerializer(serializers.ModelSerializer):
           class Meta:
               model = Product
               fields = '__all__'

5. blog/api.py:
       class ProductViewSet(viewsets.ModelViewSet):
           queryset = Product.objects.all()
           serializer_class = ProductSerializer

6. urls.py - register router:
       router.register(r'products', ProductViewSet)
       path('api/', include(router.urls))

API Endpoints:
   GET    /api/products/       -> list all products
   POST   /api/products/       -> create product
   GET    /api/products/<id>/  -> retrieve product
   PUT    /api/products/<id>/  -> update product
   DELETE /api/products/<id>/  -> delete product

Steps to test:
   1. Run server: python manage.py runserver
   2. Visit http://127.0.0.1:8000/api/products/ (DRF browsable API)
"""

import os
import subprocess

project_path = os.path.join(os.path.dirname(__file__), "MyWebsite")
subprocess.run(["python", "manage.py", "runserver"], cwd=project_path)
