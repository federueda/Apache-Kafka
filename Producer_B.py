from kafka import KafkaProducer
import time

producerb = KafkaProducer(bootstrap_servers='localhost:9092')
i=1
while i<10:
    producera.send('sample',key=b'Number: ', value=bytes(i))
    time.sleep(2)
    i+=2
