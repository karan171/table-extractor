# table-extractor
 Extracting tables from PDFs or Any files using Deeplearning,OCR and Tabula

#Support for tabula is added in tables.py file.
#We have used MASKRCNN here and trained it on images of pdf files to detect tables.
#Things to do:
1)Adding a deep learning model than can detect columns of the tables.
2)Using Coordinates of detected tables and feeding it to tabula.
3)Adding support for OCR if PDFs are not avaliable.

Note:Use Tabula if you need the data extracted from pdfs,until the pytesseract branch is merged.


Standalone Api's that are used for extracting tables from Images of documents or PDFs are either Expensive(Abbey)
or Not good enough(tabula,camelot,pdfminer etc) there are various types of tables in documents some easy to detect
and Put in databases and some very unorthodox.Abbey uses Deep learning to solve that problem and probably the best
api out there but its expensive.On the other hand Camelot,Tabula they only work for PDFs because they don't use OCR
techniques instead they go for a Rule Based Approach and some classic EdgeDetection algorithms and GhostScript.
They are free but don't really work that well if the table structure isn't good , also if tables countinue on
other pages etc.We are going to solve those problems soon with this approach which combines all the approaches above
and Give you a free and a flexible solution for your use case.