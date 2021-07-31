from django.core.mail import EmailMultiAlternatives, get_connection
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from os import getenv

from planner.models import Week


class send_email():
    def __init__(self, item, files, user):
        self.item = item
        self.files = files
        self.user = user

    def process_email(self, s, c, files, e):
        connect = get_connection(
            host=getenv("ADMIN_HOST"),
            port=getenv("ADMIN_PORT"),
            username=getenv("ADMIN_EMAIL"),
            password=getenv("ADMIN_PASSWORD"),
            use_tls=getenv("ADMIN_TLS")
        )
        with connect as connection:
            msg = EmailMultiAlternatives(
                s, c['text_content'], getenv("ADMIN_EMAIL"), e,
                connection=connection)
            msg.attach_alternative(c['html_content'], "text/html")
            msg.content_subtype = "text/html"
            for file in files:
                msg.attach(file['name'], file['file'], file['type'])
            msg.send()
            return 'Email Message Sent'

    def week_planner_email(self):
        week_item = Week.objects.filter(id=self.item).first()
        subject = f'{week_item.name} - Planned Meals'
        context = {
            'id': week_item.id,
            'user': self.user,
            'site': getenv('SITE_URL'),
        }
        content = {}
        content['html_content'] = render_to_string(
            'email_comms/week_planner_email.html', context=context)
        content['text_content'] = strip_tags(content['html_content'])
        if getenv("DEBUG_TYPE") == 'True':
            e = [getenv("ADMIN_EMAIL")]
        else:
            e = [self.user.email]
        self.process_email(subject, content, self.files, e)
