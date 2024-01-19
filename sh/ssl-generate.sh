#! /bin/bash

# cd ~/ngrok/
url="0.0.0.0:8080"
openssl genrsa -out base.key 2048
openssl req -new -x509 -nodes -key base.key -days 10000 -subj "/CN=$url" -out base.pem
openssl genrsa -out server.key 2048
openssl req -new -key server.key -subj "/CN=$url" -out server.csr
openssl x509 -req -in server.csr -CA base.pem -CAkey base.key -CAcreateserial -days 10000 -out server.crt


# cp base.pem assets/client/tls/ngrokroot.crt
# make release-server release-client
# chmod +x ngrokd
# chmod +x ngrok
# ./ngrokd -tlsKey=server.key -tlsCrt=server.crt -domain="tunel.chatbot-p.ru" -httpAddr=":8080" -httpsAddr=":8081"
#
# touch chatbot-server.cfg
# "server_addr: tunel.chatbot-p.ru:4443" >> chatbot-server.cfg
# "trust_host_root_certs: false" >> chatbot-server.cfg
#
