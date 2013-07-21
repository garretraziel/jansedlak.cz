from django import template
from django.template.defaultfilters import stringfilter
import markdown
from markdown_processor import CodeBlockExtension

register = template.Library()

@register.filter(name="markdown", is_safe=True)
@stringfilter
def convertmarkdown(value):
    """Convert text from markdown to html."""
    return markdown.markdown(value, extensions=[CodeBlockExtension()])