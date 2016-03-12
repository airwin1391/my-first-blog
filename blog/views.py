from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
# This import will allow us to go directly to the post_detail page
# for your newly created blog post

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

from django.shortcuts import render, get_object_or_404
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # this saves the form
            # The commit=False means that we do not want to save Post
            # model yet, we want to add the author first
            post.author = request.user # we are adding an author
            post.published_date = timezone.now()
            post.save() # This saves changes (adding the author) so
            # a new blog post is created
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})




def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # this gets the post
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # instance so it will open
        # the post at the last moment it was saved
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
