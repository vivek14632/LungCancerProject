import sklearn

def get_train_test_data(np_matrix):
    df = pd.DataFrame(np_matrix)
    from sklearn.model_selection import train_test_split
    train, test = train_test_split(df, test_size = 0.2)
    return train,test
