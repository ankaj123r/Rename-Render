# Don't Remove Credit @shadow_blank
# Subscribe YouTube Channel For Amazing Bot @shadow_blank
# Ask Doubt on telegram @shadow_blank


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24171111")

API_HASH = os.environ.get("API_HASH", "c850cb56b64b6c3b10ade9c28ef7966a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7153070490:AAG8ZXalF7LPiYWChEbJNLm16zLweQUbFUg") 

FORCE_SUB = os.environ.get("FORCE_SUB", "autorenamethumbnailbot") 

             # Don't Remove Credit @shadow_blank
             # Subscribe YouTube Channel For Amazing Bot @shadow_blank
             # Ask Doubt on telegram @shadow_blank

DB_NAME = os.environ.get("DB_NAME", "renamebot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://pankaj1123r:DeFV9aOdch29rLVvPIDD@cluster0.y53pq4k.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1335306418').split()]

PORT = os.environ.get("PORT", "8080")