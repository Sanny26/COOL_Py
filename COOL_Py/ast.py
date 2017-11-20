"""An Abstract Syntax Tree for Parsing COOL tokens and converting to Python Tokens."""


class AST:
    """Class for AST."""

    def __init__(self):
        """Constructor."""
        pass

    @property
    def clsname(self):
        """Give the name of the class."""
        return str(self.__class__.__name__)

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname)
        ])

    def to_readable(self):
        """Readable string when class is printed, overloaded in individual classes."""
        return "{}".format(self.clsname)

    def __repr__(self):
        """Printable object."""
        return self.__str__()

    def __str__(self):
        """Create a string for the class when print is called."""
        return str(self.to_readable())


class Program(AST):
    """Class for COOL Program."""

    def __init__(self, classes):
        """Constructor."""
        super(Program, self).__init__()
        self.classes = classes

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("classes", self.classes)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(classes={})".format(self.clsname, self.classes)


class Class(AST):
    """Class for COOL Class."""

    def __init__(self, name, parent, features):
        """Constructor."""
        super(Class, self).__init__()
        self.name = name
        self.parent = parent
        self.features = features

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("name", self.name),
            ("parent", self.parent),
            ("features", self.features)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(name='{}', parent={}, features={})".format(self.clsname, self.name, self.parent, self.features)


class ClassFeature(AST):
    """Class for COOL ClassFeature."""

    def __init__(self):
        """Constructor."""
        super(ClassFeature, self).__init__()


class ClassMethod(ClassFeature):
    """Class for COOL ClassMethod."""

    def __init__(self, name, formal_params, return_type, body):
        """Constructor."""
        super(ClassMethod, self).__init__()
        self.name = name
        self.formal_params = formal_params
        self.return_type = return_type
        self.body = body

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("name", self.name),
            ("formal_params", self.formal_params),
            ("return_type", self.return_type),
            ("body", self.body)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(name='{}', formal_params={}, return_type={}, body={})".format(
            self.clsname, self.name, self.formal_params, self.return_type, self.body)


class ClassAttribute(ClassFeature):
    """Class for COOL ClassAttribute."""

    def __init__(self, name, attr_type, init_expr):
        """Constructor."""
        super(ClassAttribute, self).__init__()
        self.name = name
        self.attr_type = attr_type
        self.init_expr = init_expr

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("name", self.name),
            ("attr_type", self.attr_type),
            ("init_expr", self.init_expr)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(name='{}', attr_type={}, init_expr={})".format(
            self.clsname, self.name, self.attr_type, self.init_expr)


class FormalParameter(ClassFeature):
    """Class for COOL FormalParameter."""

    def __init__(self, name, param_type):
        """Constructor."""
        super(FormalParameter, self).__init__()
        self.name = name
        self.param_type = param_type

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("name", self.name),
            ("param_type", self.param_type)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(name='{}', param_type={})".format(self.clsname, self.name, self.param_type)


class Object(AST):
    """Class for COOL Object base Class."""

    def __init__(self, name):
        """Constructor."""
        super(Object, self).__init__()
        self.name = name

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("name", self.name)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(name='{}')".format(self.clsname, self.name)


class Self(Object):
    """Class for COOL Self object."""

    def __init__(self):
        """Constructor."""
        super(Self, self).__init__("SELF")

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}".format(self.clsname)


class Constant(AST):
    """Class for COOL Constants like Int, Str, Bool."""

    def __init__(self):
        """Constructor."""
        super(Constant, self).__init__()


class Integer(Constant):
    """Class for COOL Integer."""

    def __init__(self, content):
        """Constructor."""
        super(Integer, self).__init__()
        self.content = content

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("content", self.content)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(content={})".format(self.clsname, self.content)


class String(Constant):
    """Class for COOL String."""

    def __init__(self, content):
        """Constructor."""
        super(String, self).__init__()
        self.content = content

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("content", self.content)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(content={})".format(self.clsname, repr(self.content))


class Boolean(Constant):
    """Class for COOL Boolean."""

    def __init__(self, content):
        """Constructor."""
        super(Boolean, self).__init__()
        self.content = content

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("content", self.content)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(content={})".format(self.clsname, self.content)


class Expr(AST):
    """Class for COOL Expression."""

    def __init__(self):
        """Constructor."""
        super(Expr, self).__init__()


class NewObject(Expr):
    """Class for COOL Object declarations."""

    def __init__(self, new_type):
        """Constructor."""
        super(NewObject, self).__init__()
        self.type = new_type

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("type", self.type)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(type={})".format(self.clsname, self.type)


class IsVoid(Expr):
    """Class for COOL isVoid Function."""

    def __init__(self, expr):
        """Constructor."""
        super(IsVoid, self).__init__()
        self.expr = expr

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("expr", self.expr)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(expr={})".format(self.clsname, self.expr)


class Assignment(Expr):
    """Class for COOL Assignment operation."""

    def __init__(self, instance, expr):
        """Constructor."""
        super(Assignment, self).__init__()
        self.instance = instance
        self.expr = expr

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("instance", self.instance),
            ("expr", self.expr)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(instance={}, expr={})".format(self.clsname, self.instance, self.expr)


class Block(Expr):
    """Class for COOL Expression Blocks."""

    def __init__(self, expr_list):
        """Constructor."""
        super(Block, self).__init__()
        self.expr_list = expr_list

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("expr_list", self.expr_list)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(expr_list={})".format(self.clsname, self.expr_list)


class DynamicDispatch(Expr):
    """Class for COOL Dynamic Dispatch."""

    def __init__(self, instance, method, arguments):
        """Constructor."""
        super(DynamicDispatch, self).__init__()
        self.instance = instance
        self.method = method
        self.arguments = arguments if arguments is not None else tuple()

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("instance", self.instance),
            ("method", self.method),
            ("arguments", self.arguments)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(instance={}, method={}, arguments={})".format(
            self.clsname, self.instance, self.method, self.arguments)


class StaticDispatch(Expr):
    """Class for COOL StaticDispatch."""

    def __init__(self, instance, dispatch_type, method, arguments):
        """Constructor."""
        super(StaticDispatch, self).__init__()
        self.instance = instance
        self.dispatch_type = dispatch_type
        self.method = method
        self.arguments = arguments if arguments is not None else tuple()

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("instance", self.instance),
            ("dispatch_type", self.dispatch_type),
            ("method", self.method),
            ("arguments", self.arguments)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(instance={}, dispatch_type={}, method={}, arguments={})".format(
            self.clsname, self.instance, self.dispatch_type, self.method, self.arguments)


class Let(Expr):
    """Class for COOL Let Operation."""

    def __init__(self, instance, return_type, init_expr, body):
        """Constructor."""
        super(Let, self).__init__()
        self.instance = instance
        self.return_type = return_type
        self.init_expr = init_expr
        self.body = body

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("instance", self.instance),
            ("return_type", self.return_type),
            ("init_expr", self.init_expr),
            ("body", self.body)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(instance={}, return_type={}, init_expr={}, body={})".format(
            self.clsname, self.instance, self.return_type, self.init_expr, self.body)


class If(Expr):
    """Class for COOL If...Then...Else block."""

    def __init__(self, predicate, then_body, else_body):
        """Constructor."""
        super(If, self).__init__()
        self.predicate = predicate
        self.then_body = then_body
        self.else_body = else_body

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("predicate", self.predicate),
            ("then_body", self.then_body),
            ("else_body", self.else_body)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(predicate={}, then_body={}, else_body={})".format(
            self.clsname, self.predicate, self.then_body, self.else_body)


class WhileLoop(Expr):
    """Class for COOL Loop expressions."""

    def __init__(self, predicate, body):
        """Constructor."""
        super(WhileLoop, self).__init__()
        self.predicate = predicate
        self.body = body

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("predicate", self.predicate),
            ("body", self.body)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(predicate={}, body={})".format(self.clsname, self.predicate, self.body)


class Case(Expr):
    """Class for COOL Switch Case expressions."""

    def __init__(self, expr, actions):
        """Constructor."""
        super(Case, self).__init__()
        self.expr = expr
        self.actions = actions

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("expr", self.expr),
            ("actions", self.actions)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(expr={}, actions={})".format(self.clsname, self.expr, self.actions)


class Action(AST):
    """Class for COOL Action Expressions."""

    def __init__(self, name, action_type, body):
        """Constructor."""
        super(Action, self).__init__()
        self.name = name
        self.action_type = action_type
        self.body = body

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("name", self.name),
            ("action_type", self.action_type),
            ("body", self.body)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(name='{}', action_type={}, body={})".format(self.clsname, self.name, self.action_type, self.body)


class UnaryOperation(Expr):
    """Class for COOL Unary Operations."""

    def __init__(self):
        """Constructor."""
        super(UnaryOperation, self).__init__()


class IntegerComplement(UnaryOperation):
    """Class for COOL IntegerComplement."""

    def __init__(self, integer_expr):
        """Constructor."""
        super(IntegerComplement, self).__init__()
        self.symbol = "~"
        self.integer_expr = integer_expr

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("integer_expr", self.integer_expr)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(expr={})".format(self.clsname, self.integer_expr)


class BooleanComplement(UnaryOperation):
    """Class for COOL BooleanComplement."""

    def __init__(self, boolean_expr):
        """Constructor."""
        super(BooleanComplement, self).__init__()
        self.symbol = "!"
        self.boolean_expr = boolean_expr

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("boolean_expr", self.boolean_expr)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(expr={})".format(self.clsname, self.boolean_expr)


class BinaryOperation(Expr):
    """Class for COOL BinaryOperation."""

    def __init__(self):
        """Constructor."""
        super(BinaryOperation, self).__init__()


class Addition(BinaryOperation):
    """Class for COOL Addition Operation."""

    def __init__(self, first, second):
        """Constructor."""
        super(Addition, self).__init__()
        self.symbol = "+"
        self.first = first
        self.second = second

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("first", self.first),
            ("second", self.second)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(first={}, second={})".format(self.clsname, self.first, self.second)


class Subtraction(BinaryOperation):
    """Class for COOL Subtraction operation."""

    def __init__(self, first, second):
        """Constructor."""
        super(Subtraction, self).__init__()
        self.symbol = "-"
        self.first = first
        self.second = second

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("first", self.first),
            ("second", self.second)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(first={}, second={})".format(self.clsname, self.first, self.second)


class Multiplication(BinaryOperation):
    """Class for COOL Multiplication Operation."""

    def __init__(self, first, second):
        """Constructor."""
        super(Multiplication, self).__init__()
        self.symbol = "*"
        self.first = first
        self.second = second

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("first", self.first),
            ("second", self.second)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(first={}, second={})".format(self.clsname, self.first, self.second)


class Division(BinaryOperation):
    """Class for COOL Division Operation."""

    def __init__(self, first, second):
        """Constructor."""
        super(Division, self).__init__()
        self.symbol = "/"
        self.first = first
        self.second = second

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("first", self.first),
            ("second", self.second)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(first={}, second={})".format(self.clsname, self.first, self.second)


class Equal(BinaryOperation):
    """Class for COOL Equality Comparator."""

    def __init__(self, first, second):
        """Constructor."""
        super(Equal, self).__init__()
        self.symbol = "="
        self.first = first
        self.second = second

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("first", self.first),
            ("second", self.second)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(first={}, second={})".format(self.clsname, self.first, self.second)


class LessThan(BinaryOperation):
    """Class for COOL LessThan Comparator."""

    def __init__(self, first, second):
        """Constructor."""
        super(LessThan, self).__init__()
        self.symbol = "<"
        self.first = first
        self.second = second

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("first", self.first),
            ("second", self.second)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(first={}, second={})".format(self.clsname, self.first, self.second)


class LessThanOrEqual(BinaryOperation):
    """Class for COOL LessThanOrEqual Comparator."""

    def __init__(self, first, second):
        """Constructor."""
        super(LessThanOrEqual, self).__init__()
        self.symbol = "<="
        self.first = first
        self.second = second

    def to_tuple(self):
        """Convert class to Tuple."""
        return tuple([
            ("class_name", self.clsname),
            ("first", self.first),
            ("second", self.second)
        ])

    def to_readable(self):
        """Readable string when class is printed."""
        return "{}(first={}, second={})".format(self.clsname, self.first, self.second)


def is_valid_unary_operation(operation):
    """Check if valid unary operation."""
    return operation in ["~", "not"]


def is_valid_binary_operation(operation):
    """Check if valid binary operation."""
    return operation in ["+", "-", "*", "/", "<", "<=", "="]


def get_operation(operation):
    """Get the coresponding operation for a Token."""
    if operation is None or not isinstance(operation, str):
        return None

    operation = operation.upper()
    operations = {
        "PLUS": "+",
        "MINUS": "-",
        "TIME": "*",
        "DIVIDE": "/",
        "LTHAN": "<",
        "LTEQ": "<=",
        "EQUALS": "=",
        "NOT": "not",
        "INT_COMP": "~"
    }

    if operation in operations:
        return operations[operation]
    else:
        return None
