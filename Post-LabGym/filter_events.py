'''
This script is used to filter out the continued behavior events in the 
'all_events.xlsx' output by LabGym analysis so that it resembles how
the 'count' of the behaviors is presented.

For example, if an episode of  behavior 'A' lasts for several frames in 
the 'all_events.xlsx' sheet, this script will output a modiefied 
'filtered_all_events.xlsx' in which the behavior 'A' only shows once at 
the first frame of this episode.


How to use:
Use 'cd' command to navigate to where this script locates,
then type 'python3 filter_events.py'


dependencies:

numpy
pandas

python3 -m pip install numpy pandas
'''




###################################################################
# to customize by users

path_to_events='path to the all_events.xlsx'
out_path='the output path'

###################################################################



import os
import numpy as np
import pandas as pd



def filter_events(path_to_events,out_path):

	df=pd.read_excel(path_to_events)

	event_probability={}
	time_points=[]

	for col_name,col in df.items():

		if col_name=='time/ID':

			time_points=[float(i) for i in col]

		else:

			previous_behavior=None
			idx=int(col_name)
			event_probability[idx]=[np.nan]*len(time_points)
			for n,i in enumerate(col):
				event=eval(i)
				behavior=event[0]
				if behavior!='NA':
					if behavior!=previous_behavior:
						previous_behavior=behavior
						event_probability[idx][n]=event

	events_df=pd.DataFrame(event_probability,index=time_points)
	events_df.to_excel(os.path.join(out_path,'filtered_all_events.xlsx'),float_format='%.2f',index_label='time/ID')



filter_events(path_to_events,out_path)

