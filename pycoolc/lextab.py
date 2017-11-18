# lextab.py. This file automatically created by PLY (version 3.10). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('POOL', 'INTEGER', 'ISVOID', 'IN', 'FI', 'MINUS', 'DOT', 'TYPE', 'LTEQ', 'ELSE', 'BOOLEAN', 'INT_COMP', 'OF', 'RBRACE', 'LPAREN', 'LBRACE', 'SEMICOLON', 'WHILE', 'NOT', 'EQ', 'MULTIPLY', 'CASE', 'LET', 'ARROW', 'PLUS', 'SELF', 'CLASS', 'AT', 'LOOP', 'ESAC', 'STRING', 'LT', 'ID', 'THEN', 'RPAREN', 'INHERITS', 'COLON', 'COMMA', 'DIVIDE', 'NEW', 'IF', 'ASSIGN'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'COMMENT': 'exclusive', 'INITIAL': 'inclusive', 'STRING': 'exclusive'}
_lexstatere   = {'COMMENT': [('(?P<t_COMMENT_startanother>\\(\\*)|(?P<t_COMMENT_end>\\*\\))', [None, ('t_COMMENT_startanother', 'startanother'), ('t_COMMENT_end', 'end')])], 'INITIAL': [('(?P<t_BOOLEAN>(true|false))|(?P<t_INTEGER>\\d+)|(?P<t_TYPE>[A-Z][a-zA-Z_0-9]*)|(?P<t_ID>[a-z_][a-zA-Z_0-9]*)|(?P<t_newline>\\n+)|(?P<t_start_string>\\")|(?P<t_start_comment>\\(\\*)|(?P<t_ignore_SINGLE_LINE_COMMENT>\\-\\-[^\\n]*)|(?P<t_ASSIGN>\\<\\-)|(?P<t_LTEQ>\\<\\=)|(?P<t_ARROW>\\=\\>)|(?P<t_NOT>not)|(?P<t_MINUS>\\-)|(?P<t_DOT>\\.)|(?P<t_RPAREN>\\))|(?P<t_SEMICOLON>\\;)|(?P<t_AT>\\@)|(?P<t_MULTIPLY>\\*)|(?P<t_DIVIDE>\\/)|(?P<t_RBRACE>\\})|(?P<t_COMMA>\\,)|(?P<t_LBRACE>\\{)|(?P<t_PLUS>\\+)|(?P<t_EQ>\\=)|(?P<t_COLON>\\:)|(?P<t_LT>\\<)|(?P<t_LPAREN>\\()|(?P<t_INT_COMP>~)', [None, ('t_BOOLEAN', 'BOOLEAN'), None, ('t_INTEGER', 'INTEGER'), ('t_TYPE', 'TYPE'), ('t_ID', 'ID'), ('t_newline', 'newline'), ('t_start_string', 'start_string'), ('t_start_comment', 'start_comment'), (None, None), (None, 'ASSIGN'), (None, 'LTEQ'), (None, 'ARROW'), (None, 'NOT'), (None, 'MINUS'), (None, 'DOT'), (None, 'RPAREN'), (None, 'SEMICOLON'), (None, 'AT'), (None, 'MULTIPLY'), (None, 'DIVIDE'), (None, 'RBRACE'), (None, 'COMMA'), (None, 'LBRACE'), (None, 'PLUS'), (None, 'EQ'), (None, 'COLON'), (None, 'LT'), (None, 'LPAREN'), (None, 'INT_COMP')])], 'STRING': [('(?P<t_STRING_newline>\\n)|(?P<t_STRING_end>\\")|(?P<t_STRING_anything>[^\\n])', [None, ('t_STRING_newline', 'newline'), ('t_STRING_end', 'end'), ('t_STRING_anything', 'anything')])]}
_lexstateignore = {'COMMENT': '', 'INITIAL': ' \t\r\x0c', 'STRING': ''}
_lexstateerrorf = {'COMMENT': 't_COMMENT_error', 'INITIAL': 't_error', 'STRING': 't_STRING_error'}
_lexstateeoff = {}
