# Ceramic Py - Python client for ceramic streams

This Ceramic client implements the payload building, encoding and signing needed to interact with the [Ceramic Network](https://ceramic.network/).

## Working with the streams

### Install the ceramic client using pip

```
pip3 install ceramic-py
```

### Create a stream

Generate a DID using a DID library. Ceramic provides the [Glaze suite](https://github.com/ceramicstudio/js-glaze), which can be used for generating DIDs.

```python
from ceramic.client import Ceramic

# Dummy DID
did = "did:key:z6Mkon3Necd6NkkyfoGoHxid2znGc59LU3K7mubaRcFbLfLX"
did_seed = "0101010101010101010101010101010101010101010101010101010101010101"

# Instantiate the client
ceramic = Ceramic(<CERAMIC_NODE_URL>)

# Create a new stream
initial_data = { "hello": 'world'}
stream_id = ceramic.create_stream(did, did_seed, initial_data)
print(f"Stream creates with ID: {stream_id}")
```
### Read from stream

```python
from ceramic.client import Ceramic

# Dummy DID
did = "did:key:z6Mkon3Necd6NkkyfoGoHxid2znGc59LU3K7mubaRcFbLfLX"
did_seed = "0101010101010101010101010101010101010101010101010101010101010101"

# Instantiate the client
ceramic = Ceramic(<CERAMIC_NODE_URL>)

# Get the data
data, _, _ = ceramic.get_data(<STREAM_ID>)
print(f"Data from stream: {data}")
```

### Update stream

```python
from ceramic.client import Ceramic

# Dummy DID
did = "did:key:z6Mkon3Necd6NkkyfoGoHxid2znGc59LU3K7mubaRcFbLfLX"
did_seed = "0101010101010101010101010101010101010101010101010101010101010101"

# Add a new update commit
new_data = {"foo": "baz"}
ceramic.update_stream(did, did_seed, <STREAM_ID>, new_data)

# Get the data again
data, _, _ = ceramic.get_data(<STREAM_ID>)
print(f"Updated data: {data}")
```

## For Developement

* Clone the git repository 
    ```
    git clone git@github.com:valory-xyz/ceramic-py.git
    ```
* Install [pipenv](https://pipenv.pypa.io/en/latest/).
* Generate the virtual environment:
    ```
    make new_env && pipenv shell
    ```
