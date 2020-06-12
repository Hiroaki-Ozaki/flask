from flask import Flask, request, jsonify, abort
from keras.preprocessing import image
import numpy as np
from keras.models import load_model

app = Flask(__name__)

import tensorflow as tf
graph = tf.get_default_graph()

@app.route('/api/predict', methods=["POST"])
def predict():
    global graph
    with graph.as_default():
        try:
            image_path = request.json["image_path"]
            img = image.load_img(image_path, target_size=(150, 150))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = x / 255.0
            result_predict = model.predict(x)
            response = {"status": "OK", "prediction": float(result_predict[0])}
            return jsonify(response)
        except Exception as e:
            print(e)
            abort(400)

@app.errorhandler(400)
def error_handler(error):
    response = {"status": "Error", "message": "Invalid Parameters"}
    return jsonify(response)


if __name__ == "__main__":
    model = load_model('dog_cat.h5')
    app.run(host="localhost")