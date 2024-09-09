from app.elasticsearch_initializer import elasticsearch_client, index_name_image, index_name_text

def save_image(image_id, embedding, image_data):
    #function to store an image in the elastic index
    #TODO implement

   return ""
    
    
def save_product(product_id, embedding, image_data, product_name="", product_description=""):
    #function to store a product in the elastic index
    #TODO implement

   return ""

def search_similar_items(query_embedding, index_name, top_k=15, min_score=0.8):
    #function to search in the elastic index for similiar items
    #TODO implement

   return ""

def get_all(offset, per_page, selected_index):
    #function to get all items of an index
    query = {
        "query": {
            "match_all": {}
        },
        "from": offset,
        "size": per_page
    }
    response = elasticsearch_client.search(index=selected_index, body=query)
    return response

def delete_all_images_in_index(selected_index):
    #function to delete an index
    elasticsearch_client.indices.delete(index=selected_index, ignore=[400, 404])
    
    
def index_exists(index_name):
    #check if an index exists
    return elasticsearch_client.indices.exists(index=index_name)

def getRelevantTextData(response):
     return [(hit["_id"], hit["_score"], hit["_source"]['image_data'], hit["_source"]['product_name'], hit["_source"]['product_description']) for hit in response["hits"]["hits"]]
 
def getRelevantImageData(response):
    return [(hit["_id"], hit["_score"], hit["_source"]['image_data']) for hit in response["hits"]["hits"]]  