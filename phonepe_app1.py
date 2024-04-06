import pandas as pd
import plotly.express as px
import streamlit as st
import pyodbc

st.set_page_config(layout="wide")
st.markdown("# :violet[Data Visualization and Exploration]")
st.write('')
st.write('')


# st.title('phonepe pulse data visualization')


def page_home():
    server = r'Purna\SQLEXPRESS'
    database = 'phonepe'
    username = 'sa'
    password = 'sqlserver'
    driver = '{SQL Server}'
    conn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password,
        autocommit=True)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Year FROM Agg_Transaction")
    rows = cursor.fetchall()
    year = [i.Year for i in rows]

    clm1, clm2, clm3 = st.columns(3)
    with clm1:
        option_clm1 = st.selectbox('Select Transaction or Users', ['Transaction', 'Users'], index=0)
    with clm2:
        option_clm2 = st.selectbox('Select Year', year, index=0)
    with clm3:
        option_clm3 = st.selectbox('Select  Quarter', ['1', '2', '3', '4'], index=0)
    server = r'Purna\SQLEXPRESS'
    database = 'phonepe'
    username = 'sa'
    password = 'sqlserver'
    driver = '{SQL Server}'
    conn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password,
        autocommit=True)
    cursor = conn.cursor()

    if option_clm1 == 'Transaction':
        query = '''select State, sum(cast(Transaction_Count as bigint)) as Transactions 
                       from Agg_Transaction 
                       where Year = ? and Quarter = ? 
                       group by State'''

        cursor.execute(query, int(option_clm2), int(option_clm3))
        rows = cursor.fetchall()
        data = [{'State': row.State, 'Transaction': row.Transactions} for row in rows]
        df = pd.DataFrame(data)
        fig = px.choropleth(
            df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Transaction',
            color_continuous_scale='Reds'
        )

        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(width=1000, height=800)
        st.plotly_chart(fig)

        # fig.show()

    if option_clm1 == 'Users':
        query = '''select State, Registered_Users as Users
                               from Agg_User 
                               where Year = ? and Quarter = ?
                               '''

        cursor.execute(query, int(option_clm2), int(option_clm3))
        rows = cursor.fetchall()
        data = [{'State': row.State, 'Users': row.Users} for row in rows]
        df = pd.DataFrame(data)
        fig = px.choropleth(
            df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Users',
            color_continuous_scale='Reds'
        )

        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(width=1000, height=800)
        st.plotly_chart(fig)

    df = pd.read_csv \
        ("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")
    # print(df)

    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='active cases',
        color_continuous_scale='Reds'
    )

    fig.update_geos(fitbounds="locations", visible=False)
    conn.close()


def explore_data():
    server = r'Purna\SQLEXPRESS'
    database = 'phonepe'
    username = 'sa'
    password = 'sqlserver'
    driver = '{SQL Server}'
    conn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password,
        autocommit=True)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Year FROM Agg_Transaction")
    rows = cursor.fetchall()
    year = [i.Year for i in rows]

    clm1, clm2, clm3 = st.columns(3)
    with clm1:
        option_clm1 = st.selectbox('Select Transaction or Users', ['Transaction', 'Users'], index=0)
    with clm2:
        option_clm2 = st.selectbox('Select Year', year, index=0)
    with clm3:
        option_clm3 = st.selectbox('Select  Quarter', ['1', '2', '3', '4'], index=0)

    col1, col2 = st.columns(2)
    if option_clm1 == 'Transaction':


        st.write('Visualize the Transaction data based on the Transaction type')

        query = """
                                  SELECT DISTINCT Transaction_Type, SUM(cast(Transaction_Count as bigint)) AS Transactions
                                  FROM Agg_Transaction
                                  WHERE Year = ? AND Quarter = ?
                                  GROUP BY Transaction_Type

                                  """
        cursor.execute(query, int(option_clm2), int(option_clm3))
        rows = cursor.fetchall()
        data = [list(row) for row in rows]
        df = pd.DataFrame(data, columns=['Transaction_Type', 'Transactions'])
        fig = px.pie(df, values='Transactions', names='Transaction_Type', title='Transaction Type')
        st.plotly_chart(fig)
        st.write('Visualize Top 10 States based on Transactions')

        query = """
                                          select distinct TOP 10 State, sum(Transaction_Amount) as Amount 
                                          from Agg_Transaction  where Year = ? and Quarter = ?
                                          group by State 
                                          order by Amount desc 

                                          """
        cursor.execute(query, int(option_clm2), int(option_clm3))
        rows = cursor.fetchall()
        data = [list(row) for row in rows]
        df = pd.DataFrame(data, columns=['State', 'Amount'])
        fig = px.bar(df, x="State", y="Amount", color=df["Amount"], labels={"State": "State"},
                         color_continuous_scale='Viridis', title='Top 10 States')
        st.plotly_chart(fig)
        st.write('Visualize Top 10 Districts based on Transactions')

        query = """
                                                SELECT DISTINCT TOP 10 District, sum(Amount) AS Amount 
                                                FROM Map_Transaction WHERE Year = ? and Quarter = ? 
                                                GROUP BY District 
                                                Order by Amount desc

                                                 """
        cursor.execute(query, int(option_clm2), int(option_clm3))
        rows = cursor.fetchall()
        data = [list(row) for row in rows]
        df = pd.DataFrame(data, columns=['District', 'Amount'])
        fig = px.bar(df, x="District", y="Amount", color=df["Amount"], labels={"District": "District"},
                         color_continuous_scale='Viridis', title='Top 10 Districts')
        st.plotly_chart(fig)
        st.write('Visualize Top 10 Pincodes based on Transactions')
        query = """
                                                       select distinct top 10 Pincode, sum(Amount) as Amount 
                                                       from Top_Transaction_Pincode where Year = ? and Quarter = ? 
                                                       group by Pincode 
                                                       order by Amount desc

                                                        """
        cursor.execute(query, int(option_clm2), int(option_clm3))
        rows = cursor.fetchall()
        data = [list(row) for row in rows]
        df = pd.DataFrame(data, columns=['Pincode', 'Amount'])
        fig = px.pie(df, values='Amount', names='Pincode', hole=0.5, title='Top 10 Pincodes')
        st.plotly_chart(fig)

    elif option_clm1 == 'Users':

        st.write('Visualize Top 10 States based on Users')
        query = """
                                                 select distinct TOP 10 State, sum(Registered_Users) as Users 
                                                 from Agg_User  where Year = ? and Quarter = ?
                                                 group by State 
                                                 order by Users desc 

                                                 """
        cursor.execute(query, int(option_clm2), int(option_clm3))
        rows = cursor.fetchall()
        data = [list(row) for row in rows]
        df = pd.DataFrame(data, columns=['State', 'Users'])
        fig = px.bar(df, x="State", y="Users", color=df["Users"], labels={"State": "State"},
                         color_continuous_scale='Viridis', title='Top 10 States based on Users')
        st.plotly_chart(fig)
        st.write('Visualize Top 10 Districts based on Users')
        query = """
                                                        SELECT DISTINCT TOP 10 District, sum(cast(Registered_User as bigint)) AS Users 
                                                        FROM Map_User WHERE Year = ? and Quarter = ? 
                                                        GROUP BY District 
                                                        Order by Users desc

                                                         """
        cursor.execute(query, int(option_clm2), int(option_clm3))
        rows = cursor.fetchall()
        data = [list(row) for row in rows]
        df = pd.DataFrame(data, columns=['District', 'Users'])
        fig = px.bar(df, x="District", y="Users", color=df["Users"], labels={"District": "District"},
                         color_continuous_scale='Viridis', title='Top 10 Districts based on Users')
        st.plotly_chart(fig)
        st.write('Visualize Top 10 Pincodes based on Users')
        query = """
                                                              select distinct top 10 Pincode, sum(cast(Registered_user as bigint)) as Users 
                                                              from Top_User_Pincode where Year = ? and Quarter = ? 
                                                              group by Pincode 
                                                              order by Users desc

                                                               """
        cursor.execute(query, int(option_clm2), int(option_clm3))
        rows = cursor.fetchall()
        data = [list(row) for row in rows]
        df = pd.DataFrame(data, columns=['Pincode', 'Users'])
        fig = px.pie(df, values='Users', names='Pincode', hole=0.5,
                         title='Top 10 Pincodes based on number of users')
        st.plotly_chart(fig)
    else:
        pass


page = st.sidebar.radio("Navigation", ["Home", "Explore Data"])
if page == "Home":
    page_home()
elif page == "Explore Data":
    explore_data()
