#'‹ ٰ💸 ⇣ سورس الفراعنة ⇣ 💸 › .'#
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


API_ID = int("8186557")
API_HASH = "efd77b34c69c164ce158037ff5a0d117"
Bots = []
off =None
ch = "CH_ELMSRY" # يوزر قناتك
DEVS = ["R_R_B0"] #يوزرات المطورين المصنع
@Client.on_message(filters.private)
async def me(client, message):
   if off:#'‹ ٰ💸 ⇣ سورس الفراعنة ⇣ 💸 › .'#
    if not message.from_user.username in DEVS:
     return await message.reply_text("تم تعطيل الوضع المجاني من قبل مطور \n لتواصل مع المطور @r_r_b0")
   message.continue_propagation()

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
   if message.from_user.username in DEVS:
     kep = ReplyKeyboardMarkup([["تنصيب الان ✪", "حذف التنصيب ✪"], ["✪ البوتات المصنوعه"], ["تعطيل المجاني ✪", "تفعيل المجاني ✪"], ["السورس ✪"]], resize_keyboard=True)
     return await message.reply_text("اهلا بيك ف مصنع تيلثون  فينوم", reply_markup=kep)
   kep = ReplyKeyboardMarkup([["تنصيب الان ✪", "حذف التنصيب ✪"], ["السورس ✪"]], resize_keyboard=True)
   await message.reply_text("اهلا بيك ف صانع التيلثون لسورس فينوم\nلتواصل مع المطور :@R_R_B0", reply_markup=kep)

@Client.on_message(filters.command(["السورس ✪"], ""))
async def alivehi(client: Client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝚂𝙾𝚄𝚁𝙲𝙴️", url=f"https://t.me/rb_ro"),
            ],
            [
                 InlineKeyboardButton(f"𝗗𝗘𝗩 VENOM👀❤️", url=f"https://t.me/r_r_b0")
            ]
        ]
    )

    await message.reply_photo(
        photo="https://telegra.ph/file/d3d23e8cff24c7c1df1fe.jpg",
        caption="",
        reply_markup=keyboard,
    )
@Client.on_message(filters.command(["تفعيل المجاني ✪", "تعطيل المجاني ✪"], "") & filters.private)
async def onoff(client, message):
  if not message.from_user.username in DEVS:
    return
  global off
  if message.text == "تفعيل المجاني ✪":
    off = None
    return await message.reply_text("تم تفعيل المجاني بنجاح ✪")
  else:
    off = True
    await message.reply_text("تم تعطيل المجاني بنجاح ✪")
@Client.on_message(filters.command("تنصيب الان ✪", "") & filters.private)
async def makedhelal(client, message):
  if not message.from_user.username in DEVS:
    for x in Bots:
        if x[1] == message.from_user.id:
          return await message.reply_text("لقد قمت بصنع بوت من قبل ✪")
  try:
    ask = await client.ask(message.chat.id, "ارسل توكن البوت ✪", timeout=300)
  except:
      return
  TOKEN = ask.text
  try:
    ask = await client.ask(message.chat.id, "ارسل كود الجلسه ✪", timeout=300)
  except:
      return
  SESSION = ask.text
  if message.from_user.username:
    try:
       ask = await client.ask(message.chat.id, "ارسل ايدي المطور ✪", timeout=300)
    except:
      return
    try:
      Dev = int(ask.text)
    except:
      return await message.reply_text("قم بارسال الايدي بشكل صحيح ✪")#'‹ ٰ💸 ⇣ سورس الفراعنة ⇣ 💸 › .'#
  bot = Client(":memory:", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
  user = Client(api_id=API_ID, api_hash=API_HASH, session_name=str(SESSION) )
  try:
    await bot.start()
    username = await bot.get_me()
    username = username.username
    await bot.stop()
    await user.start()
    await user.stop()
  except:
    return await message.reply_text("تاكد من التوكن أو الجلسة ✪")
  id = username
  for x in Bots:
        if x[0] == id:
          return await message.reply_text("لقد قمت بصنع بوت من قبل ✪")
  os.system(f"cp -a source users/{id}")
  env = open(f"users/{id}/config.py", "w+", encoding="utf-8")
  x = f'from pyrogram import Client,filters,enums\nimport redis\nr = redis.Redis(\n    host="127.0.0.1",\n    port=6379,\n    charset="utf-8",\n    decode_responses=True\n    )\nsudo_id = {Dev}\nbot_user = "{id}"\napi_id = 10823881\napi_hash = "339886e2109eb67203ce12022b32e035"\nsession = "{SESSION}"\ntoken = "{TOKEN}"\nsudo_command = [5345637082, 1001132193]\npm = "{Dev}"\nmention = "{Dev}"\nplugins = dict(root="plugins")\napp = Client("user:{id}",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)\nbot = Client("{id}",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))\n'
  env.write(x)
  env.close()
  os.system(f"cd users/{id} && screen -d -m -S {id} python3 -m user.py")
  oo = [id, Dev]
  Bots.append(oo)
  await message.reply_text("تم تنصيب تيلثون بنجاح  ✪")

@Client.on_message(filters.command("حذف التنصيب ✪", "") & filters.private)
async def deletbothelal(client, message):
   if not message.from_user.username in DEVS:
     for x in Bots:
         bot = x[0]
         if x[1] == message.from_user.id:       
           os.system(f"rm -fr users/{bot}")
           os.system(f"screen -XS {bot} quit")
           Bots.remove(x)
           return await message.reply_text("تم حذف بوتك من الصانع ✪")
     return await message.reply_text("لم تقم بصنع بوتات ✪")
   try:
      bot = await client.ask(message.chat.id, "هات يوزر البوت ✪", timeout=200)
   except:
      return
   bot = bot.text.replace("@", "")
   for x in Bots:
       if x[0] == bot:
          Bots.remove(x)
   os.system(f"rm -fr users/{bot}")
   os.system(f"screen -XS {bot} quit")
   await message.reply_text("تم حذف البوت بنجاح ✪")

@Client.on_message(filters.command("✪ البوتات المصنوعه", ""))
async def bothelal(client, message):
  if not message.from_user.username in DEVS:
   return
  o = 0
  text = "قايمه البوتات\n"
  for x in Bots:
      o += 1
      text += f"{o}- @{x[0]}\n"
  if o == 0:
    return await message.reply_text("✪ لا يوجد بوتات مصنوعه")
  await message.reply_text(text)
