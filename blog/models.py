from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
# The above from and import, add bits from files

# Class is a keyword to say we are defining an object
# Post is the name of our model (don't use white space
# use underscores to separate words)
# models.Model specifies that Post is a Django model so Django knows
# to save it in the database
class Post(models.Model): # This defines our model (an object)
# The below are the attributes or this class
    author = models.ForeignKey('auth.User')
    # This links to another model
    title = models.CharField(max_length=200)
    # CharField defines text with a limited number of characters to set
    text = models.TextField()
    # Add text without a limit
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): # These are methods, the things the class can do
    # Def means to that this is a function/method
    # publish is the name of the method - naming rules are lowercase and underscores
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
    # methods return something such as the above example
    # eg _str_() to return a string
        return self.title
