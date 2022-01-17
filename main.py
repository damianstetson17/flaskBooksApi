from flask import Flask, jsonify
from werkzeug.wrappers import response
from dataset import *

app = Flask(__name__)

@app.route('/books/favorites/angy')
def libros_angy():
    return jsonify(angy_list)

@app.route('/books/favorites/diana')
def libros_diana():
    return jsonify(diana_list)

@app.route('/books/favorites/damian')
def libros_damian():
    return jsonify(damian_list)

@app.route('/books/find/all')
def get_all_libro():
        if len(libros) > 0:
            return jsonify(libros) 
        else:
            return jsonify({'result':'null'})

@app.route('/books/find/<string:book_name>')
def get_libro(book_name):

    if len(libros) > 0:
        response = jsonify({'result':'null'}) 
        for book in libros:
            if book['name'] == book_name:
                response = jsonify(book)
            return response
    else:
        return jsonify({'result':'null'}) 

if __name__ == '__main__':
    app.run(debug = True, port=4000)