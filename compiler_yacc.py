import sys
import ply.yacc as yacc
from compiler_lex import tokens

# Condicoes
# Ciclo for
# Ciclo while
# Subprograms
# int a[4] = 5
# a[] = 5


# Prog -> VarBlc MainBlc
#
# VarBlc -> vars '{' Dcls '}'
#
# Dcls    -> Dcl Dcls
#          | 
#
# Dcl -> int id
#      | int id = num 
#      | int id '[' num ']'
#
# MainBlc -> main '{' Insts '}'
# 
# Insts -> AttrInt Insts
#        | Print Insts
#        | Println Insts
#        | Repat Insts
#        | Read Insts
#        |
# 
# Attr -> id = Exp
#       | id '[' Exp ']' = Exp
#       | id '[' Exp ']' '[' Exp ']' = Exp
# 
# Print -> print '(' Exp ')'
#
# Println -> println '(' Exp ')'
#
# Repeat -> RepeatStart '(' num ')' '{' Insts '}'
# 
# RepeatStart -> repeat 
#
# Read -> read '(' id ')'
#
# Exp -> Exp '+' Term
#      | Exp '-' Term
#      | Term
# 
# Term -> Term '*' Factor
#       | Term '/' Factor
#       | Factor
#
# Factor -> id
#         | num
#         | '(' Exp ')'
#         | "id '[' Exp ']'"
#         | "id '[' Exp ']' '[' Exp ']'"

def p_Prog(p):
    "Prog : VarBlc MainBlc"

def p_VarBlc(p):
    "VarBlc : vars '{' Dcls '}'"

def p_Dcls(p):
    "Dcls : Dcl Dcls"

def p_Dcls_End(p):
    "Dcls : "
    out.write("pushn 10\n")
    out.write("start\n")
    p.parser.table["0ciclo"]=[0,1,2,3,4,5,6,7,8,9]

def p_MainBlc(p):
    "MainBlc : main '{' Insts '}'"
    out.write("stop\n")

def p_Insts_Attr(p):
    "Insts : Attr Insts"

def p_Insts_Print(p):
    "Insts : Print Insts"

def p_Insts_Println(p):
    "Insts : Println Insts"

def p_Insts_Repeat(p):
    "Insts : Repeat Insts"

def p_Insts_Read(p):
    "Insts : Read Insts"

def p_Insts_End(p):
    "Insts : "

def p_Repeat(p):
    "Repeat : RepeatS '(' num ')' '{' Insts '}' "
    
    addr = str(p.parser.numReg+p.parser.offset)
    out.write("pushg "+addr+"\n")
    out.write("pushi 1\n")
    out.write("add\n")
    out.write("storeg "+addr+"\n")

    out.write("pushg "+addr+"\n")
    out.write("pushi "+str(p[3])+"\n")
    out.write("equal\n")
    out.write("jz ciclo"+str(p.parser.table["0ciclo"][p.parser.numReg])+"\n")

    out.write("pushi 0\n")
    out.write("storeg "+addr+"\n")
    print("EReg: "+str(p.parser.table["0ciclo"][p.parser.numReg]))
    p.parser.numReg-=1

def p_RepeatS(p):
    "RepeatS : repeat"
    p.parser.numReg+=1
    p.parser.cicles+=1
    p.parser.table["0ciclo"][p.parser.numReg]=p.parser.cicles
    out.write("ciclo"+str(p.parser.cicles)+":\n")
    print("BReg: "+str(p.parser.table["0ciclo"][p.parser.numReg]))

def p_Read(p):
    "Read : read '(' id ')'"
    out.write("read\natoi\n")
    out.write("storeg "+str(p.parser.table[p[3]])+"\n")

def p_Print(p):
    "Print : print '(' Exp ')'"
    out.write(p[3])
    out.write("writei\n")

def p_Println(p):
    "Println : println '(' Exp ')'"
    out.write(p[3])
    out.write("writei\n")
    out.write("pushs \"\\n\"\n")
    out.write("writes\n")

def p_Dcl_Arr(p):
    "Dcl : int id '[' num ']'"
    out.write("pushn "+str(p[4])+"\n")
    p.parser.table[p[2]]=p.parser.offset
    p.parser.offset+=p[4]

def p_Dcl_Arr_2D(p):
    "Dcl : int id '[' num ']' '[' num ']'"
    out.write("pushn "+str(p[4]*p[7])+"\n")
    p.parser.table[p[2]]=(p.parser.offset,p[7])
    p.parser.offset+=p[4]*p[7]

def p_Dcl_0(p):
    "Dcl : int id"
    out.write("pushi 0\n")
    p.parser.table[p[2]]=p.parser.offset
    p.parser.offset+=1

def p_Dcl_num(p):
    "Dcl : int id '=' num"
    out.write("pushi "+str(p[4])+"\n")
    p.parser.table[p[2]]=p.parser.offset
    p.parser.offset+=1

def p_Attr(p):
    "Attr : id '=' Exp"
    out.write(p[3])
    out.write("storeg "+str(p.parser.table[p[1]])+"\n")

def p_Attr_arr(p):
    "Attr : id '[' Exp ']' '=' Exp"
    out.write("pushgp\n")
    out.write("pushi "+str(p.parser.table[p[1]][0])+"\n")
    out.write("padd\n")
    out.write(p[3])
    out.write(p[6])
    out.write("storen\n")

def p_Attr_arr2D(p):
    "Attr : id '[' Exp ']' '[' Exp ']' '=' Exp"
    out.write("pushgp\n")
    out.write("pushi "+str(p.parser.table[p[1]][0])+"\n")
    out.write("padd\n")
    out.write(p[3])
    out.write("pushi "+str(p.parser.table[p[1]][1])+"\n") #Tamanho das linhas
    out.write("mul\n")
    out.write(p[6])
    out.write("add\n")
    out.write(p[9])
    out.write("storen\n")



def p_Exp_add(p):
    "Exp : Exp '+' Term"
    p[0] = p[1]+p[3]+"add\n"

def p_Exp_sub(p):
    "Exp : Exp '-' Term"
    p[0] = p[1]+p[3]+"sub\n"

def p_Exp_term(p):
    "Exp : Term"
    p[0] = p[1]

def p_Term_mul(p):
    "Term : Term '*' Factor"
    p[0] = p[1]+p[3]+"mul\n"

def p_Term_div(p):
    "Term : Term '/' Factor"
    p[0] = p[1]+p[3]+"div\n"

def p_Term_factor(p):
    "Term : Factor"
    p[0] = p[1]

def p_Factor_id(p):
    "Factor : id"
    p[0] = "pushg "+str(p.parser.table[p[1]])+"\n"

def p_Factor_num(p):
    "Factor : num"
    p[0] = "pushi "+str(p[1])+"\n"


def p_Factor_arr(p):
    "Factor : id '[' Exp ']'"
    p[0]="pushgp\n"+"pushi "+str(p.parser.table[p[1]][0])+"\n"+"padd\n"+p[3]+"loadn\n"

def p_Factor_arr_2d(p):
    "Factor : id '[' Exp ']' '[' Exp ']'"
    p[0]="pushgp\n"+"pushi "+str(p.parser.table[p[1]][0])+"\n"+"padd\n"+p[3]+"pushi "+str(p.parser.table[p[1]][1])+"\n"+"mul\n"+p[6]+"add\n"+"loadn\n"


def p_Factor_group(p):
    "Factor : '(' Exp ')'"
    p[0] = p[2]


def p_error(p):
    print('Syntax error: ', p)

parser = yacc.yacc()
parser.table = {}
parser.offset = 0
parser.numReg = -1
parser.cicles = 0

f = open(sys.argv[1], "r")
out = open(sys.argv[2], "w")

result = parser.parse(f.read())