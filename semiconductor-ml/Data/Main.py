from clean_data_all import clean_all

"""
This is a dictionary consisting of different keys (materials) that contain 
urls with their parameters from ioffe website
"""
materials = {
    "Silicon": ["https://www.ioffe.ru/SVA/NSM/Semicond/Si/basic.html", 
                "https://www.ioffe.ru/SVA/NSM/Semicond/Si/bandstr.html",
                "https://www.ioffe.ru/SVA/NSM/Semicond/Si/electric.html"],

    "Gallium Phosphide": ["https://www.ioffe.ru/SVA/NSM/Semicond/GaP/basic.html",
                          "https://www.ioffe.ru/SVA/NSM/Semicond/GaP/bandstr.html",
                          "https://www.ioffe.ru/SVA/NSM/Semicond/GaP/electric.html"],

    "Indium Arsenide": ["https://www.ioffe.ru/SVA/NSM/Semicond/InAs/basic.html",
                        "https://www.ioffe.ru/SVA/NSM/Semicond/InAs/bandstr.html",
                        "https://www.ioffe.ru/SVA/NSM/Semicond/InAs/electric.html"],

    "Gallium Antimonide": ["https://www.ioffe.ru/SVA/NSM/Semicond/GaSb/basic.html",
                           "https://www.ioffe.ru/SVA/NSM/Semicond/GaSb/bandstr.html",
                           "https://www.ioffe.ru/SVA/NSM/Semicond/GaSb/electric.html"],
     
    "Indium Phosphide": ["https://www.ioffe.ru/SVA/NSM/Semicond/InP/basic.html",
                         "https://www.ioffe.ru/SVA/NSM/Semicond/InP/bandstr.html",
                         "https://www.ioffe.ru/SVA/NSM/Semicond/InP/electric.html"],

    "Germanium": ["https://www.ioffe.ru/SVA/NSM/Semicond/Ge/basic.html",
                  "https://www.ioffe.ru/SVA/NSM/Semicond/Ge/bandstr.html",
                  "https://www.ioffe.ru/SVA/NSM/Semicond/Ge/electric.html"],

    "Gallium Arsenide": ["https://www.ioffe.ru/SVA/NSM/Semicond/GaAs/basic.html",
                         "https://www.ioffe.ru/SVA/NSM/Semicond/GaAs/bandstr.html",
                         "https://www.ioffe.ru/SVA/NSM/Semicond/GaAs/electric.html"],

    "Diamond": ["https://www.ioffe.ru/SVA/NSM/Semicond/Diamond/basic.html",
                "https://www.ioffe.ru/SVA/NSM/Semicond/Diamond/bandstr.html",
                "https://www.ioffe.ru/SVA/NSM/Semicond/Diamond/ebasic.html"],

    "Indium Antimonide": ["https://www.ioffe.ru/SVA/NSM/Semicond/InSb/basic.html",
                          "https://www.ioffe.ru/SVA/NSM/Semicond/InSb/bandstr.html",
                          "https://www.ioffe.ru/SVA/NSM/Semicond/InSb/electric.html"],

    "Gallium Arsenide Antimonide": ["https://www.ioffe.ru/SVA/NSM/Semicond/GaAsSb/basic.html",
                                    "https://www.ioffe.ru/SVA/NSM/Semicond/GaAsSb/bandstr.html",
                                    "https://www.ioffe.ru/SVA/NSM/Semicond/GaAsSb/electric.html"],

    "Alluminum Gallium Arsenide": ["https://www.ioffe.ru/SVA/NSM/Semicond/AlGaAs/basic.html",
                                   "https://www.ioffe.ru/SVA/NSM/Semicond/AlGaAs/bandstr.html",
                                   "https://www.ioffe.ru/SVA/NSM/Semicond/AlGaAs/ebasic.html"],

    "Alluminum Nitride": ["https://www.ioffe.ru/SVA/NSM/Semicond/AlN/basic.html",
                          "https://www.ioffe.ru/SVA/NSM/Semicond/AlN/bandstr.html",
                          "https://www.ioffe.ru/SVA/NSM/Semicond/AlN/ebasic.html"],
    
    "Boron Nitride": ["https://www.ioffe.ru/SVA/NSM/Semicond/BN/basic.html",
                      "https://www.ioffe.ru/SVA/NSM/Semicond/BN/bandstr.html",
                      "https://www.ioffe.ru/SVA/NSM/Semicond/BN/ebasic.html"],

    "Indium Nitride": ["https://www.ioffe.ru/SVA/NSM/Semicond/InN/basic.html",
                    "https://www.ioffe.ru/SVA/NSM/Semicond/InN/bandstr.html",
                    "https://www.ioffe.ru/SVA/NSM/Semicond/InN/ebasic.html"],

    "Gallium Nitride": ["https://www.ioffe.ru/SVA/NSM/Semicond/GaN/basic.html",
                        "https://www.ioffe.ru/SVA/NSM/Semicond/GaN/bandstr.html",
                        "https://www.ioffe.ru/SVA/NSM/Semicond/GaN/ebasic.html"]

}

"""
Calls the clean_all function from clean_data_all with 
two parameters: ({dict of materials}, {name of excel})
"""
excel_name = "All_Materials"
clean_all(materials,excel_name)
print(f"Excel made: {excel_name}")

