from PIL import Image

# assumes you have a test.jpg in the working directory!
def lala():
    picturearray = []
    for x in range(38):
        pic = Image.open('cell-re'+ str(x) +'.jpg')
        # load image data
        imgData = pic.load()

        r, g, b = 0, 0, 0
        count = 0
        for x in xrange(pic.size[0]):
            for y in xrange(pic.size[1]):
                tempr,tempg,tempb = imgData[x,y]

                r += tempr
                g += tempg
                b += tempb
                count = count +1

        c = (r, g, b)
        a = [r/count, g/count, b/count]
        picturearray.append(a) 
       
    #print picturearray
    return picturearray