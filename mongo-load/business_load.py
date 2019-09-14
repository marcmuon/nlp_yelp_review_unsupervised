from pymongo import MongoClient
import pandas as pd
import numpy as np
import pickle

client = MongoClient()
db = client.yelp  #  assumes db name in mongo is 'yelp'
biz = list(
    db.business.find(
        {}, {'_id':0, 'business_id': 1, 'review_count': 1, 'categories': 1
    })
)
biz_df = pd.DataFrame(list(biz))
with open('biz_df.pkl', 'wb') as f:
    pickle.dump(biz_df, f)
client.close()