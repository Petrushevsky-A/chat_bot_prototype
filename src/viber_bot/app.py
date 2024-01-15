from fastapi import FastAPI, Response
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

from starlette.requests import Request

from ..templates.keyboard import DateKeyboard
from ..templates.viber_serializer import ViberSerializerKeyboard 

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

app = FastAPI()


viber = Api(BotConfiguration(
    name='PythonSampleBot',
    avatar='https://site.com/avatar.jpg',
    auth_token='5240fdd4e827d044-90c0e8dc1a384048-9bc6c17e71c9a195'
))

@app.get('/')
def register_viberbot(request: Request):
    viber.unset_webhook()
    viber.set_webhook("https://b8fa-90-151-94-184.ngrok-free.app")
    return Response(content = "Success",status_code=200)

@app.post('/')
async def incoming(request: Request):
    # logger.debug("received request. post data: {0}".format(request.get_data()))
    # every viber message is signed, you can verify the signature using this method
    request_body = await request.body()
    request_param = request.query_params
    request_header = request.headers
    print('='*33)
    print(f'{request=}')
    print(f'{request_body=}')
    print(f'{request_param=}')
    print(f'{request_header=}')
    print('='*33)
    if not viber.verify_signature(request_body , request_header.get('x-viber-content-signature')):
        return Response(status_code=403)
    #
    # this library supplies a simple way to receive a request object
    viber_request = viber.parse_request(request_body)
    print('='*33)
    print(f"{viber_request=}")
    print(f"{isinstance(viber_request, ViberMessageRequest)=}")
    print('='*33)
    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        serializer_keyboard = ViberSerializerKeyboard(DateKeyboard()).set_buttons_data()
        print('='*13+"KEYBOARD"+'='*13)
        print(f'{serializer_keyboard.data=}')
        print('='*33)
        keyboard = KeyboardMessage(
            keyboard=serializer_keyboard.data 
        )

        # lets echo back
        await viber.send_messages(viber_request.sender.id, [
            keyboard ,
        ])
    elif isinstance(viber_request, ViberSubscribedRequest):
        await viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!"),
        ])
    elif isinstance(viber_request, ViberFailedRequest):
        pass
        # logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return Response(content = "Success",status_code=200)

#
# import uvicorn
#
# if __name__ == "__main__":
#     uvicorn.run("app:app", host="0.0.0.0", port=8080)
