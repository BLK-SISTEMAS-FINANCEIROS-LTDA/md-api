import grpc
import requests as rq
import json

import common_pb2
import quote_pb2
import services_pb2_grpc
import services_pb2

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':

    usuario = "user"
    senha = "password"
    client_id = "blk-api-client"
    client_secret = "acdfd8f5-2803-451e-9b9c-5bb55e98b06e"
    grant_type = "password"
    aud = "BLK-API"

    print(usuario, senha, client_id, client_secret, grant_type, aud)

    payload = {"username": usuario,
               "password": senha,
               "client_id": client_id,
               "client_secret": client_secret,
               "grant_type": "password",
               "aud": "BLK-API"}

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    urlauth = 'https://autenticacao.blk.com.br/auth/realms/BLK-API/protocol/openid-connect/token'

    token = rq.post(urlauth, headers=headers, data=payload)
    token = json.loads(token.text)['access_token']

    auth_token = [('authorization', 'bearer ' + token)]

    print(auth_token)

    maxMsgLength = 1024 ** 3
    channel = grpc.insecure_channel("autenticacao.blk.com.br:9000",
                                    options=[('grpc.max_message_length', maxMsgLength),
                                             ('grpc.max_send_message_length', maxMsgLength),
                                             ('grpc.max_receive_message_length', maxMsgLength)])

    quote = services_pb2_grpc.QuotesSvcStub(channel)
    rr = common_pb2.SecuritySymbolOrId(symbol='petr4')

    c = 0
    for f in quote.GetQuoteStream(rr, metadata=auth_token):
        print(f)
        print("###############################", " Update: " + str(c), "###############################")
        c += 1
        if c > 10000:
            break
