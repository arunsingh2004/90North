"""
ASGI config for chat_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
try:
    import chat_app.routing  # Ensure this matches the actual app folder name
except ModuleNotFoundError:
    import sys
    sys.stderr.write("Error: chat_app.routing module not found. Ensure the module path is correct.\n")
    sys.exit(1)

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat_app.routing.websocket_urlpatterns
        )
    ),
})
