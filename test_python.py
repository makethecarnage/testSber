import pandas as pd

ATM = {
    'ATM_ID' : [1095, 1095, 1095, 765, 765, 9832],
    'ADR' : ['Москва, ул. Кирова, 5', 'Москва, ТЦ Гагаринский', 'Москва, ул. Менделеева, 7', 
             'Казань, ТЦ Рио', 'Казань, ТЦ Тандем', 'Москва, ТРЦ Европейский'],
    'DT_INS_DATE' : ['15-01-2019 00:00:00', '25-06-2023 00:00:00', '25-12-2022 00:00:00',
                     '19-01-2024 00:00:00', '14-03-2019 00:00:00', '15-02-2024 00:00:00']
}

atm_df = pd.DataFrame(ATM)

atm_df["DT_INS_DATE"] = pd.to_datetime(atm_df["DT_INS_DATE"], format='%d-%m-%Y %H:%M:%S')

sub_date_df = (atm_df[atm_df["DT_INS_DATE"] < '2023-01-01 00:00:00']
               .groupby("ATM_ID", as_index=False)["DT_INS_DATE"].max()
)

result_df = pd.merge(atm_df, sub_date_df, left_on=["ATM_ID", "DT_INS_DATE"], right_on=["ATM_ID", "DT_INS_DATE"])

result_df["CITY"] = result_df["ADR"].str.split(',').str[0]
result_df["ADDRESS"] = result_df["ADR"].str.split(',', n=1).str[1].str.strip()
result_df["DT_INS_DATE"] = result_df["DT_INS_DATE"].dt.strftime('%d-%m-%Y 00:00:00')

result_df = result_df[["ATM_ID", "CITY", "ADDRESS", "DT_INS_DATE"]]
print(result_df)
