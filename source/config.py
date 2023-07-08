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
token = "6247911571:AAE5BigKpsEb26VLCi19M3V-nWg_L5NQY4Y"
sudo_command = [1099460779, 1001132193]
pm = ""
mention = ""
plugins = dict(root="plugins")
app = Client("user:",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
