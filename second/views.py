from django.shortcuts import render
from second.models import Post


# Create your views here.
def list(request):
    content = {
        "items": Post.objects.all()
    }

    return render(request, 'second/list.html', content)