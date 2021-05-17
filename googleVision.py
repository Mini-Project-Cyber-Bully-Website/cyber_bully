import os, io
from google.cloud import vision
import pandas as pd
from PIL import Image,ImageFilter
from datetime import datetime


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'booming-coast-313509-bb494bed1251.json'
client=vision.ImageAnnotatorClient()
def googleVision():
    # FILE_NAME= 'demoImage.jpeg'
    FILE_NAME= 'cussWords.jpg'
    # FOLDER_PATH=r'C:\Users\HP\Documentss\miniproject_sem6'
    # FOLDER_PATH=r'C:\\Users\\acer\\Desktop\\Divyesh\\Projects\\college_projects\\Mini_project_organisation\\cyber_bully\\'
    FOLDER_PATH=r'C:\\Users\\acer\\Desktop\\Divyesh\\Projects\\college_projects\\Mini_project_organisation\\cyber_bully'

    with io.open (os.path.join(FOLDER_PATH,FILE_NAME),'rb') as image_file:
        content=image_file.read()

    image=vision.Image(content=content) 
    response=client.text_detection(image=image)   
    texts=response.text_annotations
    # print(texts)
    a=(texts[0].description)
    la = (texts[0].description.split())
    print(a)
    return check_special_character(a, cuss_words_list, la, texts)
    # ogimage=Image.open(r'C:\\Users\\acer\\Desktop\\Divyesh\\Projects\\college_projects\\Mini_project_organisation\\cyber_bully\\demoImage.jpeg')
    # ogimage=Image.open(image_file.name)
    # li = []
    # for i in range(len(a)):
    #     if a[i] == 'THE':

    #         c=i
    # og_image_with_path = r'C:\\Users\\acer\\Desktop\\Divyesh\\Projects\\college_projects\\Mini_project_organisation\\cyber_bully\\demoImage.jpeg'
    # def blur_image(og_image_with_path,c):
    #     a1=texts[c+1].bounding_poly.vertices[0].x
    #     a2=texts[c+1].bounding_poly.vertices[0].y
    #     b1=texts[c+1].bounding_poly.vertices[2].x
    #     b2=texts[c+1].bounding_poly.vertices[2].y

    #     # ogimage=Image.open(r'C:\\Users\\acer\\Desktop\\Divyesh\\Projects\\college_projects\\Mini_project_organisation\\cyber_bully\\demoImage.jpeg')
    #     ogimage = Image.open(og_image_with_path)
    #     cropped_image=ogimage.crop((a1,a2,b1,b2))
    # # cropped_image.show()
    #     blurred_image=cropped_image.filter(ImageFilter.GaussianBlur(radius=30))
    #     ogimage.paste(blurred_image,(a1,a2,b1,b2))
    #     return ogimage

    # print(texts[c+1].bounding_poly)
    # print(c)
    # bounds=[]
    #         a1=texts[c+1].bounding_poly.vertices[0].x
    #         a2=texts[c+1].bounding_poly.vertices[0].y
    #         b1=texts[c+1].bounding_poly.vertices[2].x
    #         b2=texts[c+1].bounding_poly.vertices[2].y

    #         cropped_image=ogimage.crop((a1,a2,b1,b2))
    #         # cropped_image.show()
    #         blurred_image=cropped_image.filter(ImageFilter.GaussianBlur(radius=30))
    #         opimage = ogimage.paste(blurred_image,(a1,a2,b1,b2))
    #         ogimage.save(result_image_path+'im {}.jpeg'.format(i))
    #         li.append(result_image_path+'im {}.jpeg'.format(i))
    #         ogimage = Image.open(result_image_path+'im {}.jpeg'.format(i))

    # for j in range(len(li)-1):
    #     os.remove(li[j])


    # ans = blur_image(og_image_with_path, c)
    # ans.show()




########################## Detecting Cuss Words #####################
def blur_word(a_word, la, texts):
    imgg = Image.open(r'C:\\Users\\acer\\Desktop\\Divyesh\\Projects\\college_projects\\Mini_project_organisation\\cyber_bully\\cussWords.jpg')
    c = la.index(a_word)
    a1=texts[c+1].bounding_poly.vertices[0].x
    a2=texts[c+1].bounding_poly.vertices[0].y
    b1=texts[c+1].bounding_poly.vertices[2].x
    b2=texts[c+1].bounding_poly.vertices[2].y
    cropped_image=imgg.crop((a1,a2,b1,b2))
    # cropped_image.show()
    blurred_image=cropped_image.filter(ImageFilter.GaussianBlur(radius=30))
    opimage = imgg.paste(blurred_image,(a1,a2,b1,b2))
    return imgg

    
def convert_cuss_word_to_stars(a_word):
    final_starred_word = "*" * len(a_word)
    return final_starred_word

def check_for_special_character(a_word):
    for j in a_word:
        if j.isalpha()==False:
            return True


def check_if_actually_a_cussword(a_word,cuss_words_list):
    thatword=""
    for k in a_word:
        if k.isalpha()==True:
                thatword+=k
    if thatword in a_word and thatword in cuss_words_list:
        return True
    else:
        return False



def check_special_character(a_string, cuss_words_list, la, texts):
    list_of_words_from_string = a_string.split()
    for a_word in list_of_words_from_string:
        if a_word.lower() in cuss_words_list:
            list_of_words_from_string[list_of_words_from_string.index(a_word)]=convert_cuss_word_to_stars(a_word)
            imgg=blur_word(a_word, la, texts)

        else:
            if check_for_special_character(a_word.lower())==True:
                if check_if_actually_a_cussword(a_word.lower(),cuss_words_list)==True:
                    list_of_words_from_string[list_of_words_from_string.index(a_word)] = convert_cuss_word_to_stars(a_word)
                    imgg=blur_word(a_word, la, texts)


    return [" ".join(list_of_words_from_string), imgg]
# cuss_words_list=tuple(Cusslist.objects.all().values_list('cussword', flat=True))
cuss_words_list = ['jerk', 'bastard', 'dick']
ans, imgg = googleVision()
print(ans)
imgg.show()