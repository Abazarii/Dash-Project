import pathlib, dash
import preprocess, viz1_line_chart, viz2_bar_chart, viz4_box_chart, viz7_area_chart, viz3_bar_chart
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import dcc
from dash.dependencies import Input, Output
import pandas as pd

# Define Path to get the datas
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

# Get the data
oltc_data = pd.read_csv(DATA_PATH.joinpath("OLTCresults.csv"))

# Preprocess the data
data = preprocess.convert_dates(oltc_data)
data = preprocess.drop_irrelevant_time(data)

# Plot line chart - Viz 1
fig_viz1 = viz1_line_chart.plot_line_chart(data, selected_range = 0)

# Plot bar chart for viz 2
fig_viz2 = viz2_bar_chart.BarChart(data, 2)
fig_viz2.update_layout(height = 600, width = 1000)
fig_viz2.update_layout(dragmode = False)

# Plot for box chart - Viz 3
data1 = preprocess.drop_irrelevant_time(oltc_data)
data2 =  preprocess.adjust_data_for_viz3(data1)
fig_viz3 = viz3_bar_chart.bar_plot_animation_Max_PowerLoss(data2)

# Plot for box chart - Viz 4
fig_viz4=viz4_box_chart.plot_box_chart(data,2020)
fig_viz4.update_layout(height=600, width=1000)
fig_viz4.update_layout(dragmode=False)

# Plot for area chart - Viz 7
df = preprocess.adjust_data_for_viz7(oltc_data)
fig_viz7 = viz7_area_chart.area_plot_Power_Loss(df)


# The page 2 layout
layout = html.Div(children=[
        html.Div([
            html.H3('Tap Changer Performance',style={'textAlign':'center'}),
            html.Hr(style={'borderWidth': "0.3vh", "width": "25%", "color": "balck",'margin-left': "auto",'margin-right': "auto"}),
            
            # Display the visualization 1
            html.H5('Tap Switching Pattern'),
            html.Label('Use slider below to change the duration'),
            html.Div([dcc.Slider(0,3,step=None,id='slider-duration-viz1',value=0,marks={
                                                          0: {'label': 'Past Week'},
                                                          1: {'label': 'Past Two Weeks'},
                                                          2: {'label': 'Past Three Weeks'},
                                                          3: {'label': 'Past_Month'}})],style={"width": "100%"}),
            dcc.Graph(id='tap-switch',figure=fig_viz1),
            
            # Display the visualization 2
            html.Hr(style={'borderWidth': "0.3vh", "width": "75%", "color": "balck",'margin-left': "auto",'margin-right': "auto"}),
            html.H5('The frequency of tap changing over time'),
            html.Label('Use the slider to Change the timeframe of plot below:'),
            dcc.Slider(
                        0,
                        2,
                        step=None,
                        id='slider-duration-viz2',
                        value=2,
                        marks={
                            0: {'label': 'Last 7-days'},
                            1: {'label': 'Last 30-days'},
                            2: {'label': 'All-Time'}}),
            dcc.Graph(id='barchart',figure = fig_viz2),
            
            # Display the visualization 3
            html.Hr(style={'borderWidth': "0.3vh", "width": "75%", "color": "balck",'margin-left': "auto",'margin-right': "auto"}),
            html.H5('The power loss through heat during tap change'),
            dcc.Graph(figure = fig_viz3),

            # Display the visualization 4
            html.Hr(style={'borderWidth': "0.3vh", "width": "75%", "color": "balck",'margin-left': "auto",'margin-right': "auto"}),
            html.H5('Variation of tap operation time'),
            html.Label('Use slider below to change the year'),
            dcc.Slider(
                2015,
                2020,
                step = None,
                id = 'sliderYear',
                value = 2020,
                marks = {str(year): str(year) for year in [2015,2016,2017,2018,2019,2020]},),
            dcc.Graph(id = 'box_chart',figure = fig_viz4),

            # Display the visualization 7
            html.Hr(style={'borderWidth': "0.3vh", "width": "75%", "color": "balck",'margin-left': "auto",'margin-right': "auto"}),         
            html.H5("Tap changers stress vary throughout several time periods"),
            dcc.Dropdown(
                        id = 'choice',
                        options = ['Energy Loss','Power Loss'],
                        value = 'Power Loss',
                        clearable = True,
                        style={'borderWidth': "0.3vh", "width": "40%", "color": "balck"}),
            dcc.Graph(id='areagraph',figure = fig_viz7),
            
        ]),
],style={'padding': 10, 'flex': 1})


# Callback for viz2
@dash.callback(
    Output('barchart', 'figure'),
    [Input('slider-duration-viz2', 'value')])

def update_viz2(value):
    fig_viz2 = viz2_bar_chart.BarChart(data,value)
    
    return fig_viz2

# Callback for viz4
@dash.callback(
    Output('box_chart', 'figure'),
    [Input('sliderYear', 'value')])

def update_viz4(value):
    fig_viz4 = viz4_box_chart.plot_box_chart(data,value)
    
    return fig_viz4


# Callback for viz 1
@dash.callback(
    Output('tap-switch', 'figure'),
    [Input('slider-duration-viz1', 'value')])

def update_viz(value):
    fig_viz1 = viz1_line_chart.plot_line_chart(data, selected_range = value)
    return fig_viz1


# Callback for viz 7
@dash.callback(
    Output('areagraph', 'figure'),
    [Input('choice', 'value')])

def update_viz7(value):
    if value=='Power Loss':
        fig_viz7 = viz7_area_chart.area_plot_Power_Loss(df)
    else : fig_viz7 = viz7_area_chart.area_plot_Energy_Loss(df)
    return fig_viz7