from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn import tree

'''
MODELO DE MACHINE LEARNING, PARA MAS INFO LEER DOCUMENTACION
https://github.com/Lilsup99/indice_esperanza_vida/blob/main/Modelo%20ML/README4ML.md
'''

data = pd.read_csv('LBmodel\Lb_data.csv')

X = data[['Life expectancy at birth, total (years)',
          'Population growth (annual %)', 'School enrollment, tertiary (% gross)',
          'Internet Users(%)', 'GDP per capita (current US$)',
          'Inflation, consumer prices (annual %)']]
Y = data['Y']

X = np.array(X)
Y = np.array(Y)

lb_model = tree.DecisionTreeClassifier(max_depth=3)
lb_model = lb_model.fit(X,Y)

# Create your views here.

def model(request):
    pred = None
    life_expectancy = None
    population_growth = None
    school_enrollment = None
    internet_users = None
    gdp = None
    inflation = None
    pais = None
    year = None

    if request.method == 'POST':
        pais = str(request.POST['pais'])
        try:
            data1 = data[data['country'] == pais.capitalize()].sort_values('year', ascending=False)
            year = data1['year'].iloc[0]
            data1 = np.array(data1[['Life expectancy at birth, total (years)','Population growth (annual %)',
                                'School enrollment, tertiary (% gross)','Internet Users(%)','GDP per capita (current US$)',
                                "Inflation, consumer prices (annual %)"]].iloc[0])

            life_expectancy = float(data1[0])
            population_growth = float(data1[1])
            school_enrollment = float(data1[2])
            internet_users = float(data1[3])
            gdp = float(data1[4])
            inflation = float(data1[5])


            pred = lb_model.predict(data1.reshape(1,-1))
            pred = int(pred)

            return render(request, 'model.html',{'pred':pred, 
                                            'life_expectancy': life_expectancy,
                                            'population_growth':population_growth,
                                            'school_enrollment':school_enrollment,
                                            'internet_users':internet_users,
                                            'gdp':gdp,
                                            'inflation':inflation,
                                            'pais': pais,
                                            'year':year})
        except:
            pais = f'no se encontraron datos de: {pais}'        
        
    return render(request, 'model.html',{'pred':pred, 
                                        'life_expectancy': life_expectancy,
                                        'population_growth':population_growth,
                                        'school_enrollment':school_enrollment,
                                        'internet_users':internet_users,
                                        'gdp':gdp,
                                        'inflation':inflation,
                                        'pais': pais,
                                        'year':year})
