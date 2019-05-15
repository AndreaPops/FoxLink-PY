import kafka_interface
from kafka import KafkaConsumer
import os
from time import sleep
import classifier


KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
TOPIC_INPUT = os.environ.get('TOPIC_INPUT')
TOPIC_OUTPUT = os.environ.get('TOPIC_OUTPUT')
MESSAGES_PER_SECOND = float(os.environ.get('MESSAGES_PER_SECOND'))
SLEEP_TIME = 1 / MESSAGES_PER_SECOND
TRAINING_SET = os.environ.get('TRAINING_SET')
TRAINING_PARQUET = os.environ.get('TRAINING_PARQUET')
MODEL = os.environ.get('MODEL')



def main():
    model = classifier.load_classifier(MODEL, TRAINING_PARQUET, TRAINING_SET)
    print('Running Consumer')
    try:
        consumer = kafka_interface.connectConsumer(TOPIC_INPUT, KAFKA_BROKER_URL)
        print("Consumer connected")
    except Exception as ex:
        print("Error connecting kafka broker as Consumer")
        print(ex)
    try:
        producer = kafka_interface.connectProducer(KAFKA_BROKER_URL)
        print("Producer connected")
    except Exception as ex:
        print("Error connecting kafka broker as Producer")
        print(ex)

    working = True
    while working:
        message_dict = kafka_interface.consume(consumer)
        #message_dict = consumer.poll(timeout_ms=10, max_records = 5)
        #print(message_dict)
        if (message_dict != {}):
            for topic, messages in message_dict.items():
                for message in messages:
                    if classifier.predict(model, message.value) == 1:
                        print(message.value)
                        kafka_interface.send_message(producer, TOPIC_OUTPUT, message.value)
                    # print(transaction)  # DEBUG

if __name__ == '__main__':
    main()

