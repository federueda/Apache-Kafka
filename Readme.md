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



### Screenshots of Producer+Consumer



## 2. Read the entire Documentation of Apache Kafka.

What is new / different about Kafka Streams? Write to paragraphs.

## 3. Watch the AlphaGo Movie on NetFlix

Done!
