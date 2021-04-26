from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")


def page2(request):
    return HttpResponse("<h1>Hey Buddy</h1>")


def page3(request):
    content = """<h1>hello world</h1>
               <h2>hai Binode...<h2>"""
    return HttpResponse(content)
