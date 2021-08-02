from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration


class Pdf():
    def __init__(self, site_url, directory, browser_output=False):
        self.browser_output = browser_output
        self.data = {
            'site_url': site_url,
            'directory': directory,
            'browser_output': browser_output
        }

    def template(self, temp_vars):
        self.template = temp_vars['template']
        self.css = temp_vars['css']

    def context_data(self, data):
        for item in data:
            self.data[item] = data[item]

    def name(self, file_name):
        self.file_name = file_name

    def generate(self, request=None):
        if self.browser_output:
            response = HTML(
                string=render_to_string(self.template, self.data),
                base_url='').write_pdf(
                    font_config=FontConfiguration(),
                    stylesheets=[CSS(self.css)]
                    )
        else:
            response = HttpResponse(content_type="application/pdf")
            response['Content-Disposition'] = (
                f"inline; filename={self.file_name}.pdf")
            HTML(
                string=render_to_string(self.template, self.data),
                base_url=request.build_absolute_uri()
            ).write_pdf(
                response, font_config=FontConfiguration(),
                stylesheets=[CSS(self.css)]
                )
        return response
