from ceramic.client import Ceramic

# Optionally, generate a DID using some DID library.
# Ceramic provides the Glaze suite, which can be used for this purpose running: glaze did:create
# https://github.com/ceramicstudio/js-glaze

# Dummy DID
did = "did:key:z6Mkon3Necd6NkkyfoGoHxid2znGc59LU3K7mubaRcFbLfLX"
did_seed = "0101010101010101010101010101010101010101010101010101010101010101"

# Instantiate the client
ceramic = Ceramic()

# Create a new stream
initial_data = { "hello": 'world'}
stream_id = ceramic.create_stream(did, did_seed, initial_data)

# Get the data
data, _, _ = ceramic.get_data(stream_id)
print(f"Current data is {data}")

# Add a new update commit
new_data = {"foo": "baz"}
ceramic.update_stream(did, did_seed, stream_id, new_data)

# Get the data again
data, _, _ = ceramic.get_data(stream_id)
print(f"Current data is {data}")