# Using the example code from 'user_profile.py', build a profile for yourself 
# by calling 'build_profile()' using your first and last name, and 3 other 
# key-value pairs that describe you

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile("steven", "polanco",
                            location = "new york", 
                            field = "design",
                            hobby = "gaming")

print(user_profile)