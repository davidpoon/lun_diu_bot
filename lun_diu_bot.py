import telepot
import time
import re
import lundiubotbasicfn as ldb_basic


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    bot.answerCallbackQuery(query_id, text="55 ok")
    # print msg
    # bot.kickChatMember()


# def on_inline_query(msg):
#     def compute():
#         query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
#         articles = telepot.get_inline_query(query_id)
#         return articles
#         # bot.answerInlineQuery(query_id, articles)
#     answerer.answer(msg, compute)


# def on_inline_feedback(msg):
#     result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
#     print result_id, from_id, query_string


def lun_diu_bot():
    bot.message_loop(run_forever='Listening ...')
    # bot.message_loop({
    #     "chat": handle,
    #     "callback_query": on_callback_query,
    #     "inline_query": on_inline_query
    # }, run_forever='Listening ...')


if __name__ == '__main__':
    with open('token', 'r') as token_fp:
        bot, lun_diu_quote, bin_c_list = ldb_basic.init(token_fp.read().strip())
    answerer = telepot.helper.Answerer(bot)
    # inlineQ = {}
    lun_diu_bot()
