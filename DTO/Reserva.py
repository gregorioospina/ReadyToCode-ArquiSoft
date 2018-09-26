class Reserva:

	def__init__(self,usc,usv,cos,fei,fec):
		self.costo = cos
		self.fechaInicio = fei
		self.fechaCaduca = fec
		self.carro = car
		self.parqueadero = par 
		self.duenoParqueadero = dpa
		self.usuarioParqueadero = upa
		
		## GETTERS ##
		
	def darUsuarioParqueadero(self):
		return usuarioParqueadero

	def darDuenoParqueadero(self):
		return duenoParqueadero
	
	def darCosto(self):
		return costo
	
	def darFechaInicio(self):
		return fechaInicio
	
	def darFechaCaduca(self):
		return fechaCaduca

	def darCarro(self):
		return carro

	def darParqueadero(self):
		return parqueadero
	
		## SETTERS ##

	def setUsuarioParqueadero(self, upa):
		self.usuarioParqueadero = upa;

	def setDuenoParqueadero(self, dpa):
		self.duenoParqueadero = dpa;

	def setCosto(self, cos):
		self.costo = cos;

	def setFechaInicio(self, fei):
		self.fechaInicio = fei;

	def setFechaCaduca(self, fec):
		self.fechaCaduca = fec;	
		
	def setCarro(self, car):
		self.carro = car;

	def setParqueadero(self, par):
		self.parqueadero = par;
