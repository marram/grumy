import logging

GROVE_CHANNEL_KEY = "edit in private_settings.py"
SCRUMY_BOARD_URL = "edit in private_settings.py"
ICON_URL = "https://secure.gravatar.com/avatar/696d38ee8bab910de6079ff226b8be0c"
GROVE_ENDPOINT = "https://grove.io/api/notice/%s/" % GROVE_CHANNEL_KEY

SCRUMY_PROJECT = "edit in private_settings.py"
SCRUMY_PASSWORD = ""
SCRUMY_ENDPOINT = "https://scrumy.com/api/"

PITHY_COMMENTS = ["Cool story, bro.",
                  "Great job!",
                  "A for effort!",
                  "I'm coming. That's what I'm here for. That's why you had me, Mama, to save you.",
                  "Atta boy.",
                  "Weath... Witch... Work. That's it, work. I gotta work on where it is.",
                  "Atta girl.",
                  "That was a hell of a thing.",
                  "Girl power!",
                  "Now that's what I call great IT work!",
                  "Could you possibly try NOT to hit EVERY SINGLE ONE?",
                  "Thanks. I was hoping you'd do that one.",
                  "NEVER GIVE UP! NEVER SURRENDER!",
                  "You know, with all that makeup and stuff, I actually thought you were SMART for a second.",
                  "And it's about fucking time."]

PITHY_NEW_COMMENTS = ["...AND BOY ARE MY ARMS TIRED!",
                      "The more you know!",
                      "Do you even have a life?",
                      "Anybody else?",
                      "You're just going to have to kill it.",
                      "Go for the heart, then, the throat, his vulnerable spots!",
                      "CAW!!! CAW!!!",
                      "I don't like this. I don't like this at all.",
                      "I see you've managed to get your shirt off.",
                      "What I could really use here is a cup holder and a couple of Advil.",
                      "Give her a hand, she's British.",
                      "So if you could just go ahead and take care of that, that would be terrific, mmmmkay?",
                      "SO THERE'S THAT."]
PITHY_NEW_COMMENTS.extend(PITHY_COMMENTS)

PITHY_TAKE_COMMENTS = ["Good job, yo.",
                       "BREAKS EVERYTHING.",
                       "Don't forget to bring a towel.",
                       "Now you're playing with power!",
                       "See you on the other side, brother.",
                       "Try not to break anything.",
                       "And posted a really distasteful video of it on the internet.",
                       "...WITH GUSTO!!!",
                       "Better you than me.",
                       "But who will guard the guards themselves?!",
                       "But the--the law won.",
                       "You can do it, put your back into it.",
                       "What? You want a cookie or something?",
                       "Thanks. I was hoping you'd do that one."]
PITHY_TAKE_COMMENTS.extend(PITHY_COMMENTS)

PITHY_DONE_COMMENTS = ["The end."
                       "That'll do, pig. That'll do.",
                       "Maybe you could mow the lawn next?",
                       "Aren't YOU special."]
PITHY_DONE_COMMENTS.extend(PITHY_COMMENTS)

try:
    from private_settings import *
except Exception, e:
    logging.error(e)
    pass

ALL = locals()

