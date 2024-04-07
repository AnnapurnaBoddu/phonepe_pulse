**Tilte**: Phonepe Pulse Data Visualization and Exploration</br>
**Introduction**:  Project is to extract data from phonepe pulse Github repository and process it to to obtain insights and information that can be visulaized in a user-friendly manner.</br></br>
**Tools/Software used**:</br>
**Programming language** : python(python packages used: os, pandas, json, pyodbc, streamlit, plotly.express, git)</br>
**Database** : MS SQL server Express</br></br>
**Files**:</br>
1. data_clone.py : This program is for extracting the data from Github Phonepe Pulse Data repository to local file system</br>
Update the **local_directory** variable to the required folder location on the PC </br>

2. extract_data.py: This program is to extract the required data and return the dictionary.</br>
Update the **path** variable in this file .</br>

3.  sql_data.py : This program is to create MSSQL server database and tables to  store phonepe pulse data.</br>
Update  **MSSQLSEVER** connection details</br>

4. phonepe_app1.py : This program is to create **streamlit** user friendly application to visulaize the **Phonepe pulse data** using **plotly**</br>

**project execution**:</br>

1. Setup the environment with the required python packages and MSSQL Server.</br>
2. Execute the **data_clone.py** to copy data from Github Phonepe Pulse Data repository</br>
3. execute the **extract_data.py** and **sql_data.py** file for transforming the cloned data and load it to MSSQL Server.</br>
4. Execute the **phonepe_app1.py** in the terminal by the command: **streamlit run phonepe_app1.py** </br>
