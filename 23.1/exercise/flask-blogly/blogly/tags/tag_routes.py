from flask import render_template, Blueprint, redirect, request, g

from blogly.tags.tag_model import Tag

tag_routes = Blueprint('tag_routes', __name__,
                       url_prefix='/blogly',
                       static_folder="../tags")


@tag_routes.route('/tags')
def listing():
    tags = Tag.all(Tag)
    return render_template('tag_list.html',
                           page_title=g.TAGS.LIST_PG,
                           tags=tags)


@tag_routes.route('/tags/new', methods=['GET'])
def add_form():
    """
    Renders the Add Tag form. Sends some special variables to the front-end:
    - method: the method to be sent by the form on click on the 'Save' button.
    - crud: the operation to configure the form.

    'From' Context
    --------------
        Tags -> Add Tag

    """
    tag = Tag({})
    return render_template('tag_form.html',
                           method='POST',
                           crud='create',
                           page_title=g.TAGS.ADD_PG,
                           tag=tag)


@tag_routes.route('/tags/new', methods=['POST'])
def new():
    """
    Treats the POST request to add the a new post.

    'From' Context
    --------------
        Add Tag Form -> Save

    """
    dict_form = dict(request.form)
    tag_id = Tag.add(Tag, dict_form)
    return redirect(f'{g.TAGS.PATH}/{tag_id}')


@tag_routes.route('/tags/<int:tag_id>')
def details(tag_id):
    """
    Renders the form that shows the tag details.

    'From' Contexts
    ---------------
        Tags -> <Name on the List>
        Tag Add Form -> Save or Cancel
        Tag Edit Form -> Save or Cancel
    """
    tag = Tag.get(Tag, tag_id)
    return render_template('tag_view.html',
                           page_title=g.TAGS.VIEW_PG,
                           tag=tag,
                           posts=[])


@tag_routes.route('/tags/<int:tag_id>/edit')
def edit_form(tag_id):
    """Renders Edit Tag form. Sends some special variables to the front-end:

    - method: the method to be sent by the form on click on the 'Save' button.
    - crud: the operation to configure the form.

    'From' Contexts
    ---------------
        Tag View -> Edit
    """
    tag = Tag.get(Tag, tag_id)
    return render_template('tag_form.html',
                           method='POST',
                           crud='update',
                           page_title='Edit Tag',
                           tag=tag)


@tag_routes.route('/tags/<int:tag_id>/edit/save', methods=['POST'])
def save(tag_id):
    """
    Treats the POST request to update a tag.
    """
    dict_form = dict(request.form)
    dict_form['id'] = tag_id
    tag = Tag.get(Tag, tag_id)
    tag.update(dict_form)
    return redirect(f'{g.TAGS.PATH}/{tag_id}')


@tag_routes.route('/tags/<int:tag_id>/delete', methods=['POST'])
def delete(tag_id):
    """
    Treats the POST request to delete a tag.
    """
    tag = Tag.get(Tag, tag_id)
    tag.delete()
    return redirect('/blogly/list')
