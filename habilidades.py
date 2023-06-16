from flask_restful import Resource

# lista das habilidades
lista_habilidades = ['Python', 'Java', 'PHP', 'Django', 'MySQL', 'SQLServer', 'Windows', 'Flask', 'C#']


class Habilidades(Resource):

    # lista as habilidades
    def get(self):
        return lista_habilidades