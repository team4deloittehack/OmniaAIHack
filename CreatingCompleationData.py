# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 09:52:32 2019

@author: Krishna Chaitanya Gopaluni
"""

import pandas as pd 


data = pd.read_excel("completion_rate_199798-201718.xlsx")


d_data = data[data["YEAR_6_OF_COHORT"]== "2017/2018"] 

d_data2= d_data[d_data["DATA_LEVEL"] == "DISTRICT LEVEL"]

data_data3= d_data2[d_data2["FACILITY_TYPE"] == "STANDARD"]

data_data3["MODEL_TYPE"].unique()

data_data3["DISTRICT_NUMBER"].unique()



data_data3.to_csv("Filtered_2017-2018_compleationRate.csv")

DATA4= data_data3.groupby('DISTRICT_NAME')['DISTRICT_NUMBER'].value_counts().to_list()

count_list = DATA4.tolist()
district_names = sorted( data_data3['DISTRICT_NAME'].unique().tolist())

#[[i,j] for i in count_list for j in district_names if i ]

COUNTS_DF = {'DISTRICT_NAME' : district_names, 'DISTRICT_COUNT': count_list}
COUNTS_DF = pd.DataFrame(COUNTS_DF)
#DATA4.to_csv("DISTRICT_COUNTS _compleationRates.csv")



data_data3["DISTRICT_COUNTS"] = data_data3['DISTRICT_NAME'].apply(lambda x :COUNTS_DF[COUNTS_DF["DISTRICT_NAME"]== x]["DISTRICT_COUNT"].values[0] )




st_Start = pd.read_csv("strongstart.csv")

DATA5 = st_Start.groupby("SCHOOL_DISTRICT_NAME")["SCHOOL_DISTRICT_NUMBER"].value_counts()
count_list2 = DATA5.tolist()

district_names2 = sorted( st_Start['SCHOOL_DISTRICT_NAME'].unique().tolist())


COUNTS_DF_2 = {'DISTRICT_NAME' : district_names2, 'DISTRICT_COUNT': count_list2}
COUNTS_DF_2 = pd.DataFrame(COUNTS_DF_2)



COUNTS_DF_2.to_csv("Strong_startDistrictCounts.csv")
    
#
#data_data3["STRONG_START_DISTRICT_COUNTS"] = data_data3['DISTRICT_NAME'].apply(lambda x : COUNTS_DF_2[COUNTS_DF_2["DISTRICT_NAME"]== x]["DISTRICT_COUNT"] )


#data_data3.to_csv("CompleationRate.csv")



#COUNTS_DF_2[COUNTS_DF_2["DISTRICT_NAME"]== 'Nicola-Similkameen']["DISTRICT_COUNT"].values[0]

def apply_onRows(x):
    if (COUNTS_DF_2[COUNTS_DF_2["DISTRICT_NAME"]== x]["DISTRICT_COUNT"].values)  >= 1:
        return COUNTS_DF_2[COUNTS_DF_2["DISTRICT_NAME"]== x]["DISTRICT_COUNT"].values[0]
    return 0

data_data3["STRONG_START_DISTRICT_COUNTS"] = data_data3['DISTRICT_NAME'].apply(lambda x : apply_onRows(x) )

data_data3.to_csv("Regression_CompletionPredictionModel1.csv")





