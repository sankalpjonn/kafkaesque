# kafkaesque
This A flask style kafka consumer. It is an extention of the KafkaConsumer from the kafka-python package available [`here`](https://github.com/dpkp/kafka-python) 

## Installation
```sh
pip install kafkaesque
```

## writing a consumer looks like this

```
from kafkaesque import Kafkaesque

app = Kafkaesque(
        bootstrap_servers=",".join([
                "bs_1:9092",
                "bs_2:9093",
                "bs_3:9094"
        ]),
        group_id="consumer-grp-id"
)

@app.handle('test-topic')
def test_topic_handler(msg):
        print "consumed {} from test-topic".format(msg)

if __name__ == "__main__":
        app.start()
```

## Author
* **Sankalp Jonna**

Email me with any queries: [sankalpjonna@gmail.com](sankalpjonna@gmail.com).