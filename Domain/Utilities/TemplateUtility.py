import os
import jinja2

from Configuration import Config

# Single class to handle all template requests made by controller classes
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/Http/Templates/'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=False)

def render(template_name, template_values):
    template_values = dict(Config.GLOBAL_TEMPLATE_VALUES.items() + template_values.items())
    return JINJA_ENVIRONMENT.get_template(template_name).render(template_values)