import re
from clean import clean_func
from datetime import datetime
from support_regex import (
    actos_pattern,
    enterprise_pattern,
    nombr_aud_pat,
    reel_aud_pat,
    rev_aud_pat,
    ces_aud_pat,
    nombr_audcs_pat,
    reel_audcs_pat,
    rev_audcs_pat,
    ces_audcs_pat,
    both_nombr_aud_pat,
    both_reel_aud_pat,
    both_rev_aud_pat,
    both_ces_aud_pat,
)


def main():
    pass


def change_date_format(fecha):
    # Convert to datetime object
    fecha = datetime.strptime(fecha, "%Y%m%d")
    # Convert to dd-mm-yyyy format
    fecha = fecha.strftime("%d-%m-%Y")
    return fecha


# Parseo el texto del pdf y devuelvo una lista con los datos deseados. Es una lista de tuplas
# [(fecha, empresa, tipo de acto, nombre del auditor),(...),(...),...].
def get_rows(text, fecha_Ymd, urlPdf):
    # Divide todo el texto del urlPdf en parrafos
    actos = actos_pattern.findall(text)
    # Variable en la que vamos a almacenar los datos deseados en el formato deseado
    data_endpoint = []
    # Solo aquellos parrafos que contengan la palabra "Aud"
    actos = [re.sub(" {2,}", " ", a.replace("\n", " ")) for a in actos if "Aud" in a]

    for acto in actos:
        # Nombre de la empresa
        enterprise = enterprise_pattern.search(acto)
        enterprise = clean_func(enterprise.group(1).split("(R.M.")[0], False)
        if "Aud.C.Con" in acto:
            # SI SOLO APARECE UN ENCABEZADO PARA AUDITOR Y AUDITOR DE CONSOLIDADO
            if nombr_auditores_both := both_nombr_aud_pat.search(acto):
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Nombramientos",
                    clean_func(nombr_auditores_both.group(1)),
                    urlPdf,
                )
                data_endpoint.append(row)
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Nombramientos (consolidado)",
                    clean_func(nombr_auditores_both.group(2)),
                    urlPdf,
                )
            if reel_auditores_both := both_reel_aud_pat.search(acto):
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Reelecciones",
                    clean_func(reel_auditores_both.group(1)),
                    urlPdf,
                )
                data_endpoint.append(row)
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Reelecciones (consolidado)",
                    clean_func(reel_auditores_both.group(2)),
                    urlPdf,
                )
                data_endpoint.append(row)

            if rev_auditores_both := both_rev_aud_pat.search(acto):
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Revocaciones",
                    clean_func(rev_auditores_both.group(1)),
                    urlPdf,
                )
                data_endpoint.append(row)
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Revocaciones (consolidado)",
                    clean_func(rev_auditores_both.group(2)),
                    urlPdf,
                )
                data_endpoint.append(row)
            if ces_auditores_both := both_ces_aud_pat.search(acto):
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Ceses/Dimisiones",
                    clean_func(ces_auditores_both.group(1)),
                    urlPdf,
                )
                data_endpoint.append(row)
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Ceses/Dimisiones (consolidado)",
                    clean_func(ces_auditores_both.group(2)),
                    urlPdf,
                )
                data_endpoint.append(row)
            if (
                nombr_auditores_both
                or reel_auditores_both
                or rev_auditores_both
                or ces_auditores_both
            ):
                continue
            # -----------------------------------------------------------------------------------------------------------------
            # En caso de que sea auditor de consolidado (no lo junto con el de arriba, porque puede haber auditor y auditor de consolidado en el mismo parrafo)
            if nombr_auditor_cons := nombr_audcs_pat.search(acto):
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Nombramientos (consolidado)",
                    clean_func(nombr_auditor_cons.group(1)),
                    urlPdf,
                )
                data_endpoint.append(row)
            if reelecc_auditor_cons := reel_audcs_pat.search(acto):
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Reelecciones (consolidado)",
                    clean_func(reelecc_auditor_cons.group(1)),
                    urlPdf,
                )
                data_endpoint.append(row)

            if revoc_auditor_cons := rev_audcs_pat.search(acto):
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Revocaciones (consolidado)",
                    clean_func(revoc_auditor_cons.group(1)),
                    urlPdf,
                )
                data_endpoint.append(row)
            if ceses_auditor_cons := ces_audcs_pat.search(acto):
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Ceses/Dimisiones (consolidado)",
                    clean_func(ceses_auditor_cons.group(1)),
                    urlPdf,
                )
                data_endpoint.append(row)
        if "Auditor" in acto:
            # Nombramiento auditor
            if nombr_auditor := nombr_aud_pat.search(acto):
                # Si hubo nombramiento auditor, añademe a la lista data_endpoint con el formato adecuado
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Nombramientos",
                    clean_func(nombr_auditor.group(1)),
                    urlPdf,
                )
                data_endpoint.append(row)

            # Reeleccion auditor
            if reelecc_auditor := reel_aud_pat.search(acto):
                # Si hubo reeleccion auditor, añademe a la lista data_endpoint con el formato adecuado
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Reelecciones",
                    clean_func(reelecc_auditor.group(1)),
                    urlPdf,
                )
                data_endpoint.append(row)
            # Revocacion auditor
            if revoc_auditor := rev_aud_pat.search(acto):
                # Si hubo revocacion auditor, añademe a la lista data_endpoint con el formato adecuado
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Revocaciones",
                    clean_func(revoc_auditor.group(1)),
                    urlPdf,
                )
                data_endpoint.append(row)

            # Cese/Dimision auditor
            if ceses_auditor := ces_aud_pat.search(acto):
                # Si hubo cese/dimision auditor, , añademe a la lista data_endpoint con el formato adecuado
                row = (
                    fecha_Ymd,
                    enterprise,
                    "Ceses/Dimisiones",
                    clean_func(ceses_auditor.group(1)),
                    urlPdf,
                )
                data_endpoint.append(row)

    return data_endpoint


if __name__ == "__main__":
    main()
