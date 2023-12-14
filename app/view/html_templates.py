BODY_OPEN = '<body class="main">'

CHAT_NAME = '<h1 class="chat_name">{}</h1>'

SEPARATOR = '<hr />'

BODY_CLOSE = '</body>'

INTERRUPTED_TAG = '<h1 class="chat_name">Message backup has been interrupted</h1>'

HEAD = """

<head>
    <style>
        * {
            font-family: 'Segoe UI';
            margin: 0px;
            padding: 0px;
        }
        .chat_name {
            font-size: 40px;
            margin: 15px;
            margin-bottom: 30px;
            color: #693af5;
        }
        .main {
            background: #ecedef;
        }
        details > summary {
            list-style: none;

            font-weight: bold;
            background: #906ef7;
            color: #fbfbfb;
            border-radius: 16px;
            padding: 13px;
            padding-top: 7px;
            padding-bottom: 7px;

            width: fit-content;
            margin-left: 0px;
            margin-top: 5px;
            font-size: 14px;
        }
        details > summary:hover {
            background-color: #8d52fc;
        }
        details > summary:active  {
            background-color: #693af5;
        }
        hr {
            margin-top: 3px;
            margin-bottom: 7px;
            width: 100%;
            height: 0px;
            border: none;
            border-top: 1px solid #dbcffc;
        }
        .top_hr {
            margin-top: 3px;
            margin-bottom: 15px;
        }
        .bottom_hr {
            margin-top: 15px;
            margin-bottom: 7px;
        }
        .message_header {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
        }

        .user_name {
            order: 1;
            font-size:18px;
        }
        .date{
            font-size:12px;
            color: #909090;
            //text-decoration: underline;
            padding-left: 30px;
            margin-bottom: 2px;
            order: 2;

        }
        .message_text {
            font-size:14px;
            margin-left: -10px;
        }
        .ordered_list {
            list-style-type: none;
            padding-left: 10px;
        }
        .attachments_text {
            font-size:13px;
            margin-left: -10px;
            color: #693af5;
        }
        .message_body {
            background: #FFFFFF;
            color: #3B3B3B;
            width: fit-content;
            max-width: 700px;
            border-radius: 10px;
            border-top-left-radius: 3px;
            margin: 15px;
            padding: 10px;
            word-wrap: break-word;
        }
        .message_body_reply {
            background: #FFFFFF;
            color: #3B3B3B;
            width: fit-content;
            max-width: 700px;
            border: 1px solid #dbcffc;
            border-radius: 10px;
            border-top-left-radius: 3px;
            margin: 7px;
            padding: 10px;
            word-wrap: break-word;
        }

    </style>
</head>
"""
