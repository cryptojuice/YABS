from flask import Flask, request, session, redirect, url_for,\
         abort, render_template, flash, Blueprint, escape
from pymongo import Connection
from bson import ObjectId, json_util
from datetime import datetime
import json

connection = Connection()
collection = connection['yabs'].posts

main = Blueprint('main', __name__)

@main.route('/post/.json', methods=['GET'])
def show_post():
    post = [p for p in collection.find()]
    return json.dumps(post, default=json_util.default)

@main.route('/post/new', methods=['POST'])
def create_post():
    author = request.form['author']
    title  = request.form['title']
    text   = request.form['text']
    tags   = request.form['tags'].split(' ')
    date   = datetime.now()
    collection.insert({'author':author, 'title':title, 'text':text, 'tags':tags, 'date':date})
    return True

@main.route('/post/update/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    pass

@main.route('/post/delete/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    pass


