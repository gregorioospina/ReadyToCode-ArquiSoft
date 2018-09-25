import Usuario.py

	class AdministradorNidoo(Usuario):
		def __init__(self, nom, log, iden, corr, fot, tipo):
			super().__init__(self, nom, log, iden, corr, fot)
			self.tipoAdministrador = tipo


		## GETTERS ##

		def darTipo(self):
			return tipoAdministrador

		## SETTER ## 
		
		def setTipo(self, tipoX):
			self.tipoAdministrador = tipoX