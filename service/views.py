from django.core import serializers
from multiprocessing import context
from django.shortcuts import HttpResponse
from django.shortcuts import render
# Create your views here.


from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
import os
from pdf2image import convert_from_path
from django.conf import settings
import tensorflow as tf
from PIL import Image
import cv2
import numpy as np
from .models import ANNResult, CNNResult
import json
# Create your views here.


def index(request):
    return render(request, 'service/index.html')


def result(request):
    context = {
        'cnndata': CNNResult.objects.latest('id'),
        'anndata': ANNResult.objects.latest('id')
    }
    return render(request, 'service/result.html', context)


def annResult(request):
    data = ANNResult.objects.latest('id')
    context = {
        'data': data
    }
    return render(request, 'service/resultann.html', context)


def predict(request):
    if request.method == 'POST' and request.FILES['citra']:
        fs = FileSystemStorage()
        # get file from post method
        myfile = request.FILES['citra']
        fs.save(myfile.name, myfile)

        image = convert_from_path(settings.MEDIA_ROOT / myfile.name)
        image[0].save(settings.MEDIA_ROOT / 'foto.jpg', 'JPEG')

        fs.delete(settings.MEDIA_ROOT / myfile.name)

        print('FILE IS UPLOADING...')
        return redirect('cut')
    if request.method == 'GET':
        context = {}
        path = settings.MEDIA_ROOT / os.listdir(settings.MEDIA_ROOT)[0]
        img = tf.keras.preprocessing.image.load_img(path)
        image_arr = tf.keras.preprocessing.image.img_to_array(img)
        image_arr /= 255.

        inputs = [
            image_arr[:200, :492], image_arr[230:450, :492],
            image_arr[500:700, :492], image_arr[:200, 492:987],
            image_arr[230:450, 492:987], image_arr[500:700, 492:987],
            image_arr[:220, 987:1478], image_arr[230:480, 987:1478],
            image_arr[450:700, 987:1478], image_arr[:220, 1478:],
            image_arr[230:480, 1478:], image_arr[450:700, 1478:]
        ]

        for i in range(len(inputs)):
            inputs[i] = tf.image.resize(inputs[i], [32, 32])
            inputs[i] = tf.expand_dims(inputs[i], axis=0)

        model = tf.keras.models.load_model('cnn_model.h5')
        print('FILE IS PREDICTING...')
        result = model.predict(inputs)
        context['af'] = np.argmax(result[0])
        context['hr'] = result[1].flatten()[0]
        context['hc'] = np.argmax(result[2])
        context['re'] = np.argmax(result[3])
        context['qp'] = np.argmax(result[4])
        context['ql'] = np.argmax(result[5])
        context['ss'] = np.argmax(result[6])
        context['sc'] = np.argmax(result[7])
        context['si'] = np.argmax(result[8])
        context['sn'] = np.argmax(result[9])
        context['sl'] = np.argmax(result[10])
        context['qi'] = result[11].flatten()[0]
        context['qc'] = result[12].flatten()[0]
        context['tw'] = np.argmax(result[13])
        context['tl'] = np.argmax(result[14])
        context['td'] = result[15].flatten()[0]
        context['vs'] = np.argmax(result[16])
        context['as'] = np.argmax(result[17])
        context['js'] = np.argmax(result[18])
        context['uw'] = np.argmax(result[19])

        data = CNNResult(
            af=context['af'],
            hr=context['hr'],
            hc=context['hc'],
            re=context['re'],
            qp=context['qp'],
            ql=context['ql'],
            ss=context['ss'],
            sc=context['sc'],
            si=context['si'],
            sn=context['sn'],
            sl=context['sl'],
            qi=context['qi'],
            qc=context['qc'],
            tw=context['tw'],
            tl=context['tl'],
            td=context['td'],
            vs=context['vs'],
            ae=context['as'],
            js=context['js'],
            uw=context['uw']
        )
        data.save()
        return redirect('predict2')


def predict2(request):
    data = CNNResult.objects.latest('id')
    arr_data = np.array([
        data.af,
        data.hr,
        data.hc,
        data.re,
        data.qp,
        data.ql,
        data.ss,
        data.sc,
        data.si,
        data.sn,
        data.sl,
        data.qi,
        data.qc,
        data.tw,
        data.tl,
        data.td,
        data.vs,
        data.ae,
        data.js,
        data.uw
    ])
    arr_data = tf.expand_dims(arr_data, axis=0)

    model = tf.keras.models.load_model('annmodel.h5')
    print('ANNMODEL IS PREDICTING...')
    result = model.predict(arr_data)

    for i in range(len(result)):
        result[i] = np.argmax(result[i])

    data = ANNResult.objects.create(
        si=result[0],
        ta=result[1],
        br=result[2],
        lv=result[3],
        qr=result[4],
        lt=result[5],
        st=result[6],
        be=result[7],
        tx=result[8],
        ec=result[9],
    )
    data.save()
    return redirect('result')


def cut(request):
    im = Image.open(settings.MEDIA_ROOT / 'foto.jpg')
    left = 250
    top = 572
    right = 2216
    bottom = 1514

    im1 = im.crop((left, top, right, bottom))
    im1.save(settings.MEDIA_ROOT / 'foto.jpg')
    print('FILE IS CUTTING...')
    return redirect('denoising')


def denoising(request):
    f = 'E:/7. SEMESTER 7/Bismillah Skripsi/mysite/media/foto.jpg'
    img = cv2.imread(f, 0)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j] >= 100:
                img[i][j] = 255
            else:
                img[i][j] = 0
    cv2.imwrite(f, img)
    print('FILE IS DENOISING...')
    return redirect('predict')
