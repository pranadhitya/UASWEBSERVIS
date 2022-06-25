from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot("Ron Obvious")

# english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# trainer = ChatterBotCorpusTrainer(english_bot)
# trainer.train("chatterbot.corpus.english")
# bot = ChatBot(
#     "Chat Bot",
#     storage_adapter="chatterbot.storage.SQLStorageAdapter",
#     database="botData.sqlite3"
# )

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("indonesian/conversations.yml")

trainer = ListTrainer(chatbot)
# trainer.train(conversation)

response = chatbot.get_response("Good morning!")
print(response)