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
FILE_VALIDATION = 'FILE_VALIDATION'
CLIENT_ID = 'CLIENT_ID'
CLIENT_SECRET = 'CLIENT_SECRET'
SIGNING_SECRET = 'SIGNING_SECRET'
AUTH_URL = 'AUTH_URL'

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
    FILE_VALIDATION: f"Replace the field-text with a single word '{COMPLETE}',"
                     f" after you update slack-app auth data below.",
    CLIENT_ID: "Replace the field-text with your slack-app CLIENT_ID",
    CLIENT_SECRET: "Replace the field-text with your slack-app CLIENT_SECRET",
    SIGNING_SECRET: "Replace the field-text with your slack-app SIGNING_SECRET",
    AUTH_URL: "Replace the field-text with your slack-app authenticate URL with current user-scopes: "
              "channels:history, "
              "channels:read, "
              "files:read, "
              "groups:history, "
              "groups:read,"
              "im:history, "
              "im:read, "
              "mpim:history, "
              "mpim:read, "
              "users:read"
}

# Chat type to download
PRIVATE_CHANNEL = 'private_channel'
PUBLIC_CHANNEL = 'public_channel'
DIRECT_CHAT = 'im'
