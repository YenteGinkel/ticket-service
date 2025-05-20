from flask import Flask, request, jsonify
import threading
from pubsub_listeners import start_create_listener, start_delete_listener
from ticket_store import get_ticket

app = Flask(__name__)

@app.route('/ticket/<ticket_id>', methods=['GET'])
def view_ticket(ticket_id):
    ticket = get_ticket(ticket_id)
    if ticket:
        return jsonify(ticket)
    return jsonify({"error": "Ticket not found"}), 404

if __name__ == "__main__":
    # Start Pub/Sub listeners in aparte threads
    threading.Thread(target=start_create_listener, daemon=True).start()
    threading.Thread(target=start_delete_listener, daemon=True).start()

    # Start REST API
    app.run(host='0.0.0.0', port=80)
