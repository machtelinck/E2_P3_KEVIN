from django.shortcuts import render
from django.http import HttpResponse
from .utils import make_prediction

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
        pred = make_prediction(X_predict)

        if pred != 0:
            return render(request, 'index.html', {'data': int(pred)})
        else:
            return HttpResponse("The Input is not Correct")     
    else:
        return HttpResponse("Method Not Allowed")