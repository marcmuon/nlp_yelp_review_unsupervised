import pickle
import pandas as pd

def restaurant_filter(biz_df):
    """Extract only Restaurants from Business list using bool mask"""
    mask = biz_df['categories'].str.contains('Restaurants', na=False)
    return biz_df[mask]

def merge_df(df1, df2, join_key):
    return df1.merge(df2, left_on=join_key, right_on=join_key, how='inner')

if __name__ == '__main__':

    with open('mongo-load/biz_df.pkl', 'rb') as f:
        biz_df = pickle.load(f)
    with open('mongo-load/review_df.pkl', 'rb') as f:
        review_df = pickle.load(f)
    
    biz_df = restaurant_filter(biz_df)
    merged = merge_df(biz_df, review_df, join_key='business_id')
    biz_df, review_df = None, None  # RAM usage considerations