import re
import telepot
import lundiubotbasicfn as ldb_basic
import time
import codecs
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


# class MessageHandler(telepot.helper.ChatHandler, telepot.helper.AnswererMixin):
class MessageHandler(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(MessageHandler, self).__init__(*args, **kwargs)
        self.reply = ""
        # Storing the user id into add_key_list, for handling the request of user
        self.add_key_list = []
        # user id as key, keyword as value ==> for processing later
        self.add_value_dict = dict()
        self.quote_fname = 'lun_diu_bot'

    # callback function for message
    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        '''
        print msg
        '''
        if msg['date'] < (time.time() - 60):
            return
        if content_type == "text":
            text = ldb_basic.get_message_text(msg)
            # handling the command
            if re.search('^/[\S]+@ompbot$', text):
                command = str(text).split('@')
                command = command[0]
                if command == '/start':
                    if not ldb_basic.quote_list.has_key(chat_id):
                        ldb_basic.add_new_user_to_json(self.quote_fname, ldb_basic.quote_list, chat_id)
                if command == '/test':
                    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text='Don\'t Press', callback_data='press')]
                    ])
                    self.sender.sendMessage("Please", reply_markup=keyboard)
                elif command == '/add_quote':
                    if msg['from'] not in self.add_key_list or len(self.add_key_list) == 0:
                        self.sender.sendMessage("Please enter the key\n"
                                                "Time Limit: 30s\n"
                                                "If the Time Limit is pass, just type /add_quote again\n"
                                                "and follow the instructions,"
                                                "have fun")
                        self.add_key_list.append(msg['from']['id'])
                    else:
                        # if the user already call the command
                        self.sender.sendMessage("Please enter the key")
                    return
            # if the input message is not a command
            else:
                # check whether the user(s) is(are) the one who send out the command
                # and collecting the key
                if len(self.add_key_list) > 0:
                    if msg['from']['id'] in self.add_key_list:
                        # remove the user from the list by his/her id first
                        self.add_key_list.remove(msg['from']['id'])
                        self.sender.sendMessage("Please enter the value")
                        # then adding the user id into another dictionary as key, and the keyword as value
                        self.add_value_dict[msg['from']['id']] = msg['text'].encode("utf-8")
                        return

                # collecting the value
                if len(self.add_value_dict) > 0:
                    if msg['from']['id'] in self.add_value_dict:
                        # we can get the key from the dictionary, and the value from the msg
                        # we can now add the keyword and value into the json file and the dictionary as well
                        # but it will be very large if many users use this bot
                        ldb_basic.add_new_object_to_json(self.quote_fname, ldb_basic.quote_list, msg['chat']['id'],
                                                         self.add_value_dict[msg['from']['id']], msg['text'])
                        del self.add_value_dict[msg['from']['id']]
                        self.sender.sendMessage("Finished")
                        return
                self.reply = ""
                if not(ldb_basic.quote_list.has_key(str(chat_id))):
                    return
                # check whether the text contain any keyword
                for i in ldb_basic.quote_list[str(chat_id)].keys():
                    if re.search(i, text):
                        # casting the keys in to unicode value to avoid the codec problem
                        self.reply += ldb_basic.quote_list[str(chat_id)][unicode(i)]
                        break
                # if any keyword matched
                if self.reply is not "":
                    # sending out the message
                    self.sender.sendMessage(self.reply)
                    return


if __name__ == '__main__':
    exit()
