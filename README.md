# Wikipedia bot
Telegam bot for search and read articles in Instant View mode.
http://t.me/WikipediaTelegraphBot

## Run 
```
#!bash
apt install mongodb
pip3 install -r requirements.txt
```
Create `config.py`
```
#!bash
python3 bot_handlers.py #for development and tests
```

```
#!bash
python3 wikipedia_server.py #for prod
```
