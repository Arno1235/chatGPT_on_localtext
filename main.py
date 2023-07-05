import os
import sys

import api_key
os.environ["OPENAI_API_KEY"] = api_key.APIKEY

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

query = sys.argv[1]

loader = TextLoader('data.txt')

index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))