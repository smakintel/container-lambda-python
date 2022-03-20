import awsgi
from flask import (
    Flask,
    jsonify,
)

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(status=200, message='OK')

@app.route('/kava/test')
def kava():
    return jsonify(status=200, message='Kava test')

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})