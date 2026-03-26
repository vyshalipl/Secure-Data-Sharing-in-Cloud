users = {
    "admin": {
        "attributes": ["HR", "Manager"],
        "revoked": False
    },
    "user1": {
        "attributes": ["Employee"],
        "revoked": False
    }
}

def is_revoked(username):
    return users.get(username, {}).get("revoked", True)

def get_attributes(username):
    return users.get(username, {}).get("attributes", [])

def revoke_user(username):
    if username in users:
        users[username]["revoked"] = True
