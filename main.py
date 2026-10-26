import csv
import json
import requests

import pandas as pd



"""
    Functions declaration
"""

def get_ESNcard_holders_data(file_path):

    df_ESNcard_holders = pd.read_excel(file_path)

    return (df_ESNcard_holders)



"""
    Beggining of execution
"""

def main():
    file_path =  "../Input_data/ESNcard Application 26_27 (Responses).xlsx"

    df_ESNcard_holders = get_ESNcard_holders_data(file_path)

    new_df_ESNcard_holders = df_ESNcard_holders.iloc[:][[ 'Timestamp', 'Email address', 'Name(s)', 'Surname', 'Nationality', 'Date of birth (DD/MM/YY)', 'Host University', 'For how long are you planning to stay in Enschede? ', 'I have read and understood the terms and conditions, which outline how my personal data will be processed and protected. In order to comply with the General Data Protection Regulation, I acknowledge that my application data will be shared with ESN in order to facilitate the generation of the ESNcard.', 'I have read and understood the terms and conditions, which outline how my personal data will be processed and protected. In order to comply with the General Data Protection Regulation, I acknowledge that my application data will be shared with ESN in order to facilitate the generation of the ESNcard.', 'Paid?', 'Paid?', 'Pick-up Date (DD/MM/YY)', 'ESNcard Number', 'Pick-up Date (DD/MM/YY)', 'Expiry Date (Auto)', 'Unnamed: 13']]

    new_df_ESNcard_holders = new_df_ESNcard_holders.rename(columns={'Timestamp': 'date_form_filled',
                                                                    'Email address': 'email',
                                                                    'Name(s)': 'name',
                                                                    'Surname': 'surname',
                                                                    'Nationality': 'nationality',
                                                                    'Date of birth (DD/MM/YY)': 'birthdate',
                                                                    'Host University': 'host_university',
                                                                    'For how long are you planning to stay in Enschede? ': 'duration_of_stay',
                                                                    'I have read and understood the terms and conditions, which outline how my personal data will be processed and protected. In order to comply with the General Data Protection Regulation, I acknowledge that my application data will be shared with ESN in order to facilitate the generation of the ESNcard.': 'terms_and_conditions',
                                                                    'Paid?': 'paid',
                                                                    'Pick-up Date (DD/MM/YY)': 'pick_up_date',
                                                                    'ESNcard Number': 'esn_card_number',
                                                                    'Expiry Date (Auto)': 'expiry_date'
                                                                    })
    print(new_df_ESNcard_holders.columns.values)
    cols = list(new_df_ESNcard_holders.columns)
    cols[9] = "newsletter_consent"
    cols[11] = "card_type"
    cols[12] = "payment_date"
    cols[16] = "sync_status"
    new_df_ESNcard_holders.columns = cols

    new_df_ESNcard_holders.loc[:,'sync_status'] = 1

    mask = new_df_ESNcard_holders['date_form_filled'].isna()

    new_df_ESNcard_holders.loc[mask, 'date_form_filled'] = (
        new_df_ESNcard_holders.loc[mask, 'pick_up_date']
    )

    print(new_df_ESNcard_holders.iloc[111][:])


    # Write to a new Excel file
    for i in range(new_df_ESNcard_holders.shape[0] // 10):
        new_df_ESNcard_holders.iloc[i*10 : (i+1)*10].to_excel(f"../Output_data/output_{i}.xlsx", index=False)

    for i in range(new_df_ESNcard_holders.shape[0] // 10):
        new_df_ESNcard_holders.iloc[i*10 : (i+1)*10].to_excel(f"../Output_data/output_{i}.xlsx", index=False)

    new_df_ESNcard_holders.iloc[(new_df_ESNcard_holders.shape[0] // 10)*10 : ].to_excel(f"../Output_data/output_{(new_df_ESNcard_holders.shape[0] // 10)}.xlsx", index=False)



if __name__ == "__main__":
    main()