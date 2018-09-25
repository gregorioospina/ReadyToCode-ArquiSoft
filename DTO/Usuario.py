class Usuario:
		def __init__(self, nom, log, iden, corr, fot):
			
			self.nombre = nom
			self.login = log
			self.identificacion = iden
			self.correo = corr
			self.foto = fot


		## GETTERS ##	
			
		def darNombre(self):
			return nombre

		def darLogin(self):
			return login

		def darId(self):
			return identificacion

		def darCorreo(self):
			return correo

		def darFoto(self):
			return foto

		## SETTERS ##	

		def setNombre(self, nombreX):
			self.nombre = nombreX

		def setLogin(self, loginX):
			self.login = loginX

		def setId (self, idX):
			self.identificacion = idX

		def setCorreo (self, correoX):
			self.correo = correoX

		def setFoto (self, fotoX):
			self.foto = fotoX


