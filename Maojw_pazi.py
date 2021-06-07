import numpy as np
import seaborn as sns

#read file
import psrchive
import pylab as plt


mask_file_path="your mask.txt path"
mask_file=open(mask_file_path,"r")
kill_chans=np.array(mask_file.read().splitlines()).astype(int)
kill_mask = np.ones(512, dtype=np.bool)
kill_mask[kill_chans]= False

ar=psrchive.Archive_load("your ar path")
dm=ar.get_dispersion_measure()
print("dm= ",dm)
ar.dedisperse()
ar.pscrunch()
ar.remove_baseline()
data_raw=ar.get_data()
print("raw data shape",data_raw.shape)
#ar.fscrunch()
data_sub_ph=data_raw.mean(axis=2,keepdims=True)
print("color map of sub vs ph")
sns.heatmap(data_sub_ph[:,0,0,:],cmap="autumn").invert_yaxis()
plt.show()
data_freq_sub=data_raw.mean(axis=0,keepdims=True)
#ar.tscrunch()

#move the pulse profile peak to centre
#ar.centre()
print("color map of freq vs ph")
sns.heatmap(data_freq_sub[0,0,:,:],cmap="autumn").invert_yaxis()
plt.show()
#ar.fscrunch()
#data=ar.get_data()
print("show pulse profile")
data_profile_ph=data_raw.mean(axis=0,keepdims=True).mean(axis=2,keepdims=True)
plt.plot(data_profile_ph[0,0,0,:])
plt.show()

print("finish !")


