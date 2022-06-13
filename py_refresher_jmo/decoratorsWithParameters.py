# using parms with Decorators
# different than decorating functions with parameters



user = {"username": "jose", "access_level": "guest"}

def make_secure(access_level):  # this is a "factory" used to create a decorator.
    def make_secure(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == "admin":
                return func(*args, **kwargs)
            else:
                return f"No admin permissions for {user['username']}"

        return secure_function

@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secret_password"
    else:
        return "Go away, hacker man!"

user = {"username": "jose", "access_level": "admin"}
print(get_password("blah"))