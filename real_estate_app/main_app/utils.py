import pickle
import pandas as pd

def make_prediction(input:dict)->float:
    model = pickle.load(open('main_app/static/models/finalized_model.pkl', 'rb'))
    try:
        pred = int(model.predict(pd.DataFrame(input, index=[0])))
    except:
        pred = 0
    return pred