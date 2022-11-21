from django.shortcuts import render
from .models import Poem
import random


def index(request):
    i = random.randrange(1, len(Poem.objects.values('poem_id')) + 1)
    poem = Poem.objects.filter(poem_id=i)
    snippet = Poem.objects.get(poem_id=i).poem.split('\n[2]')
    i2 = random.randrange(1, len(Poem.objects.values('poem_id')) + 1)
    poem2 = Poem.objects.filter(poem_id=i2)
    snippet2 = Poem.objects.get(poem_id=i2).poem.split('\n[2]')
    i3 = random.randrange(1, len(Poem.objects.values('poem_id')) + 1)
    poem3 = Poem.objects.filter(poem_id=i3)
    snippet3 = Poem.objects.get(poem_id=i3).poem.split('\n[2]')
    i4 = random.randrange(1, len(Poem.objects.values('poem_id')) + 1)
    poem4 = Poem.objects.filter(poem_id=i4)
    snippet4 = Poem.objects.get(poem_id=i4).poem.split('\n[2]')
    return render(request, 'blog/index.html',
                  {'random1': poem, "snippet1": snippet, 'random2': poem2, "snippet2": snippet2, 'random3': poem3, "snippet3": snippet3, 'random4': poem4, "snippet4": snippet4})


def blogpost(request):
    poem = Poem.objects.filter(poem_id=random.randrange(1, len(Poem.objects.values('poem_id')) + 1))
    li = Poem.objects.all()
    return render(request, 'blog/blogpost.html', {'poems': poem, "li": li})


def poempage(request, poemid):
    poem = Poem.objects.filter(poem_id=poemid)
    li = Poem.objects.all()
    return render(request, 'blog/poempage.html', {'poems': poem, "li": li})
