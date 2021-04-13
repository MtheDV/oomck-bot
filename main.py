from bot import Bot
import nltk
from es.data_loader import DataLoader
import eel

nltk.download("punkt")

bot = Bot()
data_loader = DataLoader()

data_loader.load_data()

eel.init("web")


@eel.expose
def query_bot(user_input):
    responses = bot.ask(user_input)
    if isinstance(responses, list):
        type = responses.pop(0)
        if type == "twitter":
            eel.send_bot_response("Here's the latest tweets about 'Fast and Furious':")
            for response in responses:
                eel.send_bot_response(response)
        elif type == "flickr":
            eel.send_bot_response("Here's a photo about 'Fast and Furious':")
            for response in responses:
                eel.send_bot_response("<img src=" + response + " width='200px'>")
    else:
        eel.send_bot_response(responses)


eel.start("index.html")
