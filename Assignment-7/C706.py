import threading
import requests
def img_download(url):
    img_url = requests.get(url)
    name = url.split('/')[7]
    f = open(name, 'wb')
    f.write(img_url.content)
    f.close()
url_list=['https://upload.wikimedia.org/wikipedia/commons/d/db/Pelagic_stingray_fukushima.jpg'
    ,'https://upload.wikimedia.org/wikipedia/commons/d/dd/Loligo_vulgaris.jpg'
    ,'https://upload.wikimedia.org/wikipedia/commons/8/8e/Winter_Pigeons_Cropped_DOF.jpg'
    ,'https://upload.wikimedia.org/wikipedia/commons/0/08/NautilusCutawayLogarithmicSpiral.jpg'
    ,'https://upload.wikimedia.org/wikipedia/commons/1/11/Mosquito_Tasmania_crop.jpg']
threads=[]
for url in url_list:
    thread=threading.Thread(target=img_download,args=(url,))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()