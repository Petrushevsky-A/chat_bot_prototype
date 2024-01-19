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

from starlette.requests import Request
import os

from .router import Router

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
    # временное решение
    viber.unset_webhook()
    viber.set_webhook("chatbot-p.ru")
    return Response(content = "Success",status_code=200)

@app.post('/')
async def incoming(request: Request):
    # logger.debug("received request. post data: {0}".format(request.get_data()))
    # every viber message is signed, you can verify the signature using this method
    request_body = await request.body()
    request_param = request.query_params
    request_header = request.headers
    print(f'======== {request_body=}')
    if not viber.verify_signature(request_body, request_header.get('x-viber-content-signature')):
        return Response(status_code=403)

    viber_request = viber.parse_request(request_body)
    if isinstance(viber_request, ViberMessageRequest):
        answer = Router(viber_request).response
        await viber.send_messages(viber_request.sender.id, [
            answer,
        ])
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!"),
        ])
    elif isinstance(viber_request, ViberFailedRequest):
        pass
        # logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return Response(content = "Success",status_code=200)


