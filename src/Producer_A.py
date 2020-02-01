from kafka import KafkaProducer
import time

producera = KafkaProducer(bootstrap_servers='localhost:9092')
i=0
while i<10:
    producera.send('sample',key=b'Number: ', value=bytes(i))
    time.sleep(1)
    i+=2
