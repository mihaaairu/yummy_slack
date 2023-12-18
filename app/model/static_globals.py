# MessageBox setup
MSG_WARNING = 1
MSG_INFO = 2


# Slack auth statuses
AUTH_FAILED = 'auth_failed'
DATA_LOAD_FAILED = 'data_load_failed'


# Statuses
COMPLETE = 'complete'
INTERRUPTED = 'interrupted'
FAILED = 'failed'
STARTED = 'started'
TIMEOUT = 'timeout'
NO_CONNECTION = 'no connection found'

# # Errors on config loading
# NO_FILE = 10
# UNABLE_TO_PARSE_CONFIG = 11
# INVALID_APP_CONFIG = 21
# INVALID_USER_CONFIG = 22


# Config / cache / logs
LOG_PATH = 'AppData/logs'
APP_CONFIG_PATH = 'AppData/config'
APP_CONFIG_FILE = 'app_auth.conf'
USER_CACHE_PATH = 'AppData/cache'
USER_CACHE_FILE = 'user.cache'

# File for storing links for files, which failed to download
SKIPPED_FILES = 'SKIPPED_FILES.txt'


# User cache field keys
PRIVATE_TOKEN = 'PRIVATE_TOKEN'
USER_ID = 'USER_ID'
USER_NAME = 'USER_NAME'
TEAM_NAME = 'TEAM_NAME'

# App config field keys
FILE_VALIDATION = 'File validation'
CLIENT_ID = 'Client ID'
CLIENT_SECRET = 'Client Secret'
SIGNING_SECRET = 'Signing Secret'
AUTH_URL = 'Sharable URL'

# Start test ping address
TEST_PING_URL = 'https://8.8.8.8'

# Templates
USER_CACHE_FILE_TEMPLATE = {
    PRIVATE_TOKEN: "",
    USER_ID: "",
    USER_NAME: "",
    TEAM_NAME: ""
}
APP_CONFIG_FILE_TEMPLATE = {
    FILE_VALIDATION: f"Replace this text with a single word '{COMPLETE}',"
                     f" after you update Slack-App auth data below.",
    CLIENT_ID: "Replace this text with your Slack-App 'Client ID'.",
    CLIENT_SECRET: "Replace this text with your Slack-App 'Client Secret'.",
    SIGNING_SECRET: "Replace this text with your Slack-App 'Signing Secret'.",
    AUTH_URL: "Replace this text with your Slack-App 'Sharable URL'."
}

# Chat type to download
PRIVATE_CHANNEL = 'private_channel'
PUBLIC_CHANNEL = 'public_channel'
DIRECT_CHAT = 'im'
