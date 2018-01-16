#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

GITHUB_DEPLOY_BRANCH = 'master'
GITHUB_SOURCE_BRANCH = 'src'
GITHUB_REMOTE_NAME = 'origin'
GITHUB_COMMIT_SOURCE = False

LOGO_URL = "/icon_32x32.png"

BLOG_AUTHOR = "ACEF"
BLOG_TITLE = "法国东部华人联谊会 (ACEF)"
SITE_URL = "https://acef-fr.github.io/"
BLOG_EMAIL = "zhi.yan@utbm.fr"
BLOG_DESCRIPTION = "Website of the AMICALE DES CHINOIS DE L'EST DE LA FRANCE (ACEF)"

DEFAULT_LANG = "en"
TRANSLATIONS = {
    DEFAULT_LANG: "",
}
TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}"

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/", "概况"),
        ("/people/", "团队"),
        ("/projects/", "章程"),
        ("/publications/", "活动"),
        ("/ressources/", "资源"),
        ("/news/", "新闻"),
    ),
}

THEME = "cerulean"
THEME_COLOR = "#f5ab14"

POSTS = (
    ("posts/*.md", "news", "post.tmpl"),
    ("posts/*.rst", "news", "post.tmpl"),
    ("posts/*.txt", "news", "post.tmpl"),
    ("posts/*.html", "news", "post.tmpl"),
)

PAGES = (
    ("stories/*.md", "", "story.tmpl"),
    ("stories/*.rst", "", "story.tmpl"),
    ("stories/*.txt", "", "story.tmpl"),
    ("stories/*.html", "", "story.tmpl"),
)

INDEX_PATH = "news"

TIMEZONE = "Europe/Paris"

COMPILERS = {
    "rest": ('.rst', '.txt'),
    "markdown": ('.md', '.mdown', '.markdown'),
    "textile": ('.textile',),
    "txt2tags": ('.t2t',),
    "bbcode": ('.bb',),
    "wiki": ('.wiki',),
    "ipynb": ('.ipynb',),
    "html": ('.html', '.htm'),
    "php": ('.php',),
}

MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite', 'extra']

FAVICONS = (
    ("icon", "/favicon.ico", "16x16"),
    ("icon", "/icon_128x128.png", "128x128"),
)

LICENSE = ""

CONTENT_FOOTER = 'Contents &copy; {date} <a href="mailto:{email}">{author}</a> - Powered by <a href="https://getnikola.com" rel="nofollow">Nikola</a> {license} <br><br><div class="a2a_kit a2a_kit_size_32 a2a_default_style"><a class="a2a_dd" href="https://www.addtoany.com/share"></a><a class="a2a_button_facebook"></a><a class="a2a_button_twitter"></a><a class="a2a_button_google_plus"></a><a class="a2a_button_email"></a><a class="a2a_button_linkedin"></a></div><br>'
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

SEARCH_FORM = """
<!-- RSS Button -->
<form class="navbar-form navbar-right">
<a href="rss.xml" class="btn" role="button">
<img src="/rss.svg" alt="RSS" width="24">
</a>
</form>
<!-- End of RSS button -->
"""

RSS_COPYRIGHT = 'Contents © {date} <a href="mailto:{email}">{author}</a> {license}'
RSS_COPYRIGHT_PLAIN = 'Contents © {date} {author} {license}'
RSS_COPYRIGHT_FORMATS = CONTENT_FOOTER_FORMATS

BODY_END = """<script>var a2a_config = a2a_config || {};a2a_config.onclick = 1;</script><script async src="https://static.addtoany.com/menu/page.js"></script>"""

COPY_SOURCES = False
WRITE_TAG_CLOUD = True
