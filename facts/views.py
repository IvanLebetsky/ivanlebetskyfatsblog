from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Fact, Category
from django.contrib.auth.decorators import login_required

def fact_list(request):
    facts = Fact.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'facts/fact_list.html', {
        'facts': facts,
        'categories': categories
    })

def category_facts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    facts = Fact.objects.filter(category=category).order_by('-created_at')
    return render(request, 'facts/fact_list.html', {
        'facts': facts,
        'categories': Category.objects.all(),
        'current_category': category
    })

@login_required
def like_fact(request, pk):
    fact = get_object_or_404(Fact, pk=pk)
    if request.user in fact.likes.all():
        fact.likes.remove(request.user)
        liked = False
    else:
        fact.likes.add(request.user)
        liked = True
    return JsonResponse({
        'liked': liked,
        'total_likes': fact.total_likes()
    })
