#!/usr/bin/env python
import threading, logging, time
import multiprocessing

from kafka import KafkaProducer


class Producer(threading.Thread):
    daemon = True

    def run(self):
        producer = KafkaProducer(bootstrap_servers='138.197.12.79:9092')

        while True:
            producer.send('cassie', "Please visit www.haritibcoblog.com")
            time.sleep(1)


def main():
    tasks = [
        Producer()
    ]

    for t in tasks:
        t.start()

    time.sleep(10)

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    main()