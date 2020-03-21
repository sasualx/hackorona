from django.views import View
from website.posts.models import Post
from django.shortcuts import render

class MainView(View):
    title = "Title"
    template = 'main_page.html'

    def get(self, request):
        posts = list(Post.objects.values('pk', 'position_x', 'position_y', 'title', 'text'))

        context = {
            'question_text': self.title,
            'props': posts,
        }

        return render(request, self.template, context)