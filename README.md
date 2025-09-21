
<div align="center">
<h1>🛋️ divanchi</h1>
<img height="20" alt="Python 3.11+" src="https://img.shields.io/badge/python-3.11+-blue">
<img height="20" alt="License Apache 2.0" src="https://img.shields.io/badge/license-Apache%202.0-green">
<img height="20" alt="Status" src="https://img.shields.io/badge/status-pet--project-orange">
</div>

**divanchi** — это telegram-бот для дистанционного управления пк
> сидишь на диванчике и управляешь своим пк (─‿‿─)

---

## **📂 структура проекта**

```bash
divanchi/
│
├── divanchi/
│   ├── handlers/
│   │   ├── start.py
│   │   ├── system.py
│   │   ├── mouse.py
│   │   ├── keyboard.py
│   │   └── screenshot.py
│   ├── __init__.py
│   ├── app.py
│   └── config.py
│
├── divanchi.py # --- entrypoint ---
│
├── .env
│
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

---

## **🚀 установка**

```bash
git clone https://github.com/username/divanchi.git
cd divanchi
pip install -r requirements.txt
```

---

## **🤖 настройка бота**
- создай бота при помощи [@BotFather](https://telegram.me/BotFather)
- укажи Bot name и Bot username
- cкопируй API ключ и вставь его в [.env](/.env)

## [.env](/.env)
```dotenv
TOKEN="ТВОЙ_ТОКЕН_БОТА"
```

---

## **🧩 зависимости**
[requirements.txt](/requirements.txt)
```bash
# --- telegram ---
pyTelegramBotAPI==4.29.1
aiohttp==3.12.15

# --- config ---
environs==14.3.0

# --- pc control ---
PyAutoGUI==0.9.54
PyScreeze==1.0.1
pillow==11.3.0
```

