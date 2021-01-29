class ROOT:
    URL_ROOT = None
    APP_BASE = None
    APP_ROOT = None


class MISC:
    SAVE_BT = 'Save'
    CANCEL_BT = 'Cancel'


class USERS:
    PATH = None
    ROOT = None
    STATIC = None
    TEMPLATES = None
    LIST = None
    ADD = None
    EDIT = None
    VIEW = None
    DEL = None
    FIRST_NAME = None
    LAST_NAME = None
    IMAGE_URL = None


class POSTS:
    PATH = None
    ROOT = None
    STATIC = None
    TEMPLATES = None
    LIST = None
    ADD = None
    EDIT = None
    VIEW = None
    DEL = None
    TITLE = None
    CONTENT = None


class TAGS:
    PATH = None
    ROOT = None
    STATIC = None
    TEMPLATES = None
    LIST = None
    ADD = None
    EDIT = None
    VIEW = None
    DEL = None
    NAME = None


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
        USERS.LIST_PG = 'User List'
        USERS.LIST_BT = 'List Users'
        USERS.ADD_PG = 'Add User Form'
        USERS.ADD_BT = 'Add User'
        USERS.EDIT_PG = 'Edit User Form'
        USERS.EDIT_BT = 'Edit User'
        USERS.VIEW_PG = 'User View'
        USERS.VIEW_BT = 'View User'
        USERS.DEL_PG = 'Delete User Form'
        USERS.DEL_BT = 'Delete User'
        USERS.FIRST_NAME_LABEL = 'First Name'
        USERS.LAST_NAME_LABEL = 'Last Name'
        USERS.IMAGE_URL_LABEL = 'Image Url'

        POSTS.PATH = f'{ROOT.APP_BASE}/posts'
        POSTS.ROOT = f'{ROOT.APP_ROOT}/posts'
        POSTS.STATIC = f'{POSTS.ROOT}/static'
        POSTS.TEMPLATES = f'{POSTS.ROOT}/templates'
        POSTS.LIST_PG = 'Post List'
        POSTS.LIST_LABEL = 'Posts'
        POSTS.LIST_BT = 'List Posts'
        POSTS.ADD_PG = 'Add Post Form'
        POSTS.ADD_BT = 'Add Post'
        POSTS.EDIT_PG = 'Edit Post Form'
        POSTS.EDIT_BT = 'Edit Post'
        POSTS.VIEW_PG = 'Post View'
        POSTS.VIEW_BT = 'View Post'
        POSTS.DEL_BT = 'Delete Post'
        POSTS.TITLE_LABEL = 'Title'
        POSTS.CONTENT_LABEL = 'Content'

        TAGS.PATH = f'{ROOT.APP_BASE}/tags'
        TAGS.ROOT = f'{ROOT.APP_ROOT}/tags'
        TAGS.STATIC = f'{TAGS.ROOT}/static'
        TAGS.TEMPLATES = f'{TAGS.ROOT}/templates'
        TAGS.LIST_LABEL = 'Tags'
        TAGS.LIST_PG = 'Tag List'
        TAGS.LIST_BT = 'List Tags'
        TAGS.ADD_PG = 'Add Tag Form'
        TAGS.ADD_BT = 'Add Tag'
        TAGS.EDIT = 'Edit Tag'
        TAGS.EDIT_PG = 'Edit Tag Form'
        TAGS.EDIT_BT = 'Edit Tag'
        TAGS.VIEW_PG = 'Tag View'
        TAGS.VIEW_ = 'View Tag'
        TAGS.DEL_BT = 'Delete Tag'
        TAGS.NAME_LABEL = 'Name'

# Params.set_param_configs('http://localhost:5000')
#
# print(ROOT.__dict__)
# print(USERS.__dict__)
# print(POSTS.__dict__)
# print(TAGS.__dict__)
