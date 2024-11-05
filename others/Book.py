class Book:
    def __init__(self, title, author, launch_year, closed):
        self.title = title
        self.author = str(author)
        self.launch_year = launch_year
        self.closed = closed

    def read(self):
        if not self.closed:
            print('Lendo o livro...')
        else:
            print('Abra o livro antes de iniciar a leitura')

    def open(self):
        print('Abrindo o livro...')
        self.closed = False

    def close(self):
        print('Fechando o livro...')
        self.closed = True