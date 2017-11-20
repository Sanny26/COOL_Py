#!/usr/bin/env python3
"""Translator for COOL to python."""
import ast as AST
from parser import make_parser
import sys

import pdb


def flatten(content):
    """Flatten a list of strings to a single string."""
    type_ = type(content)
    if type_ is str:
        return content
    elif type_ in [list, tuple]:
        return ''.join(content)


class Translator:
    """Translator class for COOL to Python."""

    py_reserved = {'Bool': 'bool',
                   'Int': 'int',
                   'String': 'str',
                   'SELF_TYPE': 'self'}
    loop_counter = 0
    conditional_counter = 0
    block_counter = 0

    def __int__(self):
        """Constructor."""
        pass

    def indent(self, line, space):
        """Add indentation to a line for specified number of spaces."""
        return "{}{}".format(' '*space, line)

    def py_class_attr(self, word):
        """Convert class attributes to python self declarations."""
        if word in self.class_attributes:
            word = "self.{}".format(word)

        return word

    def frmt(self, line, space=0):
        """Format a given line into final printable python string."""
        return self.indent(self.py_class_attr(flatten(line)), space)

    def translate(self, obj):
        """Translate a new COOL Program to Python."""
        assert type(obj) is AST.Program

        self.functions = {'ClassMethod': self.extract_classmethod,
                          'ClassAttribute': self.extract_classattribute,
                          'Integer': self.extract_integer,
                          'String': self.extract_string,
                          'Boolean': self.extract_boolean,
                          'Block': self.extract_block,
                          'WhileLoop': self.extract_whileloop,
                          'Object': self.extract_object,
                          'If': self.extract_if,
                          'DynamicDispatch': self.extract_dynamic_dispatch,
                          'StaticDispatch': self.extract_static_dispatch,
                          'Assignment': self.extract_assignment,
                          'Self': self.extract_self,
                          'IntegerComplement': self.extract_integer_complement,
                          'BooleanComplement': self.extract_boolean_complement,
                          'Addition': self.extract_addition,
                          'Subtraction': self.extract_subtraction,
                          'Multiplication': self.extract_multiplication,
                          'Division': self.extract_division,
                          'Equal': self.extract_equal,
                          'LessThan': self.extract_less_than,
                          'LessThanOrEqual': self.extract_less_than_or_equal,
                          'IsVoid': self.extract_is_void,
                          'Let': self.extract_let,
                          'Case': self.extract_case,
                          'Action': self.extract_action,
                          'NewObject': self.extract_new_object,
                          }
        self.prgm = "'''Auto Generated Python file using COOL_Py translator.'''\n\n"
        self.prgm += "from base import IO, Object, String, Integer, Boolean\n\n"

        for each in obj.classes:
            self.class_attributes = []
            self.call_in_main = []
            self.extract_class(each)

        self.prgm += "\n\nif __name__ == '__main__':\n    m = Main()\n    m.main()\n"
        print(self.prgm)

    def extract_class(self, Class):
        """Extract and convert a COOL class to Python class."""
        self.prgm += "class {}".format(Class.name)
        if Class.parent:
                self.prgm += "({})".format(Class.parent)
        self.prgm += ":\n\n"
        space = 4
        for each in self.extract_features(Class.features):
            self.prgm += self.frmt(each, space)

    def extract_features(self, features):
        """Extract and convert the features of the given COOL class."""
        content = []
        space = 4
        main_function = -1
        for i, each in enumerate(features):
            funct_name = each.clsname
            if each.name == "main":
                main_function = i
                continue
            if funct_name is "Assignment":
                content.extend(self.functions[funct_name](each, callfromClass=True))
            elif funct_name in self.functions:
                content.extend(self.functions[funct_name](each))
            else:
                raise SyntaxError("{} not found, Internal parsing Error".format(funct_name))

        each = features[main_function]
        funct_name = each.clsname
        if funct_name in self.functions:
            main_code = self.functions[funct_name](each)
            # pdb.set_trace()
            for line in main_code:
                if 'return' in line:
                    content.extend([self.frmt("self.{}()\n".format(x), space*2) for x in self.call_in_main])
                content.append(line)
        else:
            raise SyntaxError("{} not found, Internal parsing Error".format(funct_name))

        return content

    def extract_classmethod(self, class_method):
        """Extract and convert a COOL class method."""
        content = ["\n"]
        line = ""
        space = 4

        # class definition
        line += "def {}(self, ".format(class_method.name)
        if class_method.formal_params:
            line += self.extract_parameters(class_method.formal_params)
        line += ")"
        line += ":\n"
        content.append(line)

        # class body
        for each in self.extract_method_body(class_method.body):
            content.append(self.frmt(each, space))
        content.append("\n")

        return content

    def extract_method_body(self, body):
        """Extract the body of a given class method."""
        content = []
        space = 4
        # If the body of the method is a single variable
        if body.clsname in ['Integer', 'Boolean', 'String']:
            content = [self.frmt("return {}".format(flatten(self.functions[body.clsname](body))), space)]
        # If the body of the method is a complex block/object
        elif body.clsname in ["Block", "WhileLoop", "If"]:
            return_var, body_content = self.functions[body.clsname](body)
            content.extend([self.frmt(line, space) for line in body_content])
            content.append(self.frmt("return {}".format(return_var), space))

        return content

    def extract_parameters(self, formal_params):
        """Convert method parameters."""
        content = ""
        for each in formal_params:
            content += "{}, ".format(each.name)
        return content

    def extract_classattribute(self, class_attr):
        """Extract class attributes."""
        content = []
        space = 4
        self.class_attributes.append(class_attr.name)
        if class_attr.init_expr is not None:
            funct_name = class_attr.init_expr.clsname
            if funct_name not in ['Block', 'WhileLoop', "If"]:
                subcontent = self.functions[funct_name](class_attr.init_expr)
                if subcontent.strip() in self.call_in_main:
                    content.append("{} = {}()\n".format(class_attr.name, subcontent))
                else:
                    content.append("{} = {}\n".format(class_attr.name, subcontent))
            else:
                self.call_in_main.append(class_attr.name)
                return_var, expr_code = self.functions[funct_name](class_attr.init_expr)
                content.append("def {}(self):\n".format(class_attr.name))
                content.extend([self.frmt(x, space) for x in expr_code])
                content.append("\n")
                if return_var:
                    content.append(self.frmt("return {}\n".format(return_var), space))

        return content

    def extract_integer(self, obj):
        """Extract Integer."""
        return "Integer({})".format(str(obj.content))

    def extract_string(self, obj):
        """Extract String."""
        return "String({})".format(repr(obj.content))

    def extract_boolean(self, obj):
        """Extract Boolean."""
        return "Boolean({})".format(str(obj.content))

    def extract_object(self, obj):
        """Extract Object when creating a new object."""
        return obj.name

    def extract_self(self, obj):
        """Extract Self object."""
        return "self"

    def extract_block(self, obj):
        """Extract Statement Block."""
        block_var = "block_var_{}".format(str(self.block_counter))
        self.block_counter += 1
        content = ["{} = None\n".format(block_var)]

        for i in range(len(obj.expr_list))[0:-1]:
            funct_name = obj.expr_list[i].clsname
            if funct_name in ["Block", "If"]:
                return_var, expr_code = self.functions[funct_name](obj.expr_list[i])
                content.extend(expr_code)
            else:
                expr_code = self.functions[funct_name](obj.expr_list[i])
                content.extend(expr_code)
                if funct_name in ["Boolean", "String", "Integer", "Self", "DynamicDispatch", "StaticDispatch", "Self"]:
                    content.append("\n")

        # The last expression needs to be returned
        i = -1
        funct_name = obj.expr_list[i].clsname
        if funct_name in ["Block", "If", "WhileLoop"]:
            return_var, expr_code = self.functions[funct_name](obj.expr_list[i])
            content.extend(expr_code)
            return_string = "{} = {}\n".format(block_var, return_var)
        elif funct_name in ["Boolean", "String", "Integer", "Self", "DynamicDispatch", "StaticDispatch", "Self"]:
            expr_code = self.functions[funct_name](obj.expr_list[i])
            return_string = "{} = {}\n".format(block_var, expr_code)
            content.append(return_string)
        else:
            raise TypeError("Type {} is not valid in a block Statement".format(funct_name))

        return block_var, content

    def extract_whileloop(self, obj):
        """Extract While loop."""
        space = 4
        conditional_var = "conditional_var_{}".format(str(self.conditional_counter))
        self.conditional_counter += 1
        pred_var = None
        return_var = None
        content = ["{} = None\n".format(conditional_var)]

        predicate = obj.predicate
        body = obj.body

        # Predicate evaluated once before loop execution
        if predicate.clsname in ["WhileLoop", "If", "Block"]:
            pred_var, pred_code = self.functions[predicate.clsname](predicate)
            content.extend([self.frmt(line) for line in pred_code])
            content.append("{} = {}\n".format(conditional_var, pred_var))
            content.append("while({}):\n".format(conditional_var))
        else:
            pred_code = self.functions[predicate.clsname](predicate)
            content.append("while({}):\n".format(self.frmt(pred_code)))

        # Body of the loop added to the loop
        if body.clsname in ["WhileLoop", "If", "Block"]:
            return_var, body_code = self.functions[body.clsname](body)
            # pdb.set_trace()
            content.extend([self.frmt(part, space) for part in body_code])
        else:
            body_code = self.functions[body.clsname](body)
            content.extend([self.frmt(part, space) for part in body_code])

        if pred_var:
            content.extend([self.frmt(line, space) for line in pred_code])
            content.append(self.frmt("{} = {}\n".format(conditional_var, pred_var), space))

        return return_var, content

    def extract_if(self, obj):
        """Extract If..Else block."""
        space = 4

        predicate = obj.predicate
        then_body = obj.then_body
        else_body = obj.else_body

        eval_var = "if_var_{}".format(str(self.conditional_counter))
        self.conditional_counter += 1

        content = ["{} = None\n".format(eval_var)]

        if predicate.clsname in ["If", "Block", "WhileLoop"]:
            return_var, expr_code = self.functions[predicate.clsname](predicate)
            content.extend(expr_code)
            conditional_expr = "if({}):\n".format(return_var)
            content.append(conditional_expr)
        else:
            expr_code = self.functions[predicate.clsname](predicate)
            conditional_expr = "if({}):\n".format(self.frmt(expr_code))
            content.append(conditional_expr)

        if then_body.clsname in ["If", "Block", "WhileLoop"]:
            return_var, expr_code = self.functions[then_body.clsname](then_body)
            content.extend([self.frmt(line, space) for line in expr_code])
            then_exp = "{} = {}\n".format(eval_var, return_var)
            content.append(self.frmt(then_exp, space))
        elif then_body.clsname in ["Boolean", "String", "Integer", "Self", "DynamicDispatch", "StaticDispatch"]:
            expr_code = self.functions[then_body.clsname](then_body)
            then_exp = "{} = {}\n".format(eval_var, self.frmt(expr_code))
            content.append(self.frmt(then_exp, space))
        else:
            expr_code = self.functions[then_body.clsname](then_body)
            content.append([self.frmt(line, space) for line in expr_code])

        content.append("else:\n")
        if else_body.clsname in ["If", "Block", "WhileLoop"]:
            return_var, expr_code = self.functions[else_body.clsname](else_body)
            content.extend([self.frmt(line, space) for line in expr_code])
            then_exp = "{} = {}\n".format(eval_var, return_var)
            content.append(self.frmt(then_exp, space))
        elif else_body.clsname in ["Boolean", "String", "Integer", "Self", "DynamicDispatch", "StaticDispatch"]:
            expr_code = self.functions[else_body.clsname](else_body)
            then_exp = "{} = {}\n".format(eval_var, self.frmt(expr_code))
            content.append(self.frmt(then_exp, space))
        else:
            expr_code = self.functions[else_body.clsname](else_body)
            content.append([self.frmt(line, space) for line in expr_code])

        return eval_var, content

    def extract_assignment(self, obj, callfromClass=False):
        """Extract Assignment."""
        space = 4
        instance = self.frmt(flatten(self.functions[obj.instance.clsname](obj.instance)))
        expression = obj.expr
        content = []
        # pdb.set_trace()
        if expression.clsname in ["WhileLoop", "Block", "If"]:
            return_var, expr_code = self.functions[expression.clsname](expression)
            if callfromClass:
                self.call_in_main.append(instance)
                content.append("def {}(self):\n".format(instance))
                content.extend([self.frmt(x, space) for x in expr_code])
                if return_var:
                    content.append(self.frmt("return {}\n".format(return_var), space))
            else:
                content.extend([self.frmt(x, space) for x in expr_code])
                if return_var:
                    content.append(self.frmt("{} = {}\n".format(instance, return_var), space))
        else:
            expr_code = self.frmt(self.functions[expression.clsname](expression))
            if expr_code.strip() in self.call_in_main:
                content.append("{} = self.{}()\n".format(instance, expr_code))
            else:
                content.append("{} = {}\n".format(instance, expr_code))
        return content

    def extract_dynamic_dispatch(self, obj):
        """Extract DynamicDispatch."""
        args = ""
        for arg in obj.arguments:
            args += "{}, ".format(self.frmt(self.functions[arg.clsname](arg)))
        instance = self.functions[obj.instance.clsname](obj.instance)
        return ["{}.{}({})".format(instance, obj.method, args)]

    def extract_static_dispatch(self, obj):
        """Extract StaticDispatch."""
        instance = self.functions[obj.instance.clsname](obj.instance)
        return instance

    def extract_integer_complement(self, obj):
        """Extract Integer Complement."""
        return "~({})".format(self.frmt(self.functions[obj.integer_expr.clsname](obj.integer_expr)))

    def extract_boolean_complement(self, obj):
        """Extract Boolean Complement."""
        return "not {}".format(self.frmt(self.functions[obj.boolean_expr.clsname](obj.boolean_expr)))

    def extract_addition(self, obj):
        """Extract Addition."""
        return "({}) + ({})".format(self.frmt(self.functions[obj.first.clsname](obj.first)),
                                    self.frmt(self.functions[obj.second.clsname](obj.second)))

    def extract_subtraction(self, obj):
        """Extract Subtraction."""
        return "({}) - ({})".format(self.frmt(self.functions[obj.first.clsname](obj.first)),
                                    self.frmt(self.functions[obj.second.clsname](obj.second)))

    def extract_multiplication(self, obj):
        """Extract Multiplication."""
        return "({}) * ({})".format(self.frmt(self.functions[obj.first.clsname](obj.first)),
                                    self.frmt(self.functions[obj.second.clsname](obj.second)))

    def extract_division(self, obj):
        """Extract Division."""
        return "({}) / ({})".format(self.frmt(self.functions[obj.first.clsname](obj.first)),
                                    self.frmt(self.functions[obj.second.clsname](obj.second)))

    def extract_equal(self, obj):
        """Extract Eqaul to."""
        return "({}) == ({})".format(self.frmt(self.functions[obj.first.clsname](obj.first)),
                                     self.frmt(self.functions[obj.second.clsname](obj.second)))

    def extract_less_than_or_equal(self, obj):
        """Extract Less Than/Equal to."""
        return "({}) <= ({})".format(self.frmt(self.functions[obj.first.clsname](obj.first)),
                                     self.frmt(self.functions[obj.second.clsname](obj.second)))

    def extract_less_than(self, obj):
        """Extract Less Than."""
        return "({}) < ({})".format(self.frmt(self.functions[obj.first.clsname](obj.first)),
                                    self.frmt(self.functions[obj.second.clsname](obj.second)))

    def extract_is_void(self, obj):
        """Extract isVoid."""
        return "({}) is None".format(self.frmt(self.functions[obj.expr.clsname](obj.expr)))

    def extract_let(self, obj):
        """Extract Let."""
        content = []
        return content

    def extract_case(self, obj):
        """Extract Case."""
        content = []
        return content

    def extract_action(self, obj):
        """Extract Action."""
        content = []
        return content

    def extract_new_object(self, obj):
        """Create a new object for a class."""
        return "{}()".format(obj.type)


if __name__ == '__main__':
    parser = make_parser()

    if len(sys.argv) > 1:
        if not str(sys.argv[1]).endswith(".cl"):
            print("Cool program source code files must end with .cl extension.")
            print("Usage: ./translator.py program.cl")
            exit()

        input_file = sys.argv[1]
        with open(input_file, encoding="utf-8") as file:
            cool_program_code = file.read()

        parse_result = parser.parse(cool_program_code)

        T = Translator()
        T.translate(parse_result)
    else:
        print("Please provide input file\n\n./translator.py INPUT_FILE_PATH\n\n")
