from django.shortcuts import render
from django.views import View


class Test_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, "main.html",
                      {"title": "Hello world."})
