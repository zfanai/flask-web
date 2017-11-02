#encoding:utf8

import os
rootdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

DEBUG=True


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# babel config
#
#: Default language.
# zh_Hans_CN , en
BABEL_DEFAULT_LOCALE = 'en'

#: Lock language.
#: If 'True', app language will lock to `BABEL_DEFAULT_LOCALE`.
#: If 'False', app language will match to user browser or
#: request :param:`lang`.
LANGUAGE_LOCK = True

# Language enabled list.
LANGUAGES = {
    'zh_Hans_CN': 'Chinese Simplified',
    'en': 'English'
}


CACHE_TYPE = 'filesystem'
CACHE_DIR = os.path.join(rootdir, 'data', 'cache')