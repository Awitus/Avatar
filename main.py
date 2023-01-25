import time
from pyrogram import Client
import pyrogram.raw.functions.messages as folder
import DB

api_id = ТВОЙ ID
api_hash = "ТВОЙ HASH"

app = Client("my_account", api_id, api_hash)

FromDarkweb_channel_id = -1001812490665


async def AddUsers():
    print(">> AddUsers()")
    chat_list = DB.GetChats()
    print(chat_list)
    print(type(chat_list))

    for dialog in chat_list:
        print(">> AddUsers() >>", dialog[1])  # dialog.name
        async for member in app.get_chat_members(dialog[2]):  # dialog.channel_id
            # print("  >>", member.user.username)
            DB.InsertUsers(member.user.username, member.user.id, dialog[2])
            # time.sleep(0.1)


'''
Сначала запустится Main() в DB.py
Потом добавляются все чаты в папке DDOS в Chats
Потом добавляются все люди из Chats в Users
'''

# print(">>> STEP 2")


# time.sleep(5)

async def Main():
    async with app:

        info = await app.invoke(
            folder.GetDialogFilters()
        )

        # element 0 has to title
        # print(info)

        if False:
            async for dialog in app.get_dialogs():
                print(dialog.chat.title, dialog.chat.id)

        i = 1
        while i < len(info):
            print(f"folder({info[i].title}):")
            if info[i].title == "DDOS":

                num = 0

                while num < len(info[i].include_peers):
                    ID = info[i].include_peers[num].channel_id
                    print(f"num({num}):", info[i].include_peers[num])
                    new_id = "-100" + str(ID)
                    # print(new_id)
                    chat = await app.get_chat(new_id)
                    DB.InsertChats(chat.title, chat.id)
                    num += 1
            i += 1

        await AddUsers()

        DB.Close()


# https://docs.pyrogram.org/api/methods/add_chat_members#pyrogram.Client.add_chat_members
async def DDOS():
    async with app:
        # Add one member to a group or channel
        user_list = DB.GetUsers()
        # print(user_list)
        # print(type(user_list))

        # exit(0)

        for user in user_list:
            print(">> DDOS() >>", user[1])  # user.name
            data = await app.add_chat_members(FromDarkweb_channel_id, user[2])  # user_id
            print("  >>", data)
            time.sleep(1)



if __name__ == '__main__':

    # https://ru.stackoverflow.com/questions/460207/%d0%95%d1%81%d1%82%d1%8c-%d0%bb%d0%b8-%d0%b2-python-%d0%be%d0%bf%d0%b5%d1%80%d0%b0%d1%82%d0%be%d1%80-switch-case/1265114#1265114

    while True:
        command = input("What are you doing next? ")
        match command.split():
            case ["data"]:
                app.run(Main())
            case ["ddos"]:
                app.run(DDOS())
            case ["quit"]:
                print("Goodbye Pilot!")
                exit(0)

            case _:  # default
                print(f"Sorry, I couldn't understand {command!r}")
