from kafka import KafkaProducer`n`nproducer = KafkaProducer(bootstrap_servers="localhost:9092")`nprint("Kafka producer initialized")
`n# Event format: device and temperature
`ndef send_event(topic, data):`n    producer.send(topic, value=str(data).encode("utf-8"))`n    producer.flush()
