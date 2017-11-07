
# yacctab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASSIGNrightNOTnonassocLTEQLTEQleftPLUSMINUSleftMULTIPLYDIVIDErightISVOIDrightINT_COMPleftATleftDOTID TYPE INTEGER STRING BOOLEAN LPAREN RPAREN LBRACE RBRACE COLON COMMA DOT SEMICOLON AT PLUS MINUS MULTIPLY DIVIDE EQ LT LTEQ ASSIGN INT_COMP NOT ARROW LOOP INHERITS CLASS IN ELSE IF OF LET POOL ESAC ISVOID WHILE CASE SELF NEW FI THEN\n        program : class_list\n        \n        class_list : class_list class SEMICOLON\n                   | class SEMICOLON\n        \n        class : CLASS TYPE LBRACE features_list_opt RBRACE\n        \n        class : CLASS TYPE INHERITS TYPE LBRACE features_list_opt RBRACE\n        \n        features_list_opt : features_list\n                          | empty\n        \n        features_list : features_list feature SEMICOLON\n                      | feature SEMICOLON\n        \n        feature : ID LPAREN formal_params_list RPAREN COLON TYPE LBRACE expression RBRACE\n        \n        feature : ID LPAREN RPAREN COLON TYPE LBRACE expression RBRACE\n        \n        feature : ID COLON TYPE ASSIGN expression\n        \n        feature : ID COLON TYPE\n        \n        formal_params_list  : formal_params_list COMMA formal_param\n                            | formal_param\n        \n        formal_param : ID COLON TYPE\n        \n        expression : ID\n        \n        expression : INTEGER\n        \n        expression : BOOLEAN\n        \n        expression : STRING\n        \n        expression  : SELF\n        \n        expression : LBRACE block_list RBRACE\n        \n        block_list : block_list expression SEMICOLON\n                   | expression SEMICOLON\n        \n        expression : ID ASSIGN expression\n        \n        expression : expression DOT ID LPAREN arguments_list_opt RPAREN\n        \n        arguments_list_opt : arguments_list\n                           | empty\n        \n        arguments_list : arguments_list COMMA expression\n                       | expression\n        \n        expression : expression AT TYPE DOT ID LPAREN arguments_list_opt RPAREN\n        \n        expression : ID LPAREN arguments_list_opt RPAREN\n        \n        expression : expression PLUS expression\n                   | expression MINUS expression\n                   | expression MULTIPLY expression\n                   | expression DIVIDE expression\n        \n        expression : expression LT expression\n                   | expression LTEQ expression\n                   | expression EQ expression\n        \n        expression : LPAREN expression RPAREN\n        \n        expression : IF expression THEN expression ELSE expression FI\n        \n        expression : WHILE expression LOOP expression POOL\n        \n         expression : let_expression\n        \n        let_expression : LET ID COLON TYPE IN expression\n                       | nested_lets COMMA LET ID COLON TYPE\n        \n        let_expression : LET ID COLON TYPE ASSIGN expression IN expression\n                       | nested_lets COMMA LET ID COLON TYPE ASSIGN expression\n        \n        nested_lets : ID COLON TYPE IN expression\n                    | nested_lets COMMA ID COLON TYPE\n        \n        nested_lets : ID COLON TYPE ASSIGN expression IN expression\n                    | nested_lets COMMA ID COLON TYPE ASSIGN expression\n        \n        expression : CASE expression OF actions_list ESAC\n        \n        actions_list : actions_list action\n                     | action\n        \n        action : ID COLON TYPE ARROW expression SEMICOLON\n        \n        expression : NEW TYPE\n        \n        expression : ISVOID expression\n        \n        expression : INT_COMP expression\n        \n        expression : NOT expression\n        \n        empty :\n        '
    
_lr_action_items = {'DIVIDE':([37,41,44,46,49,52,53,59,63,64,65,67,68,69,71,72,84,85,91,92,93,100,101,102,105,106,107,108,110,114,116,123,126,128,129,130,131,136,145,147,148,149,150,152,153,157,159,160,161,162,],[-17,-19,-43,-18,-20,-21,73,73,73,-57,73,73,73,-56,-58,73,-22,73,73,73,-40,-36,73,73,73,73,73,-35,73,-32,73,73,73,73,73,73,-42,-52,-45,73,73,73,-26,73,73,-41,73,73,73,-31,]),'LBRACE':([5,16,30,36,38,39,40,43,45,50,51,57,58,61,62,73,74,75,78,79,80,81,82,83,86,94,99,109,111,112,113,115,124,137,138,139,143,144,151,154,155,156,],[8,22,36,36,36,36,36,36,36,36,36,83,36,36,36,36,36,36,36,36,36,36,109,36,-24,36,36,36,-23,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'CLASS':([0,3,6,10,],[1,1,-3,-2,]),'COMMA':([25,27,37,41,42,44,46,49,52,54,56,64,68,69,71,84,90,91,92,93,100,101,102,105,106,107,108,114,128,130,131,132,136,145,147,150,152,153,157,159,161,162,],[31,-15,-17,-19,66,-43,-18,-20,-21,-14,-16,-57,-59,-56,-58,-22,115,-30,-25,-40,-36,-38,-33,-37,-34,-39,-35,-32,-48,-29,-42,-49,-52,-45,-44,-26,-50,-51,-41,-47,-46,-31,]),'INHERITS':([5,],[9,]),'LOOP':([37,41,44,46,49,52,64,65,68,69,71,84,92,93,100,101,102,105,106,107,108,114,131,136,145,147,150,157,159,161,162,],[-17,-19,-43,-18,-20,-21,-57,94,-59,-56,-58,-22,-25,-40,-36,-38,-33,-37,-34,-39,-35,-32,-42,-52,-45,-44,-26,-41,-47,-46,-31,]),'ARROW':([146,],[155,]),'FI':([37,41,44,46,49,52,64,68,69,71,84,92,93,100,101,102,105,106,107,108,114,131,136,145,147,149,150,157,159,161,162,],[-17,-19,-43,-18,-20,-21,-57,-59,-56,-58,-22,-25,-40,-36,-38,-33,-37,-34,-39,-35,-32,-42,-52,-45,-44,157,-26,-41,-47,-46,-31,]),'COLON':([15,26,28,32,37,70,95,118,120,],[20,33,34,55,60,98,117,133,134,]),'BOOLEAN':([30,36,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,86,94,99,109,111,112,113,115,124,137,138,139,143,144,151,154,155,156,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-24,41,41,41,-23,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'ISVOID':([30,36,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,86,94,99,109,111,112,113,115,124,137,138,139,143,144,151,154,155,156,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-24,39,39,39,-23,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'ASSIGN':([24,37,87,122,132,145,],[30,62,113,138,144,154,]),'CASE':([30,36,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,86,94,99,109,111,112,113,115,124,137,138,139,143,144,151,154,155,156,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-24,43,43,43,-23,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'DOT':([37,41,44,46,49,52,53,59,63,64,65,67,68,69,71,72,84,85,91,92,93,100,101,102,104,105,106,107,108,110,114,116,123,126,128,129,130,131,136,145,147,148,149,150,152,153,157,159,160,161,162,],[-17,-19,-43,-18,-20,-21,76,76,76,76,76,76,76,-56,76,76,-22,76,76,76,-40,76,76,76,125,76,76,76,76,76,-32,76,76,76,76,76,76,-42,-52,-45,76,76,76,-26,76,76,-41,76,76,76,-31,]),'IN':([37,41,44,46,49,52,64,68,69,71,84,87,92,93,100,101,102,105,106,107,108,114,122,129,131,136,145,147,148,150,157,159,161,162,],[-17,-19,-43,-18,-20,-21,-57,-59,-56,-58,-22,112,-25,-40,-36,-38,-33,-37,-34,-39,-35,-32,137,143,-42,-52,-45,-44,156,-26,-41,-47,-46,-31,]),'ESAC':([119,121,135,163,],[-54,136,-53,-55,]),'ELSE':([37,41,44,46,49,52,64,68,69,71,84,92,93,100,101,102,105,106,107,108,114,123,131,136,145,147,150,157,159,161,162,],[-17,-19,-43,-18,-20,-21,-57,-59,-56,-58,-22,-25,-40,-36,-38,-33,-37,-34,-39,-35,-32,139,-42,-52,-45,-44,-26,-41,-47,-46,-31,]),'AT':([37,41,44,46,49,52,53,59,63,64,65,67,68,69,71,72,84,85,91,92,93,100,101,102,105,106,107,108,110,114,116,123,126,128,129,130,131,136,145,147,148,149,150,152,153,157,159,160,161,162,],[-17,-19,-43,-18,-20,-21,77,77,77,77,77,77,77,-56,77,77,-22,77,77,77,-40,77,77,77,77,77,77,77,77,-32,77,77,77,77,77,77,-42,-52,-45,77,77,77,-26,77,77,-41,77,77,77,-31,]),'MINUS':([37,41,44,46,49,52,53,59,63,64,65,67,68,69,71,72,84,85,91,92,93,100,101,102,105,106,107,108,110,114,116,123,126,128,129,130,131,136,145,147,148,149,150,152,153,157,159,160,161,162,],[-17,-19,-43,-18,-20,-21,79,79,79,-57,79,79,79,-56,-58,79,-22,79,79,79,-40,-36,79,-33,79,-34,79,-35,79,-32,79,79,79,79,79,79,-42,-52,-45,79,79,79,-26,79,79,-41,79,79,79,-31,]),'NOT':([30,36,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,86,94,99,109,111,112,113,115,124,137,138,139,143,144,151,154,155,156,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-24,45,45,45,-23,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'$end':([3,4,6,10,],[-1,0,-3,-2,]),'OF':([37,41,44,46,49,52,64,67,68,69,71,84,92,93,100,101,102,105,106,107,108,114,131,136,145,147,150,157,159,161,162,],[-17,-19,-43,-18,-20,-21,-57,97,-59,-56,-58,-22,-25,-40,-36,-38,-33,-37,-34,-39,-35,-32,-42,-52,-45,-44,-26,-41,-47,-46,-31,]),'INTEGER':([30,36,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,86,94,99,109,111,112,113,115,124,137,138,139,143,144,151,154,155,156,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-24,46,46,46,-23,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'ID':([8,13,19,21,22,23,30,31,36,38,39,40,43,45,48,50,51,58,61,62,66,73,74,75,76,78,79,80,81,83,86,94,96,97,99,109,111,112,113,115,119,121,124,125,135,137,138,139,143,144,151,154,155,156,163,],[15,15,-9,26,15,-8,37,26,37,37,37,37,37,37,70,37,37,37,37,37,95,37,37,37,103,37,37,37,37,37,-24,37,118,120,37,37,-23,37,37,37,-54,120,37,141,-53,37,37,37,37,37,37,37,37,37,-55,]),'RBRACE':([8,11,12,13,19,22,23,29,37,41,44,46,49,52,58,64,68,69,71,84,86,92,93,100,101,102,105,106,107,108,110,111,114,126,131,136,145,147,150,157,159,161,162,],[-60,-7,17,-6,-9,-60,-8,35,-17,-19,-43,-18,-20,-21,84,-57,-59,-56,-58,-22,-24,-25,-40,-36,-38,-33,-37,-34,-39,-35,127,-23,-32,142,-42,-52,-45,-44,-26,-41,-47,-46,-31,]),'NEW':([30,36,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,86,94,99,109,111,112,113,115,124,137,138,139,143,144,151,154,155,156,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-24,47,47,47,-23,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'LPAREN':([15,30,36,37,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,86,94,99,103,109,111,112,113,115,124,137,138,139,141,143,144,151,154,155,156,],[21,38,38,61,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-24,38,38,124,38,-23,38,38,38,38,38,38,38,151,38,38,38,38,38,38,]),'LET':([30,36,38,39,40,43,45,50,51,58,61,62,66,73,74,75,78,79,80,81,83,86,94,99,109,111,112,113,115,124,137,138,139,143,144,151,154,155,156,],[48,48,48,48,48,48,48,48,48,48,48,48,96,48,48,48,48,48,48,48,48,-24,48,48,48,-23,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'SEMICOLON':([2,7,14,17,18,24,35,37,41,44,46,49,52,53,59,64,68,69,71,84,85,92,93,100,101,102,105,106,107,108,114,127,131,136,142,145,147,150,157,159,160,161,162,],[6,10,19,-4,23,-13,-5,-17,-19,-43,-18,-20,-21,-12,86,-57,-59,-56,-58,-22,111,-25,-40,-36,-38,-33,-37,-34,-39,-35,-32,-11,-42,-52,-10,-45,-44,-26,-41,-47,163,-46,-31,]),'RPAREN':([21,25,27,37,41,44,46,49,52,54,56,61,63,64,68,69,71,84,88,89,90,91,92,93,100,101,102,105,106,107,108,114,124,130,131,136,140,145,147,150,151,157,158,159,161,162,],[28,32,-15,-17,-19,-43,-18,-20,-21,-14,-16,-60,93,-57,-59,-56,-58,-22,114,-28,-27,-30,-25,-40,-36,-38,-33,-37,-34,-39,-35,-32,-60,-29,-42,-52,150,-45,-44,-26,-60,-41,162,-47,-46,-31,]),'PLUS':([37,41,44,46,49,52,53,59,63,64,65,67,68,69,71,72,84,85,91,92,93,100,101,102,105,106,107,108,110,114,116,123,126,128,129,130,131,136,145,147,148,149,150,152,153,157,159,160,161,162,],[-17,-19,-43,-18,-20,-21,75,75,75,-57,75,75,75,-56,-58,75,-22,75,75,75,-40,-36,75,-33,75,-34,75,-35,75,-32,75,75,75,75,75,75,-42,-52,-45,75,75,75,-26,75,75,-41,75,75,75,-31,]),'EQ':([37,41,44,46,49,52,53,59,63,64,65,67,68,69,71,72,84,85,91,92,93,100,101,102,105,106,107,108,110,114,116,123,126,128,129,130,131,136,145,147,148,149,150,152,153,157,159,160,161,162,],[-17,-19,-43,-18,-20,-21,80,80,80,-57,80,80,80,-56,-58,80,-22,80,80,80,-40,-36,None,-33,None,-34,None,-35,80,-32,80,80,80,80,80,80,-42,-52,-45,80,80,80,-26,80,80,-41,80,80,80,-31,]),'LTEQ':([37,41,44,46,49,52,53,59,63,64,65,67,68,69,71,72,84,85,91,92,93,100,101,102,105,106,107,108,110,114,116,123,126,128,129,130,131,136,145,147,148,149,150,152,153,157,159,160,161,162,],[-17,-19,-43,-18,-20,-21,74,74,74,-57,74,74,74,-56,-58,74,-22,74,74,74,-40,-36,None,-33,None,-34,None,-35,74,-32,74,74,74,74,74,74,-42,-52,-45,74,74,74,-26,74,74,-41,74,74,74,-31,]),'STRING':([30,36,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,86,94,99,109,111,112,113,115,124,137,138,139,143,144,151,154,155,156,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-24,49,49,49,-23,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'INT_COMP':([30,36,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,86,94,99,109,111,112,113,115,124,137,138,139,143,144,151,154,155,156,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-24,50,50,50,-23,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'LT':([37,41,44,46,49,52,53,59,63,64,65,67,68,69,71,72,84,85,91,92,93,100,101,102,105,106,107,108,110,114,116,123,126,128,129,130,131,136,145,147,148,149,150,152,153,157,159,160,161,162,],[-17,-19,-43,-18,-20,-21,78,78,78,-57,78,78,78,-56,-58,78,-22,78,78,78,-40,-36,None,-33,None,-34,None,-35,78,-32,78,78,78,78,78,78,-42,-52,-45,78,78,78,-26,78,78,-41,78,78,78,-31,]),'WHILE':([30,36,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,86,94,99,109,111,112,113,115,124,137,138,139,143,144,151,154,155,156,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-24,40,40,40,-23,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'IF':([30,36,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,86,94,99,109,111,112,113,115,124,137,138,139,143,144,151,154,155,156,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-24,51,51,51,-23,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'SELF':([30,36,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,86,94,99,109,111,112,113,115,124,137,138,139,143,144,151,154,155,156,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-24,52,52,52,-23,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'THEN':([37,41,44,46,49,52,64,68,69,71,72,84,92,93,100,101,102,105,106,107,108,114,131,136,145,147,150,157,159,161,162,],[-17,-19,-43,-18,-20,-21,-57,-59,-56,-58,99,-22,-25,-40,-36,-38,-33,-37,-34,-39,-35,-32,-42,-52,-45,-44,-26,-41,-47,-46,-31,]),'POOL':([37,41,44,46,49,52,64,68,69,71,84,92,93,100,101,102,105,106,107,108,114,116,131,136,145,147,150,157,159,161,162,],[-17,-19,-43,-18,-20,-21,-57,-59,-56,-58,-22,-25,-40,-36,-38,-33,-37,-34,-39,-35,-32,131,-42,-52,-45,-44,-26,-41,-47,-46,-31,]),'MULTIPLY':([37,41,44,46,49,52,53,59,63,64,65,67,68,69,71,72,84,85,91,92,93,100,101,102,105,106,107,108,110,114,116,123,126,128,129,130,131,136,145,147,148,149,150,152,153,157,159,160,161,162,],[-17,-19,-43,-18,-20,-21,81,81,81,-57,81,81,81,-56,-58,81,-22,81,81,81,-40,-36,81,81,81,81,81,-35,81,-32,81,81,81,81,81,81,-42,-52,-45,81,81,81,-26,81,81,-41,81,81,81,-31,]),'TYPE':([1,9,20,33,34,47,55,60,77,98,117,133,134,],[5,16,24,56,57,69,82,87,104,122,132,145,146,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'empty':([8,22,61,124,151,],[11,11,89,89,89,]),'features_list_opt':([8,22,],[12,29,]),'formal_param':([21,31,],[27,54,]),'class':([0,3,],[2,7,]),'features_list':([8,22,],[13,13,]),'arguments_list':([61,124,151,],[90,90,90,]),'program':([0,],[4,]),'feature':([8,13,22,],[14,18,14,]),'actions_list':([97,],[121,]),'let_expression':([30,36,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,94,99,109,112,113,115,124,137,138,139,143,144,151,154,155,156,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'formal_params_list':([21,],[25,]),'arguments_list_opt':([61,124,151,],[88,140,158,]),'action':([97,121,],[119,135,]),'block_list':([36,],[58,]),'class_list':([0,],[3,]),'nested_lets':([30,36,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,94,99,109,112,113,115,124,137,138,139,143,144,151,154,155,156,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'expression':([30,36,38,39,40,43,45,50,51,58,61,62,73,74,75,78,79,80,81,83,94,99,109,112,113,115,124,137,138,139,143,144,151,154,155,156,],[53,59,63,64,65,67,68,71,72,85,91,92,100,101,102,105,106,107,108,110,116,123,126,128,129,130,91,147,148,149,152,153,91,159,160,161,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> class_list','program',1,'p_program','parser.py',100),
  ('class_list -> class_list class SEMICOLON','class_list',3,'p_class_list','parser.py',107),
  ('class_list -> class SEMICOLON','class_list',2,'p_class_list','parser.py',108),
  ('class -> CLASS TYPE LBRACE features_list_opt RBRACE','class',5,'p_class','parser.py',117),
  ('class -> CLASS TYPE INHERITS TYPE LBRACE features_list_opt RBRACE','class',7,'p_class_inherits','parser.py',123),
  ('features_list_opt -> features_list','features_list_opt',1,'p_feature_list_opt','parser.py',129),
  ('features_list_opt -> empty','features_list_opt',1,'p_feature_list_opt','parser.py',130),
  ('features_list -> features_list feature SEMICOLON','features_list',3,'p_feature_list','parser.py',136),
  ('features_list -> feature SEMICOLON','features_list',2,'p_feature_list','parser.py',137),
  ('feature -> ID LPAREN formal_params_list RPAREN COLON TYPE LBRACE expression RBRACE','feature',9,'p_feature_method','parser.py',146),
  ('feature -> ID LPAREN RPAREN COLON TYPE LBRACE expression RBRACE','feature',8,'p_feature_method_no_formals','parser.py',152),
  ('feature -> ID COLON TYPE ASSIGN expression','feature',5,'p_feature_attr_initialized','parser.py',158),
  ('feature -> ID COLON TYPE','feature',3,'p_feature_attr','parser.py',164),
  ('formal_params_list -> formal_params_list COMMA formal_param','formal_params_list',3,'p_formal_list_many','parser.py',170),
  ('formal_params_list -> formal_param','formal_params_list',1,'p_formal_list_many','parser.py',171),
  ('formal_param -> ID COLON TYPE','formal_param',3,'p_formal','parser.py',180),
  ('expression -> ID','expression',1,'p_expression_object_identifier','parser.py',186),
  ('expression -> INTEGER','expression',1,'p_expression_integer_constant','parser.py',192),
  ('expression -> BOOLEAN','expression',1,'p_expression_boolean_constant','parser.py',198),
  ('expression -> STRING','expression',1,'p_expression_string_constant','parser.py',204),
  ('expression -> SELF','expression',1,'p_expr_self','parser.py',210),
  ('expression -> LBRACE block_list RBRACE','expression',3,'p_expression_block','parser.py',216),
  ('block_list -> block_list expression SEMICOLON','block_list',3,'p_block_list','parser.py',222),
  ('block_list -> expression SEMICOLON','block_list',2,'p_block_list','parser.py',223),
  ('expression -> ID ASSIGN expression','expression',3,'p_expression_assignment','parser.py',232),
  ('expression -> expression DOT ID LPAREN arguments_list_opt RPAREN','expression',6,'p_expression_dispatch','parser.py',240),
  ('arguments_list_opt -> arguments_list','arguments_list_opt',1,'p_arguments_list_opt','parser.py',246),
  ('arguments_list_opt -> empty','arguments_list_opt',1,'p_arguments_list_opt','parser.py',247),
  ('arguments_list -> arguments_list COMMA expression','arguments_list',3,'p_arguments_list','parser.py',253),
  ('arguments_list -> expression','arguments_list',1,'p_arguments_list','parser.py',254),
  ('expression -> expression AT TYPE DOT ID LPAREN arguments_list_opt RPAREN','expression',8,'p_expression_static_dispatch','parser.py',263),
  ('expression -> ID LPAREN arguments_list_opt RPAREN','expression',4,'p_expression_self_dispatch','parser.py',269),
  ('expression -> expression PLUS expression','expression',3,'p_expression_math_operations','parser.py',277),
  ('expression -> expression MINUS expression','expression',3,'p_expression_math_operations','parser.py',278),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_math_operations','parser.py',279),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_math_operations','parser.py',280),
  ('expression -> expression LT expression','expression',3,'p_expression_math_comparisons','parser.py',293),
  ('expression -> expression LTEQ expression','expression',3,'p_expression_math_comparisons','parser.py',294),
  ('expression -> expression EQ expression','expression',3,'p_expression_math_comparisons','parser.py',295),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_with_parenthesis','parser.py',306),
  ('expression -> IF expression THEN expression ELSE expression FI','expression',7,'p_expression_if_conditional','parser.py',314),
  ('expression -> WHILE expression LOOP expression POOL','expression',5,'p_expression_while_loop','parser.py',320),
  ('expression -> let_expression','expression',1,'p_expression_let','parser.py',328),
  ('let_expression -> LET ID COLON TYPE IN expression','let_expression',6,'p_expression_let_simple','parser.py',334),
  ('let_expression -> nested_lets COMMA LET ID COLON TYPE','let_expression',6,'p_expression_let_simple','parser.py',335),
  ('let_expression -> LET ID COLON TYPE ASSIGN expression IN expression','let_expression',8,'p_expression_let_initialized','parser.py',341),
  ('let_expression -> nested_lets COMMA LET ID COLON TYPE ASSIGN expression','let_expression',8,'p_expression_let_initialized','parser.py',342),
  ('nested_lets -> ID COLON TYPE IN expression','nested_lets',5,'p_inner_lets_simple','parser.py',348),
  ('nested_lets -> nested_lets COMMA ID COLON TYPE','nested_lets',5,'p_inner_lets_simple','parser.py',349),
  ('nested_lets -> ID COLON TYPE ASSIGN expression IN expression','nested_lets',7,'p_inner_lets_initialized','parser.py',355),
  ('nested_lets -> nested_lets COMMA ID COLON TYPE ASSIGN expression','nested_lets',7,'p_inner_lets_initialized','parser.py',356),
  ('expression -> CASE expression OF actions_list ESAC','expression',5,'p_expression_case','parser.py',364),
  ('actions_list -> actions_list action','actions_list',2,'p_actions_list','parser.py',370),
  ('actions_list -> action','actions_list',1,'p_actions_list','parser.py',371),
  ('action -> ID COLON TYPE ARROW expression SEMICOLON','action',6,'p_action_expr','parser.py',380),
  ('expression -> NEW TYPE','expression',2,'p_expression_new','parser.py',388),
  ('expression -> ISVOID expression','expression',2,'p_expression_isvoid','parser.py',394),
  ('expression -> INT_COMP expression','expression',2,'p_expression_integer_complement','parser.py',400),
  ('expression -> NOT expression','expression',2,'p_expression_boolean_complement','parser.py',406),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',414),
]
