from os import path
import faust
import logging
import asyncio

# setup logging
log_file_path = path.join(path.dirname(path.abspath(__file__)), "logging.conf")
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    filename=log_file_path,
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)

CONSUMER_TOPIC_NAME="fauster"
PRODUCER_TOPIC_NAME="kong.feedback"

app = faust.App("my-app", broker=f"kafka://kafka")
consumer_topic = app.topic(CONSUMER_TOPIC_NAME)
producer_topic = app.topic(PRODUCER_TOPIC_NAME)


async def produce_msg(msg):
    try:
        await producer_topic.send(value=msg)
        logging.info(
            f"Message: {msg} was pushed to topic: {PRODUCER_TOPIC_NAME}"
        )
    except Exception as e:
        logging.error(
            f"Failed to produce to topic {PRODUCER_TOPIC_NAME} the following message: {msg}"
        )
        logging.error(str(e))


@app.agent(consumer_topic)
async def agent(stream):
    async for msg in stream:
        logging.info(f"message received {msg}")
        # await asyncio.sleep(1)
        await produce_msg(msg)
        logging.info("Response Message Sent!")


