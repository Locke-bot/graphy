from django.shortcuts import render
from django.http import JsonResponse

import numpy as np
import cv2, time

import graphfunc as gp
# Create your views here.
prep_done = False
data, scalex, scaley, left, bottom, response = [None]*6

def HomeView(request):
    global data, scalex, scaley, left, bottom, prep_done, response
    template_name = 'home.html'
    if request.is_ajax():
        post = request.POST        
        if post.get('name') == 'sendImageData':
            prep_done = False
            scale_extractable = ''
            print('pre')
            # file = '2540.png'
            # img = cv2.imread(file)   
            rgb = post['rgb'] # in rgb format, string though.
            # rgb = eval(rgb)
            width, height = eval(post['dim'])
            rgb = rgb.split(',')
            rgb = list(map(int, rgb)) # faster than the list comprehension [int(i) for i in rgb]
            # print(len(rgb), 'after')
            eff = []
            for enum, i in enumerate(rgb, 1):
                if enum%4 == 0:
                    continue
                eff.append(i)
            
            data = np.array(eff, dtype=np.uint8).reshape((height, width, 3))
            data = cv2.cvtColor(data, cv2.COLOR_RGB2BGR)
            safari, left, bottom = gp.prep(data)
            scalex, scaley = gp.getscale(data, safari, left, bottom)
            
            if scalex:
                scale_extractable += 'x'
            if scaley:
                scale_extractable += 'y'
            if not scale_extractable:
                response = {'response': f'difference between intervals on both axes couldn\'t be extracted, please input manually'}
            
            elif len(scale_extractable) == 1:
                response = {'response': f'difference between intervals on the {scale_extractable} axis has been extracted\ndifference between intervals on the {"xy"[(list("xy").index(scale_extractable)+1)%2]} axis could not be extracted, \
                                     please input manually'}
                                     
            else: # both extracted successful
                response = {'response': f'difference between intervals on both axes has been extracted'}
            
            prep_done = True
            return JsonResponse(response)
            
        elif post.get('name') == 'getScale':
            # img, safari, left, bottom = gp.prep(data)
            # scalex, scaley = gp.getscale(data, safari, left, bottom)
            # print(scalex, scaley)
            print('here')
            while True:
                if prep_done:
                    return JsonResponse({'xunit': scalex, 'yunit': scaley, **response})
                print('Nope, don\'t exist yet')
                time.sleep(0.2)
        
        elif post.get('name') == 'getEqn':
            # dbtx distance between ticks in pixel, x axis.
            # dbty distance between ticks in pixel, y axis.     
            scalex, scaley = float(post['scalex']), float(post['scaley'])
            dbtx, dbty = post['dbtx'][0:-2], post['dbty'][0:-2]
            dbtx, dbty = int(dbtx), int(dbty)
            print(dbtx, dbty, left, bottom, scalex, scaley)
            
            # print(post['dbtx'], post['dbty'], type(post['dbty']))
            res = gp.getfunc(data, left, bottom, scalex, scaley, dbtx, dbty)
            return JsonResponse({'result': res})
    return render(request, template_name)

def TestView(request):
    template_name = "test.html"
    return render(request, template_name)
