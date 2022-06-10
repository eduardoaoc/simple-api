from flask_restx import fields
from source.server.instance import server 

book= server.api.model('Book',{
    'id': fields.String(description='O ID do registro.'),
    'title': fields.String(required=True, min_legnth=1, max_legnth=200, description='O título do livro')
})
