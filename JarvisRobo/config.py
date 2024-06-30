
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "26778642" # integer value, dont use ""
    API_HASH = "6ad48c8acff7a66f149f7203eaa73503"
    TOKEN = ""  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = "5702598840" # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "Flex_Support_Chat"  # Your own group for support, do not add the @
    START_IMG = "https://graph.org/file/143d5ec7c1f298238c42a.jpg"
    HELP_IMG = "https://graph.org/file/d3ef0577e4ae19b20f970.jpg"
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://dracogameing1:wjjwhbwbwbbwggsuegv646468181nnwjwjuhh6wjwika@cluster0.80xb4d0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # RECOMMENDED
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "X652FNVGJ0ZXABM0"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "VR8S3BA8ESW3"
    
    # Get your API key from https://timezonedb.com/api


    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
