import os
import sys
def start_bot(token):
    print(token + "\n Dima lox pishet front2")


token = os.environ.get('tg_token')

if token:
    start_bot(token)
else:
    sys.stderr.write("token not found")