import tkinter as tk
import chatbot as chat
main_window = tk.Tk()

main_window.title('Cleytin')

main_window.geometry('1000x600')

main_window.grid()

frame = tk.Frame(main_window)
frame.grid()

label = tk.Label(
    frame,
    text='opa bão?',
    foreground='black',
    background='gray',
    font='56px',
)
label.grid(row=0, column=0)

entry = tk.Entry(frame, font='64px')
entry.grid(row=1, column=1)

chat_frame = tk.Frame(main_window)
chat_frame.grid(row=1, column=1)
v = tk.StringVar()
v.set('qual é seu nome?')

chat_label = tk.Label(chat_frame, textvariable=v)
chat_label.grid()

nome_chat = 'Cleytinho'
entrada_sugstao = False
entrada_nome_de_usuario = True
nome_usuario = ''

def executa_chatbot():
    global entrada_sugstao
    global entrada_nome_de_usuario
    global nome_usuario
    global historico_de_conversa

    if entrada_nome_de_usuario:
        nome_usuario = entry.get()
        saudacao = chat.saldacao(nome_chat)
        historico_de_conversa = nome_chat + ': ' + saudacao + '\n'
        v.set(historico_de_conversa)
        entrada_nome_de_usuario = False
    
    else:
        msg = entry.get()
        historico_de_conversa += '\n' + nome_usuario + ': ' + msg
        v.set(historico_de_conversa)



main_window.mainloop()