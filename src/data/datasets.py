import pandas as pd


class Dataset:
    def __init__(self,
                 train_path="data/raw/train.csv",
                 test_path="data/raw/test.csv",
                 merch_path="data/raw/merchants.csv",
                 new_merch_path="data/raw/new_merchant_transactions.csv",
                 hist_path="data/raw/historical_transactions.csv"):

        self.train = pd.read_csv(train_path)
        self.test = pd.read_csv(test_path)
        self.merchants = pd.read_csv(merch_path)
        self.merchants_transactions = pd.read_csv(new_merch_path)
        self.historical_trans = pd.read_csv(hist_path)
