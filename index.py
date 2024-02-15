from flask import Flask, jsonify, request, render_template, url_for, redirect

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def get_maessage():
    if request.method == "GET":
        return {"status": "success-get", "result": post_maessage()}

@app.route('/', methods=['GET', 'POST'])
def post_maessage():
    name = input("give your input: ")
    return name


if __name__ == '__main__':
    app.run(debug=True)