from flask import Blueprint, jsonify, request
from models import books

books_blueprint = Blueprint('books', __name__)

# Add a new book
@books_blueprint.route('/', methods=['POST'])
def add_book():
    data = request.get_json()
    book_id = len(books) + 1
    data['id'] = book_id
    books.append(data)
    return jsonify(data), 201

# Get all books
@books_blueprint.route('/', methods=['GET'])
def get_books():
    return jsonify(books), 200

# Update a book
@books_blueprint.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    for book in books:
        if book['id'] == book_id:
            book.update(data)
            return jsonify(book), 200
    return jsonify({'error': 'Book not found'}), 404

# Delete a book
@books_blueprint.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'}), 200
