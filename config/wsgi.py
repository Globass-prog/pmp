import os
import django

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

django.setup()  # 🔥 TRÈS IMPORTANT

import dashboard.routing  # ← seulement APRÈS django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            dashboard.routing.websocket_urlpatterns
        )
    ),
})