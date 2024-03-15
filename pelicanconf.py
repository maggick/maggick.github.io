from PIL import Image, ImageOps
import datetime

AUTHOR = 'maggick'
SITENAME = "maggick's logs"
SITEURL = 'https://maggick.fr'
SITETITLE = SITENAME
SITESUBTITLE = 'Offensive security tales'

THEME = "./Flex"

RELATIVE_URLS = True
PATH = 'content'
DISABLE_URL_HASH = True
DISPLAY_PAGES_ON_MENU = "True"
ARTICLE_EXCLUDES = ('pages',)
TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%d %b %Y'
DEFAULT_LANG = 'en'

# Article
PAGE_URL = 'pages/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
DISPLAY_CATEGORIES_ON_MENU = False

# Plugins
PLUGIN_PATHS = ['./pelican-plugins/']
PLUGINS = ['summary', 'neighbors', 'post_stats', 'image_process', 'render_math']

# Social
SOCIAL = (('email', 'mailto:postmater at maggick dot fr'),
          ('github', 'https://github.com/maggick'),
          ('twitter', 'https://twitter.com/maggick_fr'),
          ('stack-overflow', 'http://stackoverflow.com/users/1827067/maggick'),
          ('rss', 'https://maggick.fr/feeds/all.atom.xml'),
          ('discord', 'https://discord.com/users/maggick'),
          ('reddit', 'https://www.reddit.com/user/maaggick/'),
          )

# Menu
MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['media', 'extra/CNAME', 'extra/.nojekyll',]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/.nojekyll':{'path':'.nojekyll'},}
FAVICON_URL = "%s/media/favicon.ico" % SITEURL
SITELOGO = "%s/media/image.png" % SITEURL

today = datetime.date.today()
year = today.year
COPYRIGHT_YEAR = year

THEME_COLOR = 'light'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = 'sas'
PYGMENTS_STYLE_DARK = 'monokai'

CC_LICENSE = {
    "name": "Creative Commons Attribution",
    "version": "4.0",
    "slug": "by"
}

def border(image):
    """Add a border to an image"""
    return ImageOps.expand(image,border=3,fill='black')

IMAGE_PROCESS_FORCE = True
IMAGE_PROCESS = {
    "article-image": {
        "type": "image",
        "ops": [border],
    },
}

ANALYTICS = """<script defer src="https://eu.umami.is/script.js" data-website-id="3fd2620b-e9b8-4445-9d3a-161dee9977e1"></script>"""
