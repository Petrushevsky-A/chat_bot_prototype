#! /bin/bash

# ngrok http https://0.0.0.0:8080 --host-header=rewrite
ngrok http https://0.0.0.0:8080 --domain chatbot-p.ru --host-header=rewrite  
