# Faust App

This application runs [Faust](https://github.com/robinhood/faust) to receive a message from a topic, then produce a message to a feedback topic.

This app was used to test the [Kafka Response Handler](https://github.com/talalkr/kong-kafka-response-handler) gateway plugins.

## Run locally

1. If not already running, uncomment the `kafka` and `zookeeper` services from the `docker-compose.yml` file
2. Run `docker-compose up --build`
