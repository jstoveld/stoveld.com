from flask import Flask, jsonify, request, render_template
from serverless_wsgi import handle_request

app = Flask(__name__, static_url_path='', static_folder='static')

## Front End Route
@app.route('/')
def home():
    return render_template('index.html')

# Define your backend routes here
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'key': 'value'}
    return jsonify(data)

def handler(event, context):
    return handle_request(app, event, context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


# if __name__ == '__main__':
#     app.run()
#     app.run(host='0.0.0.0', port=80)