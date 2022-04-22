from django.shortcuts import render


posts = [
    {
        'author': 'Author1',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 22, 2022'
    },
    {
        'author': 'Author2',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 22, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})