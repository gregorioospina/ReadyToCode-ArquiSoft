import requests
import json, time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from random import uniform

consumer = KafkaConsumer('reserva',
                                                 bootstrap_servers=['172.24.41.128:8081'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

    r = requests.post("http://172.24.41.128:8082/reserva/", data={'costo': message.value['costo'], 'fechaInicio': message.value['fechaInicio'], 'fechaCaduca': message.value['fechaCaduca'], 'carro': message.value['carro'], 'parq$
    print (r.status_code, r.reason)
