# Autor: Juan Victor
# Bibliotecas
from PySimpleGUI import PySimpleGUI as sg
# Layout
sg.theme('BlueMono')
layout = [[sg.Text('Usuário'),
           sg.Input(key='usuario', size=(20, 1))],
          [
            sg.Text('Senha'),
            sg.Input(key='senha', password_char='*', size=(20, 1))
          ], [sg.Checkbox('Salvar o login?')], [sg.Button('Entrar')]]
# Janela e icone
janela = sg.Window('  Tela de Login', layout, icon='in.ico')
# Ler eventos
while True:  # Loop "Infinito"
  eventos, valores = janela.read()
  if eventos == sg.WINDOW_CLOSED:  # Fecha a janela
    break
  if eventos == 'Entrar':  # Entra se os valores abaixo forem inseridos
    if valores['usuario'] == 'usuario' and valores['senha'] == 'senha':
      sg.Popup('   Bem-Vindo! Senhor(a) Usuário(a)!', icon='in.ico')
    else:  # Se os valores não forem corretos, o texto abaixo será exibido
      sg.Popup('  Login incorreto, tente novamente  ', icon='in.ico')
