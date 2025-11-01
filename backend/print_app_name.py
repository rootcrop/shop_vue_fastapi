from app.config import settings

print(settings.app_name)
if settings.debug:
    print("Debug mode is on")