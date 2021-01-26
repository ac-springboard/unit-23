from flask import request, g

from blogly import Init
from blogly.global_params import Params, ROOT, USERS, POSTS, TAGS

# from global import Params

app = Init.create_app()


@app.before_first_request
def before_first_request():
    Params.set_param_configs(request.url_root)


@app.before_request
def before_request():
    app.app_context()
    g.ROOT = ROOT
    g.USERS = USERS
    g.POSTS = POSTS
    g.TAGS = TAGS
    # print(g.ROOT, g.USERS, g.POSTS, g.TAGS)


if __name__ == '__main__':
    app.run(debug=True)
