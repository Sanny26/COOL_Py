#!/usr/bin/env python3
"""Lexer for COOL Programs."""

import ply.lex as lex
from ply.lex import TOKEN
import sys


class PyCoolLexer(object):
    """Lexer."""

    def __init__(self,
                 build_lexer=True,
                 debug=False,
                 lextab="pycoolc.lextab",
                 optimize=True,
                 outputdir="",
                 debuglog=None,
                 errorlog=None):
        """Initializer."""
        self.lexer = None               # ply lexer instance
        self.tokens = ()                # ply tokens collection
        self.reserved = {}              # ply reserved keywords map
        self.last_token = None          # last returned token

        # Save Flags - PRIVATE PROPERTIES
        self._debug = debug
        self._lextab = lextab
        self._optimize = optimize
        self._outputdir = outputdir
        self._debuglog = debuglog
        self._errorlog = errorlog

        # Build lexer if build_lexer flag is set to True
        if build_lexer is True:
            self.build(debug=debug, lextab=lextab, optimize=optimize, outputdir=outputdir, debuglog=debuglog,
                       errorlog=errorlog)

    @property
    def tokens_collection(self):
        """COOL Syntax Tokens."""
        return (
            # Identifiers
            "ID", "TYPE",

            # Primitive Types
            "INTEGER", "STRING", "BOOLEAN",

            # Literals
            "LPAREN", "RPAREN", "LBRACE", "RBRACE", "COLON", "COMMA", "DOT", "SEMICOLON", "AT",

            # Operators
            "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "EQ", "LT", "LTEQ", "ASSIGN", "INT_COMP", "NOT",

            # Special Operators
            "ARROW"
        )

    @property
    def basic_reserved(self):
        """Map of Basic-COOL reserved keywords."""
        return {
            "case": "CASE",
            "class": "CLASS",
            "else": "ELSE",
            "esac": "ESAC",
            "fi": "FI",
            "if": "IF",
            "in": "IN",
            "inherits": "INHERITS",
            "isvoid": "ISVOID",
            "let": "LET",
            "loop": "LOOP",
            "new": "NEW",
            "of": "OF",
            "pool": "POOL",
            "self": "SELF",
            "then": "THEN",
            "while": "WHILE"
        }

    @property
    def extended_reserved(self):
        """Map of Extended-COOL reserved keywords."""
        return {
            "abstract": "ABSTRACT",
            "catch": "CATCH",
            "do": "DO",
            "def": "DEF",
            "final": "FINAL",
            "finally": "FINALLY",
            "for": "FOR",
            "forSome": "FORSOME",
            "explicit": "IMPLICIT",
            "implicit": "IMPORT",
            "lazy": "LAZY",
            "match": "MATCH",
            "native": "NATIVE",
            "null": "NULL",
            "object": "OBJECT",
            "override": "OVERRIDE",
            "package": "PACKAGE",
            "private": "PRIVATE",
            "protected": "PROTECTED",
            "requires": "REQUIRES",
            "return": "RETURN",
            "sealed": "SEALED",
            "super": "SUPER",
            "this": "THIS",
            "throw": "THROW",
            "trait": "TRAIT",
            "try": "TRY",
            "type": "TYPE",
            "val": "VAL",
            "var": "VAR",
            "with": "WITH",
            "yield": "YIELD"
        }

    @property
    def builtin_types(self):
        """Map of the built-in types."""
        return {
            "Bool": "BOOL_TYPE",
            "Int": "INT_TYPE",
            "IO": "IO_TYPE",
            "Main": "MAIN_TYPE",
            "Object": "OBJECT_TYPE",
            "String": "STRING_TYPE",
            "SELF_TYPE": "SELF_TYPE"
        }

    # START OF LEXICAL ANALYSIS RULES DECLARATION

    # Ignore rule for single line comments
    t_ignore_SINGLE_LINE_COMMENT = r"\-\-[^\n]*"

    # SIMPLE TOKENS
    t_LPAREN = r'\('        # (
    t_RPAREN = r'\)'        # )
    t_LBRACE = r'\{'        # {
    t_RBRACE = r'\}'        # }
    t_COLON = r'\:'         # :
    t_COMMA = r'\,'         # ,
    t_DOT = r'\.'           # .
    t_SEMICOLON = r'\;'     # ;
    t_AT = r'\@'            # @
    t_MULTIPLY = r'\*'      # *
    t_DIVIDE = r'\/'        # /
    t_PLUS = r'\+'          # +
    t_MINUS = r'\-'         # -
    t_INT_COMP = r'~'       # ~
    t_LT = r'\<'            # <
    t_EQ = r'\='            # =
    t_LTEQ = r'\<\='        # <=
    t_ASSIGN = r'\<\-'      # <-
    t_NOT = r'not'          # not
    t_ARROW = r'\=\>'       # =>

    @TOKEN(r"(true|false)")
    def t_BOOLEAN(self, token):
        """Bool Primitive Type Token Rule."""
        token.value = True if token.value == "true" else False
        return token

    @TOKEN(r"\d+")
    def t_INTEGER(self, token):
        """Integer Primitive Type Token Rule."""
        token.value = int(token.value)
        return token

    @TOKEN(r"[A-Z][a-zA-Z_0-9]*")
    def t_TYPE(self, token):
        """Type Token Rule."""
        token.type = self.basic_reserved.get(token.value, 'TYPE')
        return token

    @TOKEN(r"[a-z_][a-zA-Z_0-9]*")
    def t_ID(self, token):
        """Token Rule for Identifiers."""
        token.type = self.basic_reserved.get(token.value, 'ID')
        return token

    @TOKEN(r"\n+")
    def t_newline(self, token):
        """Newline Token Rule."""
        token.lexer.lineno += len(token.value)

    # Ignore Whitespace Character Rule
    t_ignore = ' \t\r\f'

    # LEXER STATES
    @property
    def states(self):
        """."""
        return (
            ("STRING", "exclusive"),
            ("COMMENT", "exclusive")
        )

    # THE STRING STATE
    @TOKEN(r"\"")
    def t_start_string(self, token):
        """."""
        token.lexer.push_state("STRING")
        token.lexer.string_backslashed = False
        token.lexer.stringbuf = ""

    @TOKEN(r"\n")
    def t_STRING_newline(self, token):
        """."""
        token.lexer.lineno += 1
        if not token.lexer.string_backslashed:
            print("String newline not escaped")
            token.lexer.skip(1)
        else:
            token.lexer.string_backslashed = False

    @TOKEN(r"\"")
    def t_STRING_end(self, token):
        """."""
        if not token.lexer.string_backslashed:
            token.lexer.pop_state()
            token.value = token.lexer.stringbuf
            token.type = "STRING"
            return token
        else:
            token.lexer.stringbuf += '"'
            token.lexer.string_backslashed = False

    @TOKEN(r"[^\n]")
    def t_STRING_anything(self, token):
        """."""
        if token.lexer.string_backslashed:
            if token.value == 'b':
                token.lexer.stringbuf += '\b'
            elif token.value == 't':
                token.lexer.stringbuf += '\t'
            elif token.value == 'n':
                token.lexer.stringbuf += '\n'
            elif token.value == 'f':
                token.lexer.stringbuf += '\f'
            elif token.value == '\\':
                token.lexer.stringbuf += '\\'
            else:
                token.lexer.stringbuf += token.value
            token.lexer.string_backslashed = False
        else:
            if token.value != '\\':
                token.lexer.stringbuf += token.value
            else:
                token.lexer.string_backslashed = True

    # STRING ignored characters
    t_STRING_ignore = ''

    # STRING error handler
    def t_STRING_error(self, token):
        """."""
        print("Illegal character! Line: {0}, character: {1}".format(token.lineno, token.value[0]))
        token.lexer.skip(1)

    # THE COMMENT STATE
    @TOKEN(r"\(\*")
    def t_start_comment(self, token):
        """."""
        token.lexer.push_state("COMMENT")
        token.lexer.comment_count = 0

    @TOKEN(r"\(\*")
    def t_COMMENT_startanother(self, t):
        """."""
        t.lexer.comment_count += 1

    @TOKEN(r"\*\)")
    def t_COMMENT_end(self, token):
        """."""
        if token.lexer.comment_count == 0:
            token.lexer.pop_state()
        else:
            token.lexer.comment_count -= 1

    # COMMENT ignored characters
    t_COMMENT_ignore = ''

    # COMMENT error handler
    def t_COMMENT_error(self, token):
        """."""
        token.lexer.skip(1)

    def t_error(self, token):
        """Error Handling and Reporting Rule."""
        print("Illegal character! Line: {0}, character: {1}".format(token.lineno, token.value[0]))
        token.lexer.skip(1)

    def build(self, **kwargs):
        """Build the PyCoolLexer instance with lex.lex() by binding the tokens list, reserved keywords map and lexer object."""
        if kwargs is None or len(kwargs) == 0:
            debug, lextab, optimize, outputdir, debuglog, errorlog = \
                self._debug, self._lextab, self._optimize, self._outputdir, self._debuglog, self._errorlog
        else:
            debug = kwargs.get("debug", self._debug)
            lextab = kwargs.get("lextab", self._lextab)
            optimize = kwargs.get("optimize", self._optimize)
            outputdir = kwargs.get("outputdir", self._outputdir)
            debuglog = kwargs.get("debuglog", self._debuglog)
            errorlog = kwargs.get("errorlog", self._errorlog)

        # Expose the reserved map and tokens tuple to the class scope for ply.lex
        self.reserved = self.basic_reserved.keys()
        self.tokens = self.tokens_collection + tuple(self.basic_reserved.values())

        # Build internal ply.lex instance
        self.lexer = lex.lex(module=self, lextab=lextab, debug=debug, optimize=optimize, outputdir=outputdir,
                             debuglog=debuglog, errorlog=errorlog)

    def input(self, cool_program_source_code):
        """
        Run lexical analysis on a given COOL program source code string.

        :param cool_program_source_code: COOL program source code as a string.
        :return: None.
        """
        if self.lexer is None:
            raise Exception("Lexer was not built. Try calling the build() method first, and then tokenize().")

        self.lexer.input(cool_program_source_code)

    def token(self):
        """
        Advanced the lexers tokens tape one place and returns the current token.

        :side-effects: Modifies self.last_token.
        :return: Token.
        """
        if self.lexer is None:
            raise Exception("Lexer was not built. Try building the lexer with the build() method.")

        self.last_token = self.lexer.token()
        return self.last_token

    def clone_ply_lexer(self):
        """
        Clones the internal PLY's lex-generated lexer instance. Returns a new copy.

        :return: PLY's lex-generated lexer clone.
        """
        a_clone = self.lexer.clone()
        return a_clone

    @staticmethod
    def test(program_source_code):
        """
        Given a cool program source code string try to run lexical analysis on it and return all tokens as an iterator.

        :param program_source_code: String.
        :return: Iterator.
        """
        temp_lexer = PyCoolLexer()
        temp_lexer.input(program_source_code)
        iter_token_stream = iter([some_token for some_token in temp_lexer])
        del temp_lexer
        return iter_token_stream

    def __iter__(self):
        """."""
        return self

    def __next__(self):
        """."""
        t = self.token()
        if t is None:
            raise StopIteration
        return t

    def next(self):
        """."""
        return self.__next__()


def make_lexer(**kwargs):
    """Create a new lexer."""
    a_lexer = PyCoolLexer(**kwargs)
    a_lexer.build()
    return a_lexer


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./lexer.py program.cl")
        exit()
    elif not str(sys.argv[1]).endswith(".cl"):
        print("Cool program source code files must end with .cl extension.")
        print("Usage: ./lexer.py program.cl")
        exit()

    input_file = sys.argv[1]
    with open(input_file, encoding="utf-8") as file:
        cool_program_code = file.read()

    lexer = make_lexer()
    lexer.input(cool_program_code)
    for token in lexer:
        print(token)
