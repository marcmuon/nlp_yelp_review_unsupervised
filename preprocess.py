import pickle
import pandas as pd

def restaurant_filter(biz_df):
    """Extract only Restaurants from Business list using bool mask"""
    mask = biz_df['categories'].str.contains('Restaurants', na=False)
    return biz_df[mask]

def merge_df(df1, df2, join_key):
    """Merge Two DFs on same key, like SQL inner join"""
    return df1.merge(df2, left_on=join_key, right_on=join_key, how='inner')

def binarize_stars(df):
    """Convert 5-star system to pos/neg only, remove neutral"""
    df = df.loc[df['stars'] != 3.0]
    df['sentiment'] = df['stars'].transform(lambda x: 1 if x >= 4 else 0)
    df = df.drop(columns=['stars'])
    return df

def clean_outlier_text(df):
    """Filter for roughly within the 'box' of IQR range on text length"""
    mask = (df['text'].str.len() > 50) & (df['text'].str.len() < 200)
    return df.loc[mask]

def true_counts(df):
    """Calculate counts per business based of newly filtered data"""
    df['counts'] = df.groupby(['business_id'])['text'].transform('count')
    df = df.drop(columns=['review_count'])
    return df

def quantile_filter(df, q=.25):
    """Filter reviews where business has > qth percentile of review counts"""
    return df[df['counts'] > df['counts'].quantile(.25)]

def train_test_df(df):
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    train_df = df[df['year'].astype(int) == 2016]
    test_df = df[df['year'].astype(int) == 2017]
    return train_df, test_df

if __name__ == '__main__':

    with open('mongo-load/biz_df.pkl', 'rb') as f:
        biz_df = pickle.load(f)
    with open('mongo-load/review_df.pkl', 'rb') as f:
        review_df = pickle.load(f)
    
    biz_df = restaurant_filter(biz_df)
    merged = merge_df(biz_df, review_df, join_key='business_id')
    biz_df, review_df = None, None  # RAM usage considerations
    merged = binarize_stars(merged)
    merged = clean_outlier_text(merged)
    merged = true_counts(merged)
    merged = quantile_filter(merged)
    train_df, test_df = train_test_df(merged)

    with open('data/train_df.pkl', 'wb') as f:
        pickle.dump(train_df, f)
    with open('data/test_df.pkl', 'wb') as f:
        pickle.dump(test_df, f)