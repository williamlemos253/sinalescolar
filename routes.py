from bottle import route, template, request, static_file
import os
import re


@route('<filename:re:.*\.css>')
def css(filename):
    return static_file(filename,root='./static/css',mimetype='text/css')

@route('<filename:re:.*\.js>')
def js(filename):
    return static_file(filename,root='./static/js',mimetype='text/javascript')

@route('/')
def index():
    return template ('index')

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)
