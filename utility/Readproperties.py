
import json
import os

config_file_path = os.path.join(os.path.dirname(__file__), '..', 'Configuration', 'Config.json')
config_file_path = os.path.abspath(config_file_path)  # Get the absolute path

# Check if the file exists
if not os.path.isfile(config_file_path):
    raise FileNotFoundError(f"The configuration file was not found: {config_file_path}")

# Read the configuration file
with open(config_file_path, 'r') as config_file:
    config_data = json.load(config_file)

# Ensure the section exists
if 'SectionA' not in config_data:
    raise KeyError('The section "common info" is missing in the configuration file')

# Create a dictionary to store the configuration
config_dict = config_data['SectionA']


# Dictionary
# config_dict = {
#     'baseurl': config.get('Section', 'baseurl'),
#     'username': config.get('Section', 'username'),
#     'password': config.get('Section', 'password')
# }
class ReadConfig:
    @staticmethod
    def getConfig():
        return config_dict
    # @staticmethod
    # def getUrl():
    #     url = config.get('common','baseurl')
    #     print(f"Base URL from config: {url}")
    #     return url
    # @staticmethod
    # def getusername():
    #     username = config.get('common info', 'username')
    #     return  username
    #
    # @staticmethod
    # def getpassword() -> object:
    #     password = config.get('common info', 'password')
    #     return password
