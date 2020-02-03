from kafka import KafkaProducer
import time

producer_b = KafkaProducer(bootstrap_servers='localhost:9092')
i = 1

while i < 25:
    string = "Producer B -> Number "+str(i)
    message_b = string.encode("utf-8", errors="replace")    # change to bytes
    producer_b.send('sample', message_b)
    time.sleep(2)
    i += 2
