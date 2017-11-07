import ast as AST
import re
import pdb

py_reserved = {'Bool': 'bool',
				'Int': 'int',
				'String': 'str',
				'SELF_TYPE': 'self'}

def flatten(content):
	return ''.join(content)

class Translator:
	def __int__(self):
		pass

	def indent(self, line, space):
		return "{}{}".format(' '*space, line)

	def if_class_attr(self, word):
		if word in self.class_attributes:
			word = "self.{}".format(word)

		return word

	def frmt(self, line, space=0):
		return self.indent(self.if_class_attr(flatten(line)), space)

	def map_p(self, word):
		if word in py_reserved:
			return py_reserved[word]

		return word
	
	def new_prgm(self, obj: AST.Program):
		if obj is None:
			return
		#print(obj)
		
		self.class_attributes = []
		self.functions = {	'ClassMethod': self.extract_classmethod,
							'ClassAttribute': self.extract_classattribute,
							'Integer': self.extract_integer,
							'String': self.extract_string,
							'Boolean': self.extract_boolean,
							'Block' : self.extract_block,
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
						}
		self.prgm = ""	

		for each in obj.classes:
			self.extract_class(each)

	

	def extract_class(self, Class):
		self.prgm = "class {}".format(Class.name)
		if Class.parent:
				self.prgm += "({})".format(Class.parent)
		self.prgm += ":\n\n"
		space = 2
		for each in self.itr_features(Class.features):
			self.prgm += self.frmt(each, space)

		print(self.prgm)
	
	def itr_features(self, features):
		content = []
		for each in features:
			funct_name = each.clsname
			if funct_name in self.functions:
				for line in self.functions[funct_name](each):
					content.append(line)
			else:
				raise SyntaxError("{} is not a valid Keyword in COOL".format(funct_name))

		return content		

	def extract_classmethod(self, class_method):
		content = []
		line = ""

		##class definition
		line += "def {}(self, ".format(class_method.name)
		if class_method.formal_params:
			line += self.itr_parameters(class_method.formal_params)
		line += ")"
		if class_method.return_type:
			line += " -> {}".format(self.map_p(class_method.return_type))
		line += ":\n"
		content.append(line)

		##class body
		# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		space = 2
		for each in self.extract_classbody(class_method.body):
			content.append(self.frmt(each, space))
		content.append("\n")

		return content

	def extract_classbody(self, body):
		content = []
		space = 2
		if body.clsname in ['Integer', 'Boolean', 'String']:
			# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			content = [self.frmt("return {}".format(flatten(self.functions[body.clsname](body))), space)]
		else:
			body_content = self.functions[body.clsname](body)
			for i, each in enumerate(body_content):
				if i == (len(body_content)-1):
					content.append(self.frmt("return {}".format(flatten(each)), space))
				else:
					content.append(self.frmt(each, space))

		return content

	def itr_parameters(self, formal_params):
		content = ""
		for each in formal_params:
			content += self.extract_param(each)
		return content

	def extract_param(self, param):
		return "{} : {},".format(param.name, self.map_p(param.param_type))

	def extract_classattribute(self, class_attr):
		content = []
		line = ""
		self.class_attributes.append(class_attr.name)
		if class_attr.init_expr is None:
			content = ["{} = {}\n".format(class_attr.name, class_attr.init_expr)]
		else:
			funct_name = class_attr.init_expr.clsname
			subcontent = self.functions[funct_name](class_attr.init_expr)
			if funct_name not in  ['Block', 'WhileLoop']:				
				content = ["{} = {}\n".format(class_attr.name, subcontent)]
			else:
				for i, line in enumerate(subcontent):
					#if i == (len(subcontent)-1):
					#	content.append("{} = {}\n".format(class_attr.name, line))
					#else:
					content.append(self.frmt(line))
		return content

	def itr_body(self, body):
		content = []
		for i in range(len(body.expr_list)):
			each = body.expr_list[i]
			for line in self.functions[each.clsname](each):
				content.append(self.frmt(line))
		
		return content

	def extract_integer(self, obj):
		return str(obj.content)

	def extract_string(self, obj):
		return repr(obj.content)

	def extract_boolean(self, obj):
		return str(obj.content)

	def extract_block(self, obj):
		content = []
		for i in range(len(obj.expr_list)):
			funct_name = obj.expr_list[i].clsname
			sub_content = self.functions[funct_name](obj.expr_list[i])
			content.append("{}\n".format(self.frmt(sub_content)))			

		return content
		
	def extract_whileloop(self, obj):
		content = []
		space = 2
		predicate = self.functions[obj.predicate.clsname](obj.predicate)
		body = self.functions[type(obj.body).__name__](obj.body)
		content.append("while ({}):\n".format(self.frmt(predicate)))
		for line in body:
			content.append(self.indent(self.frmt(line), space))

		return content

	def extract_object(self, obj):
		return  obj.name

	def extract_self(self, obj):
		return "self"

	def extract_if(self, obj):
		###add new line after if and else body
		content = []
		space = 2
		content.append("if ({}):\n".format(self.frmt(self.functions[obj.predicate.clsname](obj.predicate))))
		if obj.then_body.clsname in ['Boolean']:
			content.append(self.frmt("return {}\n".format(self.functions[obj.then_body.clsname](obj.then_body)),
										space))
		else:
			for line in self.functions[obj.then_body.clsname](obj.then_body):
				content.append(self.frmt(line,space))
		content.append("else:\n")
		if obj.else_body.clsname in ['Boolean']:
			content.append(self.frmt("return {}\n".format(self.functions[obj.else_body.clsname](obj.else_body)),
										space))
		else:
			for line in self.functions[obj.else_body.clsname](obj.else_body):
				content.append(self.frmt(line, space))

		return content	


	def extract_dynamic_dispatch(self, obj):
		args = ""
		for arg in obj.arguments:
			args += "{}, ".format(self.frmt(self.functions[arg.clsname](arg)))
		instance = self.functions[obj.instance.clsname](obj.instance)
		return  ["{}.{}({})".format(instance, obj.method,args)]

	def extract_static_dispatch(self, obj):
		instance = self.functions[obj.instance.clsname](obj.instance)
		return []

	def extract_assignment(self, obj):
		instance = flatten(self.functions[obj.instance.clsname](obj.instance))
		content = ["{} = {}".format(self.frmt(instance), 
									self.frmt(self.functions[obj.expr.clsname](obj.expr)))]
		return content	

	def extract_integer_complement(self, obj):
		content = ""
		content += "~({})".format(self.frmt(self.functions[obj.integer_expr.clsname](obj.integer_expr)))
		return content

	def extract_boolean_complement(self, obj):
		content = ""
		content += "int(not {})".format(self.frmt(self.functions[obj.boolean_expr.clsname](obj.boolean_expr)))
		return content

	def extract_addition(self, obj):
		content = ""
		content += "({}) + ({})".format(self.frmt(self.functions[obj.first.clsname](obj.first)),
									self.frmt(self.functions[obj.second.clsname](obj.second)))
		return content

	def extract_subtraction(self, obj):
		content = ""
		content += "({}) - ({})".format(self.frmt(self.functions[obj.first.clsname](obj.first)),
									self.frmt(self.functions[obj.second.clsname](obj.second)))
		return content

	def extract_multiplication(self, obj):
		content = ""
		content += "({}) * ({})".format(self.frmt(self.functions[obj.first.clsname](obj.first)),
									self.frmt(self.functions[obj.second.clsname](obj.second)))
		return content

	def extract_division(self, obj):
		content = ""
		content += "({}) / ({})".format(self.frmt(self.functions[obj.first.clsname](obj.first)),
									self.frmt(self.functions[obj.second.clsname](obj.second)))
		return content

	def extract_equal(self, obj):
		content = ""
		content += "({}) == ({})".format(self.frmt(self.functions[obj.first.clsname](obj.first)),
									self.frmt(self.functions[obj.second.clsname](obj.second)))
		return content

	def extract_less_than_or_equal(self, obj):
		content = ""
		content += "({}) <= ({})".format(self.frmt(self.functions[obj.first.clsname](obj.first)),
									self.frmt(self.functions[obj.second.clsname](obj.second)))
		return content

	def extract_less_than(self, obj):
		content = ""
		content += "({}) < ({})".format(self.frmt(self.functions[obj.first.clsname](obj.first)),
									self.frmt(self.functions[obj.second.clsname](obj.second)))
		return content

	def extract_is_void(self, obj):
		content = ""
		content += "({}) is None".format(self.frmt(self.functions[obj.expr.clsname])(obj.expr))
		return content

	def extract_let(self, obj):
		content = []
		return content

	def extract_case(self, obj):
		content = []
		return content

	def extract_action(self, obj):
		content = []
		return content

