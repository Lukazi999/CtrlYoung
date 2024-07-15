import random

def saldacao(nome):
    frases = [
        'fala CNPJoto aqui é o ' +nome+ '.' ,
        'fala CNPJoto aqui é o ' +nome+ '.',
        'olá  ' +nome+ '.'
    ]
    return (frases[random.randint(0,2)])

def recebe_mensagem(mensagem):
    msg = 'Cliente: ' + input('cliente: ')
    proibidos = ['vasco' , 'bocó' , 'bobão']
    for palavra in proibidos:
        if palavra in msg:
            print('To namoral com tu  me respeita')
    return msg

def busca_mensagem(nome, mensagem):
    with open('base.txt', 'a+', encoding= 'utf-8') as base_conhecimento:
        base_conhecimento.seek(0)
        while True:
            linha = base_conhecimento.readline()
            if linha != '':
                if mensagem.replace('cliente: ', '') == 'Tchau':
                    print(base_conhecimento.readline())
                    return 'fim'
                elif linha.strip() == mensagem.strip():
                    proxima_linha = base_conhecimento.readline()
                    if 'Chatbot: ' in proxima_linha:
                        return proxima_linha
            else:
                print('Chatbot: sei disso não mano')
                base_conhecimento.write('\n' + mensagem)
                resposta_esperada = input('o que tu esperava?')
                base_conhecimento.write('\nChatbot: ' + resposta_esperada)
                return 'hum...'
            
def exibe_resposta(resposta, nome):
    print(resposta.replace('chat', nome))
    if resposta == 'fim':
        return resposta
    return 'continua'