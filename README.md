# ceramic-python-client
A simple Ceramic Network client written in Python.

This Ceramic client implements the payload building, encoding and signing needed to interact with the [Ceramic Network](https://ceramic.network/).

# Run the example

The example in this repository creates a new stream in a remote Ceramic node. This stream is initialized with the following data: `{"hello": "world"}`. It then retrieves the data, submits an update request to change that data to `{"foo": "baz"}` and retrieves the data again to prove that the update was successful.

> Note: the Ceramic node used in this examples should be used for testing purposes only. All the data pinned to that node is wiped periodically.

* Install [pipenv](https://pipenv.pypa.io/en/latest/).
* Generate the virtual environment:

    ```
    make new_env
    ```
* Run the example:
    ```
    python example.py
    ```
    You should see an output similar to the following:

    ```
    Created stream kjzl6cwe1jw147sv2ak3kksfgs14gc3jgjhu3mfnwn534l89joxi2tulv0ci14k
    Current data is {'hello': 'world'}
    Updated stream kjzl6cwe1jw147sv2ak3kksfgs14gc3jgjhu3mfnwn534l89joxi2tulv0ci14k
    Current data is {'foo': 'baz'}
    ```
