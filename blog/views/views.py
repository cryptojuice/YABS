from flask import Flask, request, session, redirect, url_for,\
         abort, render_template, flash, Blueprint, escape

from pymongo import Connection

connection = Connection()
db = connection.yabs

main = Blueprint('main', __name__)

@main.route('/posts', methods=['GET'])
def get_posts():
 post = db.posts.find_one()
 return str(post)

@main.route('/posts/new', methods=['POST'])
def submit_post():
    pass

@main.route('/posts/update', methods=['PUT'])
def update_post():
    pass

@main.route('/posts/delete', methods=['DELETE'])
def delete_post():
    pass


