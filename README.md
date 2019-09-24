# LDA Topic Models as Supervised Classification Inputs


## The Data

This experiment uses Yelp's publicly available restaurant review data (6,685,900 reviews across 192,609 businesses).

I've written instructions for setting up your own DB and loading Yelp data below. However, the pre-processing output from ```preprocess.py``` was compact enough that I could include the ```train_df.pkl``` and ```test_df.pkl``` files in the ```/data``` directory. Thus you can skip the DB setup sections below and just use those if desired, then explore the LDA experiment using Notebooks #2 (train corpus) and #3 (test corpus).


### Download JSON and Setup Mongo
1. Yelp data is in raw JSON here: https://www.yelp.com/dataset
2. Install Mongo locally if needed via instructions here: https://docs.mongodb.com/manual/tutorial/

### Mongo Creation
1. You'll need to start mongo as a foreground service. Generally this can be done via ```mongod --config /usr/local/etc/mongod.conf```, but if you installed Mongo via Brew on Mac you can alternatively use: ```brew services start mongodb```
2. From directory where you extracted Yelp JSON, run the following commands: ```mongoimport --db yelp --collection review review.json``` and ```mongoimport --db yelp --collection business business.json```. Those are the only two portions of the Yelp dataset I used for this experiment.

### Mongo Load Script
I've created two helper scripts to load data from Mongo and Pickle into DataFrame objects. If you want to follow along with the LDA experiments and fork your own, just run the following 2 scripts from terminal. Assuming you're in the ```mongo_load``` directory of this repo:

1. ```python business_load.py```
2. ```python reviews_load.py```

That will create two pickle ```.pkl``` dataframe objects within the ```mongo_load``` directory, and we'll use those as a basis for the rest of the project. They're filtered to a specific subset of columns.

### Mongo Load Script - Alternate

In lieu of using the two helper scripts above, you could likely just use the pandas ```read_json``` function outlined here to create the DataFrames: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html.

However, I haven't tested that, and if you're an experienced Mongo user there's likely more flexibility in just running your own DB for this data.




