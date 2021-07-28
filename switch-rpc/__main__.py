from pypresence import Presence
import time

client_id = '869402862080364575'
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

print(RPC.update(state="Playing", details="Trying to make a switch rpc"))  # Set the presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds