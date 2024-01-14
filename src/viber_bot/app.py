from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.keyboard_message import KeyboardMessage

import logging

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)


viber = Api(BotConfiguration(
    name='PythonSampleBot',
    avatar='https://site.com/avatar.jpg',
    auth_token='5240fdd4e827d044-90c0e8dc1a384048-9bc6c17e71c9a195'
))

@app.route('/', methods=['GET'])
def register_viberbot():
    viber.set_webhook("https://6f12-90-151-94-184.ngrok-free.app")
    return Response(status=200)

@app.route('/', methods=['POST'])
def incoming():
    logger.debug("received request. post data: {0}".format(request.get_data()))
    # every viber message is signed, you can verify the signature using this method
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    # this library supplies a simple way to receive a request object
    viber_request = viber.parse_request(request.get_data())

    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        keyboard = KeyboardMessage(
            # viber_request = viber_request,
            keyboard={
                        "Type": "keyboard",
                        "Buttons": [{
                            "Columns": 6,
                            "Rows": 1,
                            "Text": "ФОП Готько",
                                    "TextOpacity" : "0",
                                    "BgMedia" : "https://i.ibb.co/7rzVkgc/gotko.jpg",
                            "TextHAlign": "left",
                            "TextVAlign": "middle",
                            "ActionType": "reply",
                            "ActionBody": "ФОП Готько"
                        }, {
                        "Columns": 6,
                        "Rows": 1,
                        "Text": "Полина",
                                "TextOpacity" : "0",
                                "BgMedia" : "https://i.ibb.co/7rsb6Pc/polina.jpg",
                        "TextHAlign": "left",
                        "TextVAlign": "middle",
                        "ActionType": "reply",
                        "ActionBody": "Полина"
                        },{
                                "Columns": 6,
                        "Rows": 1,
                        "Text": "JUST Jewellery",
                                "TextOpacity" : "0",
                                "BgMedia" : "https://i.ibb.co/5TqmnBc/just.jpg",
                        "TextHAlign": "left",
                        "TextVAlign": "middle",
                        "ActionType": "reply",
                                "ActionBody": "JUST Jewellery"
                        },{
                                "Columns": 6,
                        "Rows": 1,
                        "Text": "Silverado",
                                "TextOpacity" : "0",
                                "BgMedia" : "https://i.ibb.co/fGpcMSJ/silverado.jpg",
                        "TextHAlign": "left",
                        "TextVAlign": "middle",
                        "ActionType": "reply",
                        "ActionBody": "Silverado"
                        },{
                                "Columns": 6,
                        "Rows": 1,
                        "Text": "Poli",
                                "TextOpacity" : "0",
                                "BgMedia" : "https://i.ibb.co/WttKpyw/poli.jpg",
                        "TextHAlign": "left",
                        "TextVAlign": "middle",
                        "ActionType": "reply",
                        "ActionBody": "Poli"
                        }, {
                                "Columns": 6,
                        "Rows": 1,
                        "Text": "Цепочки",
                                "TextOpacity" : "0",
                                "BgMedia" : "https://i.ibb.co/GWcfB3r/cepochki.jpg",
                        "TextHAlign": "left",
                        "TextVAlign": "middle",
                        "ActionType": "reply",
                        "ActionBody": "Цепочки"
                        }, {
                                "Columns": 6,
                        "Rows": 1,
                        "Text": "Вернутся на главное меню",
                                "TextOpacity" : "0",
                                "BgMedia" : "https://i.ibb.co/CvGsX1t/message.jpg",
                        "TextHAlign": "left",
                        "TextVAlign": "middle",
                        "ActionType": "reply",
                        "ActionBody": "Вернутся на главное меню"
                        }]
                    })
        # lets echo back
        viber.send_messages(viber_request.sender.id, [
            message, keyboard
        ])
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!"),
        ])
    elif isinstance(viber_request, ViberFailedRequest):
        pass
        logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return Response(status=200)


if __name__ == "__main__":
    # context = ('server.crt', 'server.key')
    # app.run(host='0.0.0.0', port=8080, debug=True, ssl_context=context)
    app.run(host='0.0.0.0', port=8080, debug=True)
