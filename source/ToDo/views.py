from django.shortcuts import render
from ToDo.models import Article, STATUS_CHOICES


def index_view(request):
    content = Article.objects.all()
    return render(request, 'index.html', context={'articles':content})

def tasks(request):
    if request.method == "POST":
        title = request.POST.get('title')
        status = request.POST.get('status')
        date = request.POST.get('date')
        article = Article.objects.create(title=title, status=status, date_perform=date)
        print(article)
        return index_view(request)
    elif request.method == "GET":
        return render(request, 'new_tasks.html', context={'status_choices': STATUS_CHOICES})