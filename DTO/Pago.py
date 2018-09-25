class Pago:
	def __init__(self, forPag, su, cuenDes):
		self.formaPago = forPag
		self.suma = su
		self.cuentaDestino = cuenDes

	#GETS#
	def darFormaPago(self):
		return self.formaPago

	def darSuma(self):
		return self.suma

	def darCuentaDestino(self):
		return self.cuentaDestino

	#SETS#
	def setFormaPago(self, foPag):
		self.formaPago = foPag

	def setSuma(self, s):
		self.suma = s

	def setCuentaDestino(self, cuDest):
		self.cuentaDestino = cuDest
