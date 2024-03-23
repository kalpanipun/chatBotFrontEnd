from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.document_loaders import PyPDFLoader


def load_index(file_path):
    loader = CSVLoader(file_path=file_path,
                       csv_args={
                           "delimiter": ",",
                       },
                       )
    index = VectorstoreIndexCreator().from_loaders([loader])
    return index



# read pdf

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    index = VectorstoreIndexCreator().from_loaders([loader])
    return index
