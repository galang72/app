import os
from dotenv import load_dotenv
from app import create_app

load_dotenv()  # ← tambahkan ini agar .env terbaca

config_name = os.getenv('FLASK_CONFIG', 'development')
print("DEBUG CONFIG_NAME =", config_name)

app = create_app(config_name)

if __name__ == '__main__':
    app.run()