# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 22:25:15 2021

@author: Zeyuan Li
"""

# ## Question 3

# ### (a) read and append the demographic datasets

# In[26]:


import pandas as pd 
import pickle   
DEMO_2011_2012 = pd.read_sas('DEMO_G.XPT')
DEMO_2013_2014 = pd.read_sas('DEMO_H.XPT')
DEMO_2015_2016 = pd.read_sas('DEMO_I.XPT')
DEMO_2017_2018 = pd.read_sas('DEMO_J.XPT')

DEMO_2011_2012['cohort'] = '2011-2012'
DEMO_2013_2014['cohort'] = '2013-2014'
DEMO_2015_2016['cohort'] = '2015-2016'
DEMO_2017_2018['cohort'] = '2017-2018'
DEMO = pd.concat([DEMO_2011_2012, DEMO_2013_2014, DEMO_2015_2016, DEMO_2017_2018], axis=0)
DEMO_part = DEMO[['SEQN', 'RIDAGEYR', 'RIDRETH3', 'DMDEDUC2', 'DMDMARTL', 'RIDSTATR', 'SDMVPSU',
               'SDMVSTRA','WTMEC2YR', 'WTINT2YR','RIAGENDR','cohort']]
DEMO_part.columns = ['unique ids', 'age', 'race and ethnicity', 'education', 'marital status',
                   'Interview/Examination status', 'Masked variance pseudo-PSU',
                   'Masked variance pseudo-stratum','Full sample 2 year MEC exam weight',
                   'Full sample 2 year interview weight','genderR','cohort']

#create dictionary for categorical variables
race_dict = { 1: 'Mexican American', 
            2: 'Other Hispanic',
            3: 'Non-Hispanic White',
            4: 'Non-Hispanic Black',
            6: 'Non-Hispanic Asian',
            7: 'Other Race - Including Multi-Racial',
            np.nan:'Missing'}

education_dict = {
0:'Never attended or kindergarten only',
1:'1st grade',
2:'2nd grade',
3:'3rd grade',
4:'4th grade',
5:'5th grade',
6:'6th grade',
7:'7th grade',
8:'8th grade',
9:'9th grade',
10:'10th grade',
11:'11th grade',
12:'12th grade, no diploma',
13:'High school graduate',
14:'GED or equivalent',
15:'More than high school',
55:'Less than 5th grade',
66:'Less than 9th grade',
77:'Refused',
99:'Dont Know',
np.nan:'Missing'
}
marital_dict = {
1: 'Married',
2: 'Widowed',
3: 'Divorced',
4: 'Separated',
5: 'Never married',
6: 'Living with partner',
77: 'Refused',
99: 'Dont Know',
np.nan: 'Missing'
}
RIDSTATR_dict = {
    1: 'Interviewed only',
    2: 'Both interviewed and MEC examined',
    np.nan: 'Missing'
}

DEMO_part['race and ethnicity'] = pd.Categorical(DEMO_part['race and ethnicity'].replace(race_dict))
DEMO_part['education'] = pd.Categorical(DEMO_part['education'].replace(education_dict))
DEMO_part['marital status'] = pd.Categorical(DEMO_part['marital status'].replace(marital_dict))
DEMO_part['Interview/Examination status'] = pd.Categorical(DEMO_part['Interview/Examination status'].replace(RIDSTATR_dict))

#show the dataframe
DEMO_part


# In[27]:


#save the dataframe to pickle file
f = open('DEMO_2011_2018','wb+')
pickle.dump(DEMO_part,f)
f.close


# ### (b) Repeat part a for the oral health and dentition data

# In[30]:


import numpy as np
import pandas as pd 
import pickle   
OHXDEN_2011_2012 = pd.read_sas('OHXDEN_G.XPT')
OHXDEN_2013_2014 = pd.read_sas('OHXDEN_H.XPT')
OHXDEN_2015_2016 = pd.read_sas('OHXDEN_I.XPT')
OHXDEN_2017_2018 = pd.read_sas('OHXDEN_J.XPT')
OHXDEN_2011_2012['cohort'] = '2011-2012'
OHXDEN_2013_2014['cohort'] = '2013-2014'
OHXDEN_2015_2016['cohort'] = '2015-2016'
OHXDEN_2017_2018['cohort'] = '2017-2018'
OHXDEN=pd.concat([OHXDEN_2011_2012, OHXDEN_2013_2014, OHXDEN_2015_2016, OHXDEN_2017_2018], axis=0)   
 
#find the column names like OHXxxTC  
OHXDEN.columns[OHXDEN.columns.str.startswith('OHX') & OHXDEN.columns.str.endswith('TC')] 
OHXxxTC_name_list=['OHX01TC', 'OHX02TC', 'OHX03TC', 'OHX04TC', 'OHX05TC', 'OHX06TC',
       'OHX07TC', 'OHX08TC', 'OHX09TC', 'OHX10TC', 'OHX11TC', 'OHX12TC',
       'OHX13TC', 'OHX14TC', 'OHX15TC', 'OHX16TC', 'OHX17TC', 'OHX18TC',
       'OHX19TC', 'OHX20TC', 'OHX21TC', 'OHX22TC', 'OHX23TC', 'OHX24TC',
       'OHX25TC', 'OHX26TC', 'OHX27TC', 'OHX28TC', 'OHX29TC', 'OHX30TC',
       'OHX31TC', 'OHX32TC'] 
#find the column names like OHXxxCTC              
OHXDEN.columns[OHXDEN.columns.str.startswith('OHX') & OHXDEN.columns.str.endswith('CTC')]                
OHXxxCTC_name_list=['OHX02CTC', 'OHX03CTC', 'OHX04CTC', 'OHX05CTC', 'OHX06CTC', 'OHX07CTC',
       'OHX08CTC', 'OHX09CTC', 'OHX10CTC', 'OHX11CTC', 'OHX12CTC', 'OHX13CTC',
       'OHX14CTC', 'OHX15CTC', 'OHX18CTC', 'OHX19CTC', 'OHX20CTC', 'OHX21CTC',
       'OHX22CTC', 'OHX23CTC', 'OHX24CTC', 'OHX25CTC', 'OHX26CTC', 'OHX27CTC',
       'OHX28CTC', 'OHX29CTC', 'OHX30CTC', 'OHX31CTC']
OHXDEN_part_columns_list=['SEQN','OHDDESTS']+OHXxxTC_name_list+OHXxxCTC_name_list+['cohort']               
OHXDEN_part=OHXDEN[OHXDEN_part_columns_list]

OHDDESTS_dict = {
    1: "Complete",
    2: "Partial",
    3: "Not Done",
    np.nan:"Missing"
    }
OHXxxTC_dict = {
1: 'Primary tooth (deciduous) present',
2: 'Permanent tooth present',
3: 'Dental implant',
4: 'Tooth not present',
5: 'Permanent dental root fragment present',
9: 'Could not assess',
np.nan: 'Missing'
}
OHXxxCTC_dict= {
b'A': 'Primary tooth with a restored surface condition',
b'D': 'Sound primary tooth',
b'E': 'Missing due to dental disease',
b'F': 'Permanent tooth with a restored surface condition',
b'J': 'Permanent root tip is present but no restorative replacement is present',
b'K': 'Primary tooth with a dental carious surface condition',
b'M': 'Missing due to other causes',
b'P': 'Missing due to dental disease but replaced by a removable restoration',
b'Q': 'Missing due to other causes but replaced by a removable restoration',
b'R': 'Missing due to dental disease but replaced by a fixed restoration',
b'S': 'Sound permanent tooth',
b'T': 'Permanent root tip is present but a restorative replacement is present',
b'U': 'Unerupted',
b'X': 'Missing due to other causes but replaced by a fixed restoration',
b'Y': 'Tooth present, condition cannot be assessed',
b'Z': 'Permanent tooth with a dental carious surface condition',
b'': 'Missing'
}
OHXDEN_part['OHDDESTS'] = pd.Categorical(OHXDEN_part['OHDDESTS'].replace(OHDDESTS_dict))
for OHXxxTC in OHXxxTC_name_list:
    OHXDEN_part[OHXxxTC] = pd.Categorical(OHXDEN_part[OHXxxTC].replace(OHXxxTC_dict))
for OHXxxCTC in OHXxxCTC_name_list:
    OHXDEN_part[OHXxxCTC] = pd.Categorical(OHXDEN_part[OHXxxCTC].replace(OHXxxCTC_dict))

OHXDEN_part.columns = [
'unique ids',
'Dentition Status Code',
'Tooth Count: #1',
'Tooth Count: #2',
'Tooth Count: #3',
'Tooth Count: #4',
'Tooth Count: #5',
'Tooth Count: #6',
'Tooth Count: #7',
'Tooth Count: #8',
'Tooth Count: #9',
'Tooth Count: #10',
'Tooth Count: #11',
'Tooth Count: #12',
'Tooth Count: #13',
'Tooth Count: #14',
'Tooth Count: #15',
'Tooth Count: #16',
'Tooth Count: #17',
'Tooth Count: #18',
'Tooth Count: #19',
'Tooth Count: #20',
'Tooth Count: #21',
'Tooth Count: #22',
'Tooth Count: #23',
'Tooth Count: #24',
'Tooth Count: #25',
'Tooth Count: #26',
'Tooth Count: #27',
'Tooth Count: #28',
'Tooth Count: #29',
'Tooth Count: #30',
'Tooth Count: #31',
'Tooth Count: #32',
'Coronal Caries: Tooth Count #2',
'Coronal Caries: Tooth Count #3',
'Coronal Caries: Tooth Count #4',
'Coronal Caries: Tooth Count #5',
'Coronal Caries: Tooth Count #6',
'Coronal Caries: Tooth Count #7',
'Coronal Caries: Tooth Count #8',
'Coronal Caries: Tooth Count #9',
'Coronal Caries: Tooth Count #10',
'Coronal Caries: Tooth Count #11',
'Coronal Caries: Tooth Count #12',
'Coronal Caries: Tooth Count #13',
'Coronal Caries: Tooth Count #14',
'Coronal Caries: Tooth Count #15',
'Coronal Caries: Tooth Count #16',
'Coronal Caries: Tooth Count #17',
'Coronal Caries: Tooth Count #18',
'Coronal Caries: Tooth Count #19',
'Coronal Caries: Tooth Count #20',
'Coronal Caries: Tooth Count #21',
'Coronal Caries: Tooth Count #22',
'Coronal Caries: Tooth Count #23',
'Coronal Caries: Tooth Count #24',
'Coronal Caries: Tooth Count #25',
'Coronal Caries: Tooth Count #26',
'Coronal Caries: Tooth Count #27',
'Coronal Caries: Tooth Count #28',
'Coronal Caries: Tooth Count #29',
'cohort'
    ]     

OHXDEN_part 


# In[31]:


#save the dataframe to pickle file
f = open('OHXDEN_2011_2018','wb+')
pickle.dump(OHXDEN_part,f)
f.close 


# ### （c) Report the number of cases there are in the two datasets above.

# In[36]:


print("the number of cases of the first dataset is {:}".format(DEMO_part.shape[0]))
print("the number of cases of the second dataset is {:}".format(OHXDEN_part.shape[0]))

