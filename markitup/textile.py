#!/usr/bin/env python
# encoding: utf-8
"""
markitup/__init__.py - Widget for using Rich Editors in Django Fields.

Created by http://www.sborgsolutions.com/ for HUDORA on 2009-12
Copyright (c) 2009, 2010 HUDORA. All rights reserved.
"""

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

class TextileMarkItUpEditor(forms.Textarea):
    class Media:
        css = {
            "all": (
                'http://s.hdimg.net/markitup-1.1.5/markitup/skins/simple/style.css',
                'http://s.hdimg.net/markitup-1.1.5/markitup/sets/textile/style.css'
            )
        }
        
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.2.3/jquery.js',
            'http://s.hdimg.net/markitup-1.1.5/markitup/jquery.markitup.pack.js',
            'http://s.hdimg.net/markitup-1.1.5/markitup/sets/textile/set.js'
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        if attrs:
            self.attrs.update(attrs)
        super(TextileMarkItUpEditor, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        rendered = super(TextileMarkItUpEditor, self).render(name, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
            $(document).ready(function() {
                $('#id_%s').markItUp(mySettings);
            })
            </script>''' % (name))
