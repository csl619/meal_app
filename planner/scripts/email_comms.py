from django.core.mail import EmailMultiAlternatives, get_connection
from django.utils.html import strip_tags
from django.template.loader import render_to_string


class Email():
    def __init__(
            self, host, port, admin_email, password, use_tls, debug=True):
        self.host = host
        self.port = port
        self.admin = admin_email
        self.password = password
        self.use_tls = use_tls
        self.debug = debug

    def __get_connection(self):
        connect = get_connection(
            host=self.host,
            port=self.port,
            username=self.admin,
            password=self.password,
            use_tls=self.use_tls
        )
        return connect

    def attachments(self, files):
        self.attachments = files

    def recipients(self, emails):
        if self.debug:
            emails = [self.admin]
        self.recipients = emails

    def sender(self, email):
        if self.debug:
            email = self.admin
        self.sender = email

    def subject(self, subject):
        self.subject = subject

    def body(self, template, context_vars=None):
        context = {}
        if context_vars:
            for item in context_vars:
                context[item] = context_vars[item]
        self.html_content = render_to_string(template, context=context)
        self.text_content = strip_tags(self.html_content)

    def send(self):
        with self.__get_connection() as connection:
            msg = EmailMultiAlternatives(
                self.subject, self.text_content, self.sender, self.recipients,
                connection=connection)
            msg.attach_alternative(self.html_content, "text/html")
            msg.content_subtype = "text/html"
            if self.attachments:
                for file in self.attachments:
                    msg.attach(file['name'], file['file'], file['type'])
            return msg.send()
