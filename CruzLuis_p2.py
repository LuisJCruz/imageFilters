import copy

'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is an inverted version of the input image. 
'''
def invert(image):
    imagecopy=copy.deepcopy(image)
    Li=len(imagecopy)
    Lj=len(imagecopy[0])
    for r in range(0,Li):
        for c in range(0,Lj):
            imagecopy[r][c]=255-imagecopy[r][c]
    return imagecopy


'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a blurred version of the input image. The blur function 
    uses a weighted kernel which is applied the pixels centered on 
    image[i][j]. The value in the kernel is multiplied by the corresponding
    pixels in the image and the eighted average is used as new_image[i][j].
'''
import copy
def blur(image):
  kernel = [
        [1, 1, 1],
        [1, 7, 1],
        [1, 1, 1],
    ]
  
  imagecopy=copy.deepcopy(image)
  imagecopy2=copy.deepcopy(image)
  Li=len(imagecopy)
  Lj=len(imagecopy[0])
  for y in range(0,Li):
    for x in range(0,Lj):       
      if x==0 or x==len(imagecopy[y])-1 or y==0 or y==len(imagecopy)-1:
        imagecopy2[y][x]=0
      else:
        weighted_sum=(
          imagecopy[y-1][x-1]*kernel[0][0]+imagecopy[y-1][x]*kernel[0][1]+imagecopy[y-1][x+1]*kernel[0][2]+
          imagecopy[ y ][x-1]*kernel[1][0]+imagecopy[ y ][x]*kernel[1][1]+imagecopy[ y ][x+1]*kernel[1][2]+
          imagecopy[y+1][x-1]*kernel[2][0]+imagecopy[y+1][x]*kernel[2][1]+imagecopy[y+1][x+1]*kernel[2][2])

        total_weights=(
          kernel[0][0]+kernel[0][1]+kernel[0][2]+
          kernel[1][0]+kernel[1][1]+kernel[1][2]+
          kernel[2][0]+kernel[2][1]+kernel[2][2])
        
        weighted_average= weighted_sum//total_weights
        imagecopy2[y][x]=weighted_average

  return imagecopy2
'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a vertically flipped version of the input image. 
'''
def flip(image):
    imagecopy=image[:]
    return imagecopy[::-1]

'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a 2x2 tiled version of the input image. The tile function
    will group pixels in groups of 4 and map each one to one of the 4 tiles
    based on their relative position in the group. 
'''
import copy
def tile(image):
  imagecopy=copy.deepcopy(image)
  tileimage=[]
  Li=len(imagecopy)
  Lj=len(imagecopy[0])
  
  tile1=[]
  for r in range(0,Li,2):
    r1=[]
    for c in range(0,Lj,2):
      r1.append(imagecopy[r][c])
    tile1.append(r1)

  tile2=[]
  for r in range(0,Li,2):
    r2=[]
    for c in range(1,Lj,2):
      r2.append(imagecopy[r][c])
    tile2.append(r2)

  tile3=[]
  for r in range(1,Li,2):
    r3=[]
    for c in range(0,Lj,2):
      r3.append(imagecopy[r][c])
    tile3.append(r3)
  
  tile4=[]
  for r in range(1,Li,2):
    r4=[]
    for c in range(1,Lj,2):
      r4.append(imagecopy[r][c])
    tile4.append(r4)

  for r in range(len(tile1)):
    tile1_2sum=tile1[r]+tile2[r]
    tileimage.append(tile1_2sum)

  for r in range(len(tile1)):
    tile3_4sum=tile3[r]+tile4[r]
    tileimage.append(tile3_4sum)

  return tileimage














