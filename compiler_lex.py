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

tokens = ['num', 'id', 'int','print','println','prints','string','vars','main','repeat','read','sup','inf','eq','supeq'
,'infeq','not','diff','and','or','if','else']
literals = ['=','(',')','{','}','+','*','-','/','[',']']

def t_num(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_string(t):
    r'"[^"]*"'
    return t

def t_println(t):
    r'println'
    return t

def t_read(t):
    r'read'
    return t

def t_prints(t):
    r'prints'
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

def t_if(t):
    r'if'
    return t

def t_else(t):
    r'else'
    return t


def t_supeq(t):
    r'>='
    return t

def t_infeq(t):
    r'<='
    return t

def t_sup(t):
    r'>'
    return t

def t_inf(t):
    r'<'
    return t

def t_diff(t):
    r'!='
    return t

def t_not(t):
    r'!'
    return t

def t_eq(t):
    r'=='
    return t

def t_and(t):
    r'&&'
    return t

def t_or(t):
    r'\|\|'
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
