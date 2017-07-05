from bottle import route, template, request, post
import os

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
    segunda = request.forms.get('segunda')
    terca = request.forms.get('terca')
    quarta = request.forms.get('quarta')
    quinta = request.forms.get('quinta')
    sexta = request.forms.get('sexta')
    sabado = request.forms.get('sabado')
    horario = request.forms.get('horario')
    duracao = request.forms.get('duracao')
    upload = request.files.get('upload')

    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.mp3','.wav','.m4a'):
        return "Somente músicas são aceitas"

    save_path = "./static/upload/"

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = "{path}{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)
    return "A música foi salva com sucesso '{0}'.".format(save_path)

    if check_cadastro(horario, duracao, upload):
        return "<p>Horário cadastrado com sucesso.</p>"
    else:
        return "<p>O cadastro do horário falhou, por favor tente novamente.</p>"
