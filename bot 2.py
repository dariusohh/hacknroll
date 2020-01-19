from telegram.ext import CommandHandler, Updater
from telegram import ChatAction, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime
import sched, time
import json
import os
import requests
import logging
import mysql.connector
from mysql.connector import Error

#Connect to SQL Database
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='users',
                                         user='root',
                                         password='xhisadog')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
# Initialise logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Load bot token
with open('token.ini', 'r') as file:
    BOT_TOKEN = file.read().strip()

# Create the bot
updater = Updater(token=BOT_TOKEN, use_context=True)

# Load persistent state
if os.path.isfile('data.txt'):
    with open('data.txt', 'r') as file:
        counter_dict = json.load(file)
else:
    counter_dict = {}
# Dictionary
gyms = ['Sheares','Kent Ridge','Temasek','Eusoff','Raffles',
        'PGP','KE7','UTown','USC','KRGH']
gyms_dict = {}


# Add /start handler
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Hello {}!\n \
               \nType /check to check for Gym buddies in NUS \
               \nType /book to sign up \nType /cancel to cancel'.format(update.effective_message.chat.first_name)
    )

#Add /check handler
def check(update, context):
    handle = update.effective_chat.username
    for gym in gyms:
        cursor.execute("select count(*) from users where location = " + "'" + gym + "'")
        gyms_dict[gym] = cursor.fetchone()[0]
    total_bookings = sum(gyms_dict.values())
    
    #Check location in database
    # Send thinking message
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Checking bookings...'
    )
    #Send typing status
    context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
        )
    #Send current locations and their bookings
    output = ''
    dict2 = {'Sheares':'/sh','Kent Ridge':'/kr','Temasek':'/th','Eusoff':'/eh',
             'Raffles':'/rh','PGP':'/pgp','KE7':'/ke7','UTown':'/utown',
             'USC':'/usc','KRGH':'/krgh'}
    for key in gyms_dict.keys():
        if gyms_dict[key] != 0:
            output += key + " (" + dict2[key] + ") "  + ":" + str(gyms_dict[key]) + '\n'
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Currently, ' + str(total_bookings) + ' people are looking for Gym Buddies' + '\n\n' + output
    )
    def kr(update, context):
        cursor.execute("select date,time,telegram_handle from users where \
	location = 'Kent Ridge' order by date asc, time asc")
        users = cursor.fetchall()
        output = ""
        for user in users:
            output += "Date: {} \nTime: {} \nUser: @{}\n".format(user[0],user[1],user[2])
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= output )
    updater.dispatcher.add_handler(CommandHandler('kr',kr))
    def sh(update, context):
        cursor.execute("select date,time,telegram_handle from users where \
	location = 'Sheares' order by date asc, time asc")
        users = cursor.fetchall()
        output = ""
        for user in users:
            output += "Date: {} \nTime: {} \nUser: @{}\n".format(user[0],user[1],user[2])
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= output )
    updater.dispatcher.add_handler(CommandHandler('sh', sh))


    def th(update, context):
        cursor.execute("select date,time,telegram_handle from users where \
	location = 'Temasek' order by date asc, time asc")
        users = cursor.fetchall()
        output = ""
        for user in users:
            output += "Date: {} \nTime: {} \nUser: @{}\n".format(user[0],user[1],user[2])
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= output )
    updater.dispatcher.add_handler(CommandHandler('th', th))
    def eh(update, context):
        cursor.execute("select date,time,telegram_handle from users where \
	location = 'Eusoff' order by date asc, time asc")
        users = cursor.fetchall()
        output = ""
        for user in users:
            output += "Date: {} \nTime: {} \nUser: @{}\n".format(user[0],user[1],user[2])
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= output )
    updater.dispatcher.add_handler(CommandHandler('eh', eh))
    def rh(update, context):
        cursor.execute("select date,time,telegram_handle from users where \
	location = 'Raffles' order by date asc, time asc")
        users = cursor.fetchall()
        output = ""
        for user in users:
            output += "Date: {} \nTime: {} \nUser: @{}\n".format(user[0],user[1],user[2])
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= output )
    updater.dispatcher.add_handler(CommandHandler('rh', rh))
    def pgp(update, context):
        cursor.execute("select date,time,telegram_handle from users where \
	location = 'PGP' order by date asc, time asc")
        users = cursor.fetchall()
        output = ""
        for user in users:
            output += "Date: {} \nTime: {} \nUser: @{}\n".format(user[0],user[1],user[2])
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= output )
    updater.dispatcher.add_handler(CommandHandler('pgp', pgp))
    def ke7(update, context):
        cursor.execute("select date,time,telegram_handle from users where \
	location = 'KE7' order by date asc, time asc")
        users = cursor.fetchall()
        output = ""
        for user in users:
            output += "Date: {} \nTime: {} \nUser: @{}\n".format(user[0],user[1],user[2])
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= output )
    updater.dispatcher.add_handler(CommandHandler('ke7',ke7))
    def utown(update, context):
        cursor.execute("select date,time,telegram_handle from users where \
	location = 'UTown' order by date asc, time asc")
        users = cursor.fetchall()
        output = ""
        for user in users:
            output += "Date: {} \nTime: {} \nUser: @{}\n\n".format(user[0],user[1],user[2])
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= output )
    updater.dispatcher.add_handler(CommandHandler('utown', utown))
    def usc(update, context):
        cursor.execute("select date,time,telegram_handle from users where \
	location = 'USC' order by date asc, time asc")
        users = cursor.fetchall()
        output = ""
        for user in users:
            output += "Date: {} \nTime: {} \nUser: @{}\n".format(user[0],user[1],user[2])
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= output )
    updater.dispatcher.add_handler(CommandHandler('usc', usc))
    def krgh(update, context):
        cursor.execute("select date,time,telegram_handle from users where \
	location = 'K' order by date asc, time asc")
        users = cursor.fetchall()
        output = ""
        for user in users:
            output += "Date: {} \nTime: {} \nUser: @{}\n".format(user[0],user[1],user[2])
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= output )
    updater.dispatcher.add_handler(CommandHandler('krgh', krgh))


    
#Add /book handler
    #Update time in database
def book(update, context):
    #books a location and a timing
    handle = update.effective_chat.username
    cursor.execute("select COUNT(*) from users where telegram_handle = '{}';".format(handle))
    num = cursor.fetchone()[0]


    def bookEusoff(update, context):
        handle = update.effective_chat.username
        #books a timing for Eusoff hall
        try:
            userdatetime = update.message.text.split(' ')
            userdate = userdatetime[1]
            usertime = userdatetime[2]
            datestring = userdate[0:4] + '-' + userdate[4:6] + '-' + userdate[6:8]
            timestring = usertime[0:2] + ':' + usertime[2:4]
            cursor.execute("insert into users values ('{}','Eusoff','{}','{}')".format(handle,timestring,datestring))
            connection.commit()
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Thanks for booking a slot at Eusoff Gym!' 
        )
        except:
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You have entered an invalid input. Please try again' 
        )
    updater.dispatcher.add_handler(CommandHandler('bookEusoff',bookEusoff))



    def bookKR(update, context):
        handle = update.effective_chat.username
        try:
            #books a timing for kent ridge hall
            
            userdatetime = update.message.text.split(' ')
            userdate = userdatetime[1]
            usertime = userdatetime[2]
            datestring = userdate[0:4] + '-' + userdate[4:6] + '-' + userdate[6:8]
            timestring = usertime[0:2] + ':' + usertime[2:4]
            cursor.execute("insert into users values ('{}','Kent Ridge','{}','{}')".format(handle,timestring,datestring))
            connection.commit()
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Thanks for booking a slot at Kent Ridge Gym!'
            )
        except:
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You have entered an invalid input. Please try again' 
        )
    updater.dispatcher.add_handler(CommandHandler('bookKR',bookKR))

    def bookKE7(update, context):
        handle = update.effective_chat.username
        #books a timing for King Edvard VII hall
        
        try:
            
            userdatetime = update.message.text.split(' ')
            userdate = userdatetime[1]
            usertime = userdatetime[2]
            datestring = userdate[0:4] + '-' + userdate[4:6] + '-' + userdate[6:8]
            timestring = usertime[0:2] + ':' + usertime[2:4]
            cursor.execute("insert into users values ('{}','KE7','{}','{}')".format(handle,timestring,datestring))
            connection.commit()
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Thanks for booking a slot at King Edward VII Gym!'
        )
        except:
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You have entered an invalid input. Please try again' 
        )
    updater.dispatcher.add_handler(CommandHandler('bookKE7',bookKE7))
    
    def bookPGP(update, context):
        handle = update.effective_chat.username
        #books a timing for Prince Georges Park Residences
        
        try:
            
            userdatetime = update.message.text.split(' ')
            userdate = userdatetime[1]
            usertime = userdatetime[2]
            datestring = userdate[0:4] + '-' + userdate[4:6] + '-' + userdate[6:8]
            timestring = usertime[0:2] + ':' + usertime[2:4]
            cursor.execute("insert into users values ('{}','PGP','{}','{}')".format(handle,timestring,datestring))
            connection.commit()
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Thanks for booking a slot at Prince George's Park Gym!"
        )
        except:
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You have entered an invalid input. Please try again' 
        )
    updater.dispatcher.add_handler(CommandHandler('bookPGP',bookPGP))

    def bookRaffles(update, context):
        handle = update.effective_chat.username
        #books a timing for Raffles hall
        
        try:
            
            userdatetime = update.message.text.split(' ')
            userdate = userdatetime[1]
            usertime = userdatetime[2]
            datestring = userdate[0:4] + '-' + userdate[4:6] + '-' + userdate[6:8]
            timestring = usertime[0:2] + ':' + usertime[2:4]
            cursor.execute("insert into users values ('{}','Raffles','{}','{}')".format(handle,timestring,datestring))
            connection.commit()
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Thanks for booking a slot at Raffles Gym!"
        )
        except:
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You have entered an invalid input. Please try again' 
        )
    updater.dispatcher.add_handler(CommandHandler('bookRaffles',bookRaffles))


    def bookSheares(update, context):
        handle = update.effective_chat.username
        #books a timing for Sheares hall
        
        try:
            
            userdatetime = update.message.text.split(' ')
            userdate = userdatetime[1]
            usertime = userdatetime[2]
            datestring = userdate[0:4] + '-' + userdate[4:6] + '-' + userdate[6:8]
            timestring = usertime[0:2] + ':' + usertime[2:4]
            cursor.execute("insert into users values ('{}','Sheares','{}','{}')".format(handle,timestring,datestring))
            connection.commit()
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Thanks for booking a slot at Sheares Gym!"
        )
        except:
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You have entered an invalid input. Please try again' 
        )
    updater.dispatcher.add_handler(CommandHandler('bookSheares',bookSheares))


    def bookTemasek(update, context):
        handle = update.effective_chat.username
        #books a timing for Temasek hall
        
        try:
            
            userdatetime = update.message.text.split(' ')
            userdate = userdatetime[1]
            usertime = userdatetime[2]
            datestring = userdate[0:4] + '-' + userdate[4:6] + '-' + userdate[6:8]
            timestring = usertime[0:2] + ':' + usertime[2:4]
            cursor.execute("insert into users values ('{}','Temasek','{}','{}')".format(handle,timestring,datestring))
            connection.commit()
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="thanks for booking a slot at Temasek Gym!"
        )
        except:
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You have entered an invalid input. Please try again' 
        )
    updater.dispatcher.add_handler(CommandHandler('bookTemasek',bookTemasek))



    def bookUSC(update, context):
        handle = update.effective_chat.username
        #books a timing for University Sports Center

        try:
            
            userdatetime = update.message.text.split(' ')
            userdate = userdatetime[1]
            usertime = userdatetime[2]
            datestring = userdate[0:4] + '-' + userdate[4:6] + '-' + userdate[6:8]
            timestring = usertime[0:2] + ':' + usertime[2:4]
            cursor.execute("insert into users values ('{}','USC','{}','{}')".format(handle,timestring,datestring))
            connection.commit()
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Thanks for booking a slot at University Sports Centre Gym!"
            )
        except:
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You have entered an invalid input. Please try again' 
        )
    updater.dispatcher.add_handler(CommandHandler('bookUSC',bookUSC))


    def bookUtown(update, context):
        handle = update.effective_chat.username
        #books a timing for Utown
        try:
            
            userdatetime = update.message.text.split(' ')
            userdate = userdatetime[1]
            usertime = userdatetime[2]
            datestring = userdate[0:4] + '-' + userdate[4:6] + '-' + userdate[6:8]
            timestring = usertime[0:2] + ':' + usertime[2:4]
            cursor.execute("insert into users values ('{}','UTown','{}','{}')".format(handle,timestring,datestring))
            connection.commit()
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Thanks for booking a slot at Utown Gym!"
        )
        except:
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You have entered an invalid input. Please try again' 
        )
    updater.dispatcher.add_handler(CommandHandler('bookUtown',bookUtown))



    if num != 0:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You are only allowed to book one slot! If you wish to change your slot, use /cancel to remove your current appointment.'
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= 'Which of the following gyms would you like to book?\n\
/bookEusoff \n/bookKE7 \n/bookKR \n/bookPGP \n/bookRaffles \n/bookSheares \n/bookTemasek \n/bookUSC \n/bookUtown\n\n' +
            'Please type /book<Hall> <YYYYMMDD> <HHMM>'
        )



#Add /cancel handler
def cancel(update,context):

    handle = update.effective_chat.username
    cursor.execute("select COUNT(*) from users where telegram_handle = '{}';".format(handle))
    num = cursor.fetchone()[0]
    if num == 0:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You have no bookings.\nTo return to main page, type /back'
        )
    else:
        cursor.execute("select date,time,location from users where \
telegram_handle = '{}'".format(handle))
        booking = cursor.fetchone()
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You have {} bookings!\n\
Your booking is on the {}, {} at {}.\n\n\
To confirm, type /confirm'.format(num,booking[0],booking[1],booking[2])
        )
    def confirm(update,context):
        handle = update.effective_chat.username
        cursor.execute("delete from users where telegram_handle =  '{}';".format(handle))
        connection.commit()
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Your booking has been cancelled.\nTo return to main page, type /back\
'.format(num))
        
    def back(update,context):
        return start(update,context)
    updater.dispatcher.add_handler(CommandHandler('confirm',confirm))
    updater.dispatcher.add_handler(CommandHandler('back',back))
    


#reminder function
##import time
##starttime=time.time()
##while True:
##  
##  time.sleep(60.0 - ((time.time() - starttime) % 60.0))

#Dispatcher
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('cancel', cancel))
updater.dispatcher.add_handler(CommandHandler('check',check))
updater.dispatcher.add_handler(CommandHandler('book',book))

# Start the bot
updater.start_polling()
print('Bot started!')

# Wait for the bot to stop
updater.idle()

# Dump persistent state
with open('data.txt', 'w') as file:
    json.dump(counter_dict, file)

print('Bot stopped!')
