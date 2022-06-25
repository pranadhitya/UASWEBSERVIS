import string

chatbot_name = "Chat" + "Bot"

while(True):
    user_message = input("You: ").lower().strip(string.punctuation+string.whitespace)

    print(chatbot_name + ":", end='')

    if user_message == "quit" or user_message == "selesai":
        print("sampai ketemu lagi.")
        break

    if user_message == "hallo":
        print("hallo juga", end='')

    elif user_message == "apa kabar?":
        print("baik nih, kamu gimana?", end='')

    elif "cuaca cerah" in user_message:
        print("iyaa, secerah hatiku ketika memandang wajahmu :D", end='')

    elif "mendung" in user_message:
        print("hati atau cuaca?", end='')

    elif user_message == "hati":
        print("*sending virtual hugs :)", end='')

    elif user_message == "cuaca":
        print("cuma cuaca kan, bukan hati :D", end='')

    elif user_message == "makasih" or user_message == "thanks":
        print("masama :)", end='')
        
    else:
        print("eh..., gimana?", end='')
    print()