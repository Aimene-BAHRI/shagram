## Setup

First clone this repository and install your requirements
```shell
git clone https://github.com/Aimene-BAHRI/shagram && cd shagram

pip install -r requirements.txt
```

Then create a python file called `config_secrets.py` under `shagram/` alongside `settings.py`

```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#TODO Change this
EMAIL_HOST_USER = 'GMAIL ADDRESS'
EMAIL_HOST_PASSWORD = 'GMAIL APPLICATION CODE'
```
