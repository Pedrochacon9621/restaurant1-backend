from restaurant1.asgi import application as app

def handler(request):
    return app(request)
