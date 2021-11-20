from telegram.ext import Updater, CommandHandler
import logging, requests, json

def get_by_state_date(input_state, input_date):
     response = requests.get(covid_data_base_url + input_state + '/' + input_date + '.json')
     json_str = json.loads(response.text)
     date = json_str['date']
     state = json_str['state']
     positive = json_str['positive']
     return f'Date: {date}\nState: {state}\nPositive: {positive}'

def start(update, context):
     context.bot.send_message(chat_id=update.effective_chat.id, 
                              text="I'm your COVID historical data bot")

def get_data_by_date(update, context):
     user_input = update.message.text.split(" ")
     print(user_input)
     context.bot.send_message(chat_id=update.effective_chat.id, 
                              parse_mode='Markdown',
                              text=get_by_state_date(user_input[1], user_input[2]))

def main():
     updater = Updater(token='2133734242:AAEhNN2roId-8FR7ynqJVIp2eFKU9TUCXuY', 
                    use_context=True)

     dispatcher = updater.dispatcher

     logging.basicConfig(level=logging.DEBUG,
                         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
     
     global covid_data_base_url
     covid_data_base_url = "https://api.covidtracking.com/v1/states/"
     
     start_handler = CommandHandler('start', start)
     date_handler = CommandHandler('date', get_data_by_date)
     dispatcher.add_handler(start_handler)
     dispatcher.add_handler(date_handler)

     updater.start_polling()
     
if __name__ == '__main__':
     main()
