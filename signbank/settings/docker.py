import os
import django
from datetime import datetime, timedelta
from django.utils.encoding import smart_str

# Base Django settings
PROJECT_DIR = '/app'
BASE_DIR = '/app/'
ROOT = '/app/'
WRITABLE_FOLDER = '/app/writable/'

# Security settings
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-docker-dev-key-change-in-production')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Server-specific settings for Docker
ADMINS = [('Docker Admin', 'admin@example.com')]
MANAGERS = ADMINS

# Time zone settings
TIME_ZONE = 'Europe/Amsterdam'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Site ID
SITE_ID = 2

# Locale paths
LOCALE_PATHS = [BASE_DIR+'conf/locale', BASE_DIR+'signbank/registration/locale']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/app/writable/database/signbank.db',
        'TEST': {
            'NAME': '/app/writable/database/test-signbank.db',
        }
    }
}

# Media and static files
MEDIA_ROOT = WRITABLE_FOLDER
MEDIA_URL = '/media/'
MEDIA_MOBILE_URL = MEDIA_URL

STATIC_ROOT = '/app/writable/static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, "media"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Middleware
MIDDLEWARE = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'signbank.pages.middleware.PageFallbackMiddleware',
    'reversion.middleware.RevisionMiddleware',
    'django.middleware.common.CommonMiddleware'
)

# CORS settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates/global-templates'),
                 os.path.join(PROJECT_DIR, 'signbank/registration/templates/')],
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "signbank.context_processors.url",
                "signbank.pages.context_processors.menu",
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

# Authentication backends
AUTHENTICATION_BACKENDS = (
    "signbank.registration.EmailBackend",
    "django.contrib.auth.backends.ModelBackend",
    'guardian.backends.ObjectPermissionBackend',
)

AUTH_PROFILE_MODULE = 'dictionary.UserProfile'

# Internal IPs
INTERNAL_IPS = ('127.0.0.1',)

# URL configuration
ROOT_URLCONF = 'signbank.urls'
WSGI_APPLICATION = 'signbank.wsgi.application'

# Installed apps
INSTALLED_APPS = (
    'colorfield',
    'modeltranslation',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'corsheaders',
    'reversion',
    'tagging',
    'guardian',
    'bootstrap3',
    'django_summernote',
    'signbank.dictionary',
    'signbank.feedback',
    'signbank.pages',
    'signbank.attachments',
    'signbank.video'
)

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Signbank specific settings
DO_LOGGING = False
LOG_FILENAME = "debug.log"

ANON_SAFE_SEARCH = False
ANON_TAG_SEARCH = False
SIGN_NAVIGATION = False

# File paths
UPLOAD_ROOT = MEDIA_ROOT + "upload/"
UPLOAD_URL = MEDIA_URL + "upload/"
COMMENT_VIDEO_LOCATION = "comments"
PAGES_VIDEO_LOCATION = 'pages'
VIDEO_UPLOAD_LOCATION = "upload"
ATTACHMENT_LOCATION = 'attachments'

# Various directory settings
GLOSS_VIDEO_DIRECTORY = 'glossvideo'
EXAMPLESENTENCE_VIDEO_DIRECTORY = 'sensevideo'
ANNOTATEDSENTENCE_VIDEO_DIRECTORY = 'annotatedvideo'
GLOSS_IMAGE_DIRECTORY = 'glossimage'
FEEDBANK_VIDEO_DIRECTORY = 'comments'
HANDSHAPE_IMAGE_DIRECTORY = 'handshapeimage'
OTHER_MEDIA_DIRECTORY = 'othermedia/'
IMAGES_TO_IMPORT_FOLDER = 'import_images/'
VIDEOS_TO_IMPORT_FOLDER = 'import_videos/'
API_VIDEO_ARCHIVES = 'api_video_archives/'
OTHER_MEDIA_TO_IMPORT_FOLDER = 'import_other_media/'
SIGNBANK_PACKAGES_FOLDER = 'packages/'
EAF_FILES_LOCATION = 'eaf/'
DATASET_EAF_DIRECTORY = 'eafs'
DATASET_METADATA_DIRECTORY = 'metadata_eafs'
TEST_DATA_DIRECTORY = 'test_data'
BACKUP_VIDEOS_FOLDER = 'video_backups'
DELETED_FILES_FOLDER = 'prullenmand'

TMP_DIR = '/tmp'
METADATA_LOCATION = 'metadata.csv'
FFMPEG_PROGRAM = "ffmpeg"

# Signbank configuration
LANGUAGE_NAME = 'Global'
COUNTRY_NAME = 'Docker'
SIGNBANK_VERSION_CODE = 'mysignbank'
URL = 'http://localhost:8000/'
PREFIX_URL = ''

# Language settings
gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
)
MODELTRANSLATION_LANGUAGES = ['en']
MODELTRANSLATION_FIELDCHOICE_LANGUAGES = ['en']
LANGUAGES_LANGUAGE_CODE_3CHAR = (
    ('en', 'eng'),
)
INTERFACE_LANGUAGE_SHORT_NAMES = ['EN']
LANGUAGE_CODE = "en"
DEFAULT_KEYWORDS_LANGUAGE = {'language_code_2char': 'en'}
DEFAULT_LANGUAGE_HEADER_COLUMN = {'English': 'name_en'}
FALLBACK_FIELDCHOICE_HUMAN_LANGUAGE = 'english'
SHOW_ENGLISH_ONLY = False
SEPARATE_ENGLISH_IDGLOSS_FIELD = True
LANGUAGE_CODE_MAP = [
    {2: 'en', 3: 'eng'}
]

# Quick update fields
QUICK_UPDATE_GLOSS_FIELDS = ['signlanguage', 'dialect']

# Login settings
ALWAYS_REQUIRE_LOGIN = True
ALLOW_REGISTRATION = True
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_URL = PREFIX_URL+'/accounts/login/'
LOGIN_REDIRECT_URL = PREFIX_URL+'/accounts/user_profile/'

# Video settings
FFMPEG_TIMEOUT = 60
FFMPEG_OPTIONS = ["-vcodec", "h264", "-an"]
VIDEO_ASPECT_RATIO = 3.0/4.0

# Tagging
FORCE_LOWERCASE_TAGS = False

# CSS
PRIMARY_CSS = "css/"+SIGNBANK_VERSION_CODE+"/main.css"

# Mimetypes
import mimetypes
mimetypes.add_type("video/mp4", ".mov", True)

# Test runner
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Other settings
EARLIEST_GLOSS_CREATION_DATE = datetime(2015,1,1)
SUPPORTED_CITATION_IMAGE_EXTENSIONS = ['.jpg','.jpeg','.png']
MAXIMUM_UPLOAD_SIZE = 5000000
DATA_UPLOAD_MAX_NUMBER_FIELDS = None
DATA_UPLOAD_MAX_MEMORY_SIZE = None

# Django 4 compatibility
django.utils.encoding.smart_text = smart_str
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# ECV settings
ECV_FOLDER = 'ecv/'
ECV_FILE = 'myecv.ecv'
ECV_FOLDER_ABSOLUTE_PATH = WRITABLE_FOLDER + ECV_FOLDER

# Default dataset
DEFAULT_DATASET = 'Docker Dataset'
DEFAULT_DATASET_ACRONYM = 'DOCKER'
DEFAULT_DATASET_LANGUAGE_ID = 1
DEFAULT_DATASET_PK = 1
TEST_DATASET_ACRONYM = 'TESTDB'

# Feature flags
SHOW_MORPHEME_SEARCH = True
SHOW_LETTER_NUMBER_PHONOLOGY = True
SHOW_FIELD_CHOICE_COLORS = True
SHOW_DATASET_INTERFACE_OPTIONS = True
SHOW_NAMED_ENTITY = False
USE_HANDSHAPE = True
USE_DERIVATIONHISTORY = True
USE_FIELD_CHOICE_FOREIGN_KEY = True

# API settings
API_FIELDS = ['idgloss']

# Performance settings
RECENTLY_ADDED_SIGNS_PERIOD = timedelta(days=90)
DATE_FORMAT = "%Y-%m-%d"
SPEED_UP_RETRIEVING_ALL_SIGNS = True
DELETE_FILES_ON_GLOSSVIDEO_DELETE = False
ESCAPE_UPLOADED_VIDEO_FILE_PATH = False
USE_X_SENDFILE = False
MAX_SCROLL_BAR = 500

# Show numbersigns (from base.py)
SHOW_NUMBERSIGNS = True

# Email settings
DEFAULT_FROM_EMAIL = 'noreply@localhost'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEBUG_EMAILS_ON = False

# Admin settings
ADMIN_URL = 'admin'
LOGOUT_REDIRECT_URL = '/'

# File system settings
FILESYSTEM_SIGNBANK_GROUPS = ['signbank', 'www-data', 'signbank-writable', 'wwwsignbank']

# Debug flags
DEBUG_CSV = False
DEBUG_SENSES = False
DEBUG_VIDEOS = False
DEBUG_API = False

# Deletion settings
GUARDED_GLOSS_DELETE = False
GUARDED_MORPHEME_DELETE = True

# File upload settings
FILE_UPLOAD_HANDLERS = ['django.core.files.uploadhandler.TemporaryFileUploadHandler',]
FILE_UPLOAD_MAX_MEMORY_SIZE = 15728640  # 15 MB

# Other settings for compatibility
SHARE_SENSES = False
CROP_GLOSS_IMAGES = True
MINIMUM_OVERLAP_BETWEEN_SIGNING_HANDS = 40
DISABLE_MOVING_THUMBNAILS_ABOVE_NR_OF_GLOSSES = 200

# Field definitions for completeness (can be customized)
DEFINITION_FIELDS = ['general', 'noun', 'verb', 'interact', 'deictic', 'modifier', 'question', 'augment', 'note']

# From all possible gloss fields available, display these
FIELDS = {}

FIELDS['main'] = ['useInstr', 'wordClass']

PUBLIC_MAIN_FIELDS = ['wordClass']

# fields are ordered per kind: Field Choice Lists, Text, Boolean
# followed by etymology and articulation
FIELDS['phonology'] = ['handedness', 'domhndsh', 'subhndsh', 'handCh', 'relatArtic', 'locprim',
                       'contType', 'movSh', 'movDir',
                       'repeat', 'altern',
                       'relOriMov', 'relOriLoc', 'oriCh',
                       'locVirtObj', 'phonOth', 'mouthG', 'mouthing', 'phonetVar',
                       'domhndsh_letter', 'domhndsh_number', 'subhndsh_letter', 'subhndsh_number',
                       'weakdrop', 'weakprop']

PUBLIC_PHONOLOGY_FIELDS = ['handedness', 'domhndsh', 'subhndsh', 'handCh', 'relatArtic', 'locprim',
                           'contType', 'movSh', 'movDir',
                           'repeat', 'altern',
                           'relOriMov', 'relOriLoc', 'oriCh',
                           'domhndsh_letter', 'domhndsh_number', 'subhndsh_letter', 'subhndsh_number',
                           'weakdrop', 'weakprop']

FIELDS['semantics'] = ['semField', 'derivHist', 'namEnt','valence','iconImg','concConcSet']

PUBLIC_SEMANTICS_FIELDS = ['semField']

FIELDS['frequency'] = ['tokNo','tokNoSgnr']

FIELDS['handshape'] = ['hsNumSel','hsFingSel','hsFingSel2','hsFingConf','hsFingConf2','hsAperture','hsSpread',
                       'hsFingUnsel','fsT','fsI','fsM','fsR','fsP','fs2T','fs2I','fs2M','fs2R','fs2P','ufT','ufI','ufM',
                       'ufR','ufP']

FIELDS['publication'] = ['inWeb', 'isNew']

FIELDS['properties'] = ['hasvideo', 'hasnmevideo', 'hasothermedia', 'hasmultiplesenses', 'hasannotatedsentences',
                        'definitionRole', 'definitionContains', 'defspublished',
                        'createdBy', 'createdAfter', 'createdBefore',
                        'tags', 'excludeFromEcv']
FIELDS['relations'] = ['relation', 'hasRelation', 'relationToForeignSign', 'hasRelationToForeignSign']
FIELDS['morpheme'] = ['morpheme', 'isablend', 'ispartofablend']
FIELDS['morpheme_properties'] = ['hasvideo',
                                 'definitionRole', 'definitionContains', 'defspublished',
                                 'createdBy', 'createdAfter', 'createdBefore',
                                 'tags']

GLOSS_CHOICE_FIELDS = ['handedness', 'domhndsh', 'subhndsh', 'handCh', 'relatArtic', 'locprim',
                       'relOriMov',
                       'relOriLoc', 'oriCh', 'contType', 'movSh', 'movDir', 'wordClass',
                       'semField', 'derivHist', 'namEnt', 'valence',
                       'definitionRole', 'hasComponentOfType', 'mrpType', 'hasRelation']

GLOSSSENSE_CHOICE_FIELDS = ['handedness', 'domhndsh', 'subhndsh', 'handCh', 'relatArtic', 'locprim',
                            'relOriMov',
                            'relOriLoc', 'oriCh', 'contType', 'movSh', 'movDir', 'wordClass',
                            'semField', 'derivHist', 'namEnt', 'valence',
                            'definitionRole', 'hasComponentOfType']

# these are the multiple select fields for Morpheme Search, the field definitionRole is a search form field,
# the field mrpType appears in Morpheme, the rest are also in Gloss
MORPHEME_CHOICE_FIELDS = ['handedness', 'handCh', 'relatArtic', 'locprim', 'relOriMov',
                          'relOriLoc', 'oriCh', 'contType', 'movSh', 'movDir', 'mrpType', 'wordClass',
                          'semField', 'derivHist', 'namEnt', 'valence', 'definitionRole']

# Use these fields in the server specific settings to specify frequency fields, if available
FREQUENCY_CATEGORIES = []
FREQUENCY_REGIONS = []
FREQUENCY_FIELDS = {}

# the following are used to avoid using fieldnames in the code
# although these are all Boolean fields
# it's not sufficient to identify per type because repeat and altern are also Booleans
HANDSHAPE_ETYMOLOGY_FIELDS = ['domhndsh_letter','domhndsh_number','subhndsh_letter','subhndsh_number']
HANDEDNESS_ARTICULATION_FIELDS = ['weakdrop','weakprop']

# Use these fields to figure out which glosses are minimal pairs
MINIMAL_PAIRS_FIELDS = ['handedness','domhndsh','subhndsh','handCh','relatArtic','locprim','relOriMov','relOriLoc',
                        'oriCh','contType','movSh','movDir','repeat','altern']
MINIMAL_PAIRS_SEARCH_FIELDS = MINIMAL_PAIRS_FIELDS + ['namEnt','semField','valence']
MINIMAL_PAIRS_CHOICE_FIELDS = ['handedness', 'domhndsh', 'subhndsh', 'handCh', 'relatArtic', 'locprim', 'relOriMov',
                               'relOriLoc', 'oriCh', 'contType', 'movSh', 'movDir', 'namEnt', 'semField', 'valence']

# Display these fields as columns in the list view
GLOSS_LIST_DISPLAY_FIELDS = ['handedness', 'domhndsh', 'subhndsh', 'locprim']

# These are fields in the Search forms by panel
SEARCH_BY = {}
# the ordering of the list of publication fields is important for the Gloss Search template
SEARCH_BY['publication'] = FIELDS['publication'] + FIELDS['properties']
SEARCH_BY['morpheme_publication'] = FIELDS['publication'] + FIELDS['morpheme_properties']
SEARCH_BY['relations'] = FIELDS['relations']
SEARCH_BY['morpheme'] = ['morpheme', 'hasComponentOfType', 'mrpType', 'isablend', 'ispartofablend']

QUERY_DISPLAY_FIELDS = MINIMAL_PAIRS_SEARCH_FIELDS
SHOW_QUERY_PARAMETERS_AS_BUTTON = True

# fields are ordered per kind: Field Choice Lists, Text, Boolean
MORPHEME_DISPLAY_FIELDS = ['handedness', 'handCh', 'relatArtic', 'locprim', 'relOriMov', 'relOriLoc', 'oriCh',
                           'contType', 'movSh', 'movDir', 'locVirtObj', 'phonOth', 'repeat', 'altern']

# The following fields have been implemented
# OBLIGATORY_FIELDS = ['videofile', 'handedness', 'domhndsh', 'subhndsh',
#                      'domhndsh_number', 'domhndsh_letter', 'subhndsh_number', 'subhndsh_letter']
OBLIGATORY_FIELDS = []

HANDSHAPE_RESULT_FIELDS = ['name',
                           'hsFingSel', 'hsFingConf', 'hsFingSel2', 'hsFingConf2', 'hsNumSel',
                           'hsFingUnsel', 'hsSpread', 'hsAperture']

# Initialize required variables that might be referenced
REGEX_SPECIAL_CHARACTERS = '[+]'
USE_REGULAR_EXPRESSIONS = False
LEFT_DOUBLE_QUOTE_PATTERNS = '[\"\u201c]'
RIGHT_DOUBLE_QUOTE_PATTERNS = '[\"\u201d]'