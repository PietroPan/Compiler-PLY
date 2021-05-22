import sys
import ply.yacc as yacc
from compiler_lex import tokens


# Subprograms
# int a[4] = 5
# a[] = 5
# int a,b,f


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
#      | int id '[' num ']' '[' num ']'
#
# MainBlc -> main '{' Insts '}'
# 
# Insts -> Inst Insts
#        | 
#
# Inst -> AttrInt
#       | Print
#       | Println
#       | Repat
#       | Read
#       | If
#       | IfElse
#       | For
#       | While
# 
# Attr -> id = Exp
#       | id '[' Exp ']' = Exp
#       | id '[' Exp ']' '[' Exp ']' = Exp
# 
# Print -> print '(' Exp ')'
#
# Println -> println '(' Exp ')'
#
# Prints -> prints '(' string ')'
#
# Repeat -> RepeatStart '(' num ')' '{' Insts '}'
# 
# RepeatStart -> repeat 
#
# For -> for '(' Insts ';' Cond ';' Insts ')' '{' Insts '}'
#
# While -> while '(' Cond ')' '{' Insts '}'
#
# Read -> read '(' id ')'
#
# Exp -> Exp '+' Term
#      | Exp '-' Term
#      | id addeq Term
#      | id subeq Term
#      | id addeql Term
#      | id subeql Term
#      | Term
# 
# Term -> Term '*' Factor
#       | Term '/' Factor
#       | id muleq Factor
#       | id diveq Factor
#       | id muleql Factor
#       | id diveql Factor
#       | id modeq Factor
#       | id modeql Factor
#       | Factor
#
# Factor -> id
#         | num
#         | id minus
#         | id plus
#         | id minusl
#         | id plusl
#         | '(' Cond ')'
#         | '(' Exp ')'
#         | "id '[' Exp ']'"
#         | "id '[' Exp ']' '[' Exp ']'"
#
# Cond -> Exp sup Exp
#       | Exp inf Exp
#       | Exp supeq Exp
#       | Exp infeq Exp
#       | not Exp
#       | Exp eq Exp
#       | Exp diff Exp
#       | Cond and Cond
#       | Cond or Cond
#       | '(' Cond and Cond ')'
#       | '(' Cond or Cond ')'
#
# If -> IfStart '{' Insts '}'
#     | IfStart '{' Insts '}' ElseStart '{' Insts '}'
#
# IfStart -> if '(' Cond ')'
# 
# ElseStart -> else

def p_Prog(p):
    "Prog :  MainBlc DefBlcs"
    out.write(p[1]+p[2])

def p_DefBlcs(p):
    "DefBlcs : DefBlcs DefBlc "
    p[0] = p[1]+p[2]

def p_Def_End(p):
    "DefBlcs : "
    p[0] = ""

def p_DefBlc(p):
    "DefBlc : id '{' VarBlc Insts '}' "
    p[0]=p[1]+":\n"
    p[0]+=p[3]+p[4]
    p[0]+="pushi 0\nstorel -1\nreturn\n"

    parser.table = {}
    parser.offset = 0
    parser.level = -1


def p_VarBlc(p):
    "VarBlc :  Dcls "
    p[0]=p[1]
    p[0]+="pushn 10\n"
    #out.write("pushn 10\n")
    #out.write("start\n")
    #p.parser.table["0ciclo"]=[0,1,2,3,4,5,6,7,8,9]

def p_Dcls(p):
    "Dcls : Dcls Dcl"
    p[0]=p[1]+p[2]
    #out.write(p[1])

def p_Dcls_End(p):
    "Dcls : "
    p[0]=""

def p_MainBlc(p):
    "MainBlc : main '{' VarBlc Insts '}'"
    p[0]=p[3]+p[4]+"stop\n"
    
    parser.table = {}
    parser.offset = 0
    parser.level = -1
    #out.write(p[3])
    #out.write("stop\n")

def p_Insts(p):
    "Insts : Insts Inst "
    p[0]=p[1]+p[2]

def p_Insts_End(p):
    "Insts :"
    p[0]=""

def p_Inst_Attr(p):
    "Inst : Attr"
    p[0]=p[1]
    #out.write(p[1])

def p_Inst_Return(p):
    "Inst : Return"
    p[0]=p[1]

def p_Inst_Exp(p):
    "Inst : Exp"
    p[0]=p[1]

def p_Inst_Print(p):
    "Inst : Print"
    p[0]=p[1]
    #out.write(p[1])

def p_Inst_Println(p):
    "Inst : Println"
    p[0]=p[1]
    #out.write(p[1])

def p_Inst_Prints(p):
    "Inst : Prints"
    p[0]=p[1]
    #out.write(p[1])


def p_Inst_Repeat(p):
    "Inst : Repeat"
    p[0]=p[1]
    #out.write(p[1])

def p_Inst_For(p):
    "Inst : For"
    p[0]=p[1]

def p_Inst_While(p):
    "Inst : While"
    p[0]=p[1]

def p_Inst_Read(p):
    "Inst : Read"
    p[0]=p[1]
    #out.write(p[1])

def p_Inst_If(p):
    "Inst : If"
    p[0]=p[1]
    #out.write(p[1])



def p_Repeat(p):
    "Repeat : RepeatS '(' num ')' '{' Insts '}' "
    p.parser.currTag+=1
    p[0]="repeat"+str(p.parser.currTag)+":\n"
    #print("BReg: "+str(p.parser.table["0ciclo"][p.parser.level]))
    #p.parser.table["0ciclo"][p.parser.level]=p.parser.currTag
    #out.write("ciclo"+str(p.parser.currTag)+":\n")

    p[0]+=p[6]
    addr = str(p.parser.level+p.parser.offset)
    p[0]+="pushl "+addr+"\n"
    p[0]+="pushi 1\n"
    p[0]+="add\n"
    p[0]+="storel "+addr+"\n"

    p[0]+="pushl "+addr+"\n"
    p[0]+="pushi "+str(p[3])+"\n"
    p[0]+="equal\n"
    #p[0]+="jz ciclo"+str(p.parser.table["0ciclo"][p.parser.level])+"\n"
    p[0]+="jz repeat"+str(p.parser.currTag)+"\n"

    p[0]+="pushi 0\n"
    p[0]+="storel "+addr+"\n"

    #out.write("pushl "+addr+"\n")
    #out.write("pushi 1\n")
    #out.write("add\n")
    #out.write("storel "+addr+"\n")

    #out.write("pushl "+addr+"\n")
    #out.write("pushi "+str(p[3])+"\n")
    #out.write("equal\n")
    #out.write("jz ciclo"+str(p.parser.table["0ciclo"][p.parser.level])+"\n")

    #out.write("pushi 0\n")
    #out.write("storel "+addr+"\n")
    #print("EReg: "+str(p.parser.table["0ciclo"][p.parser.level]))
    print("EReg: "+str(p.parser.level))
    p.parser.level-=1


def p_RepeatS(p):
    "RepeatS : repeat"
    p.parser.level+=1
    print("BReg: "+str(p.parser.level))
    #p.parser.currTag+=1
    #p.parser.table["0ciclo"][p.parser.level]=p.parser.currTag
    #out.write("ciclo"+str(p.parser.currTag)+":\n")
    #p[0]="ciclo"+str(p.parser.currTag)+":\n"
    #print("BReg: "+str(p.parser.table["0ciclo"][p.parser.level]))

# For -> ForStart Cond ';' Insts ')' '{' Insts '}'
#
# ForStart -> for '(' Insts ';'

def p_For(p):
    "For : for '(' Insts ';' Cond ';' Insts ')' '{' Insts '}'"
    p.parser.currTag+=1
    p[0]=p[3]
    p[0]+="forStart"+str(p.parser.currTag)+":\n"
    p[0]+=p[5]
    p[0]+="jz forEnd"+str(p.parser.currTag)+"\n"
    p[0]+=p[10]+p[7]
    p[0]+="jump forStart"+str(p.parser.currTag)+"\n"
    p[0]+="forEnd"+str(p.parser.currTag)+":\n"

def p_While(p):
    "While : while '(' Cond ')' '{' Insts '}'"
    p.parser.currTag+=1
    p[0]="whileStart"+str(p.parser.currTag)+":\n"
    p[0]+=p[3]
    p[0]+="jz whileEnd"+str(p.parser.currTag)+"\n"
    p[0]+=p[6]
    p[0]+="jump whileStart"+str(p.parser.currTag)+"\n"
    p[0]+="whileEnd"+str(p.parser.currTag)+":\n"
    

def p_Read(p):
    "Read : read '(' id ')'"
    #out.write("read\natoi\n")
    #out.write("storel "+str(p.parser.table[p[3]])+"\n")

    p[0]="read\natoi\n"
    p[0]+="storel "+str(p.parser.table[p[3]])+"\n"

def p_Print(p):
    "Print : print '(' Exp ')'"
    #out.write(p[3])
    #out.write("writei\n")
    p[0]=p[3]
    p[0]+="writei\n"

def p_Println(p):
    "Println : println '(' Exp ')'"
    #out.write(p[3])
    #out.write("writei\n")
    #out.write("pushs \"\\n\"\n")
    #out.write("writes\n")

    p[0]=p[3]
    p[0]+="writei\n"
    p[0]+="pushs \"\\n\"\n"
    p[0]+="writes\n"

def p_Prints(p):
    "Prints : prints '(' string ')'"
    p[0]="pushs "+p[3]+"\n"
    p[0]+="writes\n"
    #out.write("pushs "+p[3]+"\n")
    #out.write("writes\n")

def p_Dcl_Arr(p):
    "Dcl : int id '[' num ']'"
    #out.write("pushn "+str(p[4])+"\n")
    p[0]="pushn "+str(p[4])+"\n"
    p.parser.table[p[2]]=p.parser.offset
    p.parser.offset+=p[4]

def p_Dcl_Arr_2D(p):
    "Dcl : int id '[' num ']' '[' num ']'"
    #out.write("pushn "+str(p[4]*p[7])+"\n")
    p[0]="pushn "+str(p[4]*p[7])+"\n"
    p.parser.table[p[2]]=(p.parser.offset,p[7])
    p.parser.offset+=p[4]*p[7]

def p_Dcl_0(p):
    "Dcl : int id"
    #out.write("pushi 0\n")
    p[0]=("pushi 0\n")
    p.parser.table[p[2]]=p.parser.offset
    p.parser.offset+=1

def p_Dcl_num(p):
    "Dcl : int id '=' num"
    p[0]="pushi "+str(p[4])+"\n"
    #out.write("pushi "+str(p[4])+"\n")
    p.parser.table[p[2]]=p.parser.offset
    p.parser.offset+=1

def p_Attr(p):
    "Attr : id '=' Exp"
    #out.write(p[3])
    #out.write("storel "+str(p.parser.table[p[1]])+"\n")

    p[0]=p[3]
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"


def p_Attr_arr(p):
    "Attr : id '[' Exp ']' '=' Exp"
    #out.write("pushfp\n")
    #out.write("pushi "+str(p.parser.table[p[1]][0])+"\n")
    #out.write("padd\n")
    #out.write(p[3])
    #out.write(p[6])
    #out.write("storen\n")

    p[0]="pushfp\n"
    p[0]+="pushi "+str(p.parser.table[p[1]])+"\n"
    p[0]+="padd\n"
    p[0]+=p[3]
    p[0]+=p[6]
    p[0]+="storen\n"
    

def p_Attr_arr2D(p):
    "Attr : id '[' Exp ']' '[' Exp ']' '=' Exp"
    #out.write("pushfp\n")
    #out.write("pushi "+str(p.parser.table[p[1]][0])+"\n")
    #out.write("padd\n")
    #out.write(p[3])
    #out.write("pushi "+str(p.parser.table[p[1]][1])+"\n") #Tamanho das linhas
    #out.write("mul\n")
    #out.write(p[6])
    #out.write("add\n")
    #out.write(p[9])
    #out.write("storen\n")

    p[0]="pushfp\n"
    p[0]+="pushi "+str(p.parser.table[p[1]][0])+"\n"
    p[0]+="padd\n"
    p[0]+=p[3]
    p[0]+="pushi "+str(p.parser.table[p[1]][1])+"\n" #Tamanho das linhas
    p[0]+="mul\n"
    p[0]+=p[6]
    p[0]+="add\n"
    p[0]+=p[9]
    p[0]+="storen\n"

def p_Return(p):
    "Return : return '(' Exp ')'"
    p[0]=p[3]
    p[0]+="storel -1\n"
    p[0]+="return\n"

def p_If(p):
    "If : if '(' Cond ')' '{' Insts '}' "
    #p.parser.level+=1
    p.parser.currTag+=1
    #p.parser.table["0ciclo"][p.parser.level]=p.parser.currTag
    #out.write(p[3]+"jz ifEnd"+str(p.parser.currTag)+"\n")
    p[0]=p[3]+"jz ifEnd"+str(p.parser.currTag)+"\n"

    #out.write("ifEnd"+str(p.parser.table["0ciclo"][p.parser.level])+":\n")
    p[0]+=p[6]
    p[0]+="ifEnd"+str(p.parser.currTag)+":\n"

    print("EReg: "+str(p.parser.currTag))
    p.parser.level-=1

def p_If_0(p):
    "If : if '(' Cond ')' Inst "
    #p.parser.level+=1
    p.parser.currTag+=1
    #p.parser.table["0ciclo"][p.parser.level]=p.parser.currTag
    #out.write(p[3]+"jz ifEnd"+str(p.parser.currTag)+"\n")
    p[0]=p[3]+"jz ifEnd"+str(p.parser.currTag)+"\n"

    #out.write("ifEnd"+str(p.parser.table["0ciclo"][p.parser.level])+":\n")
    p[0]+=p[5]
    p[0]+="ifEnd"+str(p.parser.currTag)+":\n"

    print("EReg: "+str(p.parser.currTag))
    p.parser.level-=1

def p_IfStart(p):
    "IfStart : if '(' Cond ')'"
    p.parser.level+=1
    p.parser.currTag+=1
    p.parser.table["0ciclo"][p.parser.level]=p.parser.currTag
    #out.write(p[3]+"jz ifEnd"+str(p.parser.currTag)+"\n")
    p[0]=p[3]+"jz ifEnd"+str(p.parser.currTag)+"\n"
    
    print("BReg: "+str(p.parser.table["0ciclo"][p.parser.level]))

def p_If_Else(p):
    "If : if '(' Cond ')' '{' Insts '}' else '{' Insts '}'"
    #p.parser.level+=1
    p.parser.currTag+=1
    #p.parser.table["0ciclo"][p.parser.level]=p.parser.currTag
    #out.write(p[3]+"jz ifEnd"+str(p.parser.currTag)+"\n")
    p[0]=p[3]+"jz ifEnd"+str(p.parser.currTag)+"\n"
    #out.write("elseEnd"+str(p.parser.table["0ciclo"][p.parser.level])+":\n")
    p[0]+=p[6]
    p[0]+="jump elseEnd"+str(p.parser.currTag)+"\n"
    p[0]+="ifEnd"+str(p.parser.currTag)+":\n"
    #out.write("jump elseEnd"+str(p.parser.currTag)+"\n")
    #out.write("ifEnd"+str(p.parser.table["0ciclo"][p.parser.level])+":\n")

    print("EReg: "+str(p.parser.currTag))
    #p.parser.table["0ciclo"][p.parser.level]=p.parser.currTag
    print("BReg: "+str(p.parser.currTag))
    p[0]+=p[10]
    p[0]+="elseEnd"+str(p.parser.currTag)+":\n"

    print("EReg: "+str(p.parser.currTag))
    p.parser.level-=1

def p_ElseStart(p):
    "ElseStart : else "
    p.parser.currTag+=1
    p[0]="jump elseEnd"+str(p.parser.currTag)+"\n"
    p[0]+="ifEnd"+str(p.parser.table["0ciclo"][p.parser.level])+":\n"
    #out.write("jump elseEnd"+str(p.parser.currTag)+"\n")
    #out.write("ifEnd"+str(p.parser.table["0ciclo"][p.parser.level])+":\n")

    print("EReg: "+str(p.parser.table["0ciclo"][p.parser.level]))
    p.parser.table["0ciclo"][p.parser.level]=p.parser.currTag
    print("BReg: "+str(p.parser.table["0ciclo"][p.parser.level]))


def p_Exp_add(p):
    "Exp : Exp '+' Term"
    p[0] = p[1]+p[3]+"add\n"

def p_Exp_sub(p):
    "Exp : Exp '-' Term"
    p[0] = p[1]+p[3]+"sub\n"

def p_Exp_id_addeq(p):
    "Exp : id addeq Term"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="add\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"

def p_Exp_id_subeq(p):
    "Exp : id subeq Term"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="sub\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"

def p_Exp_id_addeql(p):
    "Exp : id addeql Term"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="add\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"

def p_Exp_id_subeql(p):
    "Exp : id subeql Term"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="sub\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"

def p_Exp_term(p):
    "Exp : Term"
    p[0] = p[1]

def p_Term_mul(p):
    "Term : Term '*' Factor"
    p[0] = p[1]+p[3]+"mul\n"

def p_Term_div(p):
    "Term : Term '/' Factor"
    p[0] = p[1]+p[3]+"div\n"

def p_Term_mod(p):
    "Term : Term '%' Factor"
    p[0] = p[1]+p[3]+"mod\n"

def p_Term_id_muleq(p):
    "Term : id muleq Factor"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="mul\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"

def p_Term_id_diveq(p):
    "Term : id diveq Factor"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="div\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"

def p_Term_id_modeq(p):
    "Term : id modeq Factor"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="mod\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"


def p_Term_id_muleql(p):
    "Term : id muleql Factor"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="mul\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"

def p_Term_id_diveql(p):
    "Term : id diveql Factor"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="div\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"

def p_Term_id_modeql(p):
    "Term : id modeql Factor"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+=p[3]
    p[0]+="mod\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"

def p_Term_factor(p):
    "Term : Factor"
    p[0] = p[1]

def p_Factor_id_plus(p):
    "Factor : id plus"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushi 1\n"
    p[0]+="add\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"

def p_Factor_id_plusl(p):
    "Factor : id plusl"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushi 1\n"
    p[0]+="add\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"

def p_Factor_id_minus(p):
    "Factor : id minus"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushi 1\n"
    p[0]+="sub\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"

def p_Factor_id_minusl(p):
    "Factor : id minusl"
    p[0]="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushl "+str(p.parser.table[p[1]])+"\n"
    p[0]+="pushi 1\n"
    p[0]+="sub\n"
    p[0]+="storel "+str(p.parser.table[p[1]])+"\n"

def p_Factor_id(p):
    "Factor : id"
    p[0] = "pushl "+str(p.parser.table[p[1]])+"\n"

def p_Factor_num(p):
    "Factor : num"
    p[0] = "pushi "+str(p[1])+"\n"

def p_Factor_call(p):
    "Factor : id '(' ')' "
    p[0] = "pushi 0\n"
    p[0]+= "pusha "+str(p[1])+"\ncall\n"


def p_Factor_cond(p):
    "Factor : '(' Cond ')'"
    p[0] = p[2]


def p_Factor_arr(p):
    "Factor : id '[' Exp ']'"
    p[0]="pushfp\n"
    p[0]+="pushi "+str(p.parser.table[p[1]])+"\n"
    p[0]+="padd\n"+p[3]
    p[0]+="loadn\n"

def p_Factor_arr_2d(p):
    "Factor : id '[' Exp ']' '[' Exp ']'"
    p[0]="pushfp\n"
    p[0]+="pushi "+str(p.parser.table[p[1]][0])+"\n"
    p[0]+="padd\n"+str(p[3])
    p[0]+="pushi "+str(p.parser.table[p[1]][1])+"\n"
    p[0]+="mul\n"+str(p[6])
    p[0]+="add\n"+"loadn\n"


def p_Factor_group(p):
    "Factor : '(' Exp ')'"
    p[0] = p[2]


def p_Id(p):
    "Id : id"
    p[0] = "pushl "+str(p.parser.table[p[1]])+"\n"

def p_Id_arr(p):
    "Id : id '[' Exp ']'"
    p[0]="pushfp\n"
    p[0]+="pushi "+str(p.parser.table[p[1]])+"\n"
    p[0]+="padd\n"+p[3]
    p[0]+="loadn\n"

def p_Id_arr_2d(p):
    "Id : id '[' Exp ']' '[' Exp ']'"
    p[0]="pushfp\n"
    p[0]+="pushi "+str(p.parser.table[p[1]][0])+"\n"
    p[0]+="padd\n"+str(p[3])
    p[0]+="pushi "+str(p.parser.table[p[1]][1])+"\n"
    p[0]+="mul\n"+str(p[6])
    p[0]+="add\n"+"loadn\n"

def p_Cond_and(p):
    "Cond : Cond and Cond"
    p[0] = p[1]+p[3]+"mul\n"

def p_Cond_or(p):
    "Cond : Cond or Cond"
    p[0]=p[1]+p[3]+"add\n"
    p[0]+=p[1]+p[3]+"mul\n"+"sub\n"

def p_Cond_and_par(p):
    "Cond : '(' Cond and Cond ')'"
    p[0] = p[2]+p[4]+"mul\n"

def p_Cond_or_par(p):
    "Cond : '(' Cond or Cond ')' "
    p[0] = p[2]+p[4]+"add\n"
    p[0]+=p[2]+p[4]+"mul\n"+"sub\n"

def p_Cond_sup(p):
    "Cond : Exp sup Exp"
    p[0] = p[1]+p[3]+"sup\n"

def p_Cond_inf(p):
    "Cond : Exp inf Exp"
    p[0] = p[1]+p[3]+"inf\n"

def p_Cond_supeq(p):
    "Cond : Exp supeq Exp"
    p[0] = p[1]+p[3]+"supeq\n"

def p_Cond_infeq(p):
    "Cond : Exp infeq Exp"
    p[0] = p[1]+p[3]+"infeq\n"

def p_Cond_not(p):
    "Cond : not Exp"
    p[0] = p[2]+"not\n"

def p_Cond_eq(p):
    "Cond : Exp eq Exp"
    p[0] = p[1]+p[3]+"equal\n"

def p_Cond_diff(p):
    "Cond : Exp diff Exp"
    p[0] = p[1]+p[3]+"equal\n"+"not\n"


def p_error(p):
    print('Syntax error: ', p)

parser = yacc.yacc()
parser.table = {}
parser.offset = 0
parser.level = -1
parser.currTag = 0

f = open(sys.argv[1], "r")
out = open(sys.argv[2], "w")

result = parser.parse(f.read())