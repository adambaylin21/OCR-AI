from flask import Flask, request, jsonify
import io
import os
from PIL import Image
from tesseract import snapImage001
import moondream as md

app = Flask(__name__)
model = md.vl(model="moondream-2b-int8.mf")

def read_image(image_bytes):
	image = Image.open(io.BytesIO(image_bytes))
	text = snapImage001(image)
	if text == "":
		print("Option 2")
		encoded_image = model.encode_image(image)
		answer = model.query(encoded_image, "Please transcribe it")["answer"]
		return answer

	return text

@app.route('/api/ocr', methods=['POST'])
def ocr_api():
	try:
		if 'file' not in request.files:
			return jsonify({'error': 'Image file not found'}), 400

		file = request.files['file']
		if file:
		# Đọc dữ liệu ảnh trực tiếp vào bộ nhớ dưới dạng bytes
			image_bytes = file.read()

		# Đọc văn bản từ ảnh
			text = read_image(image_bytes)

		# Trả về kết quả dưới dạng JSON
			return jsonify({'text': text}), 200

	except Exception as e:
		return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
	# pass
	# gunicorn -w 4 -b 0.0.0.0:3179 master:app
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 3179)))