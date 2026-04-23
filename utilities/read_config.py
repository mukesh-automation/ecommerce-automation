import configparser

config = configparser.ConfigParser()
config.read("configurations/config.ini")

def get_base_url():
    return config.get("DEFAULT", "base_url")

def get_username():
    return config.get("DEFAULT", "username")

def get_password():
    return config.get("DEFAULT", "password")

def get_browser():
    return config.get("DEFAULT", "browser")