import streamlit as st
import pandas as pd
import plotly.express as px

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
    doses = pd.DataFrame(data_graph.groupby(["supplier"])["first_dose","second_dose"].sum()).head(50)
    st.bar_chart(doses)
    
    st.subheader('Total of Doses by Region')
    regions = pd.DataFrame(data_graph.groupby(["region_name"])["Total_doses"].sum()).head(50)
    st.bar_chart(data=regions)
        
    st.subheader('Choose the Best combination between date and age range for you')
    
    data_graph['administration_date'] = pd.to_datetime(data_graph['administration_date']).dt.strftime('%Y-%m-%d')
    
    age_options = data_graph['age_range'].unique().tolist()
    date_options = data_graph['administration_date'].unique().tolist()
    
    date = st.selectbox("Which date would you like to see", date_options,100)
    age = st.multiselect("Which Age Range would you like to see", age_options, ['80-89'])
    
    data_graph = data_graph[data_graph['age_range'].isin(age)]
    data_graph = data_graph[data_graph['administration_date']==date]
    
    fig2 = px.bar(data_graph,x="age_range",y="Total_doses",color="age_range", range_y=[0,35000])
    
    fig2.update_layout(width=800)
    
    st.write(fig2)
    
    st.subheader('Choose the Best combination between supplier and age range for you')
    
      
    supplier_options = data_graph['supplier'].unique().tolist()
    age_option = data_graph['age_range'].unique().tolist()
    
    suppliers = st.selectbox("Which supplier would you like to see", supplier_options,1)
    age2 = st.multiselect("Which Age Range would you like to see", age_option, ['80-89'])
    
    data_graph = data_graph[data_graph['age_range'].isin(age2)]
    data_graph = data_graph[data_graph['supplier']==suppliers]
    
    fig3 = px.bar(data_graph,x="age_range",y="Total_doses",color="age_range", range_y=[0,35000])
    
    fig3.update_layout(width=800)
    
    st.write(fig3)
    
    
    
    