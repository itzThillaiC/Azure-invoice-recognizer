key = "9f8b8c3e8dee4a5cbc12cd3ae7044740"
endPoint = "https://billok.cognitiveservices.azure.com/"


import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from pdf2image import convert_from_path



document_analysis_client = DocumentAnalysisClient(endpoint=endPoint, credential=AzureKeyCredential(key))
# import module



# Store Pdf with convert_from_path function
import pdf2jpg
from pdf2jpg import pdf2jpg
inputpath = r"ltest.pdf"
outputpath = r""
result = pdf2jpg.convert_pdf2jpg(inputpath,outputpath, pages="ALL")
print(outputpath)

import os
import glob

folder = inputpath+"_dir/"
for count, filename in enumerate(os.listdir(folder)):
    oldname = folder + filename   
    newname = folder + "invoice_" + str(count + 1) + ".jpg"
    os.rename(oldname, newname)


image= "ltest.pdf_dir\invoice_1.jpg"

fd= open(image, "rb")



poller = document_analysis_client.begin_analyze_document_from_url(
            "prebuilt-document", "https://templates.invoicehome.com/invoice-template-us-neat-750px.png")
result = poller.result()




for idx, invoice in enumerate(result.documents):
    print("--------Recognizing invoice #{}--------".format(idx + 1))
    vendor_name = result.fields.get("VendorName")
    if vendor_name:
        print(
            "Vendor Name: {} has confidence: {}".format(
                vendor_name.value, vendor_name.confidence
            )
        )