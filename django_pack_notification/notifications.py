from .slack import slack_success, slack_error


def send_notification_success(url, title, message, subtitle=None):
    slack_success(url, title, message, subtitle)


def send_notification_error(url, title, message, subtitle=None):
    slack_error(url, title, message, subtitle)