import json
from google.cloud import pubsub_v1

project_id = "ticket-ada"
publisher = pubsub_v1.PublisherClient()

def publish_event(topic_name, message_dict):
    topic_path = publisher.topic_path(project_id, topic_name)
    data = json.dumps(message_dict).encode("utf-8")
    future = publisher.publish(topic_path, data)
    return future.result()
