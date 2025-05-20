import json, time
from google.cloud import pubsub_v1
from ticket_store import create_ticket, delete_ticket
from pubsub_helpers import publish_event

project_id = "ticket-ada"

def callback_create(message):
    data = json.loads(message.data.decode("utf-8"))
    ticket = create_ticket(data["user_id"], data["event_id"])
    print("Created:", ticket)
    publish_event("ticket-created", ticket)
    message.ack()

def callback_delete(message):
    data = json.loads(message.data.decode("utf-8"))
    deleted = delete_ticket(data["ticket_id"])
    if deleted:
        print("Deleted:", data["ticket_id"])
        publish_event("ticket-refunded", {"ticket_id": data["ticket_id"]})
    else:
        print("Not found:", data["ticket_id"])
    message.ack()

def start_create_listener():
    subscriber = pubsub_v1.SubscriberClient()
    sub_path = subscriber.subscription_path(project_id, "ticket-create-sub")
    subscriber.subscribe(sub_path, callback=callback_create)
    print("Listening for create-ticket...")
    while True: time.sleep(60)

def start_delete_listener():
    subscriber = pubsub_v1.SubscriberClient()
    sub_path = subscriber.subscription_path(project_id, "ticket-delete-sub")
    subscriber.subscribe(sub_path, callback=callback_delete)
    print("Listening for delete-ticket...")
    while True: time.sleep(60)
