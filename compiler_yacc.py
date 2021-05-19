import sys
import ply.yacc as yacc
from compiler_lex import tokens

# Prog -> VarBlc MainBlc
#
# VarBlc -> vars '{' Dcls '}'
#
# Dcls    -> DclInt Dcls
#          | 
#
# DclInt -> int id = num 
#         | int id num
#         | int id
#
# MainBlc -> main '{' Insts '}'
# 
# Insts -> AttrInt Insts
#        | Print Insts
#        | Println Insts
#        |
# 
# AttrInt -> id = num 
#          | id num
# 
# Print -> print '(' id ')'

def p_Prog(p):
    "Prog : VarBlc MainBlc"


def p_VarBlc(p):
    "VarBlc : vars '{' Dcls '}'"

def p_Dcls(p):
    "Dcls : DclInt Dcls"

def p_Dcls_End(p):
    "Dcls : "
    print("start")

def p_MainBlc(p):
    "MainBlc : main '{' Insts"

def p_Insts_Attr(p):
    "Insts : AttrInt Insts"

def p_Insts_Print(p):
    "Insts : Print Insts"

def p_Insts_Println(p):
    "Insts : Println Insts"

def p_Insts_End(p):
    "Insts : '}'"
    print("stop")

def p_Print(p):
    "Print : print '(' id ')'"
    print("pushg "+str(p.parser.table[p[3]]))
    print("writei")
    #print(p[1] + " " + p[2]+p[3]+p[4])

def p_Println(p):
    "Println : println '(' id ')'"
    print("pushg "+str(p.parser.table[p[3]]))
    print("writei")
    print("pushs \"\\n\"")
    print("writes")
    #print(p[1] + " " + p[2]+p[3]+p[4])

def p_DclInt(p):
    "DclInt : int id"
    print("pushi 0")
    p.parser.table[p[2]]=p.parser.offset
    p.parser.offset+=1
    #print(p[1]+" "+p[2])

def p_DclInt_Attr(p):
    "DclInt : int id num"
    print("pushi "+str(p[2]))
    p.parser.table[p[2]]=p.parser.offset
    p.parser.offset+=1
    #print(p[1]+" "+p[2]+" "+str(p[3]))

def p_DclInt_AttrEq(p):
    "DclInt : int id '=' num"
    print("pushi "+str(p[4]))
    p.parser.table[p[2]]=p.parser.offset
    p.parser.offset+=1
    #print(p[1]+" "+p[2]+" "+p[3]+" "+str(p[4]))

def p_AttrInt(p):
    "AttrInt : id num"
    print("pushi "+str(p[2]))
    print("storeg "+str(p.parser.table[p[1]]))
    #print(p[1]+" "+str(p[2]))

def p_AttrInt_Eq(p):
    "AttrInt : id '=' num"
    print("pushi "+str(p[3]))
    print("storeg "+str(p.parser.table[p[1]]))
    #print(p[1]+" "+p[2]+" "+str(p[3]))

def p_error(p):
    print('Syntax error: ', p)

parser = yacc.yacc()
parser.table = {}
parser.offset = 0

f = open("text.txt", "r")

result = parser.parse(f.read())