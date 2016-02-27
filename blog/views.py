from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request): # function
# Request is a paramete of render. Request is everything
# we receive from the user via the internet.

# We created a variable 'posts' for our queryset
# Because we are using the timezone function below this is why we
# had to import timezone above.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # Template file blog/post_list.html
    # the {} are where we add things for the template to use
    # We can give them names which is the string in the ''.
    return render(request, 'blog/post_list.html', {'posts': posts})
