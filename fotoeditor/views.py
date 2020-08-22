from django.shortcuts import render
from django.http import HttpResponse


def image_display_editor(request):
    template = "fotoeditor/image_editor.html"
    context_dict = {}
    return render(request, template, context_dict)
    # return HttpResponse("Hello, world. You're at the editor.")