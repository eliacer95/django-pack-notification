# django-pack-notification
This library allows you to send notifications from Django to Slack

### Requirements
* Create an app in your Slack group.
* Generate a Webhook URL for channel that you will send the notifications or messages.

### Installation 
```sh
$ pip install django-package-notification
```
How to use:
```py
url = "https://hooks.slack.com/services/XXXXXXXXX/YYYYYYYY/OXbi63xBPrGeceUMsEsTngUA"

send_notification_success(url, title, message, subtitle)
send_notification_error(url, title, message, subtitle)
```

