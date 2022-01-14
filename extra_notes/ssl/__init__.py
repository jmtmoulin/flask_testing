from crypt import methods
from flask import Flask, request, render_template, abort, jsonify
# import flask.ext.excel
import json
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug import secure_filename
import pandas as pd
from io import StringIO



app = Flask(__name__)
auth = HTTPBasicAuth()
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'csv', 'json'}
app.config['MAX_CONTENT_LENGTH'] = 3* 1024 * 1024
users = {
    "jacob": generate_password_hash("moulin")
    # "susan": generate_password_hash("bye")
}
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route("/")
@auth.login_required
def main():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/post_json", methods=["POST"])
@auth.login_required
def post_json():
    content = request.get_json()
    print(type(content))
    if content == None:
        print("FAILURE")
        return ('', 204)
    else:
        print("SUCCESS")
        return jsonify(content)

@app.route("/post_file", methods=["POST"])
@auth.login_required
def post_file():
    file = request.files['file']
    print(request.data)
    if file:
        filename = secure_filename(file.filename)
        print(str(request.values))
        print(str(request.files))
        print("Updated String: " + str(file.read().decode("utf-8")))
        print(filename)
        print(type(filename))
        return "True"
    else:
        return "False"


@app.route("/post_certain_extensions", methods=["POST"])
@auth.login_required
def post_certain_extensions():
    file = request.files['file']
    print(request.data)
    if file:
        filename = secure_filename(file.filename)
        filename_extension = filename.rsplit('.', 1)[1].lower() 
        if filename_extension in ALLOWED_EXTENSIONS:
            print("SUCCESSFUL")
            return ("True", 200)
        else:
            print("NOT ALLOWED EXTENSIONS")
            return ("False",400)
    else:
        print("NO FILE FOUND")
        return ("False",400)

@app.route("/post_if_json", methods=["POST"])
@auth.login_required
def post_if_json():
    file = request.files['file']
    # print(request.data)
    if file:
        filename = secure_filename(file.filename)
        filename_extension = filename.rsplit('.', 1)[1].lower() 
        if filename_extension in ALLOWED_EXTENSIONS:
            # print("SUCCESSFUL")
            try: 
                json_content = json.loads(str(file.read().decode("utf-8")))
                print("SUCCESSFUL")
                print(str(json_content))
                return ("SUCCESSFUL",200)
            except ValueError:
                print("NOT JSON")
                return ("False",400)
        else:
            print("NOT ALLOWED EXTENSIONS")
            return ("False",400)
    else:
        print("NO FILE FOUND")
        return ("False",400)

@app.route("/post_if_csv", methods=["POST"])
@auth.login_required
def post_csv():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        filename_extension = filename.rsplit('.', 1)[1].lower() 
        if filename_extension in ['csv']:
            # try:
            file_content = file.read().decode("utf-8")
            # print(str(file_content))
            df = pd.read_csv(StringIO(file_content))
            print(df)
            print(type(df))
            print(df.head())
            print(df.columns)
            for col in df.columns:
                print(col)
                print(df[col].dropna(axis=0))
                print("#################")
            
            return("Success", 200)
            # except:
            #     print("NOT CSV")
            #     return("Failure", 400)
        else:
            print("NOT CSV FILE")
            return("Failure", 400)

@app.route("/post_if_csv_to_template", methods=["POST"])
@auth.login_required
def post_if_csv_to_template():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        filename_extension = filename.rsplit('.', 1)[1].lower() 
        if filename_extension in ['csv']:
            # try:
            file_content = file.read().decode("utf-8")
            # print(str(file_content))
            df = pd.read_csv(StringIO(file_content))
            return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)
            # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html
        else:
            print("NOT CSV FILE")
            return("Failure", 400)
    else:
        return("", 204)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=255, ssl_context=('cert.pem', 'key.pem'))

# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
# python3 -m pip install flask-login
# python3 -m pip install flask-sqlalchemy
# https://flask-httpauth.readthedocs.io/en/latest/
# curl -XGET "https://cernccwaam01:255/" -u 'jacob:moulin' --cacert /home/jm054897/HEARST/cert.pem  --key /home/jm054897/HEARST/cert.key -k
# curl -XPOST "https://cernccwaam01:255/post_json" -u 'jacob:moulin' --cacert /home/jm054897/HEARST/cert.pem  --key /home/jm054897/HEARST/cert.key -k -vv -H 'Content-Type: application/json' -d'{"title": "The Godfather","director": "Francis Ford Coppola","year": 1972 }'
# curl -XPOST "https://cernccwaam01:255/post_file" -u 'jacob:moulin' --cacert /home/jm054897/HEARST/cert.pem  --key /home/jm054897/HEARST/cert.key -k -F "file=@testing_post_file.txt"
# curl -XPOST "https://cernccwaam01:255/post_file" -u 'jacob:moulin' --cacert /home/jm054897/HEARST/cert.pem  --key /home/jm054897/HEARST/cert.key -k -F "file=@testing_post_file.txt"
# curl -XPOST "https://cernccwaam01:255/post_certain_extensions" -u 'jacob:moulin' --cacert /home/jm054897/HEARST/cert.pem  --key /home/jm054897/HEARST/cert.key -k -F "file=@testing_post_file.exe"
# curl -XPOST "https://cernccwaam01:255/post_if_csv" -u 'jacob:moulin' --cacert /home/jm054897/HEARST/cert.pem  --key /home/jm054897/HEARST/cert.key -k -F "file=@ESD__csv_example_please.csv"
# python3 -m venv /home/jm054897/HEARST/bin
# source /home/jm054897/HEARST/env/bin/activate
# /home/jm054897/HEARST/env/bin/pip install -r requirements.txt

#### EXCEL ####
# https://pypi.org/project/Flask-Excel/

