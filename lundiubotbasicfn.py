import json
import telepot
# import InlineQueryHandler
import MessageHandler as MH
from telepot.delegate import per_chat_id, pave_event_space, create_open


# initialize the required module
def init(token):
    temp_result = []
    for i in load_target:
        temp_result.append(load_json_from_file(i))
    return (telepot.DelegatorBot(token, [pave_event_space()(per_chat_id(), create_open,
                                                            MH.MessageHandler, timeout=30)],
                                 ), temp_result[0], temp_result[1])
    # return telepot.DelegatorBot(token, [
    #     pave_event_space()(per_chat_id(), create_open, InlineQueryHandler.InlineQueryHandler, timeout=10)
    #     , pave_event_space()(per_chat_id(), create_open, MessageHandler.MessageHandler, timeout=10)]
    #                             ), temp_result[0], temp_result[1]


def get_message_text(msg):
    return msg['text']


def get_message_id(msg):
    return msg['chat']['id']


# def is_reply(msg):
#     try:
#         if msg['reply_to_message'] is not None:
#             if msg['reply_to_message']['id'] == msg['id']:
#                 return True, msg['id'], msg['reply_to_message']['message_id'], msg['text']
#         else:
#             print msg
#     except IndexError:
#         return False, None, None, None
#     except KeyError:
#         return False, None, None, None


def load_json_from_file(file_name):
    try:
        with open(file_name, 'r') as f:
            content = json.load(fp=f)
    except KeyError:
        with open(file_name, 'w') as f:
            f.write('')
            content = {}
    return content
    

def add_new_user_to_json(target_fname, target, chat_id):
    try:
        chat_id = str(chat_id)
        target[chat_id] = dict()
        target_fname += '.json'
        with open(target_fname, 'w') as f:
            json.dump(target, f)
        return target
    except KeyError:
        print type(chat_id), type(key)
        

def add_new_object_to_json(target_fname, target, chat_id, key, value):
    try:
        chat_id = str(chat_id)
        target[chat_id][key] = value
        target_fname += '.json'
        with open(target_fname, 'w') as f:
            json.dump(target, f)
        return target
    except KeyError:
        print type(chat_id), type(key)


if __name__ == '__main__':
    exit()
else:
    load_target = ['./lun_diu_bot.json', './bin_c_list.json']
    quote_list = load_json_from_file(load_target[0])
