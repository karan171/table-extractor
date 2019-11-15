from pdf2image import convert_from_path


#For one page pdfs
#path = '/pdf_files/58.PDF'
#dpi=60


def get_images(path,dpi):

    page = convert_from_path(path,
                             poppler_path='poppler/bin',dpi=dpi)
    return page[0]