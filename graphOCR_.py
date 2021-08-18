# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:15:34 2021

@author: CHAINZ
"""
import time
import cv2
import numpy as np
from anothercv2 import distance, horizon_erase,reconstruct, clean_coord,line_partition, line_partition_y,vertice_erase,get_cordinates
from matplotlib import pyplot as plt
import pytesseract as ocr

class Graph:
    def __init__(self, filematrix,gridunit):
        self.file= filematrix
        rect,self.threshfile=cv2.threshold(filematrix, 205, 225, 0)
        self.mask=np.ones(np.shape (self.grid_removal()))*225
        self.gridunit=gridunit
        # cv2.imshow("pp", np.transpose(self.threshfile)[ : :-1])
        # if cv2.waitKey(0)==27:
            # self.destroyAllWindows()
    
    
    def get_alphaOmegaX(self):
        rowindex=-1
        last_horizone= self.threshfile[1: ]
        horizone_index=0
        for i in self.threshfile:
            rowindex+=1
            # print(np.size(i))
            
            if np.count_nonzero(i==0)>np.size(i)*0.7: 
                #if a pixel thick black line is longer than 70% of the image width
                # it should be subsequently removed, prolly a grid
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
            if np.count_nonzero(i==0)>np.size(i)*0.7: #if a pixel thick black line is longer than 70% of the image width
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
    
    
    def horizontal_grid_mask(self): #irrelevant function...just to visualize the grids
        self.grided_file=[]
        indexcount=-1
        tempfile=np.ndarray.tolist(self.mask)
        for i in self.mask:
            indexcount+=1
            if indexcount%self.gridunit==0:
                self.grided_file.append([100 for j in range(len(i))])
            else:
                self.grided_file.append(i)
        return(np.array(self.grided_file, dtype= "uint8"))
    
    
    def vertical_grid_mask(self,filemat): # a sister function to the horizontal_grid_mask function
        self.grided_file=[]
        indexcount=-1
        filemat=np.transpose(filemat)
        tempfile=np.ndarray.tolist(filemat)
        for i in filemat:
            indexcount+=1
            if indexcount%self.gridunit==0:
                self.grided_file.append([100 for j in range(len(i))])
            else:
                self.grided_file.append(i)
        return(np.transpose(np.array(self.grided_file, dtype= "uint8")))
    
    
    def create_mask_self(self): #to create the grids
        return self.vertical_grid_mask(self.horizontal_grid_mask())
    
    
    def copulate(self): #returns an image matrix of the grided file
        return cv2.bitwise_and(self.grid_removal(), self.create_mask_self())
    
    
    def interpolate(self,x, Xinit, Xfin,mat_shape): #to interpolate between the minimum and maximum of the axis
        Tlen=Xfin- Xinit
        Xlen=mat_shape/self.gridunit
        rescaled=[Xinit + (i)*Tlen/Xlen for i in x]
        return rescaled
        # return([(((i-x[0])*(xfin-xinit))/(x[-1]-x[0])) +xinit for i in x])
    
    def get_axis_x(self): #to get the minimum and maximum of the axis
        boundary=self.get_alphaOmegaY()
        axis=self.threshfile[boundary[1]: ]
        real_axis=self.file[boundary[1]: ]
        
        lines=line_partition(axis)
        real_axis=real_axis[lines[0]:lines[1]]
        # print("whiteee", line_partition(axis))
        resized=cv2.resize(real_axis, None, fx=3, fy=3, interpolation=cv2.INTER_LANCZOS4)
        rect,threshed=cv2.threshold(resized,185,225,0)
        # cv2.imshow("axis", threshed)
        realfile=np.array(self.file[boundary[1]: ], dtype=np.uint8)
        # realfile=get_xscale(realfile)
        a=ocr.image_to_string(resized,config=r"--oem 3 --psm 6")
        a=a.split("\n")[0:-1]
        a="".join(a)
        a=a.split(" ")
        # print("x",a)
        cv2.imshow("thr", resized)
        # a=reconstruct(a)
        try:
            # print("xx",a,len(a))
            a=reconstruct(a)
            # print("xx",a,len(a))
            return(min(a), max(a))
        except:
            return(0.0,1.0)
        # a=a.replace("O","0")
        # a=a.split(" ")
        
        # return(realfile)

    def get_axis_y(self):#to get minimum and maximum of the y_axis
        boundary=self.get_alphaOmegaX()
        img=np.transpose(self.threshfile)[ :boundary[0]][ : :-1]
        realfile=np.transpose(self.file)[ :boundary[0]][ : :-1]
        line=line_partition_y(img)
        # print(line)
        img=np.transpose(img[line[0]:line[1]][ : :-1])
        realfile=np.transpose(realfile[line[0]:line[1]][ : :-1])
        resized=cv2.resize(realfile, None, fx=8, fy=8, interpolation=cv2.INTER_LANCZOS4)
        rect,threshed=cv2.threshold(resized,150,225,0)
        a=ocr.image_to_string(threshed,config=r"--oem 3 --psm 6")
        # bb=open("ocr_check.txt", "w", encoding="utf8")
        # print(a, file=bb)
        # bb.close()
        # cv2.imshow("thr",threshed)
        a=a.replace("O","0")
        a=a.split("\n")[0:-1]
        # print("ds", a)
        # cv2.imshow("axcy", threshed)
        # a=reconstruct(a[ : :-1])
        # print("x",a,len(a))
        try:
            a=reconstruct(a[ : :-1])
            # print("x--",a,len(a))
            return(min(a), max(a))
        except:
            return(0.0,1.0)
        
        # xscale=get_yscale(img)
        # return(xscale)

    def de_noise(self, x,y,n): #irrelevant
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
        
    def get_coordinates(self): # get the coordinates
        cordinates=get_cordinates(self.grid_removal(),self.gridunit)
        # cv2.imshow("ddd",self.segment())
        self.shape=self.grid_removal().shape
        # print("shape", self.shape)
        X=[i/self.gridunit for i in cordinates[0]] #normalize the values to the scope of the grid units
        Y=[i/self.gridunit for i in cordinates[1]] #same
        # print("x without interpolation",X)
        xaxis=self.get_axis_x()
        yaxis=self.get_axis_y()
        points=[[X[i],Y[i]] for i in range(len(X))]
        points.sort()
        new_point_=[]
        len_points=0
        for start in range(int(len(points)/4)): #check all the way to a quarter of the img matrix vertically for the head of the graph
            new_points=[]
            for i in points[start: ]:
                if new_points==[]:
                    new_points.append(points[start])
                else:
                    if distance(i,new_points[-1])<0.2*self.gridunit: #confine the code to only read points from the graph, outliers should be left out
                        new_points.append(i)
            # new_points_list.append(new_points)
            if len(new_points)> len_points:
                # print("new", new_points)
                new_points_=new_points
                len_points=len(new_points_)
        # print(points)
        # print(new_points)
        # print("==--==")
        # print(Y)
        new_points=new_points_
        X=[i[0] for i in new_points]
        Y=[i[1] for i in new_points]
        # cv2.imshow("gd", self.grid_removal())
        X=self.interpolate(X,xaxis[0], xaxis[1],self.shape[1])
        Y=self.interpolate(Y,yaxis[0], yaxis[1],self.shape[0])
        # denoised= self.de_noise(Y,X,-1)
        clean=clean_coord(X,Y,0)
        # print(X,Y)
        return(clean[0],clean[1])

            
    
    
    
    
    
    
    
    
class Graph2:


    def __init__(self, filematrix,gridunit, x_axis, y_axis):
        self.file= filematrix
        rect,self.threshfile=cv2.threshold(filematrix, 205,225,0)
        self.mask=np.ones(np.shape (self.grid_removal()))*225
        self.gridunit=gridunit
        self.x=x_axis
        self.y=y_axis
        self.axis=[self.x, self.y]
        # cv2.imshow("pp", np.transpose(self.threshfile)[ : :-1])
        # if cv2.waitKey(0)==27:
            # self.destroyAllWindows()
    
    
    def get_alphaOmegaX(self):
        rowindex=-1
        last_horizone= self.threshfile[1: ]
        horizone_index=0
        for i in self.threshfile:
            rowindex+=1
            # print(np.size(i))
            
            if np.count_nonzero(i==0)>np.size(i)*0.7: #if a pixel thick black line is longer than 70% of the image width
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
            if np.count_nonzero(i==0)>np.size(i)*0.7: #if a pixel thick black line is longer than 70% of the image width
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
    
    
    def horizontal_grid_mask(self): #irrelevant function...just to visualize the grids
        self.grided_file=[]
        indexcount=-1
        tempfile=np.ndarray.tolist(self.mask)
        for i in self.mask:
            indexcount+=1
            if indexcount%self.gridunit==0:
                self.grided_file.append([100 for j in range(len(i))])
            else:
                self.grided_file.append(i)
        return(np.array(self.grided_file, dtype= "uint8"))
    
    
    def vertical_grid_mask(self,filemat): # a sister function to the horizontal_grid_mask function
        self.grided_file=[]
        indexcount=-1
        filemat=np.transpose(filemat)
        tempfile=np.ndarray.tolist(filemat)
        for i in filemat:
            indexcount+=1
            if indexcount%self.gridunit==0:
                self.grided_file.append([100 for j in range(len(i))])
            else:
                self.grided_file.append(i)
        return(np.transpose(np.array(self.grided_file, dtype= "uint8")))
    
    
    def create_mask_self(self): #to create the grids
        return self.vertical_grid_mask(self.horizontal_grid_mask())
    
    
    def copulate(self): #returns an image matrix of the grided file
        return cv2.bitwise_and(self.grid_removal(), self.create_mask_self())
    
    
    def interpolate(self,x,axis): #to interpolate between the minimum and maximum of the axis
        # Tlen=Xfin- Xinit
        Tlen=self.axis[axis][1]-self.x[0]
        Xlen=max(x)-min(x)
        rescaled=[self.axis[axis][0] + (i-min(x))*Tlen/Xlen for i in x]
        return rescaled
        # return([(((i-x[0])*(xfin-xinit))/(x[-1]-x[0])) +xinit for i in x])
    
    def get_axis_x(self): #to get the minimum and maximum of the axis
        boundary=self.get_alphaOmegaY()
        axis=self.threshfile[boundary[1]: ]
        real_axis=self.file[boundary[1]: ]
        
        lines=line_partition(axis)
        real_axis=real_axis[lines[0]:lines[1]]
        # print("whiteee", line_partition(axis))
        resized=cv2.resize(real_axis, None, fx=3, fy=3, interpolation=cv2.INTER_LANCZOS4)
        rect,threshed=cv2.threshold(resized,185,225,0)
        # cv2.imshow("axis", threshed)
        realfile=np.array(self.file[boundary[1]: ], dtype=np.uint8)
        # realfile=get_xscale(realfile)
        a=ocr.image_to_string(resized,config=r"--oem 3 --psm 6")
        a=a.split("\n")[0:-1]
        a="".join(a)
        a=a.split(" ")
        # print("x",a)
        cv2.imshow("thr", resized)
        # a=reconstruct(a)
        try:
            # print("xx",a,len(a))
            a=reconstruct(a)
            # print("xx",a,len(a))
            return(min(a), max(a))
        except:
            return(0.0,1.0)
        # a=a.replace("O","0")
        # a=a.split(" ")
        
        # return(realfile)

    def get_axis_y(self):#to get minimum and maximum of the y_axis
        boundary=self.get_alphaOmegaX()
        img=np.transpose(self.threshfile)[ :boundary[0]][ : :-1]
        realfile=np.transpose(self.file)[ :boundary[0]][ : :-1]
        line=line_partition_y(img)
        # print(line)
        img=np.transpose(img[line[0]:line[1]][ : :-1])
        realfile=np.transpose(realfile[line[0]:line[1]][ : :-1])
        resized=cv2.resize(realfile, None, fx=8, fy=8, interpolation=cv2.INTER_LANCZOS4)
        rect,threshed=cv2.threshold(resized,150,225,0)
        a=ocr.image_to_string(threshed,config=r"--oem 3 --psm 6")
        # bb=open("ocr_check.txt", "w", encoding="utf8")
        # print(a, file=bb)
        # bb.close()
        # cv2.imshow("thr",threshed)
        a=a.replace("O","0")
        a=a.split("\n")[0:-1]
        # print("ds", a)
        # cv2.imshow("axcy", threshed)
        # a=reconstruct(a[ : :-1])
        # print("x",a,len(a))
        try:
            a=reconstruct(a[ : :-1])
            # print("x--",a,len(a))
            return(min(a), max(a))
        except:
            return(0.0,1.0)
        
        # xscale=get_yscale(img)
        # return(xscale)

    def de_noise(self, x,y,n): #irrelevant
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
        
    def get_coordinates(self): # get the coordinates
        cordinates=get_cordinates(self.grid_removal(),self.gridunit)
        # cv2.imshow("ddd",self.segment())
        self.shape=self.grid_removal().shape
        # print("shape", self.shape)
        X=[i/self.gridunit for i in cordinates[0]] #normalize the values to the scope of the grid units
        Y=[i/self.gridunit for i in cordinates[1]] #same
        # print("x without interpolation",X)
        xaxis=self.get_axis_x()
        yaxis=self.get_axis_y()
        points=[[X[i],Y[i]] for i in range(len(X))]
        points.sort()
        new_point_=[]
        len_points=0
        for start in range(int(len(points)/4)): #check all the way to a quarter of the img matrix vertically for the head of the graph
            new_points=[]
            for i in points[start: ]:
                if new_points==[]:
                    new_points.append(points[start])
                else:
                    if distance(i,new_points[-1])<0.2*self.gridunit: #confine the code to only read points from the graph, outliers should be left out
                        new_points.append(i)
            # new_points_list.append(new_points)
            if len(new_points)> len_points:
                # print("new", new_points)
                new_points_=new_points
                len_points=len(new_points_)
        # print(points)
        # print(new_points)
        # print("==--==")
        # print(Y)
        new_points=new_points_
        X=[i[0] for i in new_points]
        Y=[i[1] for i in new_points]
        # cv2.imshow("gd", self.grid_removal())
        X=self.interpolate(X,0)
        Y=self.interpolate(Y,1)
        # denoised= self.de_noise(Y,X,-1)
        clean=clean_coord(X,Y,0)
        # print(X,Y)
        return(clean[0],clean[1])
