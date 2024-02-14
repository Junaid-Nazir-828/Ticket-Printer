import pandas as pd
import constants

def authorize(username,password):
    sheet_id = constants.SHEET_ID
    df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')
    
    # bool for checking username and password
    userbool = False
    passbool = False

    # checking credentials
    for i in df['username']:
        if i == username:
            userbool = True
            break

    for i in df['password']:
        if i == password:
            passbool = True
            break        
    
    if userbool and passbool:
        return True
    else:
        return False