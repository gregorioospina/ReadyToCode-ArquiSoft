import Usuario.py

class UsuarioParqueadero(Usuario):

	def __init__(self, nom, log, iden, corr, fot, parqueA, carr):
		super().__init__(self, nom, log, iden, corr, fot)
		self.parqueaderosActual = parqueA
		self.carros = carr

		## GETTERS ##

		def darParqueaderos(self):
			return parqueaderosActual

		def darCarros(self):
			return carros

		## SETTERS ##

		def setParqueaderos(self, parqX):
			self.parqueaderosActual = parqX

		def setCarros(self, carrosX):(Usuario)
			self.carros = carrosX

