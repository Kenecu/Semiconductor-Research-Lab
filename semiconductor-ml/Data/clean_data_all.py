import pandas as pd
from openpyxl import load_workbook
import requests
from io import StringIO

def clean_all(materials_dict, file_name):
    """
    Recieves two parameters: {a dictionary of different materials with urls as the values} and  {name of excel}

    This function retrieves the url values from a dictionary of materials and webscrapes the url data
    into an excel sheet with materials as rows and the parameters as the columns
    """

    # Combines all material datasets when their cleaned
    all_materials = []

    #Adds .xlsx if not added in the filename to create the excel
    if not file_name.endswith(".xlsx"):
        file_name += ".xlsx"

    """
    Loops through dictionary by searching for the material name and the url 
    by using the items() function, then sets the name to material_name and url to urls
    """
    for material_name, urls in materials_dict.items():

        # Sets the names to str and lowercase to avoid duplicates when updating to excel and normalize input
        material_name = str(material_name).lower()

        #Makes sure that all urls are put into a list so that it can iterated over even if it's a single url
        if isinstance(urls, str):
            urls = [urls]
        
        #Used to combine data from the urls for each material
        all_tables = []

        """
        This segment loops through the urls for each material and webscrapes
        """
        for url in urls:
            try:
                # Send HTTP GET request to url and returns that information in response
                response = requests.get(url)

                # Since encoding is unknown from webpage we test several encodings to decode the html
                # If html can't be decoded, prints "could not decode"
                html = None
                for enc in ["cp1251", "latin-1", "windows-1252", "utf-8", "iso-8859-1"]:
                    try:
                        html = response.content.decode(enc)
                        break
                    except:
                        continue

                if html is None:
                    print(f"Could not decode {url}")
                    continue
                
                # html contains non-breaking spaces (\xa0) so we replace with regular to normalize for pandas
                html = html.replace("\xa0", " ")

                # This reads the html that we cleaned and scans for <table> tags | extracts as dataframes
                # Returns a list like [df1, df2, df3]
                # Needs StringIO to wrap html string to impersonate a file for pandas to read
                tables = pd.read_html(StringIO(html))

                # Select first index from list of dataframes in tables
                df = tables[0]

                # df.shape gives the (rxc) of the dataframe | shape[0] gives rows , shape[1] gives columns
                # we use a conditional to make sure there's 2 columns 
                # we assign the first 2 columns property and value
                # .iloc is used to slice columns and rows
                if df.shape[1] >= 2:
                    df = df.iloc[:, :2]  
                    df.columns = ["Property", "Values"]
                else:
                    print(f"Skipping table on {url} (unexpected column format)")
                    continue
                
                """
                Need to normalize property value names because pandas needs the same exact format or treats
                it like a different property ("silicon" and "Silicon" would be treated as two separate)
                """
                df["Property"] = (
                    df["Property"]
                    .astype(str)
                    .str.strip()
                    .str.replace("\u00a0", " ")
                    .str.replace("\u200b", "")
                    .str.replace("\u200e", "")
                    .str.replace("\t", " ")
                    .str.replace("\n", " ")
                    .str.replace("\r", " ")
                    .str.lower()
                    )

                # Removes empty rows
                df = df.dropna()
                
                # Append the cleaned table into list of all tables
                all_tables.append(df)
            
            # If url can't be read it prints out an error and skips it
            except Exception as e:
                print(f"Failed to read {url}: {e}")

        # only runs when list is empty and no valid table for material was found
        if not all_tables:
            print(f"Table not found for {material_name}")
            continue
        
        # concat is used to merge all tables from urls into one and ignore index because each url has a new index
        merged = pd.concat(all_tables, ignore_index = True)

        # avoids collisions for the property column because they could have different name for values but mean the same thing
        merged["Property"] = (merged.groupby("Property").cumcount().astype(str) + "_" + merged["Property"])

        # Pivots the table into a single row so values are across rows and not down columns
        merged = merged.set_index("Property").T

        # Inserts a material column at the beginning of list
        merged.insert(0, "Material", material_name)

        # Stores the tables from the material into a list of all materials to concat
        all_materials.append(merged)

    # Once we get all tables for each material we combine all of it together
    final_df = pd.concat(all_materials, ignore_index = True)

    # Writes the final product to excel, removes pandas auto index numbering
    final_df.to_excel(file_name, index=False)

    """
    We then load the excel into python to format the data so that it's readable
    """
    workbook = load_workbook(file_name)
    sheet = workbook.active

    for column_cells in sheet.columns:
        max_length = 0
        column = column_cells[0].column_letter
        for cell in column_cells:
            try:
                cell_length = len(str(cell.value))
                if cell_length > max_length:
                    max_length = cell_length
            except:
                pass
        adjusted_width = max_length + 2
        sheet.column_dimensions[column].width = adjusted_width

    workbook.save(file_name)
