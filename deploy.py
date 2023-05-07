# from flask import Flask, request, jsonify, render_template
# from fruits import model
# from fruits import predict_image_class
# # Create a Flask app
# app = Flask(__name__)
#
# # Define an API endpoint for image classification
# @app.route('/', methods=['POST', 'GET'])
# def predict():
#     img = str(request.args.get('file_path'))
#     print(img)
#     result = {"Output": predict_image_class(img)}
#
#     return jsonify(result)
# if __name__ == '__main__':
# 	app.run(debug=True)
###################################################
#
# from flask import Flask, request, jsonify, render_template
# from fruits import model
# from fruits import predict_image_class
#
# # Create a Flask app
# app = Flask(__name__)
#
# # Define an API endpoint for image classification
# @app.route('/', methods=['POST', 'GET'])
# def predict():
# 	if request.method == 'POST':--
# 		file = request.files.get('file')
# 		img = file.read()
# 		result = {"Output": predict_image_class(img)}
# 		return jsonify(result)
#
# 	return render_template('index.html')
#
# if __name__ == '__main__':
# 	app.run(debug=True)
###########################################
import os
from flask import Flask, request, jsonify, render_template
from fruits import model
from fruits import predict_image_class

# Create a Flask app
app = Flask(__name__)

# Define an API endpoint for image classification
@app.route('/', methods=['POST', 'GET'])
def predict():
	if request.method == 'POST':
		file = request.files.get('file')
		filename = file.filename
		file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		file.save(file_path)
		result = {"Output": predict_image_class(file_path)}
		os.remove(file_path)
		return jsonify(result)

	return render_template('index.html')

if __name__ == '__main__':
	app.config['UPLOAD_FOLDER'] = 'uploads'
	app.run(debug=True)
