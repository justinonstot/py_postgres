#Simple Decorators in Python
# allow us to easily modify functions.
# the output of this video is to get the orginal function, which does NOT 
# enforce the password, to enforce and secure it.

# user = {"username": "jose", "access_level": "guest"}

# def get_admin_password():
#     return "1234"

# print(get_admin_password())


user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


get_admin_password = make_secure(get_admin_password)

user = {"username": "jose", "access_level": "basic"}
print(get_admin_password())



