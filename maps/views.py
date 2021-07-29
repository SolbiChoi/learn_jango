from django.shortcuts import render
import pandas as pd
import numpy as np
import collections

# Create your views here.
import folium
def home(request):
    mf = folium.Map([35.3369, 127.7306], zoom_start=10)
    mf = mf._repr_html_()
    first = 'Solbi'
    result = {'mapfolium': mf, 'f01':first}
    return render(request, template_name='maps/home.html', context= result)

def plotly(request):
    xArray = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
    yArray = [7, 8, 8, 9, 9, 9, 10, 11, 14, 14, 15]
    result = {'x_array':xArray, 'y_array':yArray}

    xArray02 = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
    yArray02 = [19, 14, 13, 9, 9, 9, 10, 11, 14, 14, 15]
    result['x_array02'] = xArray02
    result['y_array02'] = yArray02

    return render(request, template_name='maps/plotly.html', context=result)

def piegraph(request):
    df = pd.read_excel('./gp_f_Australia.xls', header=None)
    counts = collections.Counter(df[2])
    dict = {'Life': ['Food and Drink (Applications)', 'Health and Fitness (Applications)', 'Lifestyle (Applications)',
                     'Weather (Applications)', 'Medical (Applications)', 'Navigation (Applications)',
                     'Finance (Applications)'],
            'Leisure': ['Entertainment (Applications)', 'Shopping (Applications)', 'Social Networking (Applications)',
                        'Sports (Applications)', 'Travel (Applications)', 'Music (Applications)',
                        'Photo and Video (Applications)'],
            'Work': ['Business (Applications)', 'Developer Tools (Applications)', 'Graphics & Design (Applications)',
                     'Productivity (Applications)'],
            'Edu': ['Books (Applications)', 'Catalogs (Applications)', 'Education (Applications)',
                    'Reference (Applications)', ' Magazines and Newspapers (Applications)', 'News (Applications)',
                    'Utilities (Applications)'],
            'Games': ['Arcade (Games)', 'Action (Games)', 'Adventure (Games)', 'Strategy (Games)', 'Sports (Games)'
                , 'Board (Games)', 'Role Playing (Games)', 'Simulation (Games)', 'Puzzle (Games)', 'Card (Games)'
                , 'Educational (Games)', 'Music (Games)', 'Racing (Games)', 'Trivia (Games)', 'Casual (Games)']}

    set_group = ['Life', 'Leisure', 'Work', 'Edu', 'Games']
    Kids = counts.get('Kids')
    if Kids == None:
        Kids = 0

    count_group = []
    group = []
    sum = 0

    for group in set_group:  # group : key = Life
        name = dict[group]
        group = dict[group]  # dict['Life']
        for category in group:  # Food and Drink (Applications)
            for key, value in counts.items():
                if key == category:
                    sum = value + sum
        count_group.append(sum)
        sum = 0
    # set_group = {x: y for x, y in zip(set_group, count_group)}
    labels = ['Life', 'Leisure', 'Work', 'Edu', 'Games', 'Kids']
    sizes = [set_group.get('Life'), set_group.get('Leisure'), set_group.get('Work'), set_group.get('Edu'),
             set_group.get('Games'), Kids]

    xArray = labels
    yArray = sizes
    result = {'x_array': xArray, 'y_array': yArray}

    return render(request, template_name='maps/piegraph.html', context=result)

def stacked(request):
    
    return render(request, template_name='maps/piegraph.html', context=result)