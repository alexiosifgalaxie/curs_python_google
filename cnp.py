import datetime


DICT_SECOL = {
    "1": ("născuți între 1 ianuarie 1900 și 31 decembrie 1999", "masculin", "19"),
    "2": ("născuți între 1 ianuarie 1900 și 31 decembrie 1999", "femenin", "19"),
    "3": ("născuți între 1 ianuarie 1800 și 31 decembrie 1899", "masculin", "18"),
    "4": ("născuți între 1 ianuarie 1800 și 31 decembrie 1899", "femenin", "18"),
    "5": ("născuți între 1 ianuarie 2000 și 31 decembrie 2099", "masculin", "20"),
    "6": ("născuți între 1 ianuarie 2000 și 31 decembrie 2099", "femenin", "20"),
    "7": ("persoane straine rezidente in Romania", "masculin", "19"),
    "8": ("persoane straine rezidente in Romania", "femenin", "19"),
    "9": ("persoane straine", None, "19"),
}
DICT_JUDET = {
    "01": "Alba",
    "02": "Arad",
    "03": "Argeș",
    "04": "Bacău",
    "05": "Bihor",
    "06": "Bistrița-Năsăud",
    "07": "Botoșani",
    "08": "Brașov",
    "09": "Brăila",
    "10": "Buzău",
    "11": "Caraș-Severin",
    "12": "Cluj",
    "13": "Constanța",
    "14": "Covasna",
    "15": "Dâmbovița",
    "16": "Dolj",
    "17": "Galați",
    "18": "Gorj",
    "19": "Harghita",
    "20": "Hunedoara",
    "21": "Ialomița",
    "22": "Iași",
    "23": "Ilfov",
    "24": "Maramureș",
    "25": "Mehedinți",
    "26": "Mureș",
    "27": "Neamț",
    "28": "Olt",
    "29": "Prahova",
    "30": "Satu Mare",
    "31": "Sălaj",
    "32": "Sibiu",
    "33": "Suceava",
    "34": "Teleorman",
    "35": "Timiș",
    "36": "Tulcea",
    "37": "Vaslui",
    "38": "Vâlcea",
    "39": "Vrancea",
    "40": "București",
    "41": "București - Sector 1",
    "42": "București - Sector 2",
    "43": "București - Sector 3",
    "44": "București - Sector 4",
    "45": "București - Sector 5",
    "46": "București - Sector 6",
    "51": "Călărași",
    "52": "Giurgiu",
}
NUMAR_MAGIC = 279146358279

cnp = input("Introdu CNP-ul: ")
try:
    if len(cnp) != 13:
        raise ValueError
    int(cnp)
    categorie, sex, tmp = DICT_SECOL[cnp[0]]
    date = datetime.date(int(tmp + cnp[1:3]), int(cnp[3:5]), int(cnp[5:7]))
    an, luna, zi = date.year, date.month, date.day
    judet = DICT_JUDET[cnp[7:9]]
    NNN = cnp[9:12]
    if NNN == "000":
        raise ValueError

    # Cifra de control
    cnp_partial = int(cnp[:12])
    suma = 0
    while cnp_partial:
        suma += (cnp_partial % 10) * (NUMAR_MAGIC % 10)
        cnp_partial //= 10
        NUMAR_MAGIC //= 10
    cifra_de_control = suma % 11
    if cifra_de_control == 10:
        cifra_de_control = 1

    if cifra_de_control != int(cnp[-1]):
        raise ValueError

    print(f"Data nasterii: {zi}/{luna}/{an}")
    print(f"Sexul: {sex.capitalize()}")
    print(f"Judet: {judet}")
    print(f"Numarul de oridne: {NNN}")
    print(f"Categorie: {categorie.capitalize()}")
except ValueError:
    print("Nu e CNP")
