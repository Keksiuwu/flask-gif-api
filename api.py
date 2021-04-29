import flask
import random
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/images/<endpoint>', methods=['GET'])
def api(endpoint):
    return f'https://cdn.keksi.me/images/{endpoint}/' + (str(random.choice(os.listdir(f"D:\\API\\{endpoint}"))))


app.run(host="0.0.0.0", port=8888)
