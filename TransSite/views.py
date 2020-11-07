from django.shortcuts import render
from django.utils import timezone
from .models import Word
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    posts = Word.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'TransSite/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Word, pk=pk)
    return render(request, 'TransSite/post_detail.html', {'post': post})

def about(request):
    return render(request, 'TransSite/about.html', {})