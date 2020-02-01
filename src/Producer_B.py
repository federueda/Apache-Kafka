from kafka import KafkaProducer
import time

producerb = KafkaProducer(bootstrap_servers='localhost:9092')
i=1
while i<20:
    string_b="Producer_B_"+str(i)
    key_b = string_b.encode()	#tobytes
    producerb.send('sample',key=key_b, value=bytes(i))
    time.sleep(2)
    i+=2
