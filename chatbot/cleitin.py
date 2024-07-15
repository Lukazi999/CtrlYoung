import chatbot

nome_chatbot = 'cleitin'
chatbot.saldacao(nome_chatbot)
while True:
    msg = chatbot.recebe_mensagem()
    resposta = chatbot.busca_mensagem(nome_chatbot, msg)
    if chatbot.exibe_resposta(resposta, nome_chatbot) == 'fim':
        break

    