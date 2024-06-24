import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_trainig = st.beta_container()

with header:
    st.title('Welcome')
    st.text('This is the Dashboard of the italian vaccine Campaign')

with dataset:
    st.header('Dataset')
    st.text('The dateset include the total of the applied vaccines')
   
    data_graph = pd.read_csv('data/graph.csv', sep=';')
    st.write(data_graph.head())
    
    st.subheader('Total of Doses by Supplier')
    doses = pd.DataFrame(data_graph.groupby(["supplier"])["first_dose","second_dose"].sum()).head()
    st.bar_chart(doses)
    
    st.subheader('Total of Doses by Region')
    regions = pd.DataFrame(data_graph.groupby(["region_name"])["Total_doses"].sum()).head()
    st.bar_chart(data=regions)
        
    st.sidebar.subheader('Choose the Best combination between date and age range for you')
    st.subheader('Combination between date and age range for you')
    
    data_graph['administration_date'] = pd.to_datetime(data_graph['administration_date']).dt.strftime('%Y-%m-%d')
    start_date = pd.Timestamp(st.sidebar.date_input('Start date', datetime.date(2020,12,27), min_value=datetime.date(2020,12,27), max_value=datetime.date(2021,5,19)))
    end_date = pd.Timestamp(st.sidebar.date_input('End date', datetime.date(2021,5,25), min_value=datetime.date(2021,5,25), max_value=datetime.date(2021,5,20)))
    data_graph = data_graph.loc[(data_graph['administration_date']>= start_date) & (data_graph['administration_date']<= end_date),:]
    
    age_options = data_graph['age_range'].unique().tolist()
    #def vis(filter_data,list_countries,dt_choice_normal, dt_choice_cases, start_date, end_date,df_pop):
        #filter_data['Date'] = pd.to_datetime(filter_data['Date'], format='%m/%d/%y')
        #filter_data = filter_data.loc[(filter_data['Date'] >= start_date) & (filter_data['Date'] <= end_date),:]
    date_options = data_graph['administration_date'].unique().tolist()
    
    start_date = pd.Timestamp(st.sidebar.date_input('Start date', datetime.date(2020,12,27), min_value=datetime.date(2020,12,27), max_value=datetime.date(2021,5,19)))
    age = st.sidebar.multiselect("Which Age Range would you like to see", age_options, ['80-89'])
    
    data_graph = data_graph[data_graph['age_range'].isin(age)]
    data_graph = data_graph[data_graph['administration_date']]
    
    fig2 = px.bar(data_graph,x="age_range",y="Total_doses",color="age_range", range_y=[0,35000])
    
    fig2.update_layout(width=800)
    
    st.write(fig2)
    
    st.sidebar.subheader('Choose the Best combination between supplier and age range for you')
    st.subheader('Combination between supplier and age range for you')
      
    supplier_options = data_graph['supplier'].unique().tolist()
    age_option2 = data_graph['age_range'].unique().tolist()
    
    age2 = st.sidebar.multiselect("Which Age Range would you like to see", age_option2, ['80-89'])
    suppliers = st.sidebar.selectbox("Which supplier would you like to see", supplier_options,1)
    
    data_graph = data_graph[data_graph['age_range'].isin(age2)]
    data_graph = data_graph[data_graph['supplier']==suppliers]
    
    fig3 = px.bar(data_graph,x="age_range",y="Total_doses",color="age_range", range_y=[0,35000])
    
    fig3.update_layout(width=800)
    
    st.write(fig3)
    
    
    
    