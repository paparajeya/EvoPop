import math
import uuid

class Util:
    
    sigmoid = lambda x: 1 / (1 + math.exp(-x))
    
    # Generate a random UUID of length 10
    id_generator = lambda: str(uuid.uuid4()).replace('-','')[:10]
    
