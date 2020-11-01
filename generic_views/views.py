from django.shortcuts import render


def article_archive(request):
    return render(request, 'article_archive.html')
