class Factura
	def __init__(self, metodo_pago, monto, horaCreacion, idUsuarioCompra, idUsuarioVenta)
		self.metodo_pago = metodo_pago
		self.monto = monto
		self.horaCreacion = horaCreacion
		self.idUsuarioCompra = idUsuarioCompra
		self.idUsuarioVenta = idUsuarioVenta

	def darMetodoPago(self):
		return metodo_pago

	def darMonto(self):
		return monto

	def darHoraCreacion(self):
		return horaCreacion

	def idUsuarioCompra(self):
		return idUsuarioCompra

	def idUsuarioVenta(self):
		return idUsuarioVenta

	

