import json, time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from random import uniform

consumer = KafkaConsumer(bootstrap_servers=['172.24.41.128:8081'],
						value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe(pattern='reserva.*')

producer = KafkaProducer(bootstrap_servers=['172.24.41.128:8081'], 
				value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))


    producer.send('reserva', {'costo': '150000', 'fechaInicio': datetime.datetime.now().strftime("%A"), 
										'fechaCaduca': datetime.datetime.now().strftime("%A"), 'carro': 'Renault 4', 'parqueadero': '00000001',
										'duenoParqueadero': '0000000011', 'usuarioParqueadero': '000000034'})
    producer.flush()
