#making the poll modifiable in the admin
from django.contrib import admin
from .models import Question

admin.site.register(Question)