from time import sleep
from tkinter import W
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')



producer.send('test_topic', b'CANEEEEEEEE')
producer.flush()
