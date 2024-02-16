# BOE_PARSER

This project is designed to extract auditor designations in Galicia from the BOE API. The program allows data extraction for each province individually.

## Description

The project consists of several Python scripts that work together to extract, process, and output the desired data. Here's a brief overview of each script:

- `definitivo.py`: This is the main script that controls the flow of the program. It makes HTTP requests to the BOE API, parses the XML responses, extracts the PDF URLs, and writes the final data to an Excel file.

- `regularexp.py`: This script contains functions for parsing the text of the PDFs. It uses regular expressions to find and extract the desired data.

- `clean.py`: This script contains functions for cleaning the extracted data. It uses regular expressions to replace certain patterns in the data.

- `support_regex.py`: This script contains the regular expressions used in `regularexp.py` and `clean.py`.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Quickstart

1. Clone the repo
```bash
git clone https://github.com/your_username_/Project-Name.git
```

2. Change the `PROVINCIA` constant in `definitivo.py` to one of the following: "A CORUÑA", "PONTEVEDRA", "LUGO", "OURENSE".
3. Run the script
```bash
python3 definitivo.py
```
### Video
https://github.com/MiguelDonado/BOE_parser/assets/146335579/4545a9e0-5d9b-41b2-8e91-b307a044fe69

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
