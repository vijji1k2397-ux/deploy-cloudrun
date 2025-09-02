from flask import Flask
import OS
app = Flask(__name__)

@app.route('/')
def hello():
    return 'This service deployed using github actions!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
