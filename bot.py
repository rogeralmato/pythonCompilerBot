import matplotlib
matplotlib.use('Agg')
import telegram
import logging
import networkx as nx
#import matplotlib.pyplot as plt
import pandas as pd
import pickle
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)
from llegirgraph import *
from functools import reduce

PREGUNTA = range(1)

# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start

def start(bot, update, user_data):
    info = '''
    Hola! Sóc un bot d'enquestes realitzat per l'usuari _@rogeralmato_. Per qualsevol dubte escriu /help.
    '''
    bot.send_message(chat_id=update.message.chat.id, text= info, parse_mode=telegram.ParseMode.MARKDOWN)
    try:
        G = nx.read_gpickle("graph")
    except Exception:
        bot.send_message(chat_id=update.message.chat.id, text= "Graf de l'enquesta no trobat, assegurat"+
        " de crear el graf de input.txt abans")
        return
    preguntes = llegirPreguntes(G)
    if len(preguntes) == 0:
        bot.send_message(chat_id=update.message.chat.id, text="Enquesta sense preguntes. Sisplau carrega una enquesta amb contingut per evaluar.")
        return
    readData("data.pickle")
    user_data['queue'] = [preguntes[0]]

def author(bot, update):
    info = '''
*AUTOR:* Roger Almató Baucells
*EMAIL:* roger.almato@est.fib.upc.edu
'''
    bot.send_message(chat_id=update.message.chat_id, text=info, parse_mode=telegram.ParseMode.MARKDOWN)


def quiz(bot, update,user_data):
    print("inquiz")
    nom = update.message.text[6:]
    bot.send_message(chat_id=update.message.chat.id, text="Enquesta " + nom + ":")
    marcaE = nom + '> '
    user_data['marca'] = marcaE
    
    data = readData("data.pickle")
    queue = user_data['queue']
    user_data['data'] = data
    preg = queue[0]
    queue = queue[1:]
    textP = data[preg][0][1]
    textR = list(zip(list(data[preg][1][3]),data[preg][1][1]))
    textR = reduce(lambda acc,y: acc + "\n" + str(y[0]) + ":" + y[1], textR, "")
    bot.send_message(chat_id=update.message.chat_id, text= textP + textR)
    seguentP = data[preg][2][0]
    queue.append(seguentP)
    user_data['queue'] = queue
    user_data['actualP'] = preg

    if len(user_data['queue']) == 0:
        writeData("data.pickle", user_data['data'])
        return ConversationHandler.END
    else:
        return PREGUNTA




def pregunta(bot, update, user_data):
    resposta = update.message.text
    user_data['data'] = afegirResposta(user_data['actualP'], resposta, user_data['data'])
    data = user_data['data']
    

    while user_data['queue']:
        valorcua = user_data['queue'][0]
        user_data['queue'] = user_data['queue'][1:]
        if (valorcua[1] == -1) | (valorcua[1] == resposta):
            preg = valorcua[0]
            if preg == 'END':
                writeData("data.pickle", user_data['data'])
                bot.send_message(chat_id=update.message.chat_id, text= "Enquesta finalitzada amb èxit")
                return ConversationHandler.END
            textP = data[preg][0][1]
            textR = list(zip(list(data[preg][1][3]),data[preg][1][1]))
            textR = reduce(lambda acc,y: acc + "\n" + str(y[0]) + ":" + y[1], textR, "")
            bot.send_message(chat_id=update.message.chat_id, text= textP + textR)
            user_data['actualP'] = preg
            user_data['queue'] += data[preg][2]

            return PREGUNTA

    writeData("data.pickle", user_data['data'])
    return ConversationHandler.END



def pie(bot, update):
    try:
        pregunta = update.message.text[5:]
        data = readData("data.pickle")
        respostes = data[pregunta][1][2]
        opcionsRespostes = data[pregunta][1][3]
        explode = [0.1] * len(respostes)
        total = sum(respostes)
        if total == 0:
            percentatge = respostes
        else:
            percentatge = list(map(lambda x: x / total * 100, respostes))
        
        ax1 = plt.subplots()
        ax1.pie(respostes, explode=explode, labels=opcionsRespostes, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')
        plt.savefig('pie.png')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('pie.png', 'rb'))

    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text="Usage: /pie ⟨pregunta⟩ \n Assegura't que la pregunta existeixi a l'enquesta")


def bar(bot, update):
    try:
        pregunta = update.message.text[5:]
        data = readData("data.pickle")
        respostes = data[pregunta][1][2]
        opcionsRespostes = data[pregunta][1][3]

        plt.bar(opcionsRespostes, respostes,align='center', color = 'blue')
        plt.xticks(opcionsRespostes)
        plt.savefig('bar.png')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('bar.png', 'rb'))

    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text="Usage: /bar ⟨pregunta⟩ \n Assegura't que la pregunta existeixi a l'enquesta")

def report(bot, update):
    try:
        data = readData("data.pickle")
        message = "*pregunta* *valor* *respostes*"
        for d in data:
            inputData = data[d][1]
            opcionsRespostes = inputData[3]
            respostes = inputData[2]
            r = list(zip(respostes,opcionsRespostes))
            r.sort()
            r = list(reversed(r))
            r = list(filter(lambda x: x[0] > 0, r))
            for e in r :
                message += "\n " + str(d) + " " + str(e[1]) + " " + str(e[0])
        
        bot.send_message(chat_id=update.message.chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text="Usage: /report")


if __name__ == '__main__':

    # declara una constant amb el access token que llegeix de token.txt
    TOKEN = open('.token.txt').read().strip()

    # crea objectes per treballar amb Telegram
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    #  funcions que es poden executar des del telegram
    dispatcher.add_handler(CommandHandler('start', start,pass_user_data=True))
    dispatcher.add_handler(CommandHandler('author', author))
    dispatcher.add_handler(CommandHandler('pie', pie))
    dispatcher.add_handler(CommandHandler('bar', bar))
    dispatcher.add_handler(CommandHandler('report', report))


    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('quiz', quiz,pass_user_data=True)],

        states={ 

            PREGUNTA: [MessageHandler(Filters.text, pregunta,pass_user_data=True)]

        },

        fallbacks=[CommandHandler('cancel', quiz)]
    )

    dispatcher.add_handler(conv_handler)



    # engega el bot
    updater.start_polling()

    updater.idle()