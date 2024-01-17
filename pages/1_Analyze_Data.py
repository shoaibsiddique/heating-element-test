import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Analyze Data", page_icon="📈")
#st.sidebar.header("Analyze Data")
# Function to extract temperature as a float
def extract_temperature(temp_str):
    temp_str = temp_str.replace('C', '').replace(',', '')  # Remove 'C' and commas
    return float(temp_str) if temp_str else None

# Function to read data and preprocess
def read_and_process_data(file_path):
    data = pd.read_csv(file_path, sep=" ", header=None)
    data.columns = ['date', 'time', 'sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5', 'sensor6']

    # Parse the Data
    data['datetime'] = pd.to_datetime(data['date'] + ' ' + data['time'])
    for col in ['sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5', 'sensor6']:
        data[col] = data[col].apply(extract_temperature)

    # Convert seconds to minutes for the x-axis
    data['minutes'] = (data['datetime'] - data['datetime'][0]).dt.total_seconds() / 60

    return data

# Streamlit web app
st.title('Temperature Readings Data Analysis')

# Enable Comparison Mode
comparison_mode = st.checkbox('Enable Comparison Mode')

if comparison_mode:
    # Dropdown menus to select files for comparison
    file_options = {
        'Original S&H Test': 'DATALOG.TXT',
        'Original S&H Test for 1 Hours': 'DATALOG1H.TXT',
        'Pattern # 001 Run for 1 Hours': 'DATALOG_001.TXT',
        'Pattern # 001 with S&H Circuit': 'DATALOG_001SH.TXT',
        'Pattern # 002 Run for 1 Hours': 'DATALOG_002.TXT',
        'Pattern # 002 with S&H Circuit': 'DATALOG_002SH.TXT',
        'Pattern # 003 Run for 1 Hours': 'DATALOG_003.TXT',
        'Pattern # 004 Run for 1 Hours': 'DATALOG_004.TXT',
        'Pattern # 004 with S&H Circuit': 'DATALOG_004SH.TXT'
    }

    selected_file_1 = st.selectbox('Select the first file:', list(file_options.keys()))
    selected_file_2 = st.selectbox('Select the second file:', list(file_options.keys()))

    # Read and preprocess data based on the selected files
    data_1 = read_and_process_data(file_options[selected_file_1])
    data_2 = read_and_process_data(file_options[selected_file_2])

    # Plot the Data using Plotly for comparison
    fig_1 = go.Figure()
    for col in ['sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5', 'sensor6']:
        fig_1.add_trace(go.Scatter(x=data_1['minutes'], y=data_1[col], mode='lines', name=f'{col} - {selected_file_1}'))

    fig_2 = go.Figure()
    for col in ['sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5', 'sensor6']:
        fig_2.add_trace(go.Scatter(x=data_2['minutes'], y=data_2[col], mode='lines', name=f'{col} - {selected_file_2}'))
    # Add a vertical line for hover effect
    fig_1.add_trace(go.Scatter(x=[None], y=[None], mode='lines', line=dict(color='red', width=2), showlegend=False,
                            hoverinfo='none', hovertemplate='%{y:.2f} C at %{x:.2f} min'))

    fig_1.update_layout(
        xaxis_title='Time (minutes)',
        yaxis_title='Temperature (C)',
        title=selected_file_1,
        hovermode='x unified'
    )

    # Set x-axis interval to 5 minutes
    interval = 5
    fig_1.update_layout(xaxis=dict(tickmode='linear', tick0=0, dtick=interval))


    # Add a vertical line for hover effect
    fig_2.add_trace(go.Scatter(x=[None], y=[None], mode='lines', line=dict(color='red', width=2), showlegend=False,
                            hoverinfo='none', hovertemplate='%{y:.2f} C at %{x:.2f} min'))

    fig_2.update_layout(
        xaxis_title='Time (minutes)',
        yaxis_title='Temperature (C)',
        title=selected_file_2,
        hovermode='x unified'
    )

    # Set x-axis interval to 5 minutes
    interval = 5
    # For comparison mode - set y-axis range for both figures
    fig_1.update_layout(yaxis=dict(range=[24, data_1[['sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5', 'sensor6']].max().max() + 5]))
    fig_2.update_layout(yaxis=dict(range=[24, data_2[['sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5', 'sensor6']].max().max() + 5]))

    fig_2.update_layout(xaxis=dict(tickmode='linear', tick0=0, dtick=interval))


    # Display the charts side by side
    st.plotly_chart(fig_1, use_container_width=True)
    st.plotly_chart(fig_2, use_container_width=True)

else:
    # Dropdown menu to select file with custom names
    file_options = {
        'Original S&H Test': 'DATALOG.TXT',
        'Original S&H Test for 1 Hours': 'DATALOG1H.TXT',
        'Pattern # 001 Run for 1 Hours': 'DATALOG_001.TXT',
        'Pattern # 001 with S&H Circuit': 'DATALOG_001SH.TXT',
        'Pattern # 002 Run for 1 Hours': 'DATALOG_002.TXT',
        'Pattern # 002 with S&H Circuit': 'DATALOG_002SH.TXT',
        'Pattern # 003 Run for 1 Hours': 'DATALOG_003.TXT',
        'Pattern # 004 Run for 1 Hours': 'DATALOG_004.TXT',
        'Pattern # 004 with S&H Circuit': 'DATALOG_004SH.TXT'
    }

    selected_file = st.selectbox('Select a file:', list(file_options.keys()))

    # Read and preprocess data based on the selected file
    data = read_and_process_data(file_options[selected_file])
    # Plot the Data using Plotly
    fig = go.Figure()

    for col in ['sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5', 'sensor6']:
        fig.add_trace(go.Scatter(x=data['minutes'], y=data[col], mode='lines', name=col))

    # Add a vertical line for hover effect
    fig.add_trace(go.Scatter(x=[None], y=[None], mode='lines', line=dict(color='red', width=2), showlegend=False,
                            hoverinfo='none', hovertemplate='%{y:.2f} C at %{x:.2f} min'))

    fig.update_layout(
        xaxis_title='Time (minutes)',
        yaxis_title='Temperature (C)',
        title='Temperature Readings from 6 Sensors',
        hovermode='x unified'
    )

    # Set x-axis interval to 5 minutes
    interval = 5
    # For single-file mode - set y-axis range for the figure
    fig.update_layout(yaxis=dict(range=[22, data[['sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5', 'sensor6']].max().max() + 5]))

    fig.update_layout(xaxis=dict(tickmode='linear', tick0=0, dtick=interval))

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)

