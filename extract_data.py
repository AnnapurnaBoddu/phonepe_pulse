import os
import pandas as pd
import json
from pprint import pprint

# This is to direct the path to get the data as states

def agg_transaction():

    path = (
        "C:\\Users\\2anna\\Desktop\\Pyhton course\\capstoneproject2\\"
        "phonpe_data\\data\\aggregated\\transaction\\country\\india\\state\\"
    )

    Agg_state_list = os.listdir(path)
    #print(Agg_state_list)
    # This is to extract the data's to create a dataframe

    clm = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [], 'Transaction_amount': []}

    for i in Agg_state_list:
        p_i = path + i + "\\"
        Agg_yr = os.listdir(p_i)
        for j in Agg_yr:
            p_j = p_i + j + "\\"
            Agg_qr_list = os.listdir(p_j)
            for k in Agg_qr_list:
                p_k = p_j + k
                Data = open(p_k, 'r')
                D = json.load(Data)
                #pprint(D)
                for z in D['data']['transactionData']:
                    Name = z['name']
                    count = z['paymentInstruments'][0]['count']
                    amount = z['paymentInstruments'][0]['amount']
                    clm['Transaction_type'].append(Name)
                    clm['Transaction_count'].append(count)
                    clm['Transaction_amount'].append(amount)
                    clm['State'].append(i.replace('-', ' ',5).title())
                    clm['Year'].append(j)
                    clm['Quarter'].append(int(k.strip('.json')))
    # Successfully created a dataframe
    Agg_Trans = pd.DataFrame(clm)
    #pprint(Agg_Trans)
    return clm

def agg_user():

    path = (
        "C:\\Users\\2anna\\Desktop\\Pyhton course\\capstoneproject2\\"
        "phonpe_data\\data\\aggregated\\user\\country\\india\\state\\"
    )

    User_state_list = os.listdir(path)

    clm2 = {'State': [], 'Year': [], 'Quarter': [], 'Registered_Users': [], 'App_Opens': []}
    for i in User_state_list:
        p_i = path + i + "\\"
        User_yr = os.listdir(p_i)
        for j in User_yr:
            p_j = p_i + j + "\\"
            User_qr_list = os.listdir(p_j)
            for k in User_qr_list:
                p_k = p_j + k
                Data = open(p_k, 'r')
                D = json.load(Data)
                #pprint(D)
                registered_users = D['data']['aggregated']['registeredUsers']
                app_opens = D['data']['aggregated']['appOpens']
                clm2['State'].append(i.replace('-', ' ', 5).title())
                clm2['Year'].append(j)
                clm2['Quarter'].append(int(k.strip('.json')))
                clm2['Registered_Users'].append(registered_users)
                clm2['App_Opens'].append(app_opens)
    return clm2


# extract data from map transaction
def map_transaction():
    path = (
        "C:\\Users\\2anna\\Desktop\\Pyhton course\\capstoneproject2\\phonpe_data\\"
        "data\\map\\transaction\\hover\\country\\india\\state\\"
    )
    map_state_list = os.listdir(path)
    #print(map_state_list)
    # This is to extract the data's to create a dataframe
    clm3 = {'state': [], 'year': [], 'quarter': [], 'district': [], 'count': [], 'amount': []}
    for i in map_state_list:
        p_i = path + i + '\\'
        map_year_list = os.listdir(p_i)
        for j in map_year_list:
            p_j = p_i + j + '\\'
            map_qr_list = os.listdir(p_j)
            for k in map_qr_list:
                p_k = p_j + k
                Data = open(p_k, 'r')
                D = json.load(Data)
                #pprint(D)
                for x in D['data']['hoverDataList']:
                    dist_name = x['name']
                    count = x['metric'][0]['count']
                    amount = x['metric'][0]['amount']
                    clm3['state'].append(i.replace('-',' ', 5).title())
                    clm3['year'].append(j)
                    clm3['district'].append(dist_name)
                    clm3['quarter'].append(int(k.strip('.json')))
                    clm3['count'].append(count)
                    clm3['amount'].append(amount)
    map_tran = pd.DataFrame(clm3)
    #print(map_tran)
    return clm3

# for map_user data
def map_user():
    path = (
        "C:\\Users\\2anna\\Desktop\\Pyhton course\\capstoneproject2\\phonpe_data\\"
        "data\\map\\user\\hover\\country\\india\\state\\"
    )
    map_state_list = os.listdir(path)
    clm4 = {'state': [], 'year': [], 'quarter': [], 'district': [], 'app_opens': [], 'registered_users': []}
    for i in map_state_list:
        p_i = path + i + '\\'
        map_year_list = os.listdir(p_i)
        for j in map_year_list:
            p_j = p_i + j + '\\'
            map_qr_list = os.listdir(p_j)
            for k in map_qr_list:
                p_k = p_j + k
                Data = open(p_k, 'r')
                D = json.load(Data)
                #pprint(D)
                #pprint(list(D['data']['hoverData'].keys()))
                district_list = list(D['data']['hoverData'].keys())
                for z in district_list:
                    registered_user = D['data']['hoverData'][z]['registeredUsers']
                    app_open =D['data']['hoverData'][z]['appOpens']
                    clm4['state'].append(i.replace('-', ' ', 5).title())
                    clm4['year'].append(j)
                    clm4['district'].append(z)
                    clm4['quarter'].append(int(k.strip('.json')))
                    clm4['registered_users'].append(registered_user)
                    clm4['app_opens'].append(app_open)
    map_user = pd.DataFrame(clm4)
    #pprint(map_user)
    return clm4



# top
def top_transaction():

    path = (
        "C:\\Users\\2anna\\Desktop\\Pyhton course\\capstoneproject2\\phonpe_data\\"
        "data\\top\\transaction\\country\\india\\state\\"
    )
    clm5 = {'state': [], 'year': [], 'quarter': [], 'districts': [], 'dist_amount': [], 'dist_count': []}
    clm6 = {'state': [], 'year': [], 'quarter': [], 'pincodes': [], 'pin_amount': [], 'pin_count': []}
    map_state_list = os.listdir(path)
    for i in map_state_list:
        p_i = path + i + '\\'
        map_year_list = os.listdir(p_i)
        for j in map_year_list:
            p_j = p_i + j + '\\'
            map_qr_list = os.listdir(p_j)
            for k in map_qr_list:
                p_k = p_j + k
                Data = open(p_k, 'r')
                D = json.load(Data)
                #print('top transaction data')
                #pprint(D)
                for z in D['data']['districts']:
                    district_name = z['entityName']
                    count = z['metric']['count']
                    amount = z['metric']['amount']
                    clm5['districts'].append(district_name)
                    clm5['dist_amount'].append(amount)
                    clm5['dist_count'].append(count)
                    clm5['state'].append(i.replace('-', ' ', 5).title())
                    clm5['year'].append(j)
                    clm5['quarter'].append(int(k.strip('.json')))
                for x in D['data']['pincodes']:
                    pincode = x['entityName']
                    count = x['metric']['count']
                    amount = x['metric']['amount']
                    clm6['pincodes'].append(pincode)
                    clm6['pin_amount'].append(amount)
                    clm6['pin_count'].append(count)
                    clm6['state'].append(i.replace('-',' ', 5).title())
                    clm6['year'].append(j)
                    clm6['quarter'].append(int(k.strip('.json')))
    top_trans_dist = pd.DataFrame(clm5)
    top_trans_pin = pd.DataFrame(clm6)
    #pprint(top_trans_dist)
    #pprint(top_trans_pin)
    return clm5,clm6

#top user data
def top_user():
    path = (
        "C:\\Users\\2anna\\Desktop\\Pyhton course\\capstoneproject2\\phonpe_data\\"
        "data\\top\\user\\country\\india\\state\\"
    )
    clm7 = {'state': [], 'year': [], 'quarter': [], 'districts': [], 'registered_users': []}
    clm8 = {'state': [], 'year': [], 'quarter': [], 'pincodes': [], 'registered_users': []}
    map_state_list = os.listdir(path)
    for i in map_state_list:
        p_i = path + i + '\\'
        map_year_list = os.listdir(p_i)
        for j in map_year_list:
            p_j = p_i + j + '\\'
            map_qr_list = os.listdir(p_j)
            for k in map_qr_list:
                p_k = p_j + k
                Data = open(p_k, 'r')
                D = json.load(Data)
                #print('top transaction data')
                #pprint(D)
                for z in D['data']['districts']:
                    district_name = z['name']
                    registered_users = z['registeredUsers']
                    clm7['districts'].append(district_name)
                    clm7['registered_users'].append(registered_users)
                    clm7['state'].append(i.replace('-', ' ',5).title())
                    clm7['year'].append(j)
                    clm7['quarter'].append(int(k.strip('.json')))
                for x in D['data']['pincodes']:
                    pincode = x['name']
                    registered_users = x['registeredUsers']
                    clm8['pincodes'].append(pincode)
                    clm8['registered_users'].append(registered_users)
                    clm8['state'].append(i.replace('-', ' ',5).title())
                    clm8['year'].append(j)
                    clm8['quarter'].append(int(k.strip('.json')))
    top_user_dist = pd.DataFrame(clm7)
    top_user_pin = pd.DataFrame(clm8)
    #pprint(top_user_dist)
    #pprint(top_user_pin)
    return clm7,clm8















