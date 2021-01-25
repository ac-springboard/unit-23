from flask import g, request

from blogly import Init

app = Init.create_app()


@app.before_first_request
def before_first_request():
    g.URL_ROOT = request.url_root


if __name__ == '__main__':
    app.run(debug=True)
