import random

R_EATING = "I don't like eating anything becayse I'm bot obviously!"

def unknown():
    response = ['Could you please re-phrase that?', "...", "Sounds about right", "whet does that mean?"][random.randrange(4)]
    return response
