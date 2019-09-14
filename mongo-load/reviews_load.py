from pymongo import MongoClient
import pandas as pd
import numpy as np
import pickle

client = MongoClient()
db = client.yelp  #  assumes db name in mongo is 'yelp'
reviews = list(
    db.review.find({}, {
        '_id':0, 'business_id': 1, 'stars': 1, 'text': 1, 'date': 1    
    })
)
review_df = pd.DataFrame(list(reviews))
with open('review_df.pkl', 'wb') as f:
    pickle.dump(review_df, f)
client.close()