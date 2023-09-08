from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = ""
bot_user = ""
api_id = 10823881
api_hash = "339886e2109eb67203ce12022b32e035"
session = ""
token = "6438241998:AAH0e_Sat16FhiThCrkq9hmjVJBt606ICYA"
sudo_command = [5413631898, 5413631898]
pm = ""
mention = ""
plugins = dict(root="plugins")
app = Client("user:",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
