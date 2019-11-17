from pdf_to_image.image_pdf import get_images
from table_detect.detection import get_tables
from table_detect.table_area import get_table_area
from table_detect.table_area import get_table_coords
import matplotlib.pyplot as plt
import tabula
from PIL import Image
import pandas as pd

#Accept Input from user as a SinglePage PDF or a Normal Image.

path = 'C:/Intellectics/images/2.pdf'
dpi = 60
image = get_images(path=path,dpi=dpi)


def create_tables(image):
    tables_area = get_tables(image)
    output_dic,counter = tables_area
    tables_image = get_table_area(image,output_dic,counter)  #Will be used when support for tesseract-OCR is added
    tables_coords = get_table_coords(image,output_dic,counter)
    # counter = 0
    # for i in tables_image:
    #     result = i.save("out{}.jpg".format(counter))
    #     counter+=1
    return tables_coords


table_coords = create_tables(image)
counter = 0
for area in table_coords:
    # tab_df = tabula.read_pdf(input_path=path,pages='all',spreadsheet=True,multiple_tables=True,area=area,encoding='utf-8')
    tabula.convert_into(input_path=path,output_path='tables_out{}.csv'.format(counter),guess=False,area=area,pages='all')
    counter+=1

