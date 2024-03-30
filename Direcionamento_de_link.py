import PySimpleGUI as sg
import webbrowser


sg.theme = ('Black')

layout = [
    [sg.Text('Login :',size = (8,1))],
    [sg.Input(key ='login_usuario',size=(25,2))],
    [sg.Text('Senha',size=(8,1))],
    [sg.Input(key = 'senha_usuario',size= (25,2),password_char='*')],
    [sg.Text('Conheceu o Raphael por onde :',size = (30,1))],
    [sg.Listbox(['LinkedIn','Facebook','Instagram','Youtube','Kiwify','Outros'],key='list',size=(20,3))],
    [sg.Button('Entrar')]
]

window = sg.Window('GitHub',layout)
url = ['https://www.linkedin.com/in/raphael-sampaio-52475622b/','https://github.com/RaphaelSampaio1']

while True:
    event,values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Entrar':
        user = values['login_usuario']
        password = values['senha_usuario']
        for i in url:
            webbrowser.open(i)


window.Close()
        