from flask import Flask, request, session, redirect, url_for,\
         abort, render_template, flash, Blueprint, escape
from pymongo import Connection
from bson import ObjectId, json_util
from datetime import datetime
import json
import markdown2

connection = Connection()
collection = connection['yabs'].posts

main = Blueprint('main', __name__)

@main.route('/')
def index():
    post = [p for p in collection.find()]
    return render_template('index.html', post=post)

@main.route('/post/.json', methods=['GET'])
def show_post():
    post = [p for p in collection.find()]
    return render_template('index.html', post=post)

@main.route('/post/new', methods=['GET', 'POST'])
def create_post():
    if request.method == "POST":
        title = request.form['title']
        content_md = request.form['content']
        content =  markdown2.markdown(content_md)
        author =  request.form['author']
        tags = request.form['tags'].split(' ')
        date = datetime.strftime(datetime.now(),"%h %d, %Y")
        collection.insert({'title':title, 'content':content,'content_md':content_md,\
                'author':author, 'tags':tags, 'date':date})
        return redirect(url_for('main.index'));
    return render_template('form.html');

@main.route('/post/update/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    pass

@main.route('/post/delete/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    pass

@main.route('/about')
def about():
    pass


