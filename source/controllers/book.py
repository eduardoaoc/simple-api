from flask import Flask
from flask_restx import Api, Resource, api #swagger documentation
from source.server.instance import server 
from source.models.book import book


app, api= server.app, server.api

books=[
    {'id':0, 'title':'War and Peace'},
    {'id':1, 'title':'Clean Code'}
]


@api.route('/books')
class BookList(Resource):
    @api.marshal_list_with(book)
    def get(self):
        return books
        
    @api.expect(book, validate=True)    
    @api.marshal_list_with(book)
    def post(self):
        response= api.payload
        books.append(response)
        return response, 200  #successo     

