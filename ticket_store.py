# Simpele in-memory opslag
tickets = {}

def create_ticket(user_id, event_id):
    ticket_id = f"{user_id}-{event_id}"
    ticket = {
        "ticket_id": ticket_id,
        "user_id": user_id,
        "event_id": event_id,
        "status": "created"
    }
    tickets[ticket_id] = ticket
    return ticket

def delete_ticket(ticket_id):
    return tickets.pop(ticket_id, None)

def get_ticket(ticket_id):
    return tickets.get(ticket_id)
