import json, datetime
from kafka import KafkaProducer
from kafka.errors import KafkaError
from random import uniform

producer = KafkaProducer(bootstrap_servers=['172.24.41.128:8081'], 
											value_serializer=lambda v: json.dumps(v).encode('utf-8'))
										 
while True:


		producer.send('reserva1', {'costo': '150000', 'fechaInicio': datetime.datetime.now().strftime("%A"), 
										'fechaCaduca': datetime.datetime.now().strftime("%A"), 'carro': 'Renault 4', 'parqueadero': '00000001',
										'duenoParqueadero': '0000000011', 'usuarioParqueadero': '000000034'})
		producer.send('reserva2', {'costo': '250000', 'fechaInicio': datetime.datetime.now().strftime("%A"), 
										'fechaCaduca': datetime.datetime.now().strftime("%A"), 'carro': 'Renault 323', 'parqueadero': '00000002',
										'duenoParqueadero': '0000000012', 'usuarioParqueadero': '000000035'})
		producer.flush()
		time.sleep(5)
