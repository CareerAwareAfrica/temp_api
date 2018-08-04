from flask import Flask, jsonify, request, Response

from BookModel import *
from settings import *
import json

import jwt,datetime
from ApiUsersModel import ApiUsers

posts = Blog.get_all_posts()

DEFAULT_PAGE_LIMIT = 3

app.config['SECRET_KEY'] = 'meow'

@app.route('/login', methods=['POST'])
def get_token():
    request_data = request.get_json()
    username = str(request_data['username'])
    password = str(request_data['password'])

    match = ApiUsers.username_password_match(username, password)

    if match:
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
        token = jwt.encode({'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='H5256')
        return token
    else:
        return Response ('', 401, mimetype='application/json')

#GET /posts
@app.route('/posts')
def get_posts():
    token = request.args.get('token')
    try:
        jwt.decode(token, app.config['SECRET_KEY'])
    except:
        return jsonify({'error': 'Need a valid token to view this page'}); 401
    return jsonify({'blogs': posts})

#GET /post
@app.route('/posts/<int:blog_id>')
def get_post_by_blog_id(blog_id):
    return_value = Blog.ger_post(blog_id)
    return jsonify(return_value)

def validBlogObject(blogObject):
    if ("tittle" in blogObject and "post" in blogObject and "blog_id" in blogObject):
        return  True
    else:
        return False

#POST/posts
@app.route('/posts', methods=[POST])
def add_post():
    return_data = request.get_json()
    if (validBlogObject(return_data)):
        Blog.add_post(request_data['tittle'], request_data['post'], request_data['post_by'], request_data['meta_data'])
        response = Response("", status=201, mimetype='application/json')
        response.headers['Location'] = "/posts" + str(request_data['blog_id'])
        return response
    else:
        InvalidBlogObjectErrorMsg = {
            "error": "Invalid blog object passed in request"
            "helpString": "Data passed in similar to this {'tittle': 'posts', 'meta_date'}"
        }
        response = Response(json.dumps(invalidBlogObjectErrorMsg), status=400, mimetype='application/json')
        return  response;

app.run(port=5000)