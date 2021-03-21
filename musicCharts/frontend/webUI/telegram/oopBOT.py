import telebot
import logging
import configOOP
import time
import matplotlib.pyplot as plot
from csv import reader
from telebot import types

# Bot Token
bot = telebot.TeleBot(configOOP.telegram_key)

# Store temporary user information (user ID)
dic_user = []

# Icons
dice = u"\U0001f3b2"
mahjong = u"\U0001F000"
mahjongm = u"\U0001f004"
musicNote = u"\U0001F3B6"
heart = u"\u2764"
man = u"\U0001f9cd"
woman = u"\U0001f9cd\u200D\u2640\uFE0F"

# keyboard buttons lists
startList = ["Spotify", "Kai Academy", "Spotify VS Kai"]
spotifylist = ["Top 10 Ranking", "Top Artist Statistic", "Top 10 Stream", "Weekly Stream"]
kaiList = ["Top 10 Ranking", "Top Artist Statistic"]

#Open Kai file and write value to array
songName = []
songNameFeq = []
artistName = []
artistNameFeq = []
with open("/home/pi/Bot/OOP/dataNew.csv", "r") as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    if header != None:
        for row in csv_reader:
            songName.append(row[0])
            songNameFeq.append(row[1])
            artistName.append(row[2])
            artistNameFeq.append(row[3])

#Open Brandon file and write value to array
spotsongName = []
spotsongNameFeq = []
spotartistName = []
spotartistNameFeq = []
with open("/home/pi/Bot/OOP/spotify_feq.csv", "r", encoding="utf-8") as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    if header != None:
        for row in csv_reader:
            spotsongName.append(row[0])
            spotsongNameFeq.append(row[1])
            spotartistName.append(row[2])
            spotartistNameFeq.append(row[3])

#Open Brandon file and write value to array
def spotifyStreamWeekly(week):
    week = int(week)
    if week > 1:
        week = 3 * week + (week - 1)
    else:
        week = 3
    spotstreamWeekly = []
    with open("/home/pi/Bot/OOP/spotify_top.csv", "r", encoding="utf-8") as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                spotstreamWeekly.append(row[week])
    return spotstreamWeekly

# logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

def startKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    for value in startList:
        markup.add(types.InlineKeyboardButton(text=value, callback_data=value))
    return markup

def kaichoiceKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    for value in kaiList:
        markup.add(types.InlineKeyboardButton(text=value, callback_data=value + " K"))
    return markup

def spotifychoiceKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    for value in spotifylist:
        markup.add(types.InlineKeyboardButton(text=value, callback_data=value + " S"))
    return markup

def comparechoiceKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    for value in kaiList:
        if value == "Top Artist Statistic":
            break
        markup.add(types.InlineKeyboardButton(text=value, callback_data=value + " C"))
    return markup

def rankspotifyKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    count = 0
    top = 10
    markup.add(types.InlineKeyboardButton(text=mahjongm + " Rank " + mahjong, callback_data="none"),
               types.InlineKeyboardButton(text=musicNote + " Song " + musicNote, callback_data="none"),
               types.InlineKeyboardButton(text=man + " Artist " + woman, callback_data="none"))
    for value in spotsongName:
        if count < top:
            count += 1
            numCount = str(count) + "."
            markup.add(types.InlineKeyboardButton(text=numCount, callback_data="none"),
                       types.InlineKeyboardButton(text=value, callback_data="none"),
                       types.InlineKeyboardButton(text=spotartistName[count-1], callback_data="none"))
        else:
            break
    return markup

def rankkaiKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    count = 0
    top = 10
    markup.add(types.InlineKeyboardButton(text=mahjongm + " Rank " + mahjong, callback_data="none"),
               types.InlineKeyboardButton(text=musicNote + " Song " + musicNote, callback_data="none"),
               types.InlineKeyboardButton(text=man + " Artist " + woman, callback_data="none"))
    for value in songName:
        if count < top:
            count += 1
            numCount = str(count) + "."
            markup.add(types.InlineKeyboardButton(text=numCount, callback_data="none"),
                       types.InlineKeyboardButton(text=value, callback_data="none"),
                       types.InlineKeyboardButton(text=artistName[count-1], callback_data="none"))
        else:
            break
    return markup

def rankVSKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    count = 0
    top = 10
    markup.add(types.InlineKeyboardButton(text=mahjongm + " Rank " + mahjong, callback_data="none"),
               types.InlineKeyboardButton(text=musicNote + " Spotify " + musicNote, callback_data="none"),
               types.InlineKeyboardButton(text=man + " Kai " + woman, callback_data="none"))
    for value in songName:
        if count < top:
            count += 1
            numCount = str(count) + "."
            markup.add(types.InlineKeyboardButton(text=numCount, callback_data="none"),
                       types.InlineKeyboardButton(text=spotsongName[count-1], callback_data="none"),
                       types.InlineKeyboardButton(text=value, callback_data="none"))
        else:
            break
    return markup

def streamSpotifyKeyboardButtons():
    markup = types.InlineKeyboardMarkup()
    count = 0
    top = 10
    markup.add(types.InlineKeyboardButton(text=mahjongm + " Rank " + mahjong, callback_data="none"),
               types.InlineKeyboardButton(text=musicNote + " Song " + musicNote, callback_data="none"),
               types.InlineKeyboardButton(text=man + " Stream " + woman, callback_data="none"))
    for value in songName:
        if count < top:
            count += 1
            numCount = str(count) + "."
            markup.add(types.InlineKeyboardButton(text=numCount, callback_data="none"),
                       types.InlineKeyboardButton(text=value, callback_data="none"),
                       types.InlineKeyboardButton(text=spotsongNameFeq[count-1], callback_data="none"))
        else:
            break
    return markup

def weeklystreamSpotifyKeyboardButtons(week):
    markup = types.InlineKeyboardMarkup()
    count = 0
    top = 10
    stream = spotifyStreamWeekly(week)
    markup.add(types.InlineKeyboardButton(text=mahjongm + " Rank " + mahjong, callback_data="none"),
               types.InlineKeyboardButton(text=musicNote + " Song " + musicNote, callback_data="none"),
               types.InlineKeyboardButton(text=man + " Stream " + woman, callback_data="none"))
    for value in songName:
        if count < top:
            count += 1
            numCount = str(count) + "."
            markup.add(types.InlineKeyboardButton(text=numCount, callback_data="none"),
                       types.InlineKeyboardButton(text=value, callback_data="none"),
                       types.InlineKeyboardButton(text=stream[count-1], callback_data="none"))
        else:
            break
    return markup

@bot.message_handler(commands=["start"])
def _start(message):
    msg = dice*8 + "\n\nData Science Music Bot!\n\n" + dice*8
    bot.send_message(message.chat.id, msg, reply_markup=startKeyboardButtons(), parse_mode="HTML")

@bot.message_handler(commands=["kaichoice"])
def kaichoice(message):
    msg = dice*8 + "\n\nThe probability of busy recess week is 99.99% :)\n\n" + dice*8
    bot.send_message(message.chat.id, msg, reply_markup=kaichoiceKeyboardButtons(), parse_mode="HTML")

@bot.message_handler(commands=["spotifychoice"])
def spotifychoice(message):
    msg = dice*8 + "\n\nWhat do you want to see?\n\n" + dice*8
    bot.send_message(message.chat.id, msg, reply_markup=spotifychoiceKeyboardButtons(), parse_mode="HTML")

@bot.message_handler(commands=["comparechoice"])
def comparechoice(message):
    msg = dice*8 + "\n\nOld Kai (老界王神 Rō Kaiōshin) VS Spotify\n\n" + dice*8
    bot.send_message(message.chat.id, msg, reply_markup=comparechoiceKeyboardButtons(), parse_mode="HTML")

@bot.message_handler(commands=["toprankspot"])
def toprankSpotify(message):
    msg = dice + " Defeated Apple in OS version 14.5 " + dice
    bot.send_message(message.chat.id, msg, reply_markup=rankspotifyKeyboardButtons(), parse_mode="HTML")

@bot.message_handler(commands=["toprankkai"])
def toprankKai(message):
    msg = dice + " Top 10 Songs for the week! " + dice
    bot.send_message(message.chat.id, msg, reply_markup=rankkaiKeyboardButtons(), parse_mode="HTML")

@bot.message_handler(commands=["topvs"])
def toprankvs(message):
    msg = "Top 10 Songs for the week!"
    bot.send_message(message.chat.id, msg, reply_markup=rankVSKeyboardButtons(), parse_mode="HTML")

@bot.message_handler(commands=["artiststats"])
def topartiststats(message):
    artistlist = list(dict.fromkeys(artistName))
    feqlist = []
    for name in artistlist:
        for i in range(len(artistName)):
            if name == artistName[i]:
                feqlist.append(artistNameFeq[i])
                break
    feqarray = [int(numeric_string) for numeric_string in feqlist]

    for i in range(0, len(feqarray)):
        for j in range(i + 1, len(feqarray)):
            if (feqarray[i] < feqarray[j]):
                temp = feqarray[i];
                feqarray[i] = feqarray[j];
                feqarray[j] = temp;
                temp2 = artistlist[i];
                artistlist[i] = artistlist[j];
                artistlist[j] = temp2;

    top = 5
    plotartist = []
    counter = []
    for i in range(top):
        plotartist.append(artistlist[i])
        counter.append(feqarray[i])

    plot.plot(plotartist, counter)
    plot.xlabel("Name of Artist")
    plot.ylabel("Number of Top songs")
    plot.savefig("artistFeq.png")
    bot.send_message(message.chat.id, "Generating Plot of Messy Tree!" + heart)
    time.sleep(1)
    bot.send_photo(message.chat.id, photo=open("artistFeq.png", "rb"))

    markup = types.InlineKeyboardMarkup()
    count = 0
    markup.add(types.InlineKeyboardButton(text="Artist Name", callback_data="none"),
               types.InlineKeyboardButton(text="Count", callback_data="none"))
    for value in artistlist:
        markup.add(types.InlineKeyboardButton(text=value, callback_data="none"),
                   types.InlineKeyboardButton(text=feqarray[count], callback_data="none"))
        count += 1
        if count == top: break
    msg = heart*10 + "\n\n               Statistic of Artist\n\n" + heart*10
    bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="HTML")
    plot.clf()

@bot.message_handler(commands=["spotartiststats"])
def topartiststatsSpotify(message):
    artistlist = list(dict.fromkeys(spotartistName))
    feqlist = []
    for name in artistlist:
        for i in range(len(spotartistName)):
            if name == spotartistName[i]:
                feqlist.append(spotartistNameFeq[i])
                break
    feqarray = [int(numeric_string) for numeric_string in feqlist]

    for i in range(0, len(feqarray)):
        for j in range(i + 1, len(feqarray)):
            if (feqarray[i] < feqarray[j]):
                temp = feqarray[i];
                feqarray[i] = feqarray[j];
                feqarray[j] = temp;
                temp2 = artistlist[i];
                artistlist[i] = artistlist[j];
                artistlist[j] = temp2;

    top = 5
    plotartist = []
    counter = []
    for i in range(top):
        plotartist.append(artistlist[i])
        counter.append(feqarray[i])

    plot.plot(plotartist, counter)
    plot.xlabel("Name of Artist")
    plot.ylabel("Number of Top songs")
    plot.savefig("SpotifyartistFeq.png")
    bot.send_message(message.chat.id, "Generating Plot of Spotify!" + heart)
    time.sleep(1)
    bot.send_photo(message.chat.id, photo=open("SpotifyartistFeq.png", "rb"))

    markup = types.InlineKeyboardMarkup()
    count = 0
    markup.add(types.InlineKeyboardButton(text="Artist Name", callback_data="none"),
               types.InlineKeyboardButton(text="Count", callback_data="none"))
    for value in artistlist:
        markup.add(types.InlineKeyboardButton(text=value, callback_data="none"),
                   types.InlineKeyboardButton(text=feqarray[count], callback_data="none"))
        count += 1
        if count == top: break
    msg = heart*10 + "\n\n               Statistic of Artist\n\n" + heart*10
    bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="HTML")
    plot.clf()

@bot.message_handler(commands=["topstreamspotify"])
def topStreamSpotify(message):
    msg = "Top 10 Streaming for past 10 weeks"
    bot.send_message(message.chat.id, msg, reply_markup=streamSpotifyKeyboardButtons(), parse_mode="HTML")

@bot.message_handler(commands=["topweeklystreamspotify"])
def topWeeklyStreamSpotify(message, week):
    msg = "Week " + week + " Streaming"
    bot.send_message(message.chat.id, msg, reply_markup=weeklystreamSpotifyKeyboardButtons(week), parse_mode="HTML")

@bot.message_handler(func=lambda m: True)
def chat(message):
    txt = message.text
    if any(x in txt.lower() for x in ["thank", "thx", "cool", "thanks", "ty"]):
        msg = "小 cute, no problem"
        bot.send_message(message.chat.id, msg)

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith("Spotify VS Kai"):
        comparechoice(query.message)
    elif data.startswith("Spotify"):
        spotifychoice(query.message)
    elif data.startswith("Kai Academy"):
        kaichoice(query.message)
    elif data.startswith("Top 10 Stream S"):
        topStreamSpotify(query.message)
    elif data.startswith("Weekly Stream"):
        msg = "Please select which week"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text="Current Week 1", callback_data="1"))
        for i in range(2,5):
            markup.add(types.InlineKeyboardButton(text="Week " + str(i), callback_data=str(i)),
                       types.InlineKeyboardButton(text="Week " + str(i+3), callback_data=str(i+3)),
                       types.InlineKeyboardButton(text="Week " + str(i+6), callback_data=str(i+6)))
        bot.send_message(query.message.chat.id, msg, reply_markup=markup, parse_mode="HTML")
    elif data.startswith("Top 10 Ranking S"):
        toprankSpotify(query.message)
    elif data.startswith("Top 10 Ranking K"):
        toprankKai(query.message)
    elif data.startswith("Top 10 Ranking C"):
        toprankvs(query.message)
    elif data.startswith("Top Artist Statistic S"):
        topartiststatsSpotify(query.message)
    elif data.startswith("Top Artist Statistic K"):
        topartiststats(query.message)
    else:
        for i in range(1,11):
            if data == str(i):
                topWeeklyStreamSpotify(query.message, str(i))

while True:
    try:
        bot.infinity_polling(True)
    except:
        time.sleep(1)
