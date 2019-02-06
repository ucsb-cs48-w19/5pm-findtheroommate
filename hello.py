from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
@app.route("/home", methods=['POST'])
def home():
    return render_template('home.html')

@app.route("/post/new")
def new_post():
    return render_template('create_post.html', title='New Post')
    

@app.route("/success")
def success():
    name = request.args.get('user_name')
    email = request.args.get('user_email')
    gender = request.args.get('user_gender')
    description = request.args.get('user_description')

    json = {
        'name': name,
        'email': email,
        'gender': gender,
        'description': description
    }
    return jsonify(json)
    #return render_template('success.html', name = name, gender=gender,email=email, description=description)

if __name__ == "__main__":
    app.run(debug=True)