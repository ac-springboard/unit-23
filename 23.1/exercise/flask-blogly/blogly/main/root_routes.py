from flask import Blueprint, \
    redirect, request, g

root_routes = Blueprint('root_routes',
                        __name__,
                        template_folder="templates",
                        static_folder="static")


@root_routes.route('/')
def main_root():
    print('*********G.URL_ROOT:', g.URL_ROOT)
    return redirect('/blogly')
    # return render_template('landing_page.html');
