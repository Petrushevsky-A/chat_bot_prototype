#! /bin/bash

# launch option ASGI server
source ../venv/bin/activate
cd ../
uvicorn src.viber_bot.app:app --root-path ../. --reload --host 0.0.0.0 --port 8080 --ssl-keyfile ./sh/server.key --ssl-certfile ./sh/server-r.crt
# uvicorn src.viber_bot.app:app --root-path ../. --reload --host 0.0.0.0 --port 8080
# uvicorn src.viber_bot.app:app --root-path ../. --host 0.0.0.0 --port 8080

# alternative launch option ASGI server
# python ../src/viber_bot/launcher_asgi.py 

