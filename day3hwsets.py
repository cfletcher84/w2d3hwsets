# Python Sets Adventure

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def both_destinations():
    both_fly = our_routes.intersection(competitor_routes)
    print(f'Routes we both fly are: \n{both_fly}')
    return both_fly

def our_unique_routes():
    our_unique = our_routes.difference(competitor_routes)
    print(f"Routes that our unique to us are: \n{our_routes}")
    return our_unique

def their_unique_routes():
    their_unique = competitor_routes.difference(our_routes)
    print(f'Their unique routes are: \n{their_unique}')
    return their_unique

# both_destinations()
# our_unique_routes()
# their_unique_routes()

# Set Operations in Data Analysis

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def remove_dupes():
    customer_set = set(customer_ids)
    print(customer_set)

remove_dupes()
    
