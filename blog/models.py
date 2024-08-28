from django.db import models
from froala_editor.fields import FroalaField
from django.contrib.auth.models import User
from .helpers import generate_slug
from bs4 import BeautifulSoup
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Profile(models.Model):
    author_name = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField()

    def __str__(self):
        return self.author_name.username

class POSTCategory(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "PostCategory"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class Post(models.Model):
    title = models.CharField(max_length=1000)
    content = RichTextUploadingField(null=True, blank=True)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    categories = models.ManyToManyField(POSTCategory)
    read_time = models.CharField(max_length=100, null=True, default='5')
    toc = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.title)
        
        # Call the parent class's save method first
        super(Post, self).save(*args, **kwargs)
        
        # Update the TOC after saving the initial content
        if self.content:
            self.toc = self.generate_toc()
            super(Post, self).save(update_fields=['toc'])

    def generate_toc(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        toc = []
        for i, heading in enumerate(soup.find_all(['h2'])):
            id = f'heading-{i}'
            heading['id'] = id
            toc.append(f'<li><a href="#{id}">{heading.text}</a></li>')
        return '<ul>' + ''.join(toc) + '</ul>'
