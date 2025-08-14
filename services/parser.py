import pandas as pd
from pdfminer.high_level import extract_text
import shutil, os
import openpyxl
import docx



async def extract_text_from_files(file_path):
    _, extension = os.path.splitext(file_path)
    if extension == ".pdf":
        text = extract_text(file_path)
        text_dict = {"text":text} # return as json-compatible dict
        actual_text = text_dict["text"]
        return actual_text

    elif extension == ".docx":
        text = docx.Document(file_path)
        full_text = [para.text for para in text.paragraphs]
        text_dict = {"text":full_text} # return as json-compatible dict
        actual_text = text_dict["text"]
        return actual_text  # return as joined string
    elif extension == ".xlsx":
        df = pd.read_excel(file_path)

        # ✅ Replace NaN with None
        clean_df = df.where(pd.notnull(df), None)
        rows_as_text = [" | ".join(map(str,row))for row in clean_df.values.tolist()]
        return "\n".join(rows_as_text)
        # # ✅ Convert to JSON-friendly structure
        # data = clean_df.to_dict(orient="records")

        # text_dict = {"text":data} # return as json-compatible dict
        # actual_text = text_dict["data"]
        # return actual_text
    elif extension == ".csv":
        df = pd.read_csv(file_path)

        # ✅ Replace NaN with None
        clean_df = df.where(pd.notnull(df), None)
        rows_as_text = [" | ".join(map(str,row))for row in clean_df.values.tolist()]
        return "\n".join(rows_as_text)
        # # ✅ Convert to JSON-friendly structure
        # data = clean_df.to_dict(orient="records")
        # # return {"data": data}
        # text_dict = {"text":data} # return as json-compatible dict
        # actual_text = text_dict["data"]
        # return actual_text