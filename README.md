# ticket-service

ticket-service/
│
├── main.py                  # Startpunt: start Flask + listeners
├── pubsub_listeners.py      # Listeners voor create/delete
├── pubsub_helpers.py        # Publiceren van ticket-created/refunded events
├── ticket_store.py          # In-memory opslag (later Firestore mogelijk)
├── requirements.txt         # Pip dependencies
└── README.md                # Uitleg voor gebruik


# Ticket Service (Event-Driven FaaS-style)

Deze microservice biedt:

- Pub/Sub listener op `payment-succeeded` → maakt ticket aan
- Pub/Sub listener op `ticket-delete` → verwijdert ticket
- REST endpoint `/ticket/<id>` → haalt ticket op
- Emit events naar `ticket-created` en `ticket-refunded`

## Starten

1. Zorg dat je GCP-serviceaccount toegang heeft tot Pub/Sub
2. Installeer requirements:

