import Usuario.py

	class EncargadoParqueadero(Usuario):

		def __init__(self, nom, log, iden, corr, fot, contact, parqueR):
		super().__init__(self, nom, log, iden, corr, fot)
		self.contacto = contact
		self.parqueaderosResponsable = parqueR

		## GETTERS ##

	def darContacto(self):
		return contacto

	def darParqueaderos(self):
		return parqueaderosResponsable

		## SETTERS ##

	def setContacto(self, contactoX):
		self.contacto = contactoX

	def setParqueaderoResponsable(self, parqueaderoX):
		self.parqueaderosResponsable = parqueaderoX

		## Recomendable,  agregarParqueadero() y eliminarParqueadero() ##

