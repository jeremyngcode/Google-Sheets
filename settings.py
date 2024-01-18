from os import environ
from dotenv import load_dotenv
# -------------------------------------------------------------------------------------------------

load_dotenv()

# API / Secret keys here (optional)
MONKEY_API_KEY = environ.get('MONKEY_API_KEY')
GHOST_SECRET_KEY = environ.get('GHOST_SECRET_KEY')

# Google service account credentials path
GOOGLE_CREDS_PATH = environ.get('GOOGLE_CREDS_PATH')

# Spreadsheet(s)
SPREADSHEET_ID = 'sCaRY-purPLE-GHost-123-abc'
sheet_tabs = ('PRICES', 'REVENUE', 'POTATOES')
