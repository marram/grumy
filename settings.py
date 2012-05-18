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
                  "Atta boy.",
                  "Atta girl.",
                  "Girl power!",
                  "Now that's what I call great IT work!",
                  "Thanks. I was hoping you'd do that one.",
                  "NEVER GIVE UP! NEVER SURRENDER!",
                  "And it's about fucking time.",
                  "YOUNG LADY"]

PITHY_NEW_COMMENTS = ["...AND BOY ARE MY ARMS TIRED!",
                      "The more you know!",
                      "Do you even have a life?",
                      "So if you could just go ahead and take care of that, that would be terrific, mmmmkay?",
                      "SO THERE'S THAT.",
                      "You call that a task?"]
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
                       "Thanks. I was hoping you'd do that one.",
                       "Two tasks enter; One task leaves.",
                       "Have fun storming the castle.",
                       "The taskman. Taskatollah. The taskster. Task-o-rama. The taskinator. The taskmeister. Taskarino. Taskerosa.",
                       "Swiper, no swiping!"]
PITHY_TAKE_COMMENTS.extend(PITHY_COMMENTS)

PITHY_DONE_COMMENTS = ["The end."
                       "That'll do, pig. That'll do.",
                       "Maybe you could mow the lawn next?",
                       "Aren't YOU special.",
                       "Did IIII do that?",
                       "And so the task becomes the grass, and the antelope eat the grass. And so we are all connnected in the great Circle of Life. ",
                       "This task is no more! It has ceased to be!",
                       "I'm not dead yet.",
                       "Another one bites the dust."]
PITHY_DONE_COMMENTS.extend(PITHY_COMMENTS)

try:
    from private_settings import *
except Exception, e:
    logging.error(e)
    pass

ALL = locals()

