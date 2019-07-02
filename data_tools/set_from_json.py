import firebase_client_wrapper as fcw
import uuid

import json
import sys

if (len(sys.argv) != 4):
    print ("Usage python set_from_json.py crypto_token data_type path_to_json_file")
    exit(1)

CRYPTO_TOKEN_PATH = sys.argv[1]
fcw.init_client(CRYPTO_TOKEN_PATH)

DATA_TYPE = sys.argv[2]
PATH_TO_JSON = sys.argv[3]

SUPPORTED_DATA_TYPES = ['conversations']
if DATA_TYPE not in SUPPORTED_DATA_TYPES:
    print (f"data_type must be one of {SUPPORTED_DATA_TYPES}")
    exit(1)

print(DATA_TYPE)

with open(PATH_TO_JSON, 'r') as json_file:
    conversation_map = json.load(json_file)
    fcw.set_conversations(conversation_map)
print ("done")
