#Print  all the user names:
users_data = [
    {
        "user_id": 101,
        "name": "Alice",
        "role": "user",
        "active": True,
        "account": {
            "account_id": "ACC1001",
            "balance": 5000,
            "currency": "INR"
        }
    },
    {
        "user_id": 102,
        "name": "Bob",
        "role": "admin",
        "active": False,
        "account": {
            "account_id": "ACC1002",
            "balance": 12000,
            "currency": "INR"
        }
    },
    {
        "user_id": 103,
        "name": "Charlie",
        "role": "user",
        "active": True,
        "account": {
            "account_id": "ACC1003",
            "balance": 3000,
            "currency": "INR"
        }
    },
    {
        "user_id": 104,
        "name": "David",
        "role": "user",
        "active": False,
        "account": {
            "account_id": "ACC1004",
            "balance": 8000,
            "currency": "INR"
        }
    }
]

for users in users_data:
    print(users["name"])


