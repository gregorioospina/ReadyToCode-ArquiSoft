import Usuario.py

class DuenoParqueadero(Usuario):

	def __init__(self, nom, log, iden, corr, fot, tipo, parqs):
		super().__init__(self, nom, log, iden, corr, fot)
		self.tipoParqueadero = tipo
		self.parqueaderos = parqs

		## GETTERS ##

	def darTipoParqueadero(self):
		return tipoParqueadero

	def darParqueaderos(self):
		return parqueaderos

		## SETTERS ##

	def setTipoParqueadero(self, tipoX):
		self.tipoParqueadero = tipoX

	def setParqueaderos(self, parqueaderoX):
		self.parqueaderos = parqueaderoX

		## Recomendable,  agregarParqueadero() y eliminarParqueadero() ##


