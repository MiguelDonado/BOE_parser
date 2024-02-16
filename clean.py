import re

ampersand_pattern = re.compile(r"&")
y_pattern = re.compile(r" Y ")
and_pattern = re.compile(r" AND ")
guion_pattern = re.compile(r"-")
comilla_pattern = re.compile(r"'")
ernst_pattern = re.compile(r"ERNST")
kpgm_pattern = re.compile(r"KPGM")
osp_pattern = re.compile(r"O S P")
pwc_pattern = re.compile(r"PRICEWATERH(O|A)USECOOPERS AUDITORES")
agroalimentarias_pattern = re.compile(r"AGROALIMENTARIAS")
audria_pattern = re.compile(r"AUDRIA$")
calleja_pattern = re.compile(r"CALLEJA PINILLA AUDITORA")
audinfor_pattern = re.compile(r"AUDINFOR$")
escoabar_pattern = re.compile(r"ESCOABAR")
fernadez_pattern = re.compile(r"FERNADEZ")
trehuand_pattern = re.compile(r"TREHUAND")
fogueral_pattern = re.compile(r"FOGUERAL")
comtable_pattern = re.compile(r"COMTABLE")
aduditors_pattern = re.compile(r"ADUDITORS")
auditoira_pattern = re.compile(r"AUDITOIRA")
gpaudit_pattern = re.compile(r"GPAUDIT GALICIA")
consultans_pattern = re.compile(r"CONSULTANS")
auitores_pattern = re.compile(r"AUITORES")
auditore_pattern = re.compile(r"AUDITORE$")
argibay_pattern = re.compile(r"ARGIBAY GONZALEZ MARIA DEL MAR")
iberaudit_pattern = re.compile(r"IBERAUDIT KRESTON BPA AUDICONSULTING")
carballo_pattern = re.compile(r"CARBALLO FIDALGO MARIA PILAR")
audito_pattern = re.compile(r"\sAUDITO\s")
serantes_pattern = re.compile(r"SERANTES ARIAS JUAN EMILIO")
vilanova_pattern = re.compile(r"VILANOVA DACOSTA JOSE LUIS")
varela_pattern = re.compile(r"VARELA GONZALEZ JOSE LUIS")
lopez_pattern = re.compile(r"LOPEZ MERA FUENTES.*CIA AUDITORES")
balnco_pattern = re.compile(r"BALNCO")
osp_asociados_pattern = re.compile(r"OSP.*ASOCIADOS AUDITORES")
ruiz_carnota_pattern = re.compile(r"RUIZ CARNOTA.*BLANCO AUDITORES")
qulity_pattern = re.compile(r"QULITY")
quality_management_pattern = re.compile(r"QUALITY MANAGEMENT AUDITORES DE CUENTAS")
miguez_docampo_pattern = re.compile(r"MIGUE(Z|L)\sDO\s?CAMPO\sLUIS\sALBERTO")
peraza_pattern = re.compile(r"PERAZA Y CIA AUDITORES")
grup_pattern = re.compile(r"\sGRUP")
qlt_accontant_grup_pattern = re.compile(r"QLT ACCONTANT.*GRUP")

replace_list = [
    re.compile(p)
    for p in [
        "\.",
        ",",
        "\(",
        "\)",
        ";.*",
        "004060155Y SLNE",
        "SOCIEDAD LIMITADA PROFESIONAL\s?$",
        "SOCIEDAD LIMITADA\s?$",
        "SOCIEDAD ANONIMA\s?$",
        "SOCIEDAD LIMITAD\s?$",
        "SOCIEDAD LIMITADA PROFE\s?$",
        "CENSORES JURADOS DE CUEN\s?$",
        "SLP\s?$",
        "SAP\s?$",
        "SLL\s?$",
        "SAU\s?$",
        "SLU\s?$",
        "SGR\s?$",
        "SAT\s?$",
        "S L P\s?$",
        "SC\s?$",
        "SL\s?$",
        "SA\s?$",
        "SP\s?$",
        "SC\s?$",
        "SR\s?$",
        "S L\s?$",
        "\sS\s?$",
        "\s$",
    ]
]


def clean_func(s, auditores=True):
    """
    This function cleans a given string by removing certain patterns and multiple spaces between words.

    Parameters:
    s (str): The string to be cleaned.

    Returns:
    str: The cleaned string.
    """
    s = ampersand_pattern.sub(" Y ", s)
    s = y_pattern.sub(" ", s)
    s = and_pattern.sub(" ", s)
    s = guion_pattern.sub(" ", s)
    s = comilla_pattern.sub(" ", s)
    if auditores:
        s = ernst_pattern.sub("ERNEST", s)
        s = kpgm_pattern.sub("KPMG", s)
        s = osp_pattern.sub("OSP", s)
        s = pwc_pattern.sub("PRICEWATERHOUSECOOPERS", s)
        s = calleja_pattern.sub("CALLEJA PINILLA AUDITORIA", s)
        s = lopez_pattern.sub("LOPEZ MERA FUENTES AUDITORES", s)
        s = consultans_pattern.sub("CONSULTANTS", s)
        s = aduditors_pattern.sub("AUDITORS", s)
        s = fernadez_pattern.sub("FERNANDEZ", s)
        s = comtable_pattern.sub("CONTABLE", s)
        s = fogueral_pattern.sub("FOLGUERAL", s)
        s = auitores_pattern.sub("AUDITORES", s)
        s = escoabar_pattern.sub("ESCOBAR", s)
        s = trehuand_pattern.sub("TREUHAND", s)
        s = auditoira_pattern.sub("AUDITORIA", s)
        s = gpaudit_pattern.sub("GP AUDITGALICIA", s)
        s = iberaudit_pattern.sub("IBERAUDIT KRESTON BPA", s)
        s = auditore_pattern.sub("AUDITORES", s)
        s = audinfor_pattern.sub("AUDINFORM", s)
        s = agroalimentarias_pattern.sub("AGROALIMENTARIA", s)
        s = audria_pattern.sub("AUDRIA AUDITORIA CONSULTORIA", s)
        s = argibay_pattern.sub("ARGIBAY GONZALEZ MAR", s)
        s = carballo_pattern.sub("CARBALLO FIDALGO PILAR", s)
        s = serantes_pattern.sub("SERANTES ARIAS JUAN", s)
        s = audito_pattern.sub(" AUDIT ", s)
        s = balnco_pattern.sub("BLANCO", s)
        s = osp_asociados_pattern.sub("OSP ASOCIADOS AUDITORES", s)
        s = ruiz_carnota_pattern.sub("RUIZ CARNOTA BLANCO SALGADO AUDITORES", s)
        s = qulity_pattern.sub("QUALITY", s)
        s = quality_management_pattern.sub("QUALITY MANAGEMENT AUDITORES", s)
        s = miguez_docampo_pattern.sub("MIGUEZ DOCAMPO LUIS ALBERTO", s)
        s = peraza_pattern.sub("PERAZA Y COMPAÑIA AUDITORES", s)
        s = qlt_accontant_grup_pattern.sub("QLT ACCOUNTANT GROUP", s)
    s = re.sub(" {2,}", " ", s)  # To remove multiple spaces between words
    for pattern in replace_list:
        s = pattern.sub("", s)
    return s
