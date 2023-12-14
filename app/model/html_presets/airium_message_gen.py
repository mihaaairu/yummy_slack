

from airium import Airium

message_body_reply = 'message_body_reply'
message_body = 'message_body'


def message_generator(user_name: str, date: str, message_text: str,
                      replies_list: list = None, attachments_list: list = None, root_msg: Airium = None) -> Airium:
    if not root_msg:
        a = Airium()
        mes_body = message_body
    else:
        a = root_msg
        mes_body = message_body_reply
    with a.div(klass=mes_body):
        with a.div(klass='message_header'):
            with a.strong(klass='user_name'):
                a(user_name)
            with a.span(klass='date'):
                a(date)
        if message_text:
            a.hr(klass='top_hr')
        with a.ol(klass='ordered_list'):
            with a.li(klass='message_text'):
                a(message_text)
        if attachments_list:
            a.hr(klass='bottom_hr')
            with a.ol(klass='ordered_list'):
                with a.li(klass='attachments_text'):
                    for file in attachments_list:
                        with a.a(href=f"{file['path']}"):
                            a(file['name'])
                        a.br()
        if replies_list:
            a.hr(klass='bottom_hr')
            with a.details():
                with a.summary():
                    with a.strong():
                        a('Replies')
                for reply in replies_list:
                    message_generator(user_name=reply['user'], date=reply['human_ts'], message_text=reply['text'],
                                      attachments_list=reply['file_names_paths'], root_msg=a)

    return a




