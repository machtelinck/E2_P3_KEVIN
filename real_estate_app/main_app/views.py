from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('main_app/static/models/finalized_model.pkl', 'rb'))


def index(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        X_predict = {}
        for var in ['Year_Built', 'Total_Bsmt_SF', '1st_Flr_SF', 'Gr_Liv_Area','Garage_Area', 'Overall_Qual', 'Full_Bath', 'Exter_Qual',
                  'Kitchen_Qual', 'Neighborhood']:
            if var in ['Exter_Qual','Kitchen_Qual', 'Neighborhood']:
                X_predict[var]= request.POST.get(var)
            else:
                X_predict[var]= int(request.POST.get(var))
        print(X_predict)
        pred = model.predict(pd.DataFrame(X_predict, index=[0]))

        return render(request, 'index.html', {'data': int(pred)})
    else:
        return HttpResponse("Method Not Allowed")