from django.contrib import admin

# Register your models here.
from .models import Post # We defined this model previously

admin.site.register(Post) # This is needed to make the model
# visible on the admin page
