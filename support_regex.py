import re

# aud = auditor /// pat = pattern /// cs = consolidado
actos_pattern = re.compile(r"(\d{4}\d?\d?\s-\s.+?)(?=tos\s\n?registrales)", re.DOTALL)
enterprise_pattern = re.compile(r"\d{4}\d?\d?\s-\s(.+?)\s[A-Z][a-z]")
nombr_aud_pat = re.compile(r"Nombramientos\. Auditor:\s([^a-z]*)\s[A-Z][a-z]")
reel_aud_pat = re.compile(r"Reelecciones\. Auditor:\s([^a-z]*)\s[A-Z][a-z]")
rev_aud_pat = re.compile(r"Revocaciones\. Auditor:\s([^a-z]*)\s[A-Z][a-z]")
ces_aud_pat = re.compile(r"Ceses/Dimisiones\. Auditor:\s([^a-z]*)\s[A-Z][a-z]")
nombr_audcs_pat = re.compile(r"Nombramientos\. Aud\.C\.Con\.?:\s([^a-z]*)\s[A-Z][a-z]")
reel_audcs_pat = re.compile(r"Reelecciones\. Aud\.C\.Con\.?:\s([^a-z]*)\s[A-Z][a-z]")
rev_audcs_pat = re.compile(r"Revocaciones\. Aud\.C\.Con\.?:\s([^a-z]*)\s[A-Z][a-z]")
ces_audcs_pat = re.compile(r"Ceses/Dimisiones\. Aud\.C\.Con\.?:\s([^a-z]*)\s[A-Z][a-z]")
# SI SOLO APARECE UN ENCABEZADO PARA AUDITOR Y AUDITOR DE CONSOLIDADO
both_nombr_aud_pat = re.compile(
    r"Nombramientos\. Auditor:\s([^a-z]*)\sAud\.C\.Con\.?:\s([^a-z]*)\s[A-Z][a-z]",
    re.DOTALL,
)
both_reel_aud_pat = re.compile(
    r"Reelecciones\. Auditor:\s([^a-z]*)\sAud\.C\.Con\.?:\s([^a-z]*)\s[A-Z][a-z]",
    re.DOTALL,
)
both_rev_aud_pat = re.compile(
    r"Revocaciones\. Auditor:\s([^a-z]*)\sAud\.C\.Con\.?:\s([^a-z]*)\s[A-Z][a-z]",
    re.DOTALL,
)
both_ces_aud_pat = re.compile(
    r"Ceses/Dimisiones\. Auditor:\s([^a-z]*)\sAud\.C\.Con\.?:\s([^a-z]*)\s[A-Z][a-z]",
    re.DOTALL,
)
