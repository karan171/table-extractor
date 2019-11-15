from pdf_to_image.image_pdf import get_images
from table_detect.detection import get_tables
from table_detect.table_area import get_table_area
import matplotlib.pyplot as plt
from PIL import Image

#Accept Input from user as a SinglePage PDF or a Normal Image.


image = get_images(path='C:/Intellectics/images/2.pdf',dpi=300)
tables_area = get_tables(image)
output_dic,counter = tables_area
tables_image = get_table_area(image,output_dic,counter)
counter = 0
for i in tables_image:
    result = i.save("out{}.jpg".format(counter))
    counter+=1