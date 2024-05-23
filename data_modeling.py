import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Analyzing Digital Engagement for FunOlympicGames 2024", page_icon=":first_place_medal:",layout="wide")

st.markdown("<h1 style='text-align: center;'>🥇ANALYZING DIGITAL ENGAGEMENT FOR FUNOLYMPIC GAMES 2024</h1>", unsafe_allow_html=True)
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

#st.title(" :first_place_medal:ANALYZING DIGITAL ENGAGEMENT FOR FUNOLYMPIC GAMES 2024")
#st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

#fl = st.file_uploader(":file_folder: Upload a file",type=(["csv","txt","xlsx","xls"]))
#if fl is not None:
#    filename = fl.name
#    st.write(filename)
#    df = pd.read_csv(filename, encoding = "ISO-8859-1")
#else:
#    os.chdir(r"C:\Users\BIDA20-076\Desktop\star")
#    df = pd.read_csv("updated_csv_file.csv", encoding = "ISO-8859-1")

import requests
import pandas as pd
import streamlit as st
import base64
import datetime
import random

# Function to fetch real web server logs from an API
def fetch_real_web_server_logs(num_logs):
    api_endpoint = "https://my.api.mockaroo.com/olympics?key=5adf4f80"
    response = requests.get(api_endpoint)
    if response.status_code == 200:
        logs_json = response.json()
        logs = []
        for log_entry in logs_json[:num_logs]:
            logs.append([
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                log_entry.get("IP Address", ""),
                log_entry.get("Country", ""),
                log_entry.get("Referrer", ""),
                log_entry.get("Sport Category", ""),
                log_entry.get("Time Visits", ""),
                log_entry.get("Time Spent", ""),
                log_entry.get("Website Visit", ""),
                log_entry.get("Status Code", ""),
                log_entry.get("User Agent", ""),
                log_entry.get("Requested Url", "")
            ])
        return logs
    else:
        st.error("Failed to fetch web server logs from the API.")
        return None

# Function to generate dummy web server logs
def generate_web_server_logs(num_logs):
    logs = []
    for _ in range(num_logs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip_address = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        countries = ["USA", "UK", "Canada", "Germany"]
        country = random.choice(countries)
        referrers = ["Google", "Bing", "Yahoo", "Direct"]
        referrer = random.choice(referrers)
        sport_categories = ["Football", "Basketball", "Tennis", "Swimming"]
        sport_category = random.choice(sport_categories)
        time_visits = random.randint(1, 10)
        time_spent = random.randint(10, 600)
        website_visits = random.randint(1, 100)
        status_codes = [200, 304]
        status_code = random.choice(status_codes)
        user_agents = ["Chrome", "Firefox", "Safari", "Edge"]
        user_agent = random.choice(user_agents)
        requested_urls = ["/index.html", "/images/games.jpg", "/searchsports.php", "/football.html"]
        requested_url = random.choice(requested_urls)
        logs.append([
            timestamp, ip_address, country, referrer, sport_category,
            time_visits, time_spent, website_visits, status_code, user_agent, requested_url
        ])
    return logs

# Function to display the log generation form
def display_log_generation_form():
    st.subheader("Generate Web Server Logs")
    num_logs = st.number_input("Number of Logs to Generate", min_value=1, step=1, value=10)
    if st.button("Generate Logs"):
        logs = fetch_real_web_server_logs(num_logs) or generate_web_server_logs(num_logs)
        if logs:
            if "logs_df" not in st.session_state:
                st.session_state.logs_df = pd.DataFrame(columns=[
                    "Time Stamp", "IP Address", "Country", "Referrer", "Sport Category",
                    "Time Visits", "Time Spent", "Website Visit", "Status Code", "User Agent", "Requested Url"
                ])
            st.session_state.logs_df = pd.concat([st.session_state.logs_df, pd.DataFrame(logs, columns=[
                "Time Stamp", "IP Address", "Country", "Referrer", "Sport Category",
                "Time Visits", "Time Spent", "Website Visit", "Status Code", "User Agent", "Requested Url"
            ])], ignore_index=True)
            with st.expander("View Generated Logs"):
                st.dataframe(st.session_state.logs_df)  # Display logs as DataFrame
            # Add download button
            download_link = create_download_link(st.session_state.logs_df.to_csv(index=False), "web_server_logs.csv", "Download Logs")
            st.markdown(download_link, unsafe_allow_html=True)
        else:
            st.error("Failed to generate logs.")
    elif st.session_state.get("logs_df") is not None:  # Check if logs already exist
        with st.expander("View Generated Logs"):
            st.dataframe(st.session_state.logs_df)  # Display logs as DataFrame
        # Add download button
        download_link = create_download_link(st.session_state.logs_df.to_csv(index=False), "web_server_logs.csv", "Download Logs")
        st.markdown(download_link, unsafe_allow_html=True)

# Function to create download link
def create_download_link(data, filename, text):
    b64 = base64.b64encode(data.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

# Main function to display the dashboard
def main():
    display_log_generation_form()

if __name__ == "__main__":
    main()

def process_web_server_logs(log_file):
    log_df = pd.read_csv(log_file)
    return log_df

def main():
    #st.title("Web Server Log Viewer")
    uploaded_file = st.file_uploader(":file_folder: Upload a file",type=(["csv","txt","xlsx","xls"]))
    if uploaded_file is not None:
        log_df = process_web_server_logs(uploaded_file)
        st.write(log_df)
    else:
        #os.chdir(r"C:\Users\BIDA20-076\Desktop\star")
        df = pd.read_csv("updated_csv_file.csv", encoding = "ISO-8859-1")    

if __name__ == "__main__":
    main() 

df = pd.read_csv(r"C:\Users\BIDA20-076\Desktop\star\updated_csv_file.csv", encoding = "ISO-8859-1")       
# Option 1: Drop rows with any missing values
df = df.dropna()
#FRONT BAR

#SIDEBAR
st.sidebar.header("Choose your filter: ")

#col1, col2 = st.columns((2))
df["Time Stamp"] = pd.to_datetime(df["Time Stamp"])
# Getting the min and max date 
startDate = pd.to_datetime(df["Time Stamp"]).min()
endDate = pd.to_datetime(df["Time Stamp"]).max()
#with col1:
date1 = st.sidebar.date_input("Start Date", startDate)
#with col2:
date2 = st.sidebar.date_input("End Date", endDate)
filtered_df = df[(df["Time Stamp"] >= pd.to_datetime(date1)) & (df["Time Stamp"] <= pd.to_datetime(date2))].copy()

# Create for Continent
Continent = st.sidebar.multiselect("Pick your Continent", df["Continent"].unique())
if not Continent:
    df2 = df.copy()
else:
    df2 = df[df["Continent"].isin(Continent)]

# Create for Country
Country = st.sidebar.multiselect("Pick the Country", df2["Country"].unique())
if not Country:
    df3 = df2.copy()
else:
    df3 = df2[df2["Country"].isin(Country)]

# Create for Sport Category
Sport_Category= st.sidebar.multiselect("Pick the Sport Category",df3["Sport Category"].unique())

# Filter the data based on Region, State and City
if not Continent and not Country and not Sport_Category:
    filtered_df = df
elif not Country and not Sport_Category:
    filtered_df = df[df["Continent"].isin(Continent)]
elif not Continent and not Sport_Category:
    filtered_df = df[df["Country"].isin(Country)]
elif Country and Sport_Category:
    filtered_df = df3[df["Country"].isin(Country) & df3["Sport Category"].isin(Sport_Category)]
elif Continent and Sport_Category:
    filtered_df = df3[df["Continent"].isin(Continent) & df3["Sport Category"].isin(Sport_Category)]
elif Continent and Country:
    filtered_df = df3[df["Continent"].isin(Continent) & df3["Country"].isin(Country)]
elif Sport_Category:
    filtered_df = df3[df3["Sport Category"].isin(Sport_Category)]
else:
    filtered_df = df3[df3["Continent"].isin(Continent) & df3["Country"].isin(Country) & df3["Sport Category"].isin(Sport_Category)]

#Viewed_sports_categories= filtered_df.groupby(by = ["Viewed_sports_categories"], as_index = False)["Sales"].sum()
#BAR CHART
#st.title("DATA ANALYSIS & VISUALIZATION")
st.markdown("<h2 class='subtitle'>DATA ANALYSIS & VISUALIZATION</h2>", unsafe_allow_html=True)

def convert_to_hours(Time_Spent):
    if 'minutes' in Time_Spent:
        return float(Time_Spent.split()[0]) / 60
    elif 'hours' in Time_Spent:
        return float(Time_Spent.split()[0])
    elif 'days' in Time_Spent:
        return float(Time_Spent.split()[0]) * 24
    else:
        return None
df['Time Spent (hours)'] = df['Time Spent'].apply(convert_to_hours)        


col1, col2 = st.columns((2))
with col1:
    st.subheader("Website Traffic by Country")
    fig = px.bar(filtered_df,x = "Country", y = "Website Visit",
                 template = "seaborn")
    #st.plotly_chart(fig,use_container_width=True, height = 200)
    st.plotly_chart(fig, use_container_width=True, height=200, style="border: 5px solid white; padding: 20px;")
#PIE CHART
with col2:
    st.subheader("Website Visits by Continent")
    fig = px.pie(filtered_df, values = "Website Visit", names = "Continent", hole = 0.5)
    fig.update_traces(text = filtered_df["Continent"], textposition = "outside")
    st.plotly_chart(fig,use_container_width=True)

cl1, cl2 = st.columns((2))
with cl1:
    with st.expander("Website Traffic by Country Data"):
        country = filtered_df.groupby(by = "Country", as_index = False)["Website Visit"].sum()
        st.write(country.style.background_gradient(cmap="Blues"))
        csv = country.to_csv(index = False).encode('utf-8')
        st.download_button("Download Data", data = csv, file_name = "Website Traffic by Country.csv", mime = "text/csv",
                            help = 'Click here to download the data as a CSV file')

with cl2:
    with st.expander("Website Visits by Continent Data"):
        Continent = filtered_df.groupby(by = "Continent", as_index = False)["Website Visit"].sum()
        st.write(Continent.style.background_gradient(cmap="Oranges"))
        csv = Continent.to_csv(index = False).encode('utf-8')
        st.download_button("Download Data", data = csv, file_name = "Website Visits by Continent.csv", mime = "text/csv",
                        help = 'Click here to download the data as a CSV file')


#TIME SERIES ANALYSIS
#filtered_df = filtered_df.sort_values(by='Time Visits')
# Assuming you have imported Streamlit as st
#st.subheader("Visitor Engagement Over Time")
#line_fig = px.line(filtered_df, x="Time Visits", y="Website Visit", template="seaborn")
#st.plotly_chart(line_fig, use_container_width=True, height=400)
# Allow users to view and download the data
#with st.expander("View Data of Visitor Engagement Over Time:"):
    # Display the DataFrame with style
#    st.write(filtered_df.style.background_gradient(cmap="Blues"))   
# Download button for CSV
#    csv = filtered_df.to_csv(index=False).encode("utf-8")
#    st.download_button('Download Data', data=csv, file_name="Visitor Engagement Over Time.csv", mime='text/csv')

#SCATTER PLOT
filtered_df = filtered_df.sort_values(by='Time Visits')
st.subheader("Visitor Engagement Over Time")
scatter_fig = px.scatter(filtered_df, x="Time Visits", y="Website Visit", template="seaborn")
st.plotly_chart(scatter_fig, use_container_width=True, height=400)
# Allow users to view and download the data
with st.expander("View Data of Visitor Engagement Over Time:"):
    # Display the DataFrame with style
    st.write(filtered_df.style.background_gradient(cmap="Blues"))

#LINE CHART
# Convert 'Time Visits' column to datetime if it's not already
chart1, chart2 = st.columns((2))
with chart1:
    filtered_df['Time Visits'] = pd.to_datetime(filtered_df['Time Visits'])
# Extract the hour of the day from the timestamp
    filtered_df['hour_of_day'] = filtered_df['Time Visits'].dt.hour
    visits_by_hour = filtered_df.groupby('hour_of_day').size().reset_index(name='Visits')
# Create a line chart to visualize the distribution of visits by hour of the day
    st.subheader("Visits Distribution by Hour of Day")
    fig_hour = px.line(visits_by_hour, x='hour_of_day', y='Visits',
              labels={'hour_of_day': 'Hour of Day', 'Visits': 'Number of Visits'})
    st.plotly_chart(fig_hour, use_container_width=True) 


with chart2:
    st.subheader("Time Spent vs Sport Category")
    fig = px.bar(filtered_df,x = "Sport Category", y = "Time Spent (hours)",
                 template = "plotly_dark")
    st.plotly_chart(fig,use_container_width=True, height = 200)


#TREE MAP
# Create a treemap based on country,referrer,sport category, website visit 
st.subheader("Global User Engagement Treemap")
fig3 = px.treemap(filtered_df, path = ["Country","Referrer","Sport Category"], values = "Website Visit",hover_data = ["Website Visit"],
                  color = "Referrer")
fig3.update_layout(width = 800, height = 650)
st.plotly_chart(fig3, use_container_width=True)

#PIE CHART
chart1, chart2 = st.columns((2))
with chart1:
  st.subheader("Popularity of Sport Categories")
  fig = px.pie(df, values='Website Visit', names='Sport Category', template='seaborn')
  st.plotly_chart(fig, use_container_width=True)
  csv = filtered_df.to_csv(index=False).encode("utf-8")
  st.download_button('Download Data', data=csv, file_name="Popularity of Sport Categories.csv", mime='text/csv')  
#PIE CHART
with chart2:
 status_code_counts = df['Status Code'].value_counts()
 st.subheader('Error Analysis')
 fig = px.pie(values=status_code_counts, names=status_code_counts.index, template='plotly')
 st.plotly_chart(fig, use_container_width=True)
# Download button for CSV
 csv = filtered_df.to_csv(index=False).encode("utf-8")
 st.download_button('Download Data', data=csv, file_name="Error Analysis", mime='text/csv')  

#BAR CHART
st.subheader('Top Referrer Websites')
fig = px.bar(filtered_df, x='Referrer', y='Website Visit', template='gridon')
fig.update_traces(text=df['Website Visit'], textposition='inside') 
st.plotly_chart(fig, use_container_width=True)

# Download button for CSV
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button('Download Data', data=csv, file_name="Top Referrer Websites", mime='text/csv')  
#SUMMARY TABLE

#import plotly.figure_factory as ff
#st.subheader("Summary Table")

#with st.expander("Summary_Table"):
#    df_sample = df.head(5)[["Country", "Sport Category", "Time Stamp", "Website Visit", "Status Code"]]
#    fig = ff.create_table(df_sample, colorscale="Cividis")
#    st.plotly_chart(fig, use_container_width=True)

#    st.markdown("Month wise sub-Category Table")
    # Assuming you have a `filtered_df` DataFrame with an "Order Date" column
#    filtered_df = df.copy()  # Creating a copy of df, replace it with your actual filtered DataFrame
#    filtered_df["month"] = pd.to_datetime(filtered_df["Time Stamp"]).dt.month_name()
#    sub_category_Year = pd.pivot_table(data=filtered_df, values="Website Visit", index=["Sport Category"], columns="month", aggfunc='sum', fill_value=0)
#    st.write(sub_category_Year.style.background_gradient(cmap="Blues"))


import streamlit as st
import pandas as pd

def show_summary_tables(dataframe):
    
    # Selecting only the desired columns
    selected_columns = ['Continent', 'Country', 'Referrer', 'Sport Category', 'User Agent','Status Code']
    selected_dataframe = dataframe[selected_columns]
    
    # Basic statistics for numerical columns
    st.write("### Summary Statistics for Categorical Columns:")
    st.write(selected_dataframe.describe().T)
        
# Load the DataFrame
df = pd.read_csv(r"C:\Users\BIDA20-076\Desktop\star\updated_csv_file.csv")

# Display summary tables
show_summary_tables(df)
#######################
# Function to display summary tables
def show_summary_tables(dataframe):
    if 'Time Spent (hours)' not in dataframe.columns:
        dataframe['Time Spent (hours)'] = dataframe['Time Spent'].apply(convert_to_hours)
     # Selecting only the desired columns
    selected_columns = ['Website Visit', 'Time Spent (hours)']
    selected_dataframe = dataframe[selected_columns]
    # Basic statistics for numerical columns
    st.write("### Summary Statistics for Numerical Columns:")
    st.write(dataframe.describe().T)

    # Load or define the DataFrame
# Example:
df = pd.read_csv(r"C:\Users\BIDA20-076\Desktop\star\updated_csv_file.csv")
# Display summary tablesshow_summary_tables(df)
show_summary_tables(df)



































