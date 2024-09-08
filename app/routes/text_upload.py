from flask import Blueprint, render_template, request
import csv
from app.embedding import get_text_embedding
from app.elasticsearch_helper import save_product
import requests
from PIL import Image
from io import BytesIO
from app.helper_functions import convert_image_to_data_uri

text_upload_routes = Blueprint('text_upload_routes', __name__)

@text_upload_routes.route('/text_upload', methods=['GET', 'POST'])
def upload():
    message = ""
    if request.method == 'POST':
        files = request.files.getlist('files')
        for uploaded_file in files:
            if uploaded_file.filename.endswith('.csv'):
                try:
                    csv_file = uploaded_file.read().decode('utf-8').splitlines()
                    csv_reader = csv.reader(csv_file)

                    headers = next(csv_reader)
                    id_index = headers.index('id')
                    product_name_index = headers.index('product_name')
                    description_index = headers.index('description')
                    image_url_index = headers.index('image_url')

                    for row in csv_reader:
                        if row:
                            product_id = row[id_index]
                            product_name = row[product_name_index]
                            description = row[description_index]
                            image_url = row[image_url_index]

                            combined_text = f"{product_name} {description}"
                            text_embedding = get_text_embedding(combined_text)

                            try:
                                image_response = requests.get(image_url)
                                image = Image.open(BytesIO(image_response.content))
                                image_data_uri = convert_image_to_data_uri(image)

                                save_product(product_id, text_embedding, image_data_uri, product_name, description)
                            except Exception as e:
                                print(f"Error downloading or processing image from {image_url}: {str(e)}")

                    message = "CSV Upload successful!"
                except Exception as e:
                    message = f"Failed to process CSV file: {str(e)}"
            else:
                message = "Please upload a valid CSV file."

    return render_template('upload.html', message=message, webshop=True)