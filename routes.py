from bottle import route, template, request, static_file
import os
import re


@route('<filename:re:.*\.css>')
def css(filename):
    return static_file(filename,root='./static/css',mimetype='text/css')

@route('<filename:re:.*\.js>')
def js(filename):
    return static_file(filename,root='./static/js',mimetype='text/javascript')
