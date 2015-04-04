import random,re,sys,os,pprint,nltk,time,datetime,numpy as np,pandas as pd
from np.random import *
from datetime import *;from time import *
from pprint import * 
from pandas import *
### <<fun starts>>
#todays_date=datetime.datetime.now().date()
#print ('Presentation started on')
#print (todays_date)
print ('\n\n')
### <<fun ends>>
#import data into pandas environment
print('Loading data might take a few seconds . . . ')
rca=pd.read_csv('/home/vetron/documents/rough/test_clothing_accessories.txt',header=None,sep='\n')
### very large###
#rca=pd.read_csv('/media/vetron/warehouse/summer_work/Dataset/clothing_accessories.txt',header=None,sep='\n')
print('Data loaded.\n')
print('Cleaning up . . . . \n\n\n')
time.sleep(5)
#clear
#make many lists :D and use del list_name[:] to delete
#keeping it intact for tommorow's presentation
rca_list=[]
pro_ID=[]
title=[]
uid=[]
name=[]
score=[]
summary=[]

#number of rows in our raw data
lenn=len(rca.index)
i=0
#data_frame to list explicitly
print('Making a list out of raw data frame extracted . . . \n')
while i<lenn:
	rca_list.append(rca[0][i])
	i=i+1
print('#############         It\'s time for some REGEX.         ####################\n')
print('Making list so that they can be combined together to make a data frame.\n')
print('These list are PRODUCT_ID,USER_NAME,etc...(hope you got the idea)\n\n\n')
time.sleep(4)
i=0
for item in rca_list:
     popat=re.search(r'(?<=\s).*',item).group(0)
     if(i%10==0):
     	pro_ID.append(popat)
     if(i%10==1):
	title.append(popat)
     if(i%10==3):
	uid.append(popat)
     if(i%10==4):
	name.append(popat)
     if(i%10==6):
	score.append(popat)
     if(i%10==8):
	summary.append(popat)	
     i=i+1
print('Finished making lists.\n\n')
print('\t\t\t---RESULTS---\n')
i=0
while i<4:
    print(pro_ID[i])
    print(title[i])
    print(uid[i])
    print(name[i])
    print(score[i])
    print(summary[i])
    print('\n')
    i=i+1
    raw_input()

time.sleep(2)
i=0
df_rca=pd.DataFrame()
#df_rca=pd.DataFrame(columns=['PRODUCT_ID','TITLE','USER_ID','NAME','SCORE','SUMMARY'])
#first data frame is created
## here I created single row and than apppended :D
#df_rca=pd.DataFrame(pro_ID,columns=['PRODUCT_ID'])
df_rca['PRODUCT_ID']=Series(pro_ID)
df_rca['TITLE']=Series(title)
df_rca['USER_ID']=Series(uid)
df_rca['NAME']=Series(name)
df_rca['SCORE']=Series(score)
df_rca['SUMMARY']=Series(summary)
print('###########################################################################')
print ('Making our data frame named \' df_rca \'\n\n')
time.sleep(2)
#df_rca=df_rca.append(pd.Series([title,uid,name,score,summary],index=['TITLE','USER_ID','NAME','SCORE','SUMMARY']),ignore_index=True)
print('OK. Data cleaning is done.\n')
time.sleep(3)
################################################################################
######################    DATA CLEANING WORK ENDS, SIGH  #######################
################################################################################

###getting number of users OR unique names
unique_names=unique(name)
print('# of unique names are : ')
print(len(unique_names))
#for names in unique_names:#uncomment this and next lines to see names of each user
#	print names


df_rca.to_csv('/home/vetron/desktop/meme.csv',sep=',')
