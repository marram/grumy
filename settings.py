GROVE_CHANNEL_KEY = "ZEhTHQZvcDruAASNvnMSeAF3261K0DWG"
SCRUMY_BOARD_URL = "https://scrumy.com/modaoperandi"
ICON_URL = "https://secure.gravatar.com/avatar/696d38ee8bab910de6079ff226b8be0c"
GROVE_ENDPOINT = "https://grove.io/api/notice/%s/" % GROVE_CHANNEL_KEY

SCRUMY_PROJECT = "modaoperandi"
SCRUMY_PASSWORD = "devzrock"
SCRUMY_ENDPOINT = "https://scrumy.com/api/"

PITHY_COMMENTS = ["Cool story bro.",
                  "Good job, yo.",
                  "That's what she said",
                  "A for effort",
                  "Atta boy",
                  "Atta girl",
                  "See you on the other side, brother",
                  "Try not to break anything.",
                  "Thanks. I was hoping you'd do that one.",
                  "Maybe you could mow the lawn next?"]
try:
    import private_settings.py
except Exception, e:
    pass

ALL = locals()

