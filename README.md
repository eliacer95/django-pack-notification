# django-pack-notification
This library allows you to send notifications from Django to Slack

### Requirements
* Create an app in your Slack group.
* Generate a Webhook URL for channel that you will send the notifications or messages.

### Installation 
```sh
$ pip install django-package-notification
```

## Parametros

Nombre de parámetro | Tipo | Obligatorio | Descripcion
------------ | ------------- | ------------ | ----------
url | String | Si | Channel url where the notifications will send.
title | String | Si | message's Title.
message | String | Si | All description that the message will have.
subtitle | String | No | An specific name for the message.

### Enviando notificaciones:
```py
url = "https://hooks.slack.com/services/XXXXXXXXX/YYYYYYYY/OXbi63xBPrGeceUMsEsTngUA"

send_notification_success(url, title, message, subtitle)
send_notification_error(url, title, message, subtitle)
```
These functions return a boolean if the message has been sended.
