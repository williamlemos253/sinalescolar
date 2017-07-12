from bottle import route, template, request, post, static_file, get
import os


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


@route('/cadastro')
def cadastrohorario():
    return template('cadastrohorario')


@route('/cadastro', method='POST')
def do_cadastrohorario():
    domingo = request.forms.get('domingo')
    if float(domingo) > 1:
        return template('errograve')

    segunda = request.forms.get('segunda')
    if float(segunda) > 1: 
        return template('errograve')

    terca = request.forms.get('terca')
    quarta = request.forms.get('quarta')
    quinta = request.forms.get('quinta')
    sexta = request.forms.get('sexta')
    sabado = request.forms.get('sabado')
    horario = request.forms.get('horario')
    duracao = request.forms.get('duracao')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.mp3','.ogg','.wav','.m4a','.aac'):
        return 'File extension not allowed.'

    save_path = "./static/upload/"

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = "{path}{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path, overwrite=True)
    return "A música foi salva com sucesso '{0}'.".format(save_path)

    if check_cadastro(horario, duracao, upload):
        return "<p>Horário cadastrado com sucesso.</p>"
    else:
        return "<p>O cadastro do horário falhou, por favor tente novamente.</p>"
