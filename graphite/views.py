from django.shortcuts import render
from django.http import JsonResponse

import numpy as np
import cv2
# Create your views here.

def HomeView(request):
    template_name = 'home.html'
    if request.is_ajax():
        post = request.POST
        print(post, 'postal service')
        if post.get('name') == 'array':
            # file = r"C:/Users/ZAINAB/Downloads/Telegram Desktop/DataExport_2021-04-22/images/section_sessions.png"
            file = r"C:/Users/ZAINAB/Downloads/Telegram Desktop/alien.png"
            arr = cv2.imread(file)
            rgb = post['rgb'] # in rgb format, string though.
            rgb = eval(rgb)
            width, height = eval(post['dim'])
            eff = []
            for enum, i in enumerate(rgb, 1):
                if enum%4 == 0:
                    continue
                eff.append(i)
            f = np.array(eff, dtype=np.uint8).reshape((height, width, 3))
            f = cv2.cvtColor(f, cv2.COLOR_RGB2BGR)
            print((f==arr).all())
            return JsonResponse({'status': 'seen'})
    return render(request, template_name)