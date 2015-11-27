Intrusion Detection System
============================

sudo apt-get install suricata snort
sudo apt-get install oracle-java8-jdk apache2 openssl-blacklist
sudo apt-get install libhyperic-sigar-java


OSX
-----

brew install Caskroom/cask/java
brew install logstash elasticsearch 
elasticsearch


Make sure ``elasticsearch`` is running, go to  http://localhost:9200

{
  "name" : "Wild Thing",
  "cluster_name" : "elasticsearch_kevin",
  "version" : {
    "number" : "2.0.0",
    "build_hash" : "de54438d6af8f9340d50c5c786151783ce7d6be5",
    "build_timestamp" : "2015-10-22T08:09:48Z",
    "build_snapshot" : false,
    "lucene_version" : "5.2.1"
  },
  "tagline" : "You Know, for Search"
}

--------


### What is this?
Following this guide will set up a local [Elasticsearch](https://www.elastic.co/products/elasticsearch) 
with [Kibana](https://www.elastic.co/products/kibana) and [Marvel](https://www.elastic.co/products/marvel) 
using [Homebrew](http://brew.sh/) and [Homebrew Cask](http://caskroom.io/)

### Prerequisites 
If you already have Java installed on your system, skip `2`and `3`

#### 1. Install Homebrew
- `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

#### 2. Install Cask
- `brew tap caskroom/cask`
- `brew install brew-cask`

#### 3. Install Java
- `brew cask install java`

### Installation 
#### 1. Install Elasticsearch and Kibana
- `brew install elasticsearch` 
- `brew install kibana` 

#### 2. Install Marvel
- `cd /usr/local/Cellar/elasticsearch/<whatever version you have>`
- `bin/plugin install marvel-agent`
- `bin/kibana plugin --install elasticsearch/marvel/latest`

### Usage 
#### Start Applications
- `elasticsearch --config=/usr/local/opt/elasticsearch/config/elasticsearch.yml`
- `kibana`

### Access 
- Elasticsearch: [http://localhost:9200](http://localhost:9200/)
- Marvel: [http://localhost:9200/_plugin/marvel](http://localhost:9200/_plugin/marvel)
- Kibana: [http://localhost:5601](http://localhost:5601/)

-------------

elasticsearch
logstash -e 'input { file { path => "/var/log/*.log" type => "jetty" } } output { elasticsearch { host => localhost protocol => "http" port => "9200" } }'

download kibana 4.2, brew version doesn't work!!

bin/kibana

brew install suricata

