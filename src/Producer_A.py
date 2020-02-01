from kafka import KafkaProducer
import time

producera = KafkaProducer(bootstrap_servers='localhost:9092')
i=0
while i<40:
    string_a="Producer_A_"+str(i)
    key_a = string_a.encode()	#tobytes
    producera.send('sample',key=key_a, value=bytes(i))
    time.sleep(1)
    i+=2
