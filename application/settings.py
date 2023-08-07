import os

from dotenv import load_dotenv

load_dotenv()

POSTGRESHOST = os.getenv('POSTGRESHOST')
POSTGRESDB = os.getenv('POSTGRESDB')
POSTGRESUSERNAME = os.getenv('POSTGRESUSERNAME')
POSTGRESPASSWORD = os.getenv('POSTGRESPASSWORD')
#
REDISHOST = os.getenv('REDISHOST')
