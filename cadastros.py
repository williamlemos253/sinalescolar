from bottle import get, post, static_file, template, route, request
import os, sqlite3
import re


#conecta ao banco de dados
conn = sqlite3.connect('./database/database.db')
c = conn.cursor()

@route('/cadastro')
def cadastrohorario():
    return template('cadastrohorario')

#Recebe os dados do formulário válida e insere no banco de dados
@route('/cadastro', method='POST')
def do_cadastrohorario():
    domingo = request.forms.get('domingo')
    if float(domingo) > 1:
        return template('errograve')

    segunda = request.forms.get('segunda')
    if float(segunda) > 1:
        return template('errograve')

    terca = request.forms.get('terca')
    if float(terca) > 1:
        return template('errograve')

    quarta = request.forms.get('quarta')
    if float(quarta) > 1:
        return template('errograve')

    quinta = request.forms.get('quinta')
    if float(quarta) > 1:
        return template('errograve')

    sexta = request.forms.get('sexta')
    if float(sexta) > 1:
        return template('errograve')

    sabado = request.forms.get('sabado')
    if float(sabado) > 1:
        return template('errograve')

#Válida o horário usando regex
    horario = request.forms.get('horario')
    comparahorario = re.compile('^(1?[0-9]|2[0-3]):[0-5][0-9]$')
    if comparahorario.match(horario):
        print ('Horário válido')
    else:
        return template('errograve')

    duracao = request.forms.get('duracao')
    if float(duracao) > 99:
        return template('errograve')

#válida o formato do upload
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.mp3','.ogg','.wav','.m4a','.aac'):
        return template('erromusica')


#Insere os dados no banco de dados
    dados =[domingo, segunda, terca, quarta, quinta, sexta, sabado, horario, duracao, upload.filename]
    c.execute('''insert into horarios (domingo, segunda, terca, quarta, quinta,
    sexta, sabado, horario, duracao, nomemusica )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', dados)


#Salva o caminho do upload e faz o upload
    save_path = "./static/upload/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = "{path}{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path, overwrite=True)

    #Verifica se os campos obrigatórios foram preenchidos e fecha o banco de dados
    conn.commit()
    c.close()
    print('dados inseridos com sucesso')
    return "<p>Horário cadastrado com sucesso.</p>"
