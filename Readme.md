# Streaming / Messaging with Apache Kafka

## 1. Read [Kafka Messaging](https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05)  and the links to the [Kafka Libraries in Python](https://github.com/dpkp/kafka-python) to get ready, and develop the following actions:

- Program two Kafka Producers writing to the same topic.
- Producer A writes even numbers every second, the other Producer B writes odd numbers every two seconds to the topic.
- Consumer C reads the numbers and prints them with the origin A or B.

Note: In practice: You start the three Python Scripts independently (First you strt the zookeper and the Kafka server)

I started installing Kafka through Homebrew in Mac.

$ brew cask install java \
$ brew install kafka

The next step is to start Zookeeper Server followed by the Kafka Server.

$ zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties \
$ kafka-server-start /usr/local/etc/kafka/server.properties

Now, it is possible to start creating Kafka topics, consumers and producers. 

### Creating a Kafka Topic with the name "sample"

$ kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sample

### Install Kafka-Python library

pip install kafka-python

### Creating a Producer in Kafka-Python

I implemented a very basic code for producers, with a time function that held the execution of sending the messages by 1 and 2 seconds, and sending the value and origin encapsulated in the key. The consumer just read the message.key with the origin and value of the number (odd or even).

The consumer code was executed first, and started listening, and then I executed the Producer_A and Producer_B python codes (see the attached screenshot for results)

You can check the [Producer_A.py](src/Producer_A.py), [Producer_B.py](src/Producer_B.py) and [Consumer.py](src/Consumer.py) files located in the [src](src/) folder.

### Screenshots of Producer+Consumer

<p align="center">
<img src="https://github.com/federueda/Apache_Kafka/blob/master/docs/A3_Kafka.png" width="580" height="500" title="Kafka">
</p>

## 2. Read the entire Documentation of Apache Kafka.

What is new / different about Kafka Streams? Write to paragraphs.

## 3. Watch the AlphaGo Movie on NetFlix

Done!
