import sys has been unused and so was removed from the code. Here is the updated code:


def create_user(name, age, email):
    if age < 0:
        return None
    return {"name": name, "age": age, "email": email}

def is_admin(user):
    if user["role"] == "admin":
        return True
    return False

def get_user_email(user):
    if user == None:
        return ""
    return user["email"]