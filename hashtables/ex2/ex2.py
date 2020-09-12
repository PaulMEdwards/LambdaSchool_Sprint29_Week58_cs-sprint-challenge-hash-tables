debug = False

#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtable import HashTable

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = []

    ht = HashTable(length)

    for ticket in tickets:
        ht.put(ticket.source, ticket.destination)

    if debug: print(f"\nht:\n{ht}")

    first_flight = ht.get("NONE")
    route.append(first_flight)
    if debug: print(f"flight # {0}:\t{route[0]}")

    for f in range(length-1):
        flight = ht.get(route[f])
        if debug: print(f"flight # {f+1}:\t{flight}")
        route.append(flight)

    if debug: print(f"route:\t{route}")

    return route
