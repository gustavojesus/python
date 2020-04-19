class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    def __str__(self):
        return f'Nome: {self.nome}  Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'

class Playlist(list):

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)




vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)


vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

# listinha = [atlanta, vingadores, tmep, demolidor]
filmes_e_series =  [atlanta, vingadores, tmep, demolidor]
#playlist_fim_de_semana = Playlist('dim de semana', filmes_e_series)
minha_playlist = Playlist('fim de semana', filmes_e_series)

for programa in minha_playlist.listagem:
    print(programa)

print(f'Tamanho: {len(minha_playlist.listagem)}')
#print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}')




# for programa in listinha:
#     print(programa)



# listinha = [atlanta, vingadores]
# for programa in listinha:
#     if hasattr(programa, 'duracao'):
#         detalhe = f'{programa.duracao} min'
#     else:
#         detalhe = f'{programa.temporadas} temporadas'

#     print(f'Nome: {programa.nome} - {detalhe} - Likes: {programa.likes}')


# for programa in listinha:
#     print(f'Nome: {programa.nome} - Likes: {programa.likes}')