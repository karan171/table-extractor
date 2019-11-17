from PIL import Image


def get_table_area(image,output_dict,counter):
    tables = []
    im_width, im_height = image.size
    for i in range(counter):
        ymin = output_dict['detection_boxes'][i][0]
        xmin = output_dict['detection_boxes'][i][1]
        ymax = output_dict['detection_boxes'][i][2]
        xmax = output_dict['detection_boxes'][i][3]
        (left,right,top,bottom) = (xmin * im_width, xmax * im_width,
                                  ymin * im_height, ymax * im_height)
        im1 = image.crop((left,top,right,bottom))
        tables.append(im1)
    return tables


def get_table_coords(image,output_dict,counter):
    tables_coords = []
    im_width, im_height = image.size
    for i in range(counter):
        ymin = output_dict['detection_boxes'][i][0]
        xmin = output_dict['detection_boxes'][i][1]
        ymax = output_dict['detection_boxes'][i][2]
        xmax = output_dict['detection_boxes'][i][3]
        (left, right, top, bottom) = (xmin * im_width, xmax * im_width,
                                      ymin * im_height, ymax * im_height)
        tables_coords.append((top,left,bottom,right))
    return tables_coords