from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    # Comentário
    return 'Paulo Côto!'


if __name__ == '__main__':
    app.run()
