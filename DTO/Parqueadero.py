class Parqueadero:
	def __init__(self, nom, dir, due, capa, cubie, prec, durRe):
		self.nombre = nom
		self.IDdireccion = dir
		self.duenio = due
		self.capacidad = capa
		self.cubierto = cubie
		self.precio = prec
		self.duracionReserva = durRe

	#GETS#

	def darNombre(self):
		return self.nombre

	def darIDDireccion (self):
		return self.direccion

	def darDuenio (self):
		return self.duenio

	def darCapacidad (self):
		return self.capacidad

	def darCubierto (self):
		return self.cubierto

	def darPrecio (self):
		return self.precio

	def darDuracionReserva (self):
		return self.duracionReserva


	#SETS#

	def setNombre (self, nomset):
		self.nombre = nomset

	def setIDDireccion (self, dirset):
		self.IDdireccion = dirset

	def setDuenio (self, dueset):
		self.duenio =	dueset

	def setCapacidad (self, capset):
		self.capacidad = capset

	def setCubierto (self, cubset):
		self.cubierto =	cubset

	def setPrecio (self, preset):
		self.precio = preset	

	def setDuracionReserva (self, durset):
		self.duracionReserva =	duirset


























