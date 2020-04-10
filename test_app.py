import json
from io import BytesIO

from app import app

def test_base_route():
    response = app.test_client().get('/')
    assert response.get_data() == b'crop weed segmantation'
    assert response.status_code == 200


def test_bucket_name():

    with open('./input/002_image.png', 'rb') as img1:
        imgStringIO1 = BytesIO(img1.read())

    response =app.test_client().post('/predict',content_type='multipart/form-data',
                                    data={
                                          'file': (imgStringIO1, 'img1.jpg')})
    assert response.status_code == 200
