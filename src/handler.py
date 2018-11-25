import json
import random
from jokes import jokes

def handle(event, context):
    print(event)

    try:
        if event["session"]["application"]["applicationId"] == "amzn1.ask.skill.612376ef-e96a-4153-995d-3bffe90cf130":
            return handle_alexa()
        raise KeyError
    except KeyError:
        return handle_slack()

def handle_alexa():
    raise NotImplementedError("Haven't implemented Alexa yet...")

def handle_slack():
    return {
        "statusCode": 200,
        "body": json.dumps({
            "response_type": "in_channel",
            "text": random.choice(jokes)
        })
    }
