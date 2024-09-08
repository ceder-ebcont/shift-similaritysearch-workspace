from flask import Blueprint, render_template, request
from app.elasticsearch_helper import get_all, delete_all_images_in_index, index_exists
from app.elasticsearch_initializer import index_name_image

browse_routes = Blueprint('browse_routes', __name__)

@browse_routes.route('/browse', methods=['GET', 'POST'])
def browse():
    selected_index = request.form.get('index_name', index_name_image)

    if request.method == 'POST':
        selected_index = request.form['index_name']
    
    if not index_exists(selected_index):
        message = f"No indices found in the selected index: {selected_index}"
        return render_template('browse.html', images=[], message=message, selected_index=selected_index)

    page = int(request.args.get('page', 1))
    per_page = 20
    offset = (page - 1) * per_page

    response = get_all(offset, per_page, selected_index)

    images = [(hit["_id"], hit["_source"]["image_data"]) for hit in response["hits"]["hits"]]

    total_hits = response['hits']['total']['value']
    total_pages = (total_hits + per_page - 1) // per_page

    return render_template('browse.html', images=images, page=page, total_pages=total_pages, selected_index=selected_index)

@browse_routes.route('/delete_all_images', methods=['POST'])
def delete_all_images():
    selected_index = request.form.get('index_name')
    delete_all_images_in_index(selected_index)
    return render_template('browse.html', images=[], selected_index=selected_index)
