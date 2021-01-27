from google.resumable_media import InvalidResponse
from google.cloud import storage
import os

from haystack.file_converter.pdf import PDFToTextConverter

converter = PDFToTextConverter(remove_numeric_tables=True, valid_languages=["en"])
storage_client = storage.Client.create_anonymous_client()
bucket = storage_client.bucket('arxiv-dataset')

def download_by_id(id,ver):
    try:
        date, subId = str(id).split('.')
        blob = bucket.blob('arxiv/arxiv/pdf/' + date + '/' + id + ver + '.pdf')
        blob.download_to_filename('./data/arxiv/' + id + '.pdf')
        doc = converter.convert(file_path='./data/arxiv/' + id + '.pdf', meta=None)
        with open('./data/arxiv/' + id + '.txt', 'w') as txt:
            print(doc, file=txt)
        os.remove('./data/arxiv/' + id + '.pdf')
        print(
            "Blob {} downloaded.".format(
                id
            )
        )
    except InvalidResponse:
        print(
            "Blob {} 404.".format(
                id
            )
        )

with open('./arxiv_list.txt') as f:
  list = eval(f.read())
for (id,ver) in list:
    download_by_id(id,ver)