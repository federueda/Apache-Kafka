from kafka import KafkaProducer
import time

producer_a = KafkaProducer(bootstrap_servers='localhost:9092')
i = 0

while i < 50:
    string = "Producer A -> Number "+str(i)
    message_a = string.encode("utf-8", errors="replace")    # change to bytes
    producer_a.send('sample', message_a)
    time.sleep(1)
    i += 2
