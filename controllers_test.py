import dirigera
import json
from typing import Any


dirigera_hub = dirigera.Hub(
    token="eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijg2MWJmMzZiYjRmNjdjMjZmMzIzYzg0YWVlMmJiNTFmNjVmYjNlZDdhNTE4Y2UxMjBlODdjYmUwNGRlMmZlNzUifQ.eyJpc3MiOiIyZTkwMjI3NC1kZDdjLTRkZWYtYjc4NS0zYzBhYzQ0OGZkM2IiLCJ0eXBlIjoiYWNjZXNzIiwiYXVkIjoiaG9tZXNtYXJ0LmxvY2FsIiwic3ViIjoiZmY5MDZmZDYtMDlmOS00NWM0LWJiZTEtMGU5YWYzOTczODViIiwiaWF0IjoxNzA2MzY1MjU0LCJleHAiOjIwMjE5NDEyNTR9.JnfLvPYXvL8t0oEi9FIoXQrcSAwqiwwZgS4fSvygBQVc8AdRc0Pf2I6jXvjrIwAiB-5tdNiOdVoIB2J6wcF_QA",
    ip_address="192.168.0.73"
)


shortcut = dirigera_hub.get_controllers()[2]
print(shortcut.id)

def prettify(message):
    print(type(message))
    return json.dumps(json.loads(message), indent=2)

def on_message(ws: Any, message: str):
    print(prettify(message)+"\n")

def on_error(ws: Any, message: str):
    print("err",message)

dirigera_hub.create_event_listener(
on_message=on_message, on_error=on_error
)