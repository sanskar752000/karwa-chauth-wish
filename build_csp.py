#!/usr/bin/env python3
"""Re-computes the script hash in the CSP <meta> after you edit index.html (name/letter text changes the hash!)."""
import re,hashlib,base64,sys
p='index.html'; s=open(p,encoding='utf-8').read()
m=list(re.finditer(r'\n<script>(.*?)</script>',s,re.S))[-1]
h=base64.b64encode(hashlib.sha256(m.group(1).encode('utf-8')).digest()).decode()
csp=("default-src 'none'; script-src 'sha256-%s'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
     "font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src 'none'; base-uri 'none'; form-action 'none'; upgrade-insecure-requests")%h
s=re.sub(r'(<meta http-equiv="Content-Security-Policy" content=")[^"]*(">)',lambda x:x.group(1)+csp+x.group(2),s)
open(p,'w',encoding='utf-8').write(s); print(csp)
