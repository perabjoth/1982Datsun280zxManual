import base64
from bs4 import BeautifulSoup

with open("Oldindex.html") as fp:
    soup = BeautifulSoup(fp, features="html.parser")
    images = soup.select("div.pf")#pf128 > div.pc.pc128.wc.h8.opened > img
    for image in images:
        imageName = 'img/'+image['data-page-no']+'.png'
        print(imageName)
        for child in image.descendants:
            if child.name == "img":
                imgWrite = open(imageName, "wb")
                imageString = str(child['src']).replace("data:image/png;base64,", "")
                imageData = base64.b64decode(imageString)
                imgWrite.write(imageData)
                imgWrite.close()
                
                child['src'] = imageName
    
    f = open("sampleIndex.html", "w")
    f.write(str(soup))
    f.close()
