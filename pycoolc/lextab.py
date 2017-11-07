# lextab.py. This file automatically created by PLY (version 3.10). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('ELSE', 'SELF', 'STRING', 'WHILE', 'EQ', 'PLUS', 'LTEQ', 'DIVIDE', 'LPAREN', 'LT', 'BOOLEAN', 'ID', 'NEW', 'CLASS', 'INTEGER', 'DOT', 'IF', 'MULTIPLY', 'LBRACE', 'IN', 'INT_COMP', 'NOT', 'POOL', 'LET', 'FI', 'ISVOID', 'RBRACE', 'LOOP', 'THEN', 'CASE', 'INHERITS', 'ESAC', 'OF', 'COLON', 'ARROW', 'RPAREN', 'COMMA', 'SEMICOLON', 'MINUS', 'TYPE', 'ASSIGN', 'AT'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'STRING': 'exclusive', 'COMMENT': 'exclusive', 'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_BOOLEAN>(true|false))|(?P<t_INTEGER>\\d+)|(?P<t_TYPE>[A-Z][a-zA-Z_0-9]*)|(?P<t_ID>[a-z_][a-zA-Z_0-9]*)|(?P<t_newline>\\n+)|(?P<t_start_string>\\")|(?P<t_start_comment>\\(\\*)|(?P<t_ignore_SINGLE_LINE_COMMENT>\\-\\-[^\\n]*)|(?P<t_ASSIGN>\\<\\-)|(?P<t_ARROW>\\=\\>)|(?P<t_LTEQ>\\<\\=)|(?P<t_NOT>not)|(?P<t_LBRACE>\\{)|(?P<t_PLUS>\\+)|(?P<t_MINUS>\\-)|(?P<t_COMMA>\\,)|(?P<t_MULTIPLY>\\*)|(?P<t_COLON>\\:)|(?P<t_DIVIDE>\\/)|(?P<t_LPAREN>\\()|(?P<t_LT>\\<)|(?P<t_EQ>\\=)|(?P<t_DOT>\\.)|(?P<t_AT>\\@)|(?P<t_RPAREN>\\))|(?P<t_SEMICOLON>\\;)|(?P<t_RBRACE>\\})|(?P<t_INT_COMP>~)', [None, ('t_BOOLEAN', 'BOOLEAN'), None, ('t_INTEGER', 'INTEGER'), ('t_TYPE', 'TYPE'), ('t_ID', 'ID'), ('t_newline', 'newline'), ('t_start_string', 'start_string'), ('t_start_comment', 'start_comment'), (None, None), (None, 'ASSIGN'), (None, 'ARROW'), (None, 'LTEQ'), (None, 'NOT'), (None, 'LBRACE'), (None, 'PLUS'), (None, 'MINUS'), (None, 'COMMA'), (None, 'MULTIPLY'), (None, 'COLON'), (None, 'DIVIDE'), (None, 'LPAREN'), (None, 'LT'), (None, 'EQ'), (None, 'DOT'), (None, 'AT'), (None, 'RPAREN'), (None, 'SEMICOLON'), (None, 'RBRACE'), (None, 'INT_COMP')])], 'COMMENT': [('(?P<t_COMMENT_startanother>\\(\\*)|(?P<t_COMMENT_end>\\*\\))', [None, ('t_COMMENT_startanother', 'startanother'), ('t_COMMENT_end', 'end')])], 'STRING': [('(?P<t_STRING_newline>\\n)|(?P<t_STRING_end>\\")|(?P<t_STRING_anything>[^\\n])', [None, ('t_STRING_newline', 'newline'), ('t_STRING_end', 'end'), ('t_STRING_anything', 'anything')])]}
_lexstateignore = {'STRING': '', 'COMMENT': '', 'INITIAL': ' \t\r\x0c'}
_lexstateerrorf = {'STRING': 't_STRING_error', 'COMMENT': 't_COMMENT_error', 'INITIAL': 't_error'}
_lexstateeoff = {}
