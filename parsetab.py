
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "num id int print println vars main repeat readProg : VarBlc MainBlcVarBlc : vars '{' Dcls '}'Dcls : DclInt DclsDcls : MainBlc : main '{' Insts '}'Insts : AttrInt InstsInsts : Print InstsInsts : Println InstsInsts : Repeat InstsInsts : Read InstsInsts : Repeat : RepeatS '(' num ')' '{' Insts '}' RepeatS : repeatRead : read '(' id ')'Print : print '(' Exp ')'Println : println '(' Exp ')'DclInt : int idDclInt : int id numDclInt : int id '=' numAttrInt : id numAttrInt : id '=' ExpExp : Exp '+' TermExp : Exp '-' TermExp : TermTerm : Term '*' FactorTerm : Term '/' FactorTerm : FactorFactor : idFactor : numFactor : '(' Exp ')'"
    
_lr_action_items = {'vars':([0,],[3,]),'$end':([1,4,26,],[0,-1,-5,]),'main':([2,23,],[5,-2,]),'{':([3,5,58,],[6,7,65,]),'}':([6,7,8,9,11,12,13,14,15,16,24,25,27,28,29,30,31,32,38,40,41,42,43,44,50,56,57,59,60,61,62,63,64,65,66,67,],[-4,-11,23,-4,26,-11,-11,-11,-11,-11,-3,-17,-6,-7,-8,-9,-10,-20,-18,-28,-21,-24,-27,-29,-19,-15,-16,-14,-22,-23,-25,-26,-30,-11,67,-12,]),'int':([6,9,25,38,50,],[10,10,-17,-18,-19,]),'id':([7,10,12,13,14,15,16,32,33,34,35,37,40,41,42,43,44,45,51,52,53,54,56,57,59,60,61,62,63,64,65,67,],[17,25,17,17,17,17,17,-20,40,40,40,49,-28,-21,-24,-27,-29,40,40,40,40,40,-15,-16,-14,-22,-23,-25,-26,-30,17,-12,]),'print':([7,12,13,14,15,16,32,40,41,42,43,44,56,57,59,60,61,62,63,64,65,67,],[18,18,18,18,18,18,-20,-28,-21,-24,-27,-29,-15,-16,-14,-22,-23,-25,-26,-30,18,-12,]),'println':([7,12,13,14,15,16,32,40,41,42,43,44,56,57,59,60,61,62,63,64,65,67,],[19,19,19,19,19,19,-20,-28,-21,-24,-27,-29,-15,-16,-14,-22,-23,-25,-26,-30,19,-12,]),'read':([7,12,13,14,15,16,32,40,41,42,43,44,56,57,59,60,61,62,63,64,65,67,],[21,21,21,21,21,21,-20,-28,-21,-24,-27,-29,-15,-16,-14,-22,-23,-25,-26,-30,21,-12,]),'repeat':([7,12,13,14,15,16,32,40,41,42,43,44,56,57,59,60,61,62,63,64,65,67,],[22,22,22,22,22,22,-20,-28,-21,-24,-27,-29,-15,-16,-14,-22,-23,-25,-26,-30,22,-12,]),'num':([17,25,33,34,35,36,39,45,51,52,53,54,],[32,38,44,44,44,48,50,44,44,44,44,44,]),'=':([17,25,],[33,39,]),'(':([18,19,20,21,22,33,34,35,45,51,52,53,54,],[34,35,36,37,-13,45,45,45,45,45,45,45,45,]),'*':([40,42,43,44,60,61,62,63,64,],[-28,53,-27,-29,53,53,-25,-26,-30,]),'/':([40,42,43,44,60,61,62,63,64,],[-28,54,-27,-29,54,54,-25,-26,-30,]),'+':([40,41,42,43,44,46,47,55,60,61,62,63,64,],[-28,51,-24,-27,-29,51,51,51,-22,-23,-25,-26,-30,]),'-':([40,41,42,43,44,46,47,55,60,61,62,63,64,],[-28,52,-24,-27,-29,52,52,52,-22,-23,-25,-26,-30,]),')':([40,42,43,44,46,47,48,49,55,60,61,62,63,64,],[-28,-24,-27,-29,56,57,58,59,64,-22,-23,-25,-26,-30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Prog':([0,],[1,]),'VarBlc':([0,],[2,]),'MainBlc':([2,],[4,]),'Dcls':([6,9,],[8,24,]),'DclInt':([6,9,],[9,9,]),'Insts':([7,12,13,14,15,16,65,],[11,27,28,29,30,31,66,]),'AttrInt':([7,12,13,14,15,16,65,],[12,12,12,12,12,12,12,]),'Print':([7,12,13,14,15,16,65,],[13,13,13,13,13,13,13,]),'Println':([7,12,13,14,15,16,65,],[14,14,14,14,14,14,14,]),'Repeat':([7,12,13,14,15,16,65,],[15,15,15,15,15,15,15,]),'Read':([7,12,13,14,15,16,65,],[16,16,16,16,16,16,16,]),'RepeatS':([7,12,13,14,15,16,65,],[20,20,20,20,20,20,20,]),'Exp':([33,34,35,45,],[41,46,47,55,]),'Term':([33,34,35,45,51,52,],[42,42,42,42,60,61,]),'Factor':([33,34,35,45,51,52,53,54,],[43,43,43,43,43,43,62,63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Prog","S'",1,None,None,None),
  ('Prog -> VarBlc MainBlc','Prog',2,'p_Prog','compiler_yacc.py',32),
  ('VarBlc -> vars { Dcls }','VarBlc',4,'p_VarBlc','compiler_yacc.py',40),
  ('Dcls -> DclInt Dcls','Dcls',2,'p_Dcls','compiler_yacc.py',43),
  ('Dcls -> <empty>','Dcls',0,'p_Dcls_End','compiler_yacc.py',46),
  ('MainBlc -> main { Insts }','MainBlc',4,'p_MainBlc','compiler_yacc.py',52),
  ('Insts -> AttrInt Insts','Insts',2,'p_Insts_Attr','compiler_yacc.py',56),
  ('Insts -> Print Insts','Insts',2,'p_Insts_Print','compiler_yacc.py',59),
  ('Insts -> Println Insts','Insts',2,'p_Insts_Println','compiler_yacc.py',62),
  ('Insts -> Repeat Insts','Insts',2,'p_Insts_Repeat','compiler_yacc.py',65),
  ('Insts -> Read Insts','Insts',2,'p_Insts_Read','compiler_yacc.py',68),
  ('Insts -> <empty>','Insts',0,'p_Insts','compiler_yacc.py',71),
  ('Repeat -> RepeatS ( num ) { Insts }','Repeat',7,'p_Repeat','compiler_yacc.py',74),
  ('RepeatS -> repeat','RepeatS',1,'p_RepeatS','compiler_yacc.py',93),
  ('Read -> read ( id )','Read',4,'p_Read','compiler_yacc.py',101),
  ('Print -> print ( Exp )','Print',4,'p_Print','compiler_yacc.py',106),
  ('Println -> println ( Exp )','Println',4,'p_Println','compiler_yacc.py',111),
  ('DclInt -> int id','DclInt',2,'p_DclInt','compiler_yacc.py',118),
  ('DclInt -> int id num','DclInt',3,'p_DclInt_Attr','compiler_yacc.py',124),
  ('DclInt -> int id = num','DclInt',4,'p_DclInt_AttrEq','compiler_yacc.py',130),
  ('AttrInt -> id num','AttrInt',2,'p_AttrInt','compiler_yacc.py',136),
  ('AttrInt -> id = Exp','AttrInt',3,'p_AttrInt_Eq','compiler_yacc.py',142),
  ('Exp -> Exp + Term','Exp',3,'p_Exp_add','compiler_yacc.py',148),
  ('Exp -> Exp - Term','Exp',3,'p_Exp_sub','compiler_yacc.py',152),
  ('Exp -> Term','Exp',1,'p_Exp_term','compiler_yacc.py',156),
  ('Term -> Term * Factor','Term',3,'p_Term_mul','compiler_yacc.py',161),
  ('Term -> Term / Factor','Term',3,'p_Term_div','compiler_yacc.py',165),
  ('Term -> Factor','Term',1,'p_Term_factor','compiler_yacc.py',173),
  ('Factor -> id','Factor',1,'p_Factor_id','compiler_yacc.py',177),
  ('Factor -> num','Factor',1,'p_Factor_num','compiler_yacc.py',182),
  ('Factor -> ( Exp )','Factor',3,'p_Factor_group','compiler_yacc.py',186),
]
