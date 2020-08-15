#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Write a function `reconstruct_trip` to reconstruct your trip from your mass of flight tickets.
    # create another cache, I think... sensing a pattern
    array = {}
    # create dict or maybe list
    route = [None] * length
    # iterate over list of tickets, source (key) destination (val)
    for i in tickets:
        array[i.source] = i.destination
    # initial source value should be 'None'
    destination = array['NONE']
    # iterate over range and set dest and source
    for itinerary in range(length):
        route[itinerary] = destination
        destination = array[destination]
    return route
