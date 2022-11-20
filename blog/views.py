from django.shortcuts import render
from .models import Poem
import random


def index(request):
    return render(request, 'blog/index.html')


def blogpost(request):
    i = random.randrange(1, len(Poem.objects.values('poem_id')) + 1)
    poem = Poem.objects.filter(poem_id=i)
    return render(request, 'blog/blogpost.html', {'poems': poem})
