from flask import Blueprint, render_template, request
from app.embedding import get_image_embedding
from app.elasticsearch_helper import save_image
from app.routes.image_similarity_search import convert_image_to_data_uri
from PIL import Image

image_upload_routes = Blueprint('image_upload_routes', __name__)

@image_upload_routes.route('/image_embedding_upload', methods=['GET', 'POST'])
def upload():
    message = ""
    if request.method == 'POST':
        files = request.files.getlist('files')
        for uploaded_file in files:
            if uploaded_file.filename != '':
                image = Image.open(uploaded_file)
                image_id = uploaded_file.filename

                image_data = convert_image_to_data_uri(image)
                embedding = get_image_embedding(image)
                save_image(image_id, embedding, image_data)

        message = "Upload successful!"
    return render_template('upload.html', message=message)