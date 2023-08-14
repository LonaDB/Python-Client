# lonadb-client

The Lonadb Client is a Python library designed to simplify communication with the LonaDB database server. This library provides an easy way to interact with the server's various functions, allowing you to manage tables, variables, users, permissions, and more. It streamlines the process of sending requests and receiving responses from the server using the TCP protocol.

## Installation

You can install the Lonadb Client library using pip:

```bash
pip install lonadb-client
```

## Usage

To use the `lonadb-client` library, follow these steps:

1. Import the required modules and classes:

```python
from lonadb_client import LonadbClient
```

2. Create an instance of the `LonadbClient` class:

```python
client = LonadbClient(host, port, name, password)
```

Replace `host`, `port`, `name`, and `password` with the appropriate values for your Lonadb database server.

3. Use the provided methods to interact with the server:

```python
# Example: Get a list of tables
tables = await client.getTables()
print("Available tables:", tables)
```

## Available Methods

### `getTables()`

Retrieves a list of tables available in the database.

### `getTableData(table)`

Retrieves data from a specified table.

### `deleteTable(table)`

Deletes a table by its name.

### `createTable(table)`

Creates a new table with the given name.

### `set(table, name, value)`

Sets a variable within a table to the specified value.

### `delete(table, name)`

Deletes a variable from a table.

### `get(table, name)`

Retrieves the value of a variable from a table.

### `getUsers()`

Retrieves a list of users in the database.

### `createUser(name, password)`

Creates a new user with the given name and password.

### `deleteUser(name)`

Deletes a user by their name.

### `checkPassword(name, password)`

Checks if the provided password is correct for a given user.

### `checkPermission(name, permission)`

Checks if a user has a specific permission.

### `removePermission(name, permission)`

Removes a permission from a user.

### `getPermissionsRaw(name)`

Retrieves the raw permission data for a user.

### `addPermission(name, permission)`

Adds a permission to a user.

## License

This project is licensed under the GNU Affero General Public License version 3 (GNU AGPL-3.0)