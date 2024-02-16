import requests
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
from PyPDF2 import PdfReader
from regularexp import get_rows, change_date_format
from io import BytesIO
from openpyxl import Workbook
import time

HOST = "https://boe.es"
FIXED_PART_OF_URL_API = f"{HOST}/diario_boe/xml.php?id=BORME-S-"
PROVINCIA = "A CORUÑA"
# Constante, que me permite sumar un día a una fecha
DIFF1DIA = timedelta(days=1)


def main():
    start_time = time.time()
    fecha_desde, fecha_hasta = get_dates()
    http_api(fecha_desde, fecha_hasta)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")


# Consigo las fechas inicio y final, y las devuelvo en formato deseado
def get_dates():
    hoy = datetime.now().strftime("%Y%m%d")

    desde = input("Fecha desde (YYYYMMDD): ") or hoy
    hasta = input("Fecha hasta (YYYYMMDD): ") or hoy

    fecha_desde = datetime.strptime(desde, "%Y%m%d")
    fecha_hasta = datetime.strptime(hasta, "%Y%m%d")
    if fecha_desde > fecha_hasta:
        raise ValueError("La fecha de inicio no puede ser posterior a la fecha final.")
    return fecha_desde, fecha_hasta


def http_api(fecha_desde, fecha_hasta):
    table_to_csv = []
    with requests.Session() as session:
        while fecha_desde <= fecha_hasta:
            fecha_Ymd = fecha_desde.strftime("%Y%m%d")
            response = session.get(f"{FIXED_PART_OF_URL_API}{fecha_Ymd}")
            if response.status_code == 200:
                root = ET.fromstring(response.text)
                urlPdf = parse_xml(root)
                if urlPdf:
                    texto_urlPdf = http_api_endpoint(session, urlPdf)
                    fecha_Ymd = change_date_format(fecha_Ymd)
                    rows = get_rows(texto_urlPdf, fecha_Ymd, urlPdf)
                    table_to_csv.extend(rows)
            fecha_desde += DIFF1DIA
    write_to_xlsx(table_to_csv)


# El método parse_xml, recibe el root (todo el texto de la API summary del día indicado), y devuelve la urlPdf
def parse_xml(root):
    for item in root.iter("item"):
        titulo = item.find("titulo")
        if titulo is not None and titulo.text == PROVINCIA:
            urlPdf = item.find("urlPdf")
            if urlPdf is not None:
                urlPdf = f"{HOST}{urlPdf.text}"
                return urlPdf


# El método http_api_endpoint, recibe la urlPdf, y devuelve el texto extraído del pdf
def http_api_endpoint(session, urlPdf):
    response = session.get(urlPdf)
    # Create a BytesIO object from the content of the response
    pdf_file = BytesIO(response.content)

    # Create a PdfReader object
    pdf_reader = PdfReader(pdf_file)

    text_pages = [page.extract_text() for page in pdf_reader.pages]
    text_urlPdf = " ".join(text_pages)
    return text_urlPdf


# El método write_to_csv, recibe una lista de tuplas, cada tupla va a ser una fila en el csv
# La lista de tuplas, es una variable que contiene los datos deseados de todas las fechas
def write_to_xlsx(table_to_csv):
    wb = Workbook()
    ws = wb.active

    fieldnames = ("Fecha", "Empresa", "Tipo de acto", "Nombre del auditor", "urlPdf")
    ws.append(fieldnames)

    for row in table_to_csv:
        ws.append(row)

    wb.save(f"{PROVINCIA}.xlsx")


main()
