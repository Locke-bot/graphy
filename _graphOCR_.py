# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:15:34 2021

@author: CHAINZ
"""
import time
import cv2
import numpy as np
from anothercv import horizon_erase, vertice_erase, get_cordinates, get_xscale, get_yscale
from matplotlib import pyplot as plt
# import pytesseract as ocr

class Graph:
    def __init__(self, filematrix):
        self.file = filematrix
        rect, self.threshfile = cv2.threshold(filematrix, 205,225,0)
        # cv2.imshow('rr', self.threshfile)
        # cv2.imshow('rr', filematrix)
        # cv2.waitKey()
        self.mask=np.ones(np.shape (self.grid_removal()))*225

        # cv2.imshow("pp", np.transpose(self.threshfile)[ : :-1])
        # if cv2.waitKey(0)==27:
            # self.destroyAllWindows()
    
    
    def get_alphaOmegaX(self):
        rowindex=-1
        last_horizone= self.threshfile[1: ]
        # horizone_index=0
        for i in self.threshfile:
            rowindex+=1
            # print(np.size(i))
            if np.count_nonzero(i==0)>np.size(i)*0.7:
                last_horizone=self.threshfile[rowindex: ]
                # horizone_index=rowindex
        rowindex=-1
        for i in last_horizone:
            rowindex+=1
            if np.count_nonzero(i==225)==np.size(i):
                markersgrids=last_horizone[ :rowindex]
                break
        markersgrids=np.ndarray.tolist(markersgrids)
        z=markersgrids[int(len(markersgrids)/2)]
        z_reverse= z[ : :-1]
        
        return(z.index(0),len(z_reverse)-z_reverse.index(0))
    
    
    def get_alphaOmegaY(self):
        rowindex=-1
        inverted_file=np.transpose(self.threshfile)[ : :-1]
        last_horizone= inverted_file[1: ]
        horizone_index=0
        for i in inverted_file:
            rowindex+=1
            # print(np.size(i))
            if np.count_nonzero(i==0)>np.size(i)*0.7:
                last_horizone=inverted_file[rowindex: ]
                # horizone_index=rowindex
        rowindex=-1
        for i in last_horizone:
            rowindex+=1
            if np.count_nonzero(i==225)==np.size(i):
                markersgrids=last_horizone[ :rowindex]
                break
        markersgrids=np.ndarray.tolist(markersgrids)
        z=markersgrids[int(len(markersgrids)/2)]
        z_reverse= z[ : :-1]
        
        return(z.index(0),len(z_reverse)-z_reverse.index(0))
        pass
    
    
    def segment(self):
        xseg=self.get_alphaOmegaX()
        yseg=self.get_alphaOmegaY()
        # self.segmented=np.array([i[xseg[0]: xseg[1]] for i in self.threshfile])
        self.segmented=np.transpose(np.transpose(self.threshfile)[xseg[0]:xseg[1]])[yseg[0]:yseg[1]]
        return(self.segmented)
    
    
    def grid_removal(self):
        return np.array(horizon_erase(vertice_erase(self.segment())), dtype=np.uint8)   
    
    def horizontal_grid_mask(self):
        self.grided_file=[]
        indexcount=-1
        tempfile=np.ndarray.tolist(self.mask)
        for i in self.mask:
            indexcount+=1
            if indexcount%4==0:
                self.grided_file.append([100 for j in range(len(i))])
            else:
                self.grided_file.append(i)
        return(np.array(self.grided_file, dtype= "uint8"))
    
    def vertical_grid_mask(self,filemat):
        self.grided_file=[]
        indexcount=-1
        filemat=np.transpose(filemat)
        tempfile=np.ndarray.tolist(filemat)
        for i in filemat:
            indexcount+=1
            if indexcount%4==0:
                self.grided_file.append([100 for j in range(len(i))])
            else:
                self.grided_file.append(i)
        return(np.transpose(np.array(self.grided_file, dtype= "uint8")))
    
    def create_mask_self(self):
        return self.vertical_grid_mask(self.horizontal_grid_mask())
    
    def copulate(self):
        return cv2.bitwise_and(self.grid_removal(), self.create_mask_self())
    
    def interpolate(self,x, Xinit, Xfin):
        Tlen=Xfin- Xinit
        Xlen=max(x) -min(x)
        rescaled=[Xinit + (i-min(x))*Tlen/Xlen for i in x]
        return rescaled
        # return([(((i-x[0])*(xfin-xinit))/(x[-1]-x[0])) +xinit for i in x])
    
    def get_axis_x(self):
        boundary=self.get_alphaOmegaY()
        axis=np.array(self.file[boundary[1]: ], dtype=np.uint8)
        realfile=np.array(self.file[boundary[1]: ], dtype=np.uint8)
        realfile=get_xscale(realfile)
        # a=ocr.image_to_string(realfile,config=r"--oem 3 --psm 7")
        # a=a.split("\n")[0:-1]
        # a=" ".join(a)
        # a=a.replace("O","0")
        # a=a.split(" ")
        print("x",realfile)
        return(realfile)
    def get_axis_y(self):
        boundary=self.get_alphaOmegaX()
        img=np.transpose(np.transpose(self.file)[ :boundary[0]])
        xscale=get_yscale(img)
        return(xscale)
    def de_noise(self, x,y,n):
        frequencyx={i:x.count(i) for i in x}
        frequencyy={i:y.count(i) for i in y}
        newx=[]
        newy=[]
        prevx=[x[0]]
        y_equivalent=[]
        xindex=-1
        for i in x:
            xindex+=1
            if i == prevx[0]:
                prevx.append(i)
                y_equivalent.append(y[xindex])
                # print(prevx,y_equivalent)
                # print("=========")
            else:
                if len(prevx)<3:
                    newx.append(prevx[0])
                    # print(prevx,y_equivalent)
                    newy.append(y_equivalent[n])
                    prevx=[i]
                    y_equivalent=[y[xindex]]
                else:
                    newy=newy+ y_equivalent
                    newx=newx+prevx
                    prevx=[i]
                    y_equivalent=[y[xindex]]
        return(newx,newy)
        
    def get_coordinates(self):
        cordinates=get_cordinates(self.grid_removal())
        X=[i/4 for i in cordinates[0]]
        Y=[i/4 for i in cordinates[1]]
        xaxis=get_xscale(self.file)
        yaxis=get_yscale(self.file)
        X=self.interpolate(X,xaxis[0], xaxis[1])
        Y=self.interpolate(Y,yaxis[0], yaxis[1])
        # denoised= self.de_noise(Y,X,-1)
        # print(X,Y)
        return(X,Y)
    
z= time.time()       
img= cv2.imread("x_square.png", cv2.IMREAD_GRAYSCALE)    
x= Graph(img)
# cv2.imshow("seg", x.grid_removal())
# print( x.get_axis_x())
# print(x.get_axis_y())
# cv2.imshow("omw", x.copulate())
cor=x.get_coordinates()
plt.plot(cor[0], cor[1])
plt.grid(True)
plt.show()
print(time.time()-z)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()