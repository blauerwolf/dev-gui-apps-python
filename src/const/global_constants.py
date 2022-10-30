import os
from os.path import join, dirname, abspath
from dotenv import load_dotenv

dotenv_path = join(dirname(abspath('.env')), '.env')
load_dotenv(dotenv_path=dotenv_path)


postgresql = {
    'pguser': os.environ.get("DB_USERNAME"),
    'pgpasswd': os.environ.get("DB_PASSWORD"),
    'pghost': 'localhost',
    'pgport': 5432,
    'pgdb': 'pygui'
}

