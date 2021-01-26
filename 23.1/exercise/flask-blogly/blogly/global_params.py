class ROOT:
    URL_ROOT = None
    APP_BASE = None
    APP_ROOT = None


class USERS:
    PATH = None
    ROOT = None
    STATIC = None
    TEMPLATES = None


class POSTS:
    PATH = None
    ROOT = None
    STATIC = None
    TEMPLATES = None


class TAGS:
    PATH = None
    ROOT = None
    STATIC = None
    TEMPLATES = None


class Params:
    @staticmethod
    def set_param_configs(url_root):
        ROOT.URL_ROOT = url_root
        ROOT.APP_NAME = 'blogly'
        ROOT.APP_BASE = '/blogly'
        ROOT.APP_ROOT = ROOT.URL_ROOT + ROOT.APP_NAME

        USERS.PATH = f'{ROOT.APP_BASE}/users'
        USERS.ROOT = f'{ROOT.APP_ROOT}/users'
        USERS.STATIC = f'{USERS.ROOT}/static'
        USERS.TEMPLATES = f'{USERS.ROOT}/templates'

        POSTS.PATH = f'{ROOT.APP_BASE}/posts'
        POSTS.ROOT = f'{ROOT.APP_ROOT}/posts'
        POSTS.STATIC = f'{POSTS.ROOT}/static'
        POSTS.TEMPLATES = f'{POSTS.ROOT}/templates'

        TAGS.PATH = f'{ROOT.APP_BASE}/tags'
        TAGS.ROOT = f'{ROOT.APP_ROOT}/tags'
        TAGS.STATIC = f'{TAGS.ROOT}/static'
        TAGS.TEMPLATES = f'{TAGS.ROOT}/templates'


# Params.set_param_configs('http://localhost:5000')
#
# print(ROOT.__dict__)
# print(USERS.__dict__)
# print(POSTS.__dict__)
# print(TAGS.__dict__)
