
# yacctab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASSIGNrightNOTnonassocLTEQLTEQleftPLUSMINUSleftMULTIPLYDIVIDErightISVOIDrightINT_COMPleftATleftDOTID TYPE INTEGER STRING BOOLEAN LPAREN RPAREN LBRACE RBRACE COLON COMMA DOT SEMICOLON AT PLUS MINUS MULTIPLY DIVIDE EQ LT LTEQ ASSIGN INT_COMP NOT ARROW SELF OF FI WHILE IF INHERITS CLASS LOOP POOL ELSE ISVOID CASE THEN IN ESAC NEW LET\n        program : class_list\n        \n        class_list : class_list class SEMICOLON\n                   | class SEMICOLON\n        \n        class : CLASS TYPE LBRACE features_list_opt RBRACE\n        \n        class : CLASS TYPE INHERITS TYPE LBRACE features_list_opt RBRACE\n        \n        features_list_opt : features_list\n                          | empty\n        \n        features_list : features_list feature SEMICOLON\n                      | feature SEMICOLON\n        \n        feature : ID LPAREN formal_params_list RPAREN COLON TYPE LBRACE expression RBRACE\n        \n        feature : ID LPAREN RPAREN COLON TYPE LBRACE expression RBRACE\n        \n        feature : ID COLON TYPE ASSIGN expression\n        \n        feature : ID COLON TYPE\n        \n        formal_params_list  : formal_params_list COMMA formal_param\n                            | formal_param\n        \n        formal_param : ID COLON TYPE\n        \n        expression : ID\n        \n        expression : INTEGER\n        \n        expression : BOOLEAN\n        \n        expression : STRING\n        \n        expression  : SELF\n        \n        expression : LBRACE block_list RBRACE\n        \n        block_list : block_list expression SEMICOLON\n                   | expression SEMICOLON\n        \n        expression : ID ASSIGN expression\n        \n        expression : expression DOT ID LPAREN arguments_list_opt RPAREN\n        \n        arguments_list_opt : arguments_list\n                           | empty\n        \n        arguments_list : arguments_list COMMA expression\n                       | expression\n        \n        expression : expression AT TYPE DOT ID LPAREN arguments_list_opt RPAREN\n        \n        expression : ID LPAREN arguments_list_opt RPAREN\n        \n        expression : expression PLUS expression\n                   | expression MINUS expression\n                   | expression MULTIPLY expression\n                   | expression DIVIDE expression\n        \n        expression : expression LT expression\n                   | expression LTEQ expression\n                   | expression EQ expression\n        \n        expression : LPAREN expression RPAREN\n        \n        expression : IF expression THEN expression ELSE expression FI\n        \n        expression : WHILE expression LOOP expression POOL\n        \n         expression : let_expression\n        \n        let_expression : LET ID COLON TYPE IN expression\n                       | nested_lets COMMA LET ID COLON TYPE\n        \n        let_expression : LET ID COLON TYPE ASSIGN expression IN expression\n                       | nested_lets COMMA LET ID COLON TYPE ASSIGN expression\n        \n        nested_lets : ID COLON TYPE IN expression\n                    | nested_lets COMMA ID COLON TYPE\n        \n        nested_lets : ID COLON TYPE ASSIGN expression IN expression\n                    | nested_lets COMMA ID COLON TYPE ASSIGN expression\n        \n        expression : CASE expression OF actions_list ESAC\n        \n        actions_list : actions_list action\n                     | action\n        \n        action : ID COLON TYPE ARROW expression SEMICOLON\n        \n        expression : NEW TYPE\n        \n        expression : ISVOID expression\n        \n        expression : INT_COMP expression\n        \n        expression : NOT expression\n        \n        empty :\n        '
    
_lr_action_items = {'COMMA':([25,27,36,38,39,40,41,51,52,54,57,58,65,66,81,88,90,93,94,95,96,97,98,100,103,106,107,123,129,134,135,139,140,143,145,148,153,157,158,159,160,162,],[31,-15,-18,59,-20,-21,-19,-43,-17,-14,-16,-56,-59,-58,-57,-40,-22,-39,-34,-33,-37,-38,-36,-35,122,-30,-25,-32,-49,-52,-42,-29,-48,-45,-44,-26,-51,-41,-50,-47,-46,-31,]),'CLASS':([0,2,7,10,],[1,1,-3,-2,]),'POOL':([36,39,40,41,51,52,58,65,66,81,88,90,93,94,95,96,97,98,100,107,118,123,134,135,143,145,148,157,159,160,162,],[-18,-20,-21,-19,-43,-17,-56,-59,-58,-57,-40,-22,-39,-34,-33,-37,-38,-36,-35,-25,135,-32,-52,-42,-45,-44,-26,-41,-47,-46,-31,]),'THEN':([36,39,40,41,51,52,58,65,66,77,81,88,90,93,94,95,96,97,98,100,107,123,134,135,143,145,148,157,159,160,162,],[-18,-20,-21,-19,-43,-17,-56,-59,-58,102,-57,-40,-22,-39,-34,-33,-37,-38,-36,-35,-25,-32,-52,-42,-45,-44,-26,-41,-47,-46,-31,]),'INTEGER':([30,43,44,45,46,47,48,50,53,63,68,69,70,71,72,73,75,78,79,83,91,92,102,109,117,119,122,124,125,130,131,138,144,149,151,152,154,155,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-24,36,36,36,-23,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'TYPE':([1,9,20,33,34,37,55,76,80,86,112,128,132,],[5,16,24,56,57,58,82,101,108,113,129,143,147,]),'RPAREN':([21,25,27,36,39,40,41,51,52,54,57,58,62,65,66,78,81,88,90,93,94,95,96,97,98,100,103,104,105,106,107,119,123,134,135,136,139,143,145,148,149,156,157,159,160,162,],[26,32,-15,-18,-20,-21,-19,-43,-17,-14,-16,-56,88,-59,-58,-60,-57,-40,-22,-39,-34,-33,-37,-38,-36,-35,-27,123,-28,-30,-25,-60,-32,-52,-42,148,-29,-45,-44,-26,-60,162,-41,-47,-46,-31,]),'WHILE':([30,43,44,45,46,47,48,50,53,63,68,69,70,71,72,73,75,78,79,83,91,92,102,109,117,119,122,124,125,130,131,138,144,149,151,152,154,155,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-24,48,48,48,-23,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'LBRACE':([5,16,30,43,44,45,46,47,48,50,53,56,63,68,69,70,71,72,73,75,78,79,82,83,91,92,102,109,117,119,122,124,125,130,131,138,144,149,151,152,154,155,],[8,22,45,45,45,45,45,45,45,45,45,83,45,45,45,45,45,45,45,45,45,45,109,45,-24,45,45,45,-23,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'NOT':([30,43,44,45,46,47,48,50,53,63,68,69,70,71,72,73,75,78,79,83,91,92,102,109,117,119,122,124,125,130,131,138,144,149,151,152,154,155,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-24,46,46,46,-23,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'NEW':([30,43,44,45,46,47,48,50,53,63,68,69,70,71,72,73,75,78,79,83,91,92,102,109,117,119,122,124,125,130,131,138,144,149,151,152,154,155,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-24,37,37,37,-23,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'MINUS':([36,39,40,41,49,51,52,58,61,62,64,65,66,67,77,81,88,89,90,93,94,95,96,97,98,100,106,107,110,118,121,123,126,134,135,139,140,141,143,145,146,148,150,153,157,158,159,160,161,162,],[-18,-20,-21,-19,69,-43,-17,-56,69,69,69,69,-58,69,69,-57,-40,69,-22,69,-34,-33,69,69,-36,-35,69,69,69,69,69,-32,69,-52,-42,69,69,69,-45,69,69,-26,69,69,-41,69,69,69,69,-31,]),'OF':([36,39,40,41,51,52,58,61,65,66,81,88,90,93,94,95,96,97,98,100,107,123,134,135,143,145,148,157,159,160,162,],[-18,-20,-21,-19,-43,-17,-56,87,-59,-58,-57,-40,-22,-39,-34,-33,-37,-38,-36,-35,-25,-32,-52,-42,-45,-44,-26,-41,-47,-46,-31,]),'DIVIDE':([36,39,40,41,49,51,52,58,61,62,64,65,66,67,77,81,88,89,90,93,94,95,96,97,98,100,106,107,110,118,121,123,126,134,135,139,140,141,143,145,146,148,150,153,157,158,159,160,161,162,],[-18,-20,-21,-19,73,-43,-17,-56,73,73,73,73,-58,73,73,-57,-40,73,-22,73,73,73,73,73,-36,-35,73,73,73,73,73,-32,73,-52,-42,73,73,73,-45,73,73,-26,73,73,-41,73,73,73,73,-31,]),'LOOP':([36,39,40,41,51,52,58,65,66,67,81,88,90,93,94,95,96,97,98,100,107,123,134,135,143,145,148,157,159,160,162,],[-18,-20,-21,-19,-43,-17,-56,-59,-58,92,-57,-40,-22,-39,-34,-33,-37,-38,-36,-35,-25,-32,-52,-42,-45,-44,-26,-41,-47,-46,-31,]),'INT_COMP':([30,43,44,45,46,47,48,50,53,63,68,69,70,71,72,73,75,78,79,83,91,92,102,109,117,119,122,124,125,130,131,138,144,149,151,152,154,155,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-24,47,47,47,-23,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'COLON':([14,26,28,32,52,60,85,111,115,],[20,33,34,55,80,86,112,128,132,]),'LT':([36,39,40,41,49,51,52,58,61,62,64,65,66,67,77,81,88,89,90,93,94,95,96,97,98,100,106,107,110,118,121,123,126,134,135,139,140,141,143,145,146,148,150,153,157,158,159,160,161,162,],[-18,-20,-21,-19,71,-43,-17,-56,71,71,71,71,-58,71,71,-57,-40,71,-22,None,-34,-33,None,None,-36,-35,71,71,71,71,71,-32,71,-52,-42,71,71,71,-45,71,71,-26,71,71,-41,71,71,71,71,-31,]),'ESAC':([114,116,133,163,],[-54,134,-53,-55,]),'STRING':([30,43,44,45,46,47,48,50,53,63,68,69,70,71,72,73,75,78,79,83,91,92,102,109,117,119,122,124,125,130,131,138,144,149,151,152,154,155,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-24,39,39,39,-23,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'EQ':([36,39,40,41,49,51,52,58,61,62,64,65,66,67,77,81,88,89,90,93,94,95,96,97,98,100,106,107,110,118,121,123,126,134,135,139,140,141,143,145,146,148,150,153,157,158,159,160,161,162,],[-18,-20,-21,-19,68,-43,-17,-56,68,68,68,68,-58,68,68,-57,-40,68,-22,None,-34,-33,None,None,-36,-35,68,68,68,68,68,-32,68,-52,-42,68,68,68,-45,68,68,-26,68,68,-41,68,68,68,68,-31,]),'SELF':([30,43,44,45,46,47,48,50,53,63,68,69,70,71,72,73,75,78,79,83,91,92,102,109,117,119,122,124,125,130,131,138,144,149,151,152,154,155,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-24,40,40,40,-23,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'BOOLEAN':([30,43,44,45,46,47,48,50,53,63,68,69,70,71,72,73,75,78,79,83,91,92,102,109,117,119,122,124,125,130,131,138,144,149,151,152,154,155,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-24,41,41,41,-23,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'IN':([36,39,40,41,51,52,58,65,66,81,88,90,93,94,95,96,97,98,100,107,108,113,123,134,135,141,143,145,146,148,157,159,160,162,],[-18,-20,-21,-19,-43,-17,-56,-59,-58,-57,-40,-22,-39,-34,-33,-37,-38,-36,-35,-25,124,130,-32,-52,-42,151,-45,-44,154,-26,-41,-47,-46,-31,]),'DOT':([36,39,40,41,49,51,52,58,61,62,64,65,66,67,77,81,88,89,90,93,94,95,96,97,98,100,101,106,107,110,118,121,123,126,134,135,139,140,141,143,145,146,148,150,153,157,158,159,160,161,162,],[-18,-20,-21,-19,74,-43,-17,-56,74,74,74,74,74,74,74,74,-40,74,-22,74,74,74,74,74,74,74,120,74,74,74,74,74,-32,74,-52,-42,74,74,74,-45,74,74,-26,74,74,-41,74,74,74,74,-31,]),'PLUS':([36,39,40,41,49,51,52,58,61,62,64,65,66,67,77,81,88,89,90,93,94,95,96,97,98,100,106,107,110,118,121,123,126,134,135,139,140,141,143,145,146,148,150,153,157,158,159,160,161,162,],[-18,-20,-21,-19,70,-43,-17,-56,70,70,70,70,-58,70,70,-57,-40,70,-22,70,-34,-33,70,70,-36,-35,70,70,70,70,70,-32,70,-52,-42,70,70,70,-45,70,70,-26,70,70,-41,70,70,70,70,-31,]),'SEMICOLON':([4,6,12,17,19,24,35,36,39,40,41,49,51,52,58,64,65,66,81,88,89,90,93,94,95,96,97,98,100,107,123,127,134,135,142,143,145,148,157,159,160,161,162,],[7,10,18,-4,23,-13,-5,-18,-20,-21,-19,-12,-43,-17,-56,91,-59,-58,-57,-40,117,-22,-39,-34,-33,-37,-38,-36,-35,-25,-32,-11,-52,-42,-10,-45,-44,-26,-41,-47,-46,163,-31,]),'$end':([2,3,7,10,],[-1,0,-3,-2,]),'INHERITS':([5,],[9,]),'ARROW':([147,],[155,]),'FI':([36,39,40,41,51,52,58,65,66,81,88,90,93,94,95,96,97,98,100,107,123,134,135,143,145,148,150,157,159,160,162,],[-18,-20,-21,-19,-43,-17,-56,-59,-58,-57,-40,-22,-39,-34,-33,-37,-38,-36,-35,-25,-32,-52,-42,-45,-44,-26,157,-41,-47,-46,-31,]),'IF':([30,43,44,45,46,47,48,50,53,63,68,69,70,71,72,73,75,78,79,83,91,92,102,109,117,119,122,124,125,130,131,138,144,149,151,152,154,155,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-24,50,50,50,-23,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'LTEQ':([36,39,40,41,49,51,52,58,61,62,64,65,66,67,77,81,88,89,90,93,94,95,96,97,98,100,106,107,110,118,121,123,126,134,135,139,140,141,143,145,146,148,150,153,157,158,159,160,161,162,],[-18,-20,-21,-19,72,-43,-17,-56,72,72,72,72,-58,72,72,-57,-40,72,-22,None,-34,-33,None,None,-36,-35,72,72,72,72,72,-32,72,-52,-42,72,72,72,-45,72,72,-26,72,72,-41,72,72,72,72,-31,]),'MULTIPLY':([36,39,40,41,49,51,52,58,61,62,64,65,66,67,77,81,88,89,90,93,94,95,96,97,98,100,106,107,110,118,121,123,126,134,135,139,140,141,143,145,146,148,150,153,157,158,159,160,161,162,],[-18,-20,-21,-19,75,-43,-17,-56,75,75,75,75,-58,75,75,-57,-40,75,-22,75,75,75,75,75,-36,-35,75,75,75,75,75,-32,75,-52,-42,75,75,75,-45,75,75,-26,75,75,-41,75,75,75,75,-31,]),'ELSE':([36,39,40,41,51,52,58,65,66,81,88,90,93,94,95,96,97,98,100,107,121,123,134,135,143,145,148,157,159,160,162,],[-18,-20,-21,-19,-43,-17,-56,-59,-58,-57,-40,-22,-39,-34,-33,-37,-38,-36,-35,-25,138,-32,-52,-42,-45,-44,-26,-41,-47,-46,-31,]),'AT':([36,39,40,41,49,51,52,58,61,62,64,65,66,67,77,81,88,89,90,93,94,95,96,97,98,100,106,107,110,118,121,123,126,134,135,139,140,141,143,145,146,148,150,153,157,158,159,160,161,162,],[-18,-20,-21,-19,76,-43,-17,-56,76,76,76,76,76,76,76,76,-40,76,-22,76,76,76,76,76,76,76,76,76,76,76,76,-32,76,-52,-42,76,76,76,-45,76,76,-26,76,76,-41,76,76,76,76,-31,]),'LET':([30,43,44,45,46,47,48,50,53,59,63,68,69,70,71,72,73,75,78,79,83,91,92,102,109,117,119,122,124,125,130,131,138,144,149,151,152,154,155,],[42,42,42,42,42,42,42,42,42,84,42,42,42,42,42,42,42,42,42,42,42,-24,42,42,42,-23,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'ID':([8,13,18,21,22,23,30,31,42,43,44,45,46,47,48,50,53,59,63,68,69,70,71,72,73,74,75,78,79,83,84,87,91,92,102,109,114,116,117,119,120,122,124,125,130,131,133,138,144,149,151,152,154,155,163,],[14,14,-9,28,14,-8,52,28,60,52,52,52,52,52,52,52,52,85,52,52,52,52,52,52,52,99,52,52,52,52,111,115,-24,52,52,52,-54,115,-23,52,137,52,52,52,52,52,-53,52,52,52,52,52,52,52,-55,]),'CASE':([30,43,44,45,46,47,48,50,53,63,68,69,70,71,72,73,75,78,79,83,91,92,102,109,117,119,122,124,125,130,131,138,144,149,151,152,154,155,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-24,43,43,43,-23,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'LPAREN':([14,30,43,44,45,46,47,48,50,52,53,63,68,69,70,71,72,73,75,78,79,83,91,92,99,102,109,117,119,122,124,125,130,131,137,138,144,149,151,152,154,155,],[21,44,44,44,44,44,44,44,44,78,44,44,44,44,44,44,44,44,44,44,44,44,-24,44,119,44,44,-23,44,44,44,44,44,44,149,44,44,44,44,44,44,44,]),'ASSIGN':([24,52,108,113,129,143,],[30,79,125,131,144,152,]),'ISVOID':([30,43,44,45,46,47,48,50,53,63,68,69,70,71,72,73,75,78,79,83,91,92,102,109,117,119,122,124,125,130,131,138,144,149,151,152,154,155,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-24,53,53,53,-23,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'RBRACE':([8,11,13,15,18,22,23,29,36,39,40,41,51,52,58,63,65,66,81,88,90,91,93,94,95,96,97,98,100,107,110,117,123,126,134,135,143,145,148,157,159,160,162,],[-60,17,-6,-7,-9,-60,-8,35,-18,-20,-21,-19,-43,-17,-56,90,-59,-58,-57,-40,-22,-24,-39,-34,-33,-37,-38,-36,-35,-25,127,-23,-32,142,-52,-42,-45,-44,-26,-41,-47,-46,-31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'class':([0,2,],[4,6,]),'program':([0,],[3,]),'actions_list':([87,],[116,]),'feature':([8,13,22,],[12,19,12,]),'class_list':([0,],[2,]),'features_list_opt':([8,22,],[11,29,]),'block_list':([45,],[63,]),'expression':([30,43,44,45,46,47,48,50,53,63,68,69,70,71,72,73,75,78,79,83,92,102,109,119,122,124,125,130,131,138,144,149,151,152,154,155,],[49,61,62,64,65,66,67,77,81,89,93,94,95,96,97,98,100,106,107,110,118,121,126,106,139,140,141,145,146,150,153,106,158,159,160,161,]),'action':([87,116,],[114,133,]),'nested_lets':([30,43,44,45,46,47,48,50,53,63,68,69,70,71,72,73,75,78,79,83,92,102,109,119,122,124,125,130,131,138,144,149,151,152,154,155,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'let_expression':([30,43,44,45,46,47,48,50,53,63,68,69,70,71,72,73,75,78,79,83,92,102,109,119,122,124,125,130,131,138,144,149,151,152,154,155,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'features_list':([8,22,],[13,13,]),'formal_param':([21,31,],[27,54,]),'formal_params_list':([21,],[25,]),'arguments_list_opt':([78,119,149,],[104,136,156,]),'arguments_list':([78,119,149,],[103,103,103,]),'empty':([8,22,78,119,149,],[15,15,105,105,105,]),}

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
