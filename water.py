
def water(state):
    if(state != "clean"):
        print("The water is dirty")
    else:
        print("The water is clean")
    health(state)

def health(state):
    if(state != "clean"):
        print("The water is unhealthy")
    else:
        print("The water is healthy")
    

water("clean")