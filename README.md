# Wikipedia bot
Telegam bot for search and read articles in Instant View mode.
http://t.me/WikipediaTelegraphBot

## Setup & run bot 

### Setup
```bash
apt install mongodb
pip3 install -r requirements.txt
```
Create `config.py`:
```python
BOT_TOKEN = ''
TELEGRAPH_TOKEN = ''

WEBHOOK_HOST = '' # your ip adress
WEBHOOK_PORT = 88  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr

WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Path to the ssl private key

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (bot_token)
```

Quick'n'dirty SSL certificate generation:

```bash
openssl genrsa -out webhook_pkey.pem 2048`
openssl req -new -x509 -days 3650 -key webhook_pkey.pem -out webhook_cert.pem
```

When asked for "Common Name (e.g. server FQDN or YOUR name)" you should reply
with the same value in you put in WEBHOOK_HOST

### Run
```bash
python3 bot_handlers.py #for development and tests
```

```bash
python3 wikipedia_server.py #for prod
```
