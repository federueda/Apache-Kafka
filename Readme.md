# Streaming / Messaging with Apache Kafka

## 1. Read [Kafka Messaging](https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05)  and the links to the [Kafka Libraries in Python](https://github.com/dpkp/kafka-python) to get ready, and develop the following actions:

- Program two Kafka Producers writing to the same topic.
- Producer A writes even numbers every second, the other Producer B writes odd numbers every two seconds to the topic.
- Consumer C reads the numbers and prints them with the origin A or B.

Note: In practice: You start the three Python Scripts independently (First you strt the zookeper and the Kafka server)

### Step 1: installing Kafka through Homebrew in Mac.

$ brew cask install java \
$ brew install kafka

### Step 2: Start Zookeeper Server followed by the Kafka Server.

$ zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties 

<p align="center">
<img src="https://github.com/federueda/Apache_Kafka/blob/master/docs/Zookeeper.png" width="600" height="100" title="Zoo">
</p>

$ kafka-server-start /usr/local/etc/kafka/server.properties

<p align="center">
<img src="https://github.com/federueda/Apache_Kafka/blob/master/docs/Kafka_Server.png" width="600" height="100" title="Ka">
</p>

Now, it is possible to start creating Kafka topics, consumers and producers. 

### Step 3: Creating a Kafka Topic with the name "sample"

$ kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sample

Confirm the "sample" topic was created

$ kafka-topics --list --zookeeper localhost:2181


### Step 4: Install Kafka-Python library

pip install kafka-python

### Step 5: Creating a Producer/Consumer with Kafka-Python

I implemented a very basic code for producers, with a time function that held the execution of sending the messages by 1 and 2 seconds, and encapsulating the information needed to print only in the key. The consumer just read the message.key with the origin and value of the number (odd or even).

First, the consumer code is executed and it starts to listen, then is executed the Producer_A and Producer_B python codes. In the following screenshot you can see the consumer code executed, showing the keys from every message sent. The code from the producers is set to send messages for 20 seconds, but could be set to another value to see more or less messages.

<p align="center">
<img src="https://github.com/federueda/Apache_Kafka/blob/master/docs/Consumer.png" width="550" height="640" title="Consumer">
</p>

You can check the [Producer_A.py](src/Producer_A.py), [Producer_B.py](src/Producer_B.py) and [Consumer.py](src/Consumer.py) files located in the [src](src/) folder.

## 2. Read the entire [Documentation of Apache Kafka.](https://kafka.apache.org/24/documentation/streams/)

What is new / different about Kafka Streams? Write two paragraphs.

It is an API for transforming and enriching the streams of data used in Apache Kafka. It is useful when you are looking for high level of abstraction. This API is part of the open source Apache Kafka project. Several important characteristics that makes Kafka Streams different:

- Support one record at a time processing for miliseconds latenncy
- Support stateless processing, stateful processing and windowing operations
- Elastically scalable and Fault Tolerant
- Deployment agnostic (on-premise, cloud, containers, virtual machines, etc.)
- No matter if it is a small, medium or large scale use case
- Develop on Linux, Windows, Mac

From the architecture point of view, Kafka Streams code will run into your application without a separate processing cluster (seen i.e. as a Java dependency), making the deplyment much easier. Also, all the communication between Kakfa Streams and other applications are performed by Kafka, so you still have all the advatages of this tool, i.e. security features. 

Now in applications of streaming data processing Kafka Streams guarantees that for any record read from the source Kafka topics, its processing results will be reflected exactly once in the output Kafka topic as well as in the state stores for stateful operations, and this is achieved because the integration between Kafka Streams and Kafka storage system.

## 3. Watch the AlphaGo Movie on Netflix

Done!
