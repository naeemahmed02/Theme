from django.utils.text import slugify
import random
import string

def generate_random_string(N):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

def generate_slug(text):
    new_slug = slugify(text)
    from blog.models import Post
    if Post.objects.filter(slug = new_slug).exists():
        return generate_slug(text + ' ' + generate_random_string(5))
    return new_slug
