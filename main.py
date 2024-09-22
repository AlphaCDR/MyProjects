
from customtkinter import *

expression = str('0')
parent_to_input = bool(False)
value = str()

wdt = 60
hgt = 60
base = CTk(fg_color='black')

base.title('MATH CALCULATOR')
base.resizable(False, False)

screen = CTkLabel(base, text = expression, font=('consolas', 20, 'bold'), text_color='#DCDCDC', height = 45, justify = 'center')
screen.grid(row = 0)

button = CTkFrame(base, fg_color='black')
button.grid(row = 2)

developer = CTkLabel(base, text='Created by Mario Monteiro', font=('consolas', 16), justify = 'center', text_color='#DCDCDC')
developer.grid(row = 3)

def key_pressed(event):
    if event.char in '1234567890+-/*.':
        calculadora(str(event.char))
    elif event.char in '()':
        calculadora('parent')
    elif event.char.upper()[0] == 'C':
        calculadora('clean_all')
    elif event.char.upper()[0] == 'D':
        calculadora('clean_last')
    elif event.char.upper()[0] == '=':
        eval_calculator()
    elif event.char.upper()[0] == 'E':
        calculadora('cotacao_cientifica') 
    elif event.char.upper()[0] == 'X':
        calculadora('Xⁿ') 
base.bind("<Key>", key_pressed)

def eval_calculator():
    global expression, parent_to_input, value
    try:
        output = str(eval(value))  
        screen.configure(text = output)
    except:
        screen.configure(text = 'Sintax Error!')
    expression = '0' 
    parent_to_input = False
def calculadora(on_click):
    global expression, parent_to_input, value, output
    changes = str()
    
    try:
        #inserir números
        if str(on_click) in '1234567890':
            if expression[0] == '0' and len(expression) == 1:
                expression = str(on_click); value = str(on_click)
            else:
                expression += str(on_click); value += str(on_click)
        #inserir operadores e ponto flutuante
        elif str(on_click) in '+-/*.':   
            if expression[-1] in '+-/*.':
                changes = value[:-1]+str(on_click); expression = changes; value = changes
            else:
                expression += str(on_click); value += str(on_click)
        #reset/ limpar dados da calculadora   
        elif str(on_click) == 'clean_all':
            expression = '0'; value = '0'; parent_to_input = False
        #limpar ultimo elemento inserido
        elif str(on_click) == 'clean_last':
            if expression[-1] in '()':
                parent_to_input = False
            changes = expression[:-1]
            if len(changes) == 0:
                expression = '0'; value = '0'
            else:
                expression = changes; value = changes
        #abrir e fechar parentesis
        elif str(on_click) == 'parent':
            #abre parentesis caso o primeiro e único elemento seja 0
            if expression[0] == '0' and expression == '0':
                expression = '('; value = '('
                parent_to_input = True
            #abre parentesis normal
            elif parent_to_input == False:
                expression += '('; value += '('
                parent_to_input = True
            #fecha parentesis caso já a tiver aberto
            elif parent_to_input == True:
                expression += ')'; value += ')'
                parent_to_input = False
        # elevar o número ao quadrado
        elif str(on_click) == 'math_square':
            expression += '²'; value += '**2'
        #cotação cientifica e== 10
        elif str(on_click) == 'cotacao_cientifica':
            expression += 'e'; value += '*10**'
        #calcular percentagem base 100
        elif str(on_click) == 'percent':
            expression += '%'; value += '/100'
        #eleva o número a um valor dado pelo utilisador
        elif str(on_click) == 'Xⁿ':
            expression += str('^'); value += str('**')
        # atualisar label tela
        screen.configure(text = expression)
    #caso der erro na hora de executar os passos acima:
    except:
        #mostra uma mensagem dizendo que ocorreu um erro
        screen.configure(text = 'Sintax Error!')    
def help():
    help_windows = CTk()  
    help_windows.title('Help')
    help_label= CTkLabel(help_windows, text='Com esta calcladora podemos usar \no teclados para inserir dados em que:')
    help_label.grid(row = 0, padx = 10, pady = 5)
    help_menu = CTkLabel(
        help_windows,
        text='d»elimina ultimo valor inserido\n''c»apaga todos os valores\n''= mostra o resultado na tela\n''e»adiciona a cotação cientifica\n''números e operadores as adicionam para serem calculados\n'
    )
    help_menu.grid(row = 1, padx = 10, pady = 5)
    help_windows.mainloop()

#row= 0
clean1 = CTkButton(button, command = lambda:calculadora('clean_all'), text = 'C', fg_color='grey', text_color='white', font=('consolas', 18, 'bold'), width= wdt, height = hgt)
clean1.grid(row = 0, column = 0, padx = 2, pady = 2)
E10 = CTkButton(button, command = lambda:calculadora('cotacao_cientifica'), text = 'E', fg_color='grey', text_color='white', font=('consolas', 18, 'bold'), width= wdt, height = hgt)
E10.grid(row = 1, column = 0, padx = 2, pady = 2)
elevado = CTkButton(button, command = lambda:calculadora('Xⁿ'), text = 'Xⁿ', fg_color='grey', text_color='white', font=('consolas', 18, 'bold'), width= wdt, height = hgt)
elevado.grid(row = 2, column = 0, padx = 2, pady = 2)
ajuda = CTkButton(button, command = help, text = 'Help', fg_color='grey', text_color='white', font=('consolas', 18, 'bold'), width= wdt, height = hgt)
ajuda.grid(row = 3, column = 0, padx = 2, pady = 2)

#row= 0
clean_2 = CTkButton(button, command = lambda:calculadora('clean_last'), text = '⇦', fg_color='grey', text_color='white', font=('consolas', 18, 'bold'), width= wdt, height = hgt)
clean_2.grid(row = 0, column = 1, padx = 2, pady = 2)
parent = CTkButton(button, command = lambda:calculadora('parent'), text = '()', fg_color='grey', text_color='white', font=('consolas', 18, 'bold'), width= wdt, height = hgt)
parent.grid(row = 0, column = 2, padx = 2, pady = 2)
percentagem = CTkButton(button, command = lambda:calculadora('percent'), text = '%', fg_color='grey', text_color='white', font=('consolas', 18, 'bold'), width= wdt, height = hgt)
percentagem.grid(row = 0, column = 3, padx = 2, pady = 2)
square = CTkButton(button, command = lambda:calculadora('math_square'), text = 'X²', fg_color='grey', text_color='white', font=('consolas', 18, 'bold'), width= wdt, height = hgt)
square.grid(row = 0, column = 4, padx = 2, pady = 2)
#row= 1
btn_7 = CTkButton(button, command = lambda:calculadora('7'), text = '7', font=('consolas', 18), width= wdt, height = hgt)
btn_7.grid(row = 1, column = 1, padx = 2, pady = 2)
btn_8 = CTkButton(button, command = lambda:calculadora('8'), text = '8', font=('consolas', 18), width= wdt, height = hgt)
btn_8.grid(row = 1, column = 2, padx = 2, pady = 2)
btn_9 = CTkButton(button, command = lambda:calculadora('9'), text = '9', font=('consolas', 18), width= wdt, height = hgt)
btn_9.grid(row = 1, column = 3, padx = 2, pady = 2)
soma = CTkButton(button, command = lambda:calculadora('+'), text = '+', fg_color='grey', text_color='white', font=('consolas', 18, 'bold'), width= wdt, height = hgt)
soma.grid(row = 1, column = 4, padx = 2, pady = 2)
#row= 2
btn_4 = CTkButton(button, command = lambda:calculadora('4'), text = '4', font=('consolas', 18), width= wdt, height = hgt)
btn_4.grid(row = 2, column = 1, padx = 2, pady = 2)
btn_5 = CTkButton(button, command = lambda:calculadora('5'), text = '5', font=('consolas', 18), width= wdt, height = hgt)
btn_5.grid(row = 2, column = 2, padx = 2, pady = 2)
btn_6 = CTkButton(button, command = lambda:calculadora('6'), text = '6', font=('consolas', 18), width= wdt, height = hgt)
btn_6.grid(row = 2, column = 3, padx = 2, pady = 2)
subtr = CTkButton(button, command = lambda:calculadora('-'), text = '-', fg_color='grey', text_color='white', font=('consolas', 18), width= wdt, height = hgt)
subtr.grid(row = 2, column = 4, padx = 2, pady = 2)
#row= 3
btn_1 = CTkButton(button, command = lambda:calculadora('1'), text = '1', font=('consolas', 18), width= wdt, height = hgt)
btn_1.grid(row = 3, column = 1, padx = 2, pady = 2)
btn_2 = CTkButton(button, command = lambda:calculadora('2'), text = '2', font=('consolas', 18), width= wdt, height = hgt)
btn_2.grid(row = 3, column = 2, padx = 2, pady = 2)
btn_3 = CTkButton(button, command = lambda:calculadora('3'), text = '3', font=('consolas', 18), width= wdt, height = hgt)
btn_3.grid(row = 3, column = 3, padx = 2, pady = 2)
mult = CTkButton(button, command = lambda:calculadora('*'), text = 'x', fg_color='grey', text_color='white', font=('consolas', 18, 'bold'), width= wdt, height = hgt)
mult.grid(row = 3, column = 4, padx = 2, pady = 2)
#row= 0
float_point = CTkButton(button, command = lambda:calculadora('.'), text = '.', fg_color='grey', text_color='white', font=('consolas', 18, 'bold'), width= wdt, height = hgt)
float_point.grid(row = 4, column = 1, padx = 2, pady = 2)
btn_0 = CTkButton(button, command = lambda:calculadora('0'), text = '0', font=('consolas', 18), width= wdt, height = hgt)
btn_0.grid(row = 4, column = 2, padx = 2, pady = 2)
equal = CTkButton(button, command = eval_calculator , text = '=', fg_color='grey', text_color='white', font=('consolas', 18, 'bold'), width= wdt, height = hgt)
equal.grid(row = 4, column = 3, padx = 2, pady = 2)
div = CTkButton(button, command = lambda:calculadora('/'), text = '÷', fg_color='grey', text_color='white', font=('consolas', 18, 'bold'), width= wdt, height = hgt)
div.grid(row = 4, column = 4, padx = 2, pady = 2)


base.mainloop()