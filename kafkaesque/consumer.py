from kafka import KafkaConsumer
import traceback
import json
import logging
import sys
import signal

class Kafkaesque():
    def __init__(self, **kw):
        self.consumer = KafkaConsumer(**kw)
        self.handlers={}
        logger = logging.getLogger('kafkaesque-consumer')
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        logger.setLevel(logging.INFO)
        self.logger = logger


    def _add_handler(self, topic, handler):
        if self.handlers.get(topic) is None:
            self.handlers[topic] = []
        self.handlers[topic].append(handler)

    def handle(self, topic):
        def decorator(f):
            self._add_handler(topic, f)
            return f
        return decorator

    def _run_handlers(self, msg):
        try:
            handlers = self.handlers[msg.topic]
            for handler in handlers:
                payload = json.loads(msg.value)
                handler(payload)
            self.consumer.commit()
        except Exception as e:
            self.logger.critical(str(e), exc_info=1)
            self.consumer.close()
            sys.exit("Exited due to exception")

    def signal_term_handler(self, signal, frame):
        self.logger.info("closing consumer")
        self.consumer.close()
        sys.exit(0)

    def start(self):
        self.consumer.subscribe(topics=tuple(self.handlers.keys()))
        self.logger.info("starting consumer...registered signterm")

        signal.signal(signal.SIGTERM, self.signal_term_handler)
        signal.signal(signal.SIGINT, self.signal_term_handler)
        signal.signal(signal.SIGQUIT, self.signal_term_handler)
        signal.signal(signal.SIGHUP, self.signal_term_handler)

        for msg in self.consumer:
            self.logger.info("TOPIC: {}, PAYLOAD: {}".format(msg.topic, msg.value))
            self._run_handlers(msg)
