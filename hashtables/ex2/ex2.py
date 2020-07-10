#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # set up route list with slots
    route = [None] * length

    route_find = {}

    for ticket in tickets:
        route_find[ticket.source] = ticket.destination

    next_route = route_find["NONE"]

    for current in range(0, length):

        route[current] = next_route

        next_route = route_find[next_route]

    return route