import numpy as np
import h5py
data1=[]
label1=[]
data2=[]
label2=[]
for i in range(1533,2299):
#for i in range(3):
    q=str(i)+'.mat'
    print(q)
    with h5py.File(q,'r') as file:
        
        d=np.array(file['cjdata']['image'])
        m=np.array(file['cjdata']['label'])
        #d=d.reshape(1,256*256)
        #d=d.reshape(1,512*512)
        #print(d.shape)
        #print(len(d[0]),"1234444444444")
        if(len(d[0])==512):
            print("..")
            label1.append(m[0])
            data1.append(d.ravel())
        elif(len(d[0])==256):
            print("..")
            label2.append(m[0])
            data2.append(d.ravel())
        #label.append(m[0])
        #data.append(d.ravel())
        #data=np.append(data,d,axis=0)
data1=np.array(data1)
data2=np.array(data2)
label1=np.array(label1)
label2=np.array(label2)
#print(data.shape)
#print(label.shape,"===========")
np.savetxt('label1.csv',label1,delimiter=',')
np.savetxt('label2.csv',label2,delimiter=',')
np.savetxt('data2.csv',data2,delimiter=',')
np.savetxt('data1.csv',data1,delimiter=',')
