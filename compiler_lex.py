#T {int,num,id}
#Tl {=}
#N {DclVar}
#S: Progamme
#P{
#DclVar -> int id = num 
#        | int id num
#        | int id
#}


import ply.lex as lex

tokens = ['num', 'id', 'int','print','println','vars','main','repeat']
literals = ['=','(',')','{','}']

def t_num(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_println(t):
    r'println'
    return t

def t_print(t):
    r'print'
    return t

def t_int(t):
    r'int'
    return t

def t_vars(t):
    r'vars'
    return t

def t_repeat(t):
    r'repeat'
    return t

def t_main(t):
    r'main'
    return t


def t_id(t):
    r'[a-zA-Z]\w*'
    return t




t_ignore = " \t\n"

# Tratamento de erros
def t_error(t):
    print('Caracter ilegal:', t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
