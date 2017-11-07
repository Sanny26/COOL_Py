# lextab.py. This file automatically created by PLY (version 3.10). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('COMMA', 'CLASS', 'INTEGER', 'TYPE', 'EQ', 'LOOP', 'IN', 'NEW', 'DIVIDE', 'COLON', 'LTEQ', 'LT', 'SELF', 'BOOLEAN', 'POOL', 'PLUS', 'ARROW', 'OF', 'DOT', 'ELSE', 'INT_COMP', 'LET', 'CASE', 'LPAREN', 'RPAREN', 'LBRACE', 'NOT', 'WHILE', 'MINUS', 'ESAC', 'SEMICOLON', 'INHERITS', 'THEN', 'FI', 'STRING', 'IF', 'MULTIPLY', 'AT', 'ID', 'ASSIGN', 'ISVOID', 'RBRACE'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive', 'COMMENT': 'exclusive', 'STRING': 'exclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_BOOLEAN>(true|false))|(?P<t_INTEGER>\\d+)|(?P<t_TYPE>[A-Z][a-zA-Z_0-9]*)|(?P<t_ID>[a-z_][a-zA-Z_0-9]*)|(?P<t_newline>\\n+)|(?P<t_start_string>\\")|(?P<t_start_comment>\\(\\*)|(?P<t_ignore_SINGLE_LINE_COMMENT>\\-\\-[^\\n]*)|(?P<t_LTEQ>\\<\\=)|(?P<t_ARROW>\\=\\>)|(?P<t_ASSIGN>\\<\\-)|(?P<t_NOT>not)|(?P<t_RBRACE>\\})|(?P<t_LPAREN>\\()|(?P<t_LBRACE>\\{)|(?P<t_PLUS>\\+)|(?P<t_MINUS>\\-)|(?P<t_COMMA>\\,)|(?P<t_EQ>\\=)|(?P<t_LT>\\<)|(?P<t_MULTIPLY>\\*)|(?P<t_AT>\\@)|(?P<t_RPAREN>\\))|(?P<t_COLON>\\:)|(?P<t_DOT>\\.)|(?P<t_SEMICOLON>\\;)|(?P<t_DIVIDE>\\/)|(?P<t_INT_COMP>~)', [None, ('t_BOOLEAN', 'BOOLEAN'), None, ('t_INTEGER', 'INTEGER'), ('t_TYPE', 'TYPE'), ('t_ID', 'ID'), ('t_newline', 'newline'), ('t_start_string', 'start_string'), ('t_start_comment', 'start_comment'), (None, None), (None, 'LTEQ'), (None, 'ARROW'), (None, 'ASSIGN'), (None, 'NOT'), (None, 'RBRACE'), (None, 'LPAREN'), (None, 'LBRACE'), (None, 'PLUS'), (None, 'MINUS'), (None, 'COMMA'), (None, 'EQ'), (None, 'LT'), (None, 'MULTIPLY'), (None, 'AT'), (None, 'RPAREN'), (None, 'COLON'), (None, 'DOT'), (None, 'SEMICOLON'), (None, 'DIVIDE'), (None, 'INT_COMP')])], 'COMMENT': [('(?P<t_COMMENT_startanother>\\(\\*)|(?P<t_COMMENT_end>\\*\\))', [None, ('t_COMMENT_startanother', 'startanother'), ('t_COMMENT_end', 'end')])], 'STRING': [('(?P<t_STRING_newline>\\n)|(?P<t_STRING_end>\\")|(?P<t_STRING_anything>[^\\n])', [None, ('t_STRING_newline', 'newline'), ('t_STRING_end', 'end'), ('t_STRING_anything', 'anything')])]}
_lexstateignore = {'INITIAL': ' \t\r\x0c', 'COMMENT': '', 'STRING': ''}
_lexstateerrorf = {'INITIAL': 't_error', 'COMMENT': 't_COMMENT_error', 'STRING': 't_STRING_error'}
_lexstateeoff = {}
