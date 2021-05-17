import os, io
from google.cloud import vision
# from google.cloud.vision import types
import pandas as pd
from PIL import Image,ImageFilter
from datetime import datetime


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'booming-coast-313509-bb494bed1251.json'
client=vision.ImageAnnotatorClient()
def googleVision(file_name, folder_path, result_image_path):
    # FILE_NAME= 'demoImage.jpeg'
    FILE_NAME= file_name
    # FOLDER_PATH=r'C:\Users\HP\Documentss\miniproject_sem6'
    # FOLDER_PATH=r'C:\\Users\\acer\\Desktop\\Divyesh\\Projects\\college_projects\\Mini_project_organisation\\cyber_bully\\'
    FOLDER_PATH=folder_path

    with io.open (os.path.join(FOLDER_PATH,FILE_NAME),'rb') as image_file:
        content=image_file.read()

    image=vision.Image(content=content) 
    response=client.text_detection(image=image)   
    texts=response.text_annotations
    # print(texts)
    a=(texts[0].description).split()
    print(a)
    # ogimage=Image.open(r'C:\\Users\\acer\\Desktop\\Divyesh\\Projects\\college_projects\\Mini_project_organisation\\cyber_bully\\demoImage.jpeg')
    ogimage=Image.open(image_file.name)
    li = []
    for i in range(len(a)):
        if a[i] == 'THE':

            c=i
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
            a1=texts[c+1].bounding_poly.vertices[0].x
            a2=texts[c+1].bounding_poly.vertices[0].y
            b1=texts[c+1].bounding_poly.vertices[2].x
            b2=texts[c+1].bounding_poly.vertices[2].y

            cropped_image=ogimage.crop((a1,a2,b1,b2))
            # cropped_image.show()
            blurred_image=cropped_image.filter(ImageFilter.GaussianBlur(radius=30))
            opimage = ogimage.paste(blurred_image,(a1,a2,b1,b2))
            ogimage.save(result_image_path+'im {}.jpeg'.format(i))
            li.append(result_image_path+'im {}.jpeg'.format(i))
            ogimage = Image.open(result_image_path+'im {}.jpeg'.format(i))

    for j in range(len(li)-1):
        os.remove(li[j])
    return ogimage


    # ans = blur_image(og_image_with_path, c)
    # ans.show()
# googleVision('demoImage.jpeg', r'C:\\Users\\acer\\Desktop\\Divyesh\\Projects\\college_projects\\Mini_project_organisation\\cyber_bully', 'media/inputImages/{}/'.format(datetime.today().strftime('%Y/%m/%d')))