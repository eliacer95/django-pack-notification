# django-pack-notification
Es una librería que permite enviar notificaciones desde Django hacia Slack

### Requisitos
* Necesitas crear una App, respecto a un grupo existente en Slack.
* Generar un Webhook URL en el canal al cual se enviarán las notificaciones o los mensajes.

### Instalación
```sh
$ pip install django-pack-notification
```

Agregar a settings.py la ruta
```py
# Url general Channel
SLACK_DEFAULT_URL = "https://hooks.slack.com/services/XXXXXXXXX/YYYYYYYY/OXbi63xBPrGeceUMsEsTngUA"

```
A continuación se muestra un ejemplo:
```py
msg = "<html><body><h2>Se envió correctamnete</h2></body></html>"
msg_error = "<html><body><h2>No se pudo enviar</h2></body></html>"
message = ""
to_user = "everyone"

def MessageStore(request):
    store = "Admin"
    ruc = "20152345678"
    razon_social = "Inversiones Vasquez S.R.L"
    username = "Omelia432"
    email_store = "vasquez@gmail.com"

    data = StoreCreated(to_user, store, ruc, razon_social, username, email_store)
    message = send_slack(data)
    if message:
        return HttpResponse(msg)
    else:
        return HttpResponse(msg_error)
```
La funcion StoreCreated() retorna la data en formato Json de acuerdo a un estilo de mensaje que se mostrará en Slack. Luego se ejecuta la función
send_slack(), retornando un boolean si se envió el mensaje.
