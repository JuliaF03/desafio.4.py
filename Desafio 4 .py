Impress = ('Minha impressora esta pegando fogo')
Insect = ('tem um inseto no meu pc')
Site = ('o site ta piscando #medo')
Form = ('tem um bug no formulario')
Sistm = ('o sistema esta bugado')
Java = ('como faz um for em java?')
App = ('Ja resolveu o Bug do Aplicativo?')


email = {'fogo': Impress, 'inseto': Insect, 'site': Site, 'bug': Form, 'sistema': Sistm, 'app': App, 'java': Java}
palavra = input('Digite uma palavra chave para encontrar um email: ').lower()
palavra_chave = email.get(palavra, 'Não foi possivel encontrar. Tente novamente.')
print(palavra_chave)
