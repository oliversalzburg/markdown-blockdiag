from __future__ import unicode_literals, absolute_import
import re
import base64

from markdown import Markdown
from markdown.preprocessors import Preprocessor
from markdown.blockprocessors import BlockProcessor
from markdown.util import etree
from markdown_blockdiag_code.utils import draw_blockdiag, DIAG_MODULES

# Python 3 version
try:
    from urllib.parse import quote as url_quote
# Python 2 version
except ImportError:
    from urllib import quote as url_quote

FENCED_BLOCK_RE = re.compile(
    r'(?P<fence>^(?:~{3,}|`{3,}))[ ]*(\{?\.?(?P<lang>[a-zA-Z0-9_+-]*)\}?)?[ ]*\n(?P<code>.*?)(?<=\n)(?P=fence)[ ]*$',
    re.MULTILINE | re.DOTALL
)
IMG_WRAP = '<img src="%s">'


class BlockdiagProcessor(Preprocessor):
    def __init__(self, md: Markdown, extension):
        Preprocessor.__init__(self, md)
        self.extension = extension

    def run(self, lines):
        text = "\n".join(lines)
        while 1:
            match = FENCED_BLOCK_RE.search(text)
            print(match)
            if match:
                lang = match.group('lang')

                font_path = self.extension.getConfig('fontpath')
                font_antialias = self.extension.getConfig('fontantialias')
                output_fmt = self.extension.getConfig('format')
                diagram = draw_blockdiag(match.group(
                    'code'), output_fmt=output_fmt, font_path=font_path, font_antialias=font_antialias)
                if output_fmt == 'png':
                    src_data = 'data:image/png;base64,{0}'.format(
                        base64.b64encode(diagram).decode('ascii')
                    )
                else:
                    src_data = 'data:image/svg+xml;charset=utf-8,{0}'.format(
                        url_quote(diagram))
                code = IMG_WRAP % src_data

                # Replace part of text that we match, then run on the same text again.
                placeholder = self.markdown.htmlStash.store(code)
                text = '%s\n%s\n%s' % (
                    text[:match.start()], placeholder, text[match.end():])
            else:
                break
        return text.split("\n")

    def _escape(self, txt):
        """ basic html escaping """
        txt = txt.replace('&', '&amp;')
        txt = txt.replace('<', '&lt;')
        txt = txt.replace('>', '&gt;')
        txt = txt.replace('"', '&quot;')
        return txt
