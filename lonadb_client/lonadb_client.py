import socket
import json
import base64
import string
import random
from Crypto.Cipher import AES

class LonadbClient:
    def __init__(self, host, port, name, password):
        self.name = name
        self.password = password
        self.port = port
        self.host = host

    async def makeid(self, length):
        result = ""
        characters = string.ascii_letters + string.digits
        while len(result) < 16:
            result += random.choice(characters)
        return result

    def serialize_bytes(self, obj):
        if isinstance(obj, bytes):
            return base64.b64encode(obj).decode()
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    async def send_receive(self, data):
        with socket.create_connection((self.host, self.port)) as client:
            data_encoded = json.dumps(data, default=self.serialize_bytes).encode()
            client.sendall(data_encoded)
            data_raw = client.recv(1024)
            print(data_raw)
            return json.loads(data_raw)


    async def getTables(self):
        process_id = await self.makeid(5)
        data = {
            "action": "get_tables",
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }

        print(data)
        response = await self.send_receive(data)
        return response.get("tables", [])

    async def getTableData(self, table):
        process_id = await self.makeid(5)
        data = {
            "action": "get_table_data",
            "table": table,
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def deleteTable(self, table):
        process_id = await self.makeid(5)
        data = {
            "action": "delete_table",
            "table": {"name": table},
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }

        response = await self.send_receive(data)
        return response

    async def createTable(self, table):
        process_id = await self.makeid(5)
        data = {
            "action": "create_table",
            "table": {"name": table},
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def set(self, table, name, value):
        process_id = await self.makeid(5)
        data = {
            "action": "set_variable",
            "table": {"name": table},
            "variable": {
                "name": name,
                "value": value
            },
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def delete(self, table, name):
        process_id = await self.makeid(5)
        data = {
            "action": "remove_variable",
            "table": {"name": table},
            "variable": {
                "name": name
            },
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def get(self, table, name):
        process_id = await self.makeid(5)
        data = {
            "action": "get_variable",
            "table": {"name": table},
            "variable": {
                "name": name
            },
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def getUsers(self):
        process_id = await self.makeid(5)
        data = {
            "action": "get_users",
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def createUser(self, name, password):
        process_id = await self.makeid(5)
        data = {
            "action": "create_user",
            "user": {
                "name": name,
                "password": password
            },
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def deleteUser(self, name):
        process_id = await self.makeid(5)
        data = {
            "action": "delete_user",
            "user": {
                "name": name
            },
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def checkPassword(self, name, password):
        process_id = await self.makeid(5)
        data = {
            "action": "check_password",
            "checkPass": {
                "name": name,
                "password": password
            },
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def checkPermission(self, name, permission):
        process_id = await self.makeid(5)
        data = {
            "action": "create_user",
            "permission": {
                "user": name,
                "name": permission
            },
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def removePermission(self, name, permission):
        process_id = await self.makeid(5)
        data = {
            "action": "remove_permission",
            "permission": {
                "user": name,
                "name": permission
            },
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def getPermissionsRaw(self, name):
        process_id = await self.makeid(5)
        data = {
            "action": "get_permissions_raw",
            "user": {
                "name": name
            },
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def addPermission(self, name, permission):
        process_id = await self.makeid(5)
        data = {
            "action": "add_permission",
            "permission": {
                "user": name,
                "name": permission
            },
            "login": {
                "name": self.name,
                "password": self.password
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response