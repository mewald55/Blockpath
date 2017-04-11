__author__ = 'vivek'

import re

class StringValidator:
	"""A simple String validation class with a few basic validation methods"""

	REGEX_ALPHA = re.compile('^[a-z]+$', re.IGNORECASE)
	REGEX_ADDRESS_STR = re.compile('([a-z\-0-9]){33,40}$', re.IGNORECASE)
	REGEX_TX_STR = re.compile('([a-z\-0-9]){64,80}$', re.IGNORECASE)
	REGEX_HANDLE = re.compile('[a-z0-9\_]+$', re.IGNORECASE)

	def validate(self, input, checks = [], log = False):
		"""Receive an input and validate it against a list of specified checks"""

		results = {}
		fail = False

		# pass the input to the given checks one by one
		for check in checks:
			try:
				if isinstance(check, tuple): # a validation method with arguments
					check_name = check[0]
					args = check[slice(1,len(check))]
				else:
					check_name = check
					args = None

				method = getattr(self, '_check_' + check_name)
				results[check] = method(input.strip(), args) if args else method(input)

				# if the errors aren't to be logged, return False at the first error
				if not results[check]:
					if log:
						fail = True
					else:
						return False

			except Exception as e:
				print "Invalid validation check given"
				raise

		return True if not fail else results


	# === validation methods

	def _check_not_empty(self, input):
		"""Check if a given string is empty"""
		return False if not input else True

	def _check_is_numeric(self, input):
		"""Check if a given string is numeric"""
		try:
			float(input)
			return True
		except Exception as e:
			return False

	def _check_is_alpha(self, input):
		"""Check if a given string is alpha only"""
		return True if self.REGEX_ALPHA.match(input) else False

	def _check_is_alphanumeric(self, input):
		"""Check if a given string is alphanumeric"""
		return True if input.isalnum() else False

	def _check_is_integer(self, input):
		"""Check if a given string is integer"""
		try:
			int(input)
			return True
		except Exception as e:
			return False

	def _check_is_float(self, input):
		"""Check if a given string is float"""
		try:
			return True if str(float(input)) == input else False
		except Exception as e:
			return False

	def _check_longer_than(self, input, args):
		"""Check if a given string is longer than n"""
		return True if len(input) > args[0] else False

	def _check_shorter_than(self, input, args):
		"""Check if a given string is shorter than n"""
		return True if len(input) < args[0] else False


	def _check_is_tx(self, input):
		"""Check if a given string is a top level domain (only matches formats aaa.bbb and ccc.aaa.bbb)"""
		return True if self.REGEX_TX_STR.match(input) else False

	def _check_is_addr(self, input):
		"""Check if a given string is a top level domain (only matches formats aaa.bbb and ccc.aaa.bbb)"""
		return True if self.REGEX_ADDRESS_STR.match(input) else False

	def _check_is_handle(self, input):
		"""Check if a given string is a username handle (alpha-numeric-underscore)"""
		return True if self.REGEX_HANDLE.match(input) else False
