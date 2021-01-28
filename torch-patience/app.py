from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict(model):
    if request.method == 'POST':
        # we will get the file from the request
        file = request.files['file']
        # convert that to bytes
        img_bytes = file.read()
        class_id, class_name = model.get_prediction(image_bytes=img_bytes)
        return jsonify({'class_id': class_id, 'class_name': class_name})

