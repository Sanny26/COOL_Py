import ast as AST
import re
import pdb

class Translator:
	def __int__(self):
		pass
	
	def new_prgm(self, obj: AST.Program):
		#print(obj)

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
		self.space = 0		

		for each in obj.classes:
			self.extract_class(each)

	

	def extract_class(self, Class):
		self.prgm = "class {}".format(Class.name)
		if Class.parent:
				self.prgm += "({})".format(Class.parent)
		self.prgm += ":\n\n"
		self.space += 2
		self.itr_features(Class.features)
	
	def itr_features(self, features):
		for each in features:
			funct_name = type(each).__name__
			if funct_name in self.functions:
				self.prgm += self.functions[funct_name](each)
			else:
				print("error ocurred")
				pass
		print(self.prgm)
		print('--------------------------')
		

	def extract_classmethod(self, class_method):
		content = ""
		content += "{}def {}(self, ".format(" "*self.space, class_method.name)
		if class_method.formal_params:
			content += self.itr_parameters(class_method.formal_params)
		content += ")"
		if class_method.return_type:
			content += " -> {}".format(class_method.return_type)
		content += ":\n"
		self.space += 2
		content += self.extract_classbody(class_method.body)
		self.space -= 2
		content += "\n"
		return content

	def extract_classbody(self, body):
		#print(body)
		content = ""
		if body.clsname in ['Integer', 'Boolean', 'String']:
			content += "{}return {}".format(' '*self.space, self.functions[body.clsname](body))
		else:
			content += self.functions[body.clsname](body)
		return content

	def itr_parameters(self, formal_params):
		content = ""
		for each in formal_params:
			content += self.extract_param(each)
		return content

	def extract_param(self, param):
		return "{} : {},".format(param.name, param.param_type)
		####need to replace param.param_type with funct which maps cool reserved to python reserved

	def extract_classattribute(self, class_attr):
		content = ""
		if class_attr.init_expr is None:
			content += "{}self.{} = {}\n\n".format(' '*self.space, class_attr.name, class_attr.init_expr)
		else:
			funct_name = type(class_attr.init_expr).__name__
			if funct_name not in  ['Block', 'Object']:
				subcontent = self.functions[funct_name](class_attr.init_expr)
				content += "{}self.{} = {}\n\n".format(' '*self.space, class_attr.name, subcontent)
			else:
				content += self.functions[funct_name](class_attr.init_expr, class_attr.name)

		return content


	def itr_body(self, body):
		content = ""
		for i in range(len(body.expr_list)):
			each = body.expr_list[i]
			content += self.functions[each.clsname](each)
		
		return content

	def extract_integer(self, obj):
		return str(obj.content)

	def extract_string(self, obj):
		return obj.content

	def extract_boolean(self, obj):
		return str(obj.content)

	def extract_block(self, obj, name=None):
		content = ""
		for i in range(len(obj.expr_list)):
			funct_name = type(obj.expr_list[i]).__name__
			sub_content = self.functions[funct_name](obj.expr_list[i])
			if i != (len(obj.expr_list)-1):
				content += "{}{}\n".format(' '*self.space, sub_content)
			else:
				if name is not None:
					content += "{}self.{} = {}\n\n".format(' '*self.space, name, sub_content)

		return content
		
	def extract_whileloop(self, obj):
		content = ""
		predicate = self.functions[obj.predicate.clsname](obj.predicate)
		#print(obj.body)
		body = self.functions[type(obj.body).__name__](obj.body)

		content += "{}while ({}):\n".format(' '*self.space, predicate)
		self.space += 2
		##extract_body
		content += self.functions[obj.body.clsname](obj.body)+'\n'
		self.space -= 2
		return content

	def extract_object(self, obj, name=None):
		return  ""

	def extract_if(self, obj):

		###ccheck if else body is a if class then generate elif
		print(obj)
		content = ""
		content += "{}if ({}):\n".format(' '*self.space,
										self.functions[obj.predicate.clsname](obj.predicate))
		self.space += 2
		content += self.functions[obj.then_body.clsname](obj.then_body)+"\n"
		self.space -= 2
		content += "{}else:\n".format(' '*self.space)
		self.space += 2
		content += self.functions[obj.else_body.clsname](obj.else_body)+'\n'
		self.space -= 2

		return content

	def extract_dynamic_dispatch(self, obj):
		return ""

	def extract_assignment(self, obj):
		content = ""
		print(obj)
		content += "{}{} = {}".format(' '*self.space, 
										self.functions[obj.instance.clsname](obj.instance),
										self.functions[obj.expr.clsname](obj.expr))
		return content

	def extract_self(self, obj):
		return ""

	def extract_integer_complement(self, obj):
		content = ""
		content += "~({})".format(self.functions[obj.integer_expr.clsname](obj.integer_expr))
		return content

	def extract_boolean_complement(self, obj):
		content = ""
		content += "int(not {})".format(self.functions[obj.boolean_expr.clsname](obj.boolean_expr))
		return content

	def extract_addition(self, obj):
		content = ""
		content += "({}) + ({})".format(self.functions[obj.first.clsname](obj.first),
									self.functions[obj.second.clsname](obj.second))
		return content

	def extract_subtraction(self, obj):
		content = ""
		content += "({}) - ({})".format(self.functions[obj.first.clsname](obj.first),
									self.functions[obj.second.clsname](obj.second))
		return content

	def extract_multiplication(self, obj):
		content = ""
		content += "({}) * ({})".format(self.functions[obj.first.clsname](obj.first),
									self.functions[obj.second.clsname](obj.second))
		return content

	def extract_division(self, obj):
		content = ""
		content += "({}) / ({})".format(self.functions[obj.first.clsname](obj.first),
									self.functions[obj.second.clsname](obj.second))
		return content

	def extract_equal(self, obj):
		content = ""
		content += "({}) == ({})".format(self.functions[obj.first.clsname](obj.first),
									self.functions[obj.second.clsname](obj.second))
		return content

	def extract_less_than_or_equal(self, obj):
		content = ""
		content += "({}) <= ({})".format(self.functions[obj.first.clsname](obj.first),
									self.functions[obj.second.clsname](obj.second))
		return content

	def extract_less_than(self, obj):
		content = ""
		content += "({}) < ({})".format(self.functions[obj.first.clsname](obj.first),
									self.functions[obj.second.clsname](obj.second))
		return content

	def extract_is_void(self, obj):
		content = ""
		content += "({}) is None".format(self.functions[obj.expr.clsname])(obj.expr)
		return content

	def extract_let(self, obj):
		content = ""
		return content

	def extract_case(self, obj):
		content = ""
		return content

	def extract_action(self, obj):
		content = ""
		return content

