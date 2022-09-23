import json
from os import path
import re

from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.safestring import mark_safe

# borrowed from https://weautomate.org/articles/using-vite-js-with-django/


register = template.Library()


def is_absolute_url(url):
    return re.match("^https?://", url)


DEV = settings.DEBUG

if DEV:
    DEV_SERVER_ROOT = settings.VITE_DEV_SERVER


def vite_manifest(entries_names):
    app_name = "variants"
    manifest_filepath = path.join(app_name, "static/manifest.json")

    if DEV:
        scripts = [
            f"{DEV_SERVER_ROOT}/@vite/client",
        ]

        for name in entries_names:
            scripts.append(f"{DEV_SERVER_ROOT}/{name}")

        styles = []
        return scripts, styles
    else:
        with open(manifest_filepath) as fp:
            manifest = json.load(fp)
        _processed = set()

        def _process_entries(names):
            scripts = []
            styles = []

            for name in names:
                if name in _processed:
                    continue

                chunk = manifest[name]

                import_scripts, import_styles = _process_entries(chunk.get("imports", []))
                scripts += import_scripts
                styles += import_styles

                scripts += [chunk["file"]]
                styles += [css for css in chunk.get("css", [])]

                _processed.add(name)

            return scripts, styles

        return _process_entries(entries_names)


@register.simple_tag
def vite_styles(*entries_names):
    """
    Populate an html template with styles generated by vite

    Usage::

        {% vite_styles 'main.js' 'other-entry.js' %}

    Examples::
        <head>
            ...
            {% vite_styles 'main.js' 'other-entry.js' %}
        </head>
    """
    _, styles = vite_manifest(entries_names)
    styles = map(lambda href: href if is_absolute_url(href) else static(href), styles)

    def as_link_tag(href):
        return f'<link rel="stylesheet" href="{href}" />'

    return mark_safe("\n".join(map(as_link_tag, styles)))


@register.simple_tag
def vite_scripts(*entries_names):
    """
    Populate an html template with script tags generated by vite

    Usage::

        {% vite_scripts 'main.js' 'other-entry.js' %}

    Examples::
        <body>
            <!-- Your HTML -->
            {% vite_scripts 'main.js' 'other-entry.js' %}
        </body>
    """
    scripts, _ = vite_manifest(entries_names)
    scripts = map(lambda src: src if is_absolute_url(src) else static(src), scripts)

    def as_script_tag(src):
        return f'<script type="module" src="{src}"></script>'

    return mark_safe("\n".join(map(as_script_tag, scripts)))
