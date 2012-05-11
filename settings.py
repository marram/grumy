GROVE_CHANNEL_KEY = "edit in private_settings.py"
SCRUMY_BOARD_URL = "edit in private_settings.py"
ICON_URL = "https://secure.gravatar.com/avatar/696d38ee8bab910de6079ff226b8be0c"
GROVE_ENDPOINT = "https://grove.io/api/notice/%s/" % GROVE_CHANNEL_KEY

SCRUMY_PROJECT = "edit in private_settings.py"
SCRUMY_PASSWORD = ""
SCRUMY_ENDPOINT = "https://scrumy.com/api/"

try:
    import private_settings.py
except:
    pass

ALL = locals()

