""" Modelo de datos de Votación """

class Vote(object):
    """ Constructor """
    def __init__(self):
        self.year = '2018'
        self.title = 'Elecciones Presidenciales'
        self.start_date = '03/12/2017'
        self.end_date = '03/01/2018'
        self.candidates = [
            {'name': 'Gian Ramírez'},
            {'name': 'Jennifer Aranda'},
            {'name': 'Diego Martinez'}
        ]
