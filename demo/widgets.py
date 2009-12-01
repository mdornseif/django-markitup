from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

class MarkItUpEditor(forms.Textarea):
    class Media:
        css = {
            "all": (
                '/media/markitup-1.1.5/markitup/skins/simple/style.css',
                '/media/markitup-1.1.5/markitup/sets/textile/style.css'
            )
        }
        
        js = (
            '/media/markitup-1.1.5/jquery.pack.js',
            '/media/markitup-1.1.5/markitup/jquery.markitup.pack.js',
            '/media/markitup-1.1.5/markitup/sets/textile/set.js'
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        self.attrs = {'class': 'wymeditor'}
        if attrs:
            self.attrs.update(attrs)
        super(MarkItUpEditor, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        rendered = super(MarkItUpEditor, self).render(name, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
            $(document).ready(function() {
                $('#id_%s').markItUp(mySettings);
            })
            </script>''' % (name))