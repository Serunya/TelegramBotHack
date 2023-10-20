import os
import sys
def start_bot(token):
    print("hello")
    while(True):
        pass


token = os.environ.get('tg_token')

if token:
    start_bot(token)
else:
    sys.stderr.write("token not found")