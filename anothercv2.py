# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:28:20 2021

@author: CHAINZ
"""


import cv2
import numpy as np
import time
from matplotlib import pyplot as plt
import math
from random import randint


import pytesseract as ocr


ocr.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

def reconstruct(x):
    interval=[]
    # print("Xdx", x)
    n_terms=len(x)
    xx=[]
    for i in x:
        try:
            xx.append(float(i))
        except:
            if i=="":
                pass
            else:
                xx.append(0)
            
    x=xx
    for i in range(1,len(x)):
        try:
            difference=round(x[i]-x[i-1],len(str(x[i])))
            interval.append(difference)
        except:
            # interval.append("err")
            pass
    if interval!=[]:
        difference=[i for i in interval if interval.count(i)== max([interval.count(j) for j in interval])][0]
        # print(interval,"===",x)
        eligible_start=[x[i] for i in range(1,len(x)-1) if x[i]-x[i-1]==x[i+1]-x[i]==difference]
        # print(eligible_start,x)
        start=eligible_start[0]
        start_index=x.index(start)
        forward_distance_from_start=start_index
        backward_distance_from_start=len(x)-start_index
        # print(start-(forward_distance_from_start*difference))
        reconstructed_list=[i for i in np.arange(start-(forward_distance_from_start*difference),start, difference)]+[i for i in np.arange(start,start+(backward_distance_from_start*difference),difference)]
        print(reconstructed_list)
    return reconstructed_list

# def get_xscale(img):
#     resized_img=cv2.resize(img, None, fx=8, fy=5, interpolation=cv2.INTER_LANCZOS4)
#     ret,x= cv2.threshold(resized_img, 150, 225,0)
#     line=[]
#     # x=np.ndarray.tolist(x)
#     new_image=[x[0]]
#     countmax=0
#     for i in x:
#         countmax+=1
#         if np.count_nonzero(i==0)> i.size/2:
#             # z=[225 for j in range(len(i))]
#             new_image=x[countmax: ]
#             # print("===")
#             # print(len(z))
#         else:
#             # print("---")
#             # new_image=np.append(new_image,[i],axis=0)
#             # print(len(i))
#             pass
#     # print("new",new_image)
#     # cv2.imshow("new_image", new_image)
#     for i in new_image:
#     # x=np.ndarray.tolist(x)
#         new=np.array([i])
#         countmax=0
#         lines=[]
#         for i in new_image:
#             if np.count_nonzero(i==225)== i.size:
#                 # z=[225 for j in range(len(i))]
#                 new=np.append(new,[i], axis=0)
#                 # print("===")
#                 # print(len(z))
                
#                 if new.shape[0]>20  :
#                     if np.count_nonzero(new==0) > 20:
#                         # print("===")
#                         # print(new)
#                         lines.append(new)
#                     else:
#                         new=np.array([i])
#                 else:
#                     # print("new")
#                     if np.count_nonzero(new==0) > 20:
#                         # print("===")
#                         # print(new)
#                         lines.append(new)
#                     new=np.array([i])
#             elif len(lines)>8:
#                 # lines=lines[ : :-1]
#                 line=lines[-1]
#                 break
#                 break
#             else:
#                 # print("---")
#                 if new.size > 2:
#                     new=np.append(new,[i],axis=0)
#                 # print(len(i))
#             # print(new.shape)
#     # print(new,new_image)
#     # print("lines", lines)
#     if line==[]:
#         line=new_image
#     cv2.imshow("line_x", new_image)
#     if cv2.waitKey(0)==27:
#         cv2.destroyAllWindows()
#     a=ocr.image_to_string(line,config=r"--oem 3 --psm 7")
#     a=a.split("\n")[0:-1]
#     a=" ".join(a)
#     a=a.replace("O","0")
#     a=a.split(" ")
#     try:
        
#         # print(a)
#         a=[float(i) for i in a]
#         return(min(a),max(a))
#     except:
#         return (0,1)
#     # return(lines)

#     # return(new1)

def line_partition(x):    
    x=np.ndarray.tolist(x)
    # get positions of all the horizontal white spaces in the file
    whitespaces=[i for i in range(len(x)) if x[i].count(225)>len(x[i])*0.99]
    # get the whitespaces that bound text and characters in the file
    bounds=[[whitespaces[i-1],whitespaces[i]] for i  in range(1,len(whitespaces)) if whitespaces[i]-whitespaces[i-1] > 1]
    #smoothen up the returned boundaries 
    bounds=lines=[[i[0]-2, i[1]+3] for i in bounds if i[0]>2 and i[1]<len(x)-3]
    # print("bounds",bounds)
    return(bounds[0])

def line_partition_y(x):
    # totally similar to the previous function, dunno why i redefined it
    x=np.ndarray.tolist(x)
    # print(x)
    whitespaces=[i for i in range(len(x)) if x[i].count(225)>len(x[i])*0.999]
    # print("white", whitespaces)
    bounds=[[whitespaces[i-1],whitespaces[i]] for i  in range(1,len(whitespaces)) if whitespaces[i]-whitespaces[i-1] > 1]
    bounds=lines=[[i[0]-2, i[1]+3] for i in bounds if i[0]>2 and i[1]<len(x)-3]
    return(bounds[0])

def line_partition_char(x):
    # This function is meant to partition each line into a list of characters present in the lines for ocr...its not in use yet tho
    x=np.ndarray.tolist(x)
    # print(x)
    whitespaces=[i for i in range(len(x)) if x[i].count(225)>len(x[i])*0.999]
    # print("white", whitespaces)
    bounds=[[whitespaces[i-1],whitespaces[i]] for i  in range(1,len(whitespaces)) if whitespaces[i]-whitespaces[i-1] > 1]
    bounds=lines=[[i[0]-2, i[1]+3] for i in bounds if i[0]>2 and i[1]<len(x)-3]
    return(bounds)


# def get_yscale(img):
#     resized_img=cv2.resize(img, None, fx=7, fy=5, interpolation=cv2.INTER_LANCZOS4)
#     ret,thresh_img= cv2.threshold(resized_img, 150, 225,0)
#     x=np.transpose(thresh_img)[ : :-1]
#     new_image=[x[0]]
#     countmax=0
#     for i in x:
#         countmax+=1
#         if np.count_nonzero(i==0)> i.size/2:
#             # z=[225 for j in range(len(i))]
#             new_image=x[countmax: ]
#             # print("===")
#             # print(len(z))
#         else:
#             # print("---")
#             # new_image=np.append(new_image,[i],axis=0)
#             # print(len(i))
#             pass
#     # print("new",new_image)
#     for i in new_image:
#     # x=np.ndarray.tolist(x)
#         new=np.array([i])
#         countmax=0
#         lines=[]
#         for i in new_image:
#             if np.count_nonzero(i==225)== i.size:
#                 # z=[225 for j in range(len(i))]
#                 new=np.append(new,[i], axis=0)
#                 # print("===")
#                 # print(len(z))
                
#                 if new.shape[0]>20  :
#                     if np.count_nonzero(new==0) > 20:
#                         # print("===")
#                         # print(new)
#                         lines.append(np.transpose(new[ : :-1]))
#                     else:
#                         new=np.array([i])
#                 else:
#                     # print("new")
#                     if np.count_nonzero(new==0) > 20:
#                         # print("===")
#                         # print(new)
#                         lines.append(np.transpose(new[ : :-1]))
#                     new=np.array([i])
#             elif len(lines)>8:
#                 # lines=lines[ : :-1]
#                 line=lines[-1]
#                 break
#                 break
#             else:
#                 # print("---")
#                 if new.size > 2:
#                     new=np.append(new,[i],axis=0)
#                 # print(len(i))
#             # print(new.shape)
#     # print(new,new_image)
#     # print("lines", lines)
#     # print(line.shape[0]/4)
#     # cv2.imshow("line_y", line[int(line.shape[0]/2): ])
#     a=ocr.image_to_string(line,config=r"--oem 3 --psm 6")
#     # bb=open("ocr_check.txt", "w", encoding="utf8")
#     # print(a, file=bb)
#     # bb.close()
#     a=a.replace("O","0")
#     a=a.split("\n")[0:-1]
    
#     try:
#         a=[float(i) for i in a if i!=""]
#         # print(a)
#         return(min(a),max(a))
#     except:
#         return (0,1)

def distance(a,b):
    return(math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2))

# def clean_coordinates(x,y, frequency):
#     return([[x[i] for i in range(0, len(x),frequency)], [y[i] for i in range(0, len(y),frequency)], len(x)/frequency])

# def get_frequency(y):
#     frequencies=[y.count(i) for i in y]
#     modalfrequency=[frequency for frequency in frequencies if frequencies.count(frequency)==max([frequencies.count(frequency) for frequency in frequencies])]
#     # print(modalfrequency[0])
#     # return(max(frequencies))
#     return(modalfrequency[0])

def clean_coord(x,y,n):
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
            newx.append(prevx[0])
            # print(prevx,y_equivalent)
            newy.append(y_equivalent[n])
            prevx=[i]
            y_equivalent=[y[xindex]]
    
    return(newx,newy)
        
def horizon_erase(x):
    x=np.ndarray.tolist(x)
    new_image=[]
    countmax=0
    for i in x:
        #  if a pixel thick blackline is longer than half of the screen, take replace it with a white line
        if i.count(0)> 0.5*len(i):
            
            z=[225 for j in range(len(i))]
            new_image.append(z)
            # print("===")
            # print(len(z))
        else:
            # print("---")
            new_image.append(i)
            # print(len(i))
    # print("new",new_image)
    # print(new_image[0].count(0), len(new_image[0]))
    # cv2.imshow("horizone", np.array(new_image, dtype=np.uint8))
    return(new_image)

def vertice_erase(x):
    #  similar to horizone_erase but here the pictures get inverted first
    # x=np.ndarray.tolist(x)
    # unit_length= len(x[0])
    invertedx=np.transpose(x)
    new_image=[]
    invertedx=np.ndarray.tolist(invertedx)
    for i in invertedx:
        # print(np.count_nonzero(i==0),i.size)
        
        if i.count(0)> len(i)/2:
            z=[225 for j in range(len(i))]
            new_image.append(z)
            # print("===")
            # print(len(z))
        else:
            # print("---")
            new_image.append(i)
            # print(len(i))
    # print("new",new_image)
    # unit_length=new_image.shape[1]
    new_image=np.array(new_image)
    invertednew=np.transpose(new_image)
    return(invertednew)


def get_cordinates(x,grid_unit):
    # img=cv2.imread(x, cv2.IMREAD_GRAYSCALE)
    # ret,thresholded_image= cv2.threshold(img, 205, 225,0)

    # ungrided=np.array(horizon_erase(vertice_erase(thresholded_image)), dtype=np.uint8)
    cv2.imshow("auj",x)
    list_x=np.ndarray.tolist(x)
    # print("len",len(list_x[0]))
    mostappropriate_x=[0]
    mostappropriate_y=[0]
    count_y=0
    xx=[]
    yy=[]
    x_len= len(list_x[0])
    y_len= len(list_x)
    previous_index=[]
    for i in list_x:
        image=[]
        
        count_x=-1
        count_y+=1
        image.append(i)
        for j in i:
            count_x+=1
            #can't remember why i divided the grid_unit variable by 2 here
            if j==0 and (count_x)%int(grid_unit/2)==0:
                if previous_index==[]:
                    previous_index.append([count_x, y_len-count_y])
                else:
                    xx.append(count_x)
                    yy.append(y_len-count_y)
                    previous_index.append([count_x,y_len-count_y])
    
    mostappropriate_x=xx
    mostappropriate_y=yy
    # print("mostappropriate",yy)
             
    # frequencyy=get_frequency(yy)
    # cleaned=clean_coord(mostappropriate_x,mostappropriate_y,0)
    image=np.array(image,dtype=np.uint8)
    # cv2.imshow("hs", image)
    # plt.plot(xx,yy)
    # plt.show()
    # frequencyx=get_frequency(cleaned[0])
    # cleaned=clean_coord(cleaned[1], cleaned[0],-1)
    # plt.plot(cleaned[0], cleaned[1])
    # plt.plot()
    # plt.plot(mostappropriate_x,mostappropriate_y,"--r")
    # plt.show()
    return(mostappropriate_x,mostappropriate_y)
    # return(cleaned)


x=time.time()
# img=cv2.imread("graphed.png", cv2.IMREAD_GRAYSCALE)
# coordinates=get_cordinates("graphed.png")

# cv2.imshow("3xx3", thresholded_image)

# cv2.imshow("3x3", ungrided)

print(time.time() - x)

# if cv2.waitKey(0) == 27:
    # cv2.destroyAllWindows()