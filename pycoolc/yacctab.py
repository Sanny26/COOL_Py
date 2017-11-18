
# yacctab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASSIGNrightNOTnonassocLTEQLTEQleftPLUSMINUSleftMULTIPLYDIVIDErightISVOIDrightINT_COMPleftATleftDOTID TYPE INTEGER STRING BOOLEAN LPAREN RPAREN LBRACE RBRACE COLON COMMA DOT SEMICOLON AT PLUS MINUS MULTIPLY DIVIDE EQ LT LTEQ ASSIGN INT_COMP NOT ARROW FI OF CLASS ESAC POOL LOOP ISVOID LET SELF IN CASE ELSE IF NEW INHERITS THEN WHILE\n        program : class_list\n        \n        class_list : class_list class SEMICOLON\n                   | class SEMICOLON\n        \n        class : CLASS TYPE LBRACE features_list_opt RBRACE\n        \n        class : CLASS TYPE INHERITS TYPE LBRACE features_list_opt RBRACE\n        \n        features_list_opt : features_list\n                          | empty\n        \n        features_list : features_list feature SEMICOLON\n                      | feature SEMICOLON\n        \n        feature : ID LPAREN formal_params_list RPAREN COLON TYPE LBRACE expression RBRACE\n        \n        feature : ID LPAREN RPAREN COLON TYPE LBRACE expression RBRACE\n        \n        feature : ID COLON TYPE ASSIGN expression\n        \n        feature : ID COLON TYPE\n        \n        formal_params_list  : formal_params_list COMMA formal_param\n                            | formal_param\n        \n        formal_param : ID COLON TYPE\n        \n        expression : ID\n        \n        expression : INTEGER\n        \n        expression : BOOLEAN\n        \n        expression : STRING\n        \n        expression  : SELF\n        \n        expression : LBRACE block_list RBRACE\n        \n        block_list : block_list expression SEMICOLON\n                   | expression SEMICOLON\n        \n        expression : ID ASSIGN expression\n        \n        expression : expression DOT ID LPAREN arguments_list_opt RPAREN\n        \n        arguments_list_opt : arguments_list\n                           | empty\n        \n        arguments_list : arguments_list COMMA expression\n                       | expression\n        \n        expression : expression AT TYPE DOT ID LPAREN arguments_list_opt RPAREN\n        \n        expression : ID LPAREN arguments_list_opt RPAREN\n        \n        expression : expression PLUS expression\n                   | expression MINUS expression\n                   | expression MULTIPLY expression\n                   | expression DIVIDE expression\n        \n        expression : expression LT expression\n                   | expression LTEQ expression\n                   | expression EQ expression\n        \n        expression : LPAREN expression RPAREN\n        \n        expression : IF expression THEN expression ELSE expression FI\n        \n        expression : WHILE expression LOOP expression POOL\n        \n         expression : let_expression\n        \n        let_expression : LET ID COLON TYPE IN expression\n                       | nested_lets COMMA LET ID COLON TYPE\n        \n        let_expression : LET ID COLON TYPE ASSIGN expression IN expression\n                       | nested_lets COMMA LET ID COLON TYPE ASSIGN expression\n        \n        nested_lets : ID COLON TYPE IN expression\n                    | nested_lets COMMA ID COLON TYPE\n        \n        nested_lets : ID COLON TYPE ASSIGN expression IN expression\n                    | nested_lets COMMA ID COLON TYPE ASSIGN expression\n        \n        expression : CASE expression OF actions_list ESAC\n        \n        actions_list : actions_list action\n                     | action\n        \n        action : ID COLON TYPE ARROW expression SEMICOLON\n        \n        expression : NEW TYPE\n        \n        expression : ISVOID expression\n        \n        expression : INT_COMP expression\n        \n        expression : NOT expression\n        \n        empty :\n        '
    
_lr_action_items = {'NOT':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,78,82,83,84,100,101,104,114,122,124,125,127,134,135,138,143,149,151,153,154,155,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-24,40,40,-23,40,40,40,40,40,40,40,40,40,40,40,40,]),'COMMA':([24,26,37,39,41,42,44,47,49,54,57,60,73,74,79,86,88,89,91,92,93,94,99,103,106,107,110,126,132,137,139,141,142,144,147,148,156,157,158,159,161,162,],[31,-15,-14,-16,-19,-21,-18,72,-20,-43,-17,-59,-56,-57,-58,-33,-38,-36,-34,-39,-35,-37,-40,-22,-25,-30,127,-32,-52,-49,-42,-48,-29,-26,-44,-45,-51,-41,-50,-31,-46,-47,]),'COLON':([15,25,27,30,57,71,98,116,119,],[21,32,33,36,81,96,120,131,136,]),'WHILE':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,78,82,83,84,100,101,104,114,122,124,125,127,134,135,138,143,149,151,153,154,155,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-24,56,56,-23,56,56,56,56,56,56,56,56,56,56,56,56,]),'RPAREN':([20,24,26,37,39,41,42,44,49,54,57,60,73,74,75,79,83,86,88,89,91,92,93,94,99,103,106,107,108,109,110,114,126,130,132,139,142,143,144,147,148,152,157,159,161,162,],[25,30,-15,-14,-16,-19,-21,-18,-20,-43,-17,-59,-56,-57,99,-58,-60,-33,-38,-36,-34,-39,-35,-37,-40,-22,-25,-30,-28,126,-27,-60,-32,144,-52,-42,-29,-60,-26,-44,-45,159,-41,-31,-46,-47,]),'TYPE':([4,10,21,32,33,36,48,62,81,96,120,131,136,],[7,16,28,38,39,58,73,87,105,118,137,145,148,]),'LTEQ':([41,42,43,44,49,54,57,60,70,73,74,75,76,77,79,80,85,86,88,89,91,92,93,94,99,102,103,106,107,111,121,123,126,132,139,140,141,142,144,146,147,148,150,156,157,158,159,160,161,162,],[-19,-21,63,-18,-20,-43,-17,63,63,-56,-57,63,63,63,-58,63,63,-33,None,-36,-34,None,-35,None,-40,63,-22,63,63,63,63,63,-32,-52,-42,63,63,63,-26,63,63,-45,63,63,-41,63,-31,63,63,63,]),'SEMICOLON':([1,6,14,17,18,28,35,41,42,43,44,49,54,57,60,73,74,77,79,86,88,89,91,92,93,94,99,102,103,106,112,126,128,132,139,144,147,148,157,159,160,161,162,],[5,8,19,-4,23,-13,-5,-19,-21,-12,-18,-20,-43,-17,-59,-56,-57,101,-58,-33,-38,-36,-34,-39,-35,-37,-40,122,-22,-25,-11,-32,-10,-52,-42,-26,-44,-45,-41,-31,163,-46,-47,]),'SELF':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,78,82,83,84,100,101,104,114,122,124,125,127,134,135,138,143,149,151,153,154,155,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-24,42,42,-23,42,42,42,42,42,42,42,42,42,42,42,42,]),'POOL':([41,42,44,49,54,57,60,73,74,79,86,88,89,91,92,93,94,99,103,106,123,126,132,139,144,147,148,157,159,161,162,],[-19,-21,-18,-20,-43,-17,-59,-56,-57,-58,-33,-38,-36,-34,-39,-35,-37,-40,-22,-25,139,-32,-52,-42,-26,-44,-45,-41,-31,-46,-47,]),'IN':([41,42,44,49,54,57,60,73,74,79,86,88,89,91,92,93,94,99,103,105,106,118,126,132,139,140,144,146,147,148,157,159,161,162,],[-19,-21,-18,-20,-43,-17,-59,-56,-57,-58,-33,-38,-36,-34,-39,-35,-37,-40,-22,125,-25,135,-32,-52,-42,151,-26,154,-44,-45,-41,-31,-46,-47,]),'IF':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,78,82,83,84,100,101,104,114,122,124,125,127,134,135,138,143,149,151,153,154,155,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-24,52,52,-23,52,52,52,52,52,52,52,52,52,52,52,52,]),'DOT':([41,42,43,44,49,54,57,60,70,73,74,75,76,77,79,80,85,86,87,88,89,91,92,93,94,99,102,103,106,107,111,121,123,126,132,139,140,141,142,144,146,147,148,150,156,157,158,159,160,161,162,],[-19,-21,65,-18,-20,-43,-17,65,65,-56,65,65,65,65,65,65,65,65,113,65,65,65,65,65,65,-40,65,-22,65,65,65,65,65,-32,-52,-42,65,65,65,-26,65,65,-45,65,65,-41,65,-31,65,65,65,]),'ASSIGN':([28,57,105,118,137,148,],[34,82,124,134,149,155,]),'FI':([41,42,44,49,54,57,60,73,74,79,86,88,89,91,92,93,94,99,103,106,126,132,139,144,147,148,150,157,159,161,162,],[-19,-21,-18,-20,-43,-17,-59,-56,-57,-58,-33,-38,-36,-34,-39,-35,-37,-40,-22,-25,-32,-52,-42,-26,-44,-45,157,-41,-31,-46,-47,]),'ELSE':([41,42,44,49,54,57,60,73,74,79,86,88,89,91,92,93,94,99,103,106,121,126,132,139,144,147,148,157,159,161,162,],[-19,-21,-18,-20,-43,-17,-59,-56,-57,-58,-33,-38,-36,-34,-39,-35,-37,-40,-22,-25,138,-32,-52,-42,-26,-44,-45,-41,-31,-46,-47,]),'ARROW':([145,],[153,]),'EQ':([41,42,43,44,49,54,57,60,70,73,74,75,76,77,79,80,85,86,88,89,91,92,93,94,99,102,103,106,107,111,121,123,126,132,139,140,141,142,144,146,147,148,150,156,157,158,159,160,161,162,],[-19,-21,67,-18,-20,-43,-17,67,67,-56,-57,67,67,67,-58,67,67,-33,None,-36,-34,None,-35,None,-40,67,-22,67,67,67,67,67,-32,-52,-42,67,67,67,-26,67,67,-45,67,67,-41,67,-31,67,67,67,]),'$end':([2,3,5,8,],[0,-1,-3,-2,]),'MULTIPLY':([41,42,43,44,49,54,57,60,70,73,74,75,76,77,79,80,85,86,88,89,91,92,93,94,99,102,103,106,107,111,121,123,126,132,139,140,141,142,144,146,147,148,150,156,157,158,159,160,161,162,],[-19,-21,68,-18,-20,-43,-17,68,68,-56,-57,68,68,68,-58,68,68,68,68,-36,68,68,-35,68,-40,68,-22,68,68,68,68,68,-32,-52,-42,68,68,68,-26,68,68,-45,68,68,-41,68,-31,68,68,68,]),'ISVOID':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,78,82,83,84,100,101,104,114,122,124,125,127,134,135,138,143,149,151,153,154,155,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-24,50,50,-23,50,50,50,50,50,50,50,50,50,50,50,50,]),'LBRACE':([7,16,34,38,40,45,50,51,52,53,55,56,58,59,61,63,64,66,67,68,69,78,82,83,84,100,101,104,114,122,124,125,127,134,135,138,143,149,151,153,154,155,],[9,22,53,59,53,53,53,53,53,53,53,53,84,53,53,53,53,53,53,53,53,53,53,53,53,53,-24,53,53,-23,53,53,53,53,53,53,53,53,53,53,53,53,]),'INHERITS':([7,],[10,]),'AT':([41,42,43,44,49,54,57,60,70,73,74,75,76,77,79,80,85,86,88,89,91,92,93,94,99,102,103,106,107,111,121,123,126,132,139,140,141,142,144,146,147,148,150,156,157,158,159,160,161,162,],[-19,-21,62,-18,-20,-43,-17,62,62,-56,62,62,62,62,62,62,62,62,62,62,62,62,62,62,-40,62,-22,62,62,62,62,62,-32,-52,-42,62,62,62,-26,62,62,-45,62,62,-41,62,-31,62,62,62,]),'BOOLEAN':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,78,82,83,84,100,101,104,114,122,124,125,127,134,135,138,143,149,151,153,154,155,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-24,41,41,-23,41,41,41,41,41,41,41,41,41,41,41,41,]),'INTEGER':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,78,82,83,84,100,101,104,114,122,124,125,127,134,135,138,143,149,151,153,154,155,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-24,44,44,-23,44,44,44,44,44,44,44,44,44,44,44,44,]),'LPAREN':([15,34,40,45,50,51,52,53,55,56,57,59,61,63,64,66,67,68,69,78,82,83,84,90,100,101,104,114,122,124,125,127,129,134,135,138,143,149,151,153,154,155,],[20,51,51,51,51,51,51,51,51,51,83,51,51,51,51,51,51,51,51,51,51,51,51,114,51,-24,51,51,-23,51,51,51,143,51,51,51,51,51,51,51,51,51,]),'CASE':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,78,82,83,84,100,101,104,114,122,124,125,127,134,135,138,143,149,151,153,154,155,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-24,45,45,-23,45,45,45,45,45,45,45,45,45,45,45,45,]),'ESAC':([115,117,133,163,],[-54,132,-53,-55,]),'LET':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,72,78,82,83,84,100,101,104,114,122,124,125,127,134,135,138,143,149,151,153,154,155,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,97,46,46,46,46,46,-24,46,46,-23,46,46,46,46,46,46,46,46,46,46,46,46,]),'THEN':([41,42,44,49,54,57,60,73,74,76,79,86,88,89,91,92,93,94,99,103,106,126,132,139,144,147,148,157,159,161,162,],[-19,-21,-18,-20,-43,-17,-59,-56,-57,100,-58,-33,-38,-36,-34,-39,-35,-37,-40,-22,-25,-32,-52,-42,-26,-44,-45,-41,-31,-46,-47,]),'LT':([41,42,43,44,49,54,57,60,70,73,74,75,76,77,79,80,85,86,88,89,91,92,93,94,99,102,103,106,107,111,121,123,126,132,139,140,141,142,144,146,147,148,150,156,157,158,159,160,161,162,],[-19,-21,69,-18,-20,-43,-17,69,69,-56,-57,69,69,69,-58,69,69,-33,None,-36,-34,None,-35,None,-40,69,-22,69,69,69,69,69,-32,-52,-42,69,69,69,-26,69,69,-45,69,69,-41,69,-31,69,69,69,]),'NEW':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,78,82,83,84,100,101,104,114,122,124,125,127,134,135,138,143,149,151,153,154,155,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-24,48,48,-23,48,48,48,48,48,48,48,48,48,48,48,48,]),'DIVIDE':([41,42,43,44,49,54,57,60,70,73,74,75,76,77,79,80,85,86,88,89,91,92,93,94,99,102,103,106,107,111,121,123,126,132,139,140,141,142,144,146,147,148,150,156,157,158,159,160,161,162,],[-19,-21,64,-18,-20,-43,-17,64,64,-56,-57,64,64,64,-58,64,64,64,64,-36,64,64,-35,64,-40,64,-22,64,64,64,64,64,-32,-52,-42,64,64,64,-26,64,64,-45,64,64,-41,64,-31,64,64,64,]),'PLUS':([41,42,43,44,49,54,57,60,70,73,74,75,76,77,79,80,85,86,88,89,91,92,93,94,99,102,103,106,107,111,121,123,126,132,139,140,141,142,144,146,147,148,150,156,157,158,159,160,161,162,],[-19,-21,61,-18,-20,-43,-17,61,61,-56,-57,61,61,61,-58,61,61,-33,61,-36,-34,61,-35,61,-40,61,-22,61,61,61,61,61,-32,-52,-42,61,61,61,-26,61,61,-45,61,61,-41,61,-31,61,61,61,]),'RBRACE':([9,11,12,13,19,22,23,29,41,42,44,49,54,57,60,73,74,78,79,85,86,88,89,91,92,93,94,99,101,103,106,111,122,126,132,139,144,147,148,157,159,161,162,],[-60,17,-7,-6,-9,-60,-8,35,-19,-21,-18,-20,-43,-17,-59,-56,-57,103,-58,112,-33,-38,-36,-34,-39,-35,-37,-40,-24,-22,-25,128,-23,-32,-52,-42,-26,-44,-45,-41,-31,-46,-47,]),'MINUS':([41,42,43,44,49,54,57,60,70,73,74,75,76,77,79,80,85,86,88,89,91,92,93,94,99,102,103,106,107,111,121,123,126,132,139,140,141,142,144,146,147,148,150,156,157,158,159,160,161,162,],[-19,-21,66,-18,-20,-43,-17,66,66,-56,-57,66,66,66,-58,66,66,-33,66,-36,-34,66,-35,66,-40,66,-22,66,66,66,66,66,-32,-52,-42,66,66,66,-26,66,66,-45,66,66,-41,66,-31,66,66,66,]),'INT_COMP':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,78,82,83,84,100,101,104,114,122,124,125,127,134,135,138,143,149,151,153,154,155,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-24,55,55,-23,55,55,55,55,55,55,55,55,55,55,55,55,]),'OF':([41,42,44,49,54,57,60,70,73,74,79,86,88,89,91,92,93,94,99,103,106,126,132,139,144,147,148,157,159,161,162,],[-19,-21,-18,-20,-43,-17,-59,95,-56,-57,-58,-33,-38,-36,-34,-39,-35,-37,-40,-22,-25,-32,-52,-42,-26,-44,-45,-41,-31,-46,-47,]),'CLASS':([0,3,5,8,],[4,4,-3,-2,]),'ID':([9,13,19,20,22,23,31,34,40,45,46,50,51,52,53,55,56,59,61,63,64,65,66,67,68,69,72,78,82,83,84,95,97,100,101,104,113,114,115,117,122,124,125,127,133,134,135,138,143,149,151,153,154,155,163,],[15,15,-9,27,15,-8,27,57,57,57,71,57,57,57,57,57,57,57,57,57,57,90,57,57,57,57,98,57,57,57,57,116,119,57,-24,57,129,57,-54,116,-23,57,57,57,-53,57,57,57,57,57,57,57,57,57,-55,]),'STRING':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,78,82,83,84,100,101,104,114,122,124,125,127,134,135,138,143,149,151,153,154,155,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-24,49,49,-23,49,49,49,49,49,49,49,49,49,49,49,49,]),'LOOP':([41,42,44,49,54,57,60,73,74,79,80,86,88,89,91,92,93,94,99,103,106,126,132,139,144,147,148,157,159,161,162,],[-19,-21,-18,-20,-43,-17,-59,-56,-57,-58,104,-33,-38,-36,-34,-39,-35,-37,-40,-22,-25,-32,-52,-42,-26,-44,-45,-41,-31,-46,-47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'features_list_opt':([9,22,],[11,29,]),'action':([95,117,],[115,133,]),'class':([0,3,],[1,6,]),'program':([0,],[2,]),'let_expression':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,78,82,83,84,100,104,114,124,125,127,134,135,138,143,149,151,153,154,155,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'features_list':([9,22,],[13,13,]),'feature':([9,13,22,],[14,18,14,]),'arguments_list':([83,114,143,],[110,110,110,]),'arguments_list_opt':([83,114,143,],[109,130,152,]),'formal_param':([20,31,],[26,37,]),'block_list':([53,],[78,]),'nested_lets':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,78,82,83,84,100,104,114,124,125,127,134,135,138,143,149,151,153,154,155,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'actions_list':([95,],[117,]),'formal_params_list':([20,],[24,]),'empty':([9,22,83,114,143,],[12,12,108,108,108,]),'class_list':([0,],[3,]),'expression':([34,40,45,50,51,52,53,55,56,59,61,63,64,66,67,68,69,78,82,83,84,100,104,114,124,125,127,134,135,138,143,149,151,153,154,155,],[43,60,70,74,75,76,77,79,80,85,86,88,89,91,92,93,94,102,106,107,111,121,123,107,140,141,142,146,147,150,107,156,158,160,161,162,]),}

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
