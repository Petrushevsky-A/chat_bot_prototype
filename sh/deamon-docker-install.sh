#! /bin/bash

docker run -d --name=Chat-Bot --shm-size=2g -p 1521:1521 -p 8080:8080 
mv chat-bot.service /etc/systemd/system/chat-bot.service
sudo systemctl enable Chat-Bot.service

