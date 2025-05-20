# ticket-service

ticket-service/
│
├── main.py                  # Startpunt: start Flask + listeners
├── pubsub_listeners.py      # Listeners voor create/delete
├── pubsub_helpers.py        # Publiceren van ticket-created/refunded events
├── ticket_store.py          # In-memory opslag (later Firestore mogelijk)
├── requirements.txt         # Pip dependencies
└── README.md                # Uitleg voor gebruik
