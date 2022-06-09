import telegram
import elasticsearch
import json


## TELEGRAM API TOKEN CONFIGURATION

TOKEN=""
bot = telegram.Bot(TOKEN)


## RUNNER MODES

elastic= True
telegram= True


# MAIN ADMIN CHAT ID
chat_id={}

chat_id["admin"]=-744610713

## ELASTIC SEARCH CONFIG

def elkpush(indexdat,jsondat):
        
    #context = create_default_context(cafile="/etc/elasticsearch/certs/ca.pem")
    es = elasticsearch.Elasticsearch("https://ip:9200",verify_certs=False, http_auth=('elastic', ''))
    print(es.index(index=indexdat,doc_type="security_report", body=json.dumps(jsondat)))


