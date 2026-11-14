import os, re, shutil
SC=os.path.dirname(os.path.abspath(__file__))+'/'
SRC=SC+'_source/Sito.dc.html'
OUT=SC+'site/'
# keep img/fonts/favicon from previous build
s=open(SRC,encoding='utf-8').read()
ids={'4372872b5ce55017a8cca6fcaa83d7c9':'p2026-intervento','991eaab1ff558d12bfc07682efdcfe4a':'p2026-domande','042d888eebeb65222b4932a5e0171c69':'p2024-icsis','7a8bf5e6ad10e6821e328776c9369275':'p2024-imh','1347f39dcc4bb02fb09515678777b477':'p2024-workshop','dccf84409b532c9f0709e86c13b2619a':'p2020-mathura','934ef65b967e113eadb95bd89ae93c60':'p2020-gruppo','9ff6acb077fe4c73c61a3bba675cf928':'p2020-cerchio','ce9badb37f8c7f261556337317684bab':'p2020-intervento','36a237531de98960f326b8165ccd301e':'p2020-premio','4c006e4433e93f998476d7c3dd2793e3':'p2020-attestato','c0cab902df5afbfb8facc02708b6e48d':'p2018-badge','a07401cfe7e7d74cf7fe4ba5e571f92b':'p2018-relatore','fd25d0e91f2daace56ccb4964c3148fe':'p2018-panel','8ac0112ae47c5706abdab5a69bd17d39':'p2018-colleghi','224e05766db83b4d33e6ba19ddf95b5c':'antonio'}
def fix(h):
    h=h.replace('{{accent}}','#B8622B')
    for i,n in ids.items(): h=h.replace('/_blob/'+i,'img/'+n+'.jpg')
    return h
def part(a,b): return fix(s[s.index(a):s.index(b)])
CTA_MARK='<div style="max-width: 1120px; margin: 0 auto; padding: 72px 32px; display: flex; flex-direction: column; align-items: flex-start; gap: 20px">'
chi=part('<div id="chi-sono"','<div id="percorsi"')
perc=part('<div id="percorsi"','<div id="psicodramma"')
psi=part('<div id="psicodramma"',CTA_MARK)
cv=part('<div id="curriculum"','<div id="internazionale"')
intl=part('<div id="internazionale"','<div id="contatti"')
def h1(x): return x.replace('<h2 class="h2">','<h1 class="h2">',1).replace('</h2>','</h1>',1)
chi=h1(chi); intl=h1(intl)
cv=cv.replace('<h2 class="h2">Curriculum</h2>','<h2 class="h2">Curriculum</h2>',1)
TEL='+393518666942'; MAIL=os.environ.get('SITE_CONTACT_EMAIL','REPLACE_WITH_CONTACT_EMAIL')
SUBJ='mailto:'+MAIL+'?subject=Richiesta%20di%20primo%20colloquio'
WA='https://wa.me/393518666942?text=Buongiorno%2C%20vorrei%20richiedere%20un%20primo%20colloquio.'
FB='https://www.facebook.com/DottAntonioCervigni'; IG='https://www.instagram.com/dottantoniocervigni/'; LI='https://www.linkedin.com/in/antonio-cervigni-87541028/'; MAPS='https://share.google/MHg5bbZPF2NxSPYgF'; ORD='https://ordinepsicologilazio.it/albo/antoniocervigni'
css=s[s.index('<style>')+7:s.index('</style>')]
css=css.replace('body{margin:0;background:#F6F3EC}','')
fonts='''@font-face{font-family:'Cormorant Garamond';font-weight:500;font-style:normal;font-display:swap;src:url(fonts/cormorant-garamond-latin-500-normal.woff2) format('woff2')}
@font-face{font-family:'Cormorant Garamond';font-weight:600;font-style:normal;font-display:swap;src:url(fonts/cormorant-garamond-latin-600-normal.woff2) format('woff2')}
@font-face{font-family:'Inter';font-weight:400;font-style:normal;font-display:swap;src:url(fonts/inter-latin-400-normal.woff2) format('woff2')}
@font-face{font-family:'Inter';font-weight:500;font-style:normal;font-display:swap;src:url(fonts/inter-latin-500-normal.woff2) format('woff2')}
html{scroll-behavior:smooth}
:root{--ease-out:cubic-bezier(.23,1,.32,1);--ease-in-out:cubic-bezier(.77,0,.175,1)}
::selection{background:#B8622B;color:#F6F3EC}
:focus-visible{outline:2px solid #B8622B;outline-offset:2px}
.art h2{font-family:'Cormorant Garamond',Georgia,serif;font-weight:500;font-size:30px;margin:40px 0 16px;color:#1F3A3D}
.art .pq{margin:34px 0;padding:4px 0 4px 24px;border-left:3px solid #B8622B;font-family:'Cormorant Garamond',Georgia,serif;font-size:27px;line-height:1.3;color:#1F3A3D}
.art figure{margin:32px 0;max-width:440px}.art figure img{display:block;width:100%;height:auto;border-radius:10px}
.art figcaption{margin-top:8px;font-size:14px;color:#4A5F61}
.art a,.art .p a[href*=nicolecompagnoni]{color:#9A4F20}

.how{display:grid;grid-template-columns:320px 1fr;gap:48px;align-items:center;margin:0 0 64px}
.how.r{grid-template-columns:1fr 320px}.how.r .vig{order:2}
.how .vig{margin:0;width:100%;max-width:none}
.how h2{font-family:'Cormorant Garamond',Georgia,serif;font-weight:500;font-size:34px;line-height:1.15;margin:0 0 12px;color:#1F3A3D}
.how p{margin:0;font-size:18px;line-height:1.7;max-width:none}
.how .n{display:block;font-family:'Cormorant Garamond',Georgia,serif;font-size:22px;color:#B8622B;margin-bottom:4px}
.lead strong,.how strong{font-weight:600;color:#1F3A3D}
@media (max-width:820px){.how,.how.r{grid-template-columns:1fr;gap:20px;margin-bottom:48px}.how.r .vig{order:0}.how .vig{max-width:360px}}

.cform{display:grid;grid-template-columns:1fr 1fr;gap:18px;max-width:820px;margin-top:22px}
.cform .full{grid-column:1/-1}
.cform label{display:block;font-weight:500;font-size:.95rem;margin-bottom:6px;color:#1F3A3D}
.cform input,.cform select,.cform textarea{width:100%;box-sizing:border-box;min-height:48px;padding:12px 14px;border:1px solid #B9B09A;border-radius:6px;background:#fff;font:inherit;color:#1F3A3D}
.cform textarea{min-height:150px;resize:vertical;line-height:1.5}
.cform input:focus,.cform select:focus,.cform textarea:focus{outline:2px solid #B8622B;outline-offset:1px;border-color:#B8622B}
.cform .hp{position:absolute;left:-9999px;height:0;overflow:hidden}
.cform .chk{display:flex;gap:12px;align-items:flex-start;font-weight:400;font-size:.95rem;line-height:1.5}
.cform .chk input{width:22px;min-height:22px;height:22px;margin-top:2px;flex:none}
.cform .note{font-size:.95rem;color:#4A5F61;margin:0}
.cform button.btn{border:0;cursor:pointer;font:inherit;font-weight:500}
@media (max-width:700px){.cform{grid-template-columns:1fr}}

.faq{max-width:820px;margin-top:22px}
.faq details{background:#fff;border-radius:14px;margin:0 0 12px;box-shadow:0 2px 10px rgba(31,58,61,.07),0 1px 2px rgba(31,58,61,.05)}
.faq summary{cursor:pointer;list-style:none;padding:18px 54px 18px 24px;font-family:'Cormorant Garamond',serif;font-size:1.4rem;line-height:1.25;color:#1F3A3D;position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:"+";position:absolute;right:22px;top:50%;transform:translateY(-50%) rotate(0deg);font-family:Inter,sans-serif;font-size:1.6rem;color:#B8622B;transition:transform 220ms var(--ease-out)}
.faq details[open] summary:after{transform:translateY(-50%) rotate(45deg)}
.faq details p{margin:0;padding:0 24px 20px;line-height:1.6}
.faq summary:focus-visible{outline:2px solid #B8622B;outline-offset:2px;border-radius:14px}

.row a,.p a[href*=nicolecompagnoni]{color:#E8B48F;text-decoration:underline;text-underline-offset:3px}.row a:hover{color:#fff}
.ci{vertical-align:-5px;margin-right:9px;flex:none}.chd{display:flex;align-items:center}.chd .ci{margin-right:11px}.btn .ci{vertical-align:-4px;margin-right:8px}
#percorsi-e-situazioni,#faq{scroll-margin-top:90px}
body{margin:0;background:#F6F3EC;color:#1F3A3D;font-family:'Inter',Arial,sans-serif;font-size:17px;line-height:1.65}
'''
extra='''
.hd{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;max-width:1120px;margin:0 auto;padding:28px 32px}
.brand{display:flex;align-items:center;gap:14px;text-decoration:none}
.brand span{font-family:'Cormorant Garamond',Georgia,serif;font-weight:600;font-size:27px;letter-spacing:.5px;white-space:nowrap}
@media (max-width:420px){.brand span{font-size:23px;letter-spacing:.3px}.brand{gap:10px}}
.nav{display:flex;flex-wrap:wrap;align-items:center;gap:6px 22px;font-size:15px}
.nav a{text-decoration:none;padding:6px 0;border-bottom:2px solid transparent}
.nav a[aria-current=page],.ddt.cur{border-bottom-color:#B8622B}
.dd{position:relative}
.ddt{font:inherit;color:inherit;background:none;border:0;border-bottom:2px solid transparent;padding:6px 0;cursor:pointer;transition:transform 140ms var(--ease-out)}
.ddt:active{transform:scale(.97)}
.ddm{display:block;position:absolute;left:-18px;top:100%;z-index:30;min-width:250px;background:#fff;border:1px solid #D8D0BE;border-radius:10px;padding:8px 0;box-shadow:0 10px 30px rgba(31,58,61,.14);transform-origin:top left;opacity:0;visibility:hidden;transform:scale(.96);pointer-events:none;transition:opacity 160ms var(--ease-out),transform 160ms var(--ease-out)}
.dd:hover .ddm,.dd:focus-within .ddm{opacity:1;visibility:visible;transform:scale(1);pointer-events:auto}
.ddm a{display:block;padding:10px 18px;border-bottom:0}
.ddm a:hover{background:#F1ECE1}.ddm a[aria-current=page]{color:#9A4F20;font-weight:600;border-bottom:0}
.mnav{display:none}
@media (max-width:900px){
.nav{display:none}.mnav{display:block}
.hd{padding:18px 20px;flex-wrap:wrap}
.mnav summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:10px;font-weight:500;font-size:15px;padding:10px 14px;border:1px solid #1F3A3D;border-radius:6px;min-height:44px;box-sizing:border-box;transition:transform 140ms var(--ease-out)}
.mnav summary:active{transform:scale(.97)}
.mnav summary::-webkit-details-marker{display:none}
.bars{display:inline-block;width:18px;height:2px;background:#1F3A3D;box-shadow:0 6px 0 #1F3A3D,0 -6px 0 #1F3A3D}
.mnav[open]{flex-basis:100%;order:3}
.mnav[open] summary{display:inline-flex}
.mnav nav{display:flex;flex-direction:column;margin-top:14px;border-top:1px solid #D8D0BE}
.mnav nav a{padding:14px 4px;text-decoration:none;border-bottom:1px solid #E4DCCB;font-size:17px}
.mnav nav a.ms{padding-left:22px;font-size:16px}
.mnav nav a[aria-current=page]{color:#9A4F20;font-weight:600}
.mh{padding:14px 4px 6px;font-size:13px;letter-spacing:2px;text-transform:uppercase;color:#4A5F61}
}
.btn{display:inline-block;box-sizing:border-box;min-height:48px;padding:12px 28px;border-radius:4px;font-weight:500;text-decoration:none;transition:transform 140ms var(--ease-out),background 160ms var(--ease-out)}
.btn:active{transform:scale(.97)}
.btn1{background:#1F3A3D;color:#F6F3EC}.btn1:hover{background:#2C4F53;color:#F6F3EC}
.btn2{border:1px solid #1F3A3D}.btn2:hover{background:#ECE6D9;color:#1F3A3D}
.btns{display:flex;flex-wrap:wrap;gap:12px}
.eyebrow{font-size:14px;letter-spacing:5px;text-transform:uppercase;color:#9A4F20;font-weight:500}
.ft{background:#ECE6D9;margin-top:0}
.ft .in{max-width:1120px;margin:0 auto;padding:48px 32px;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:32px;font-size:15px}
.ft h3{margin:0 0 8px;font-family:'Cormorant Garamond',Georgia,serif;font-size:22px}
.ft p{margin:0 0 6px}
.mbar{display:none}
.quotes{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px}
.quotes figure{margin:0;padding:8px 0;display:flex;gap:24px;align-items:center}
.quotes .ritr{width:112px;height:112px;flex:none}
@media (max-width:700px){.quotes .ritr{width:84px;height:84px}.quotes figure{gap:16px;align-items:flex-start}.quotes blockquote{font-size:22px}}
.quotes blockquote{margin:0;font-family:'Cormorant Garamond',Georgia,serif;font-weight:500;font-size:26px;line-height:1.25;color:#1F3A3D}
.quotes figcaption{margin-top:12px;font-size:14px;letter-spacing:2px;text-transform:uppercase;color:#4A5F61}
.figbox{display:block;position:relative;align-self:stretch;width:100%;height:0}
.fig{position:absolute;right:0;top:0;width:270px;height:auto}
.figbox.sm .fig{width:190px}
@media (max-width:900px){.figbox.sm .fig{width:55%;max-width:190px}.figbox{height:auto;margin:0 0 24px}.fig{position:static;display:block;margin:0 auto;width:80%;max-width:320px}}
.vig{display:block;width:100%;max-width:520px;height:auto;margin:0 0 28px}
.when{display:grid;grid-template-columns:repeat(6,1fr);gap:22px;margin-top:22px}
.when>div{grid-column:span 2;background:#fff;border-radius:16px;padding:24px 24px 14px;box-shadow:0 2px 10px rgba(31,58,61,.07),0 1px 2px rgba(31,58,61,.05)}
.when h3{font-family:'Cormorant Garamond',serif;font-size:1.5rem;margin:0 0 12px;color:#1F3A3D}
.when ul{list-style:none;margin:0;padding:0}
.when li{position:relative;padding:0 0 12px 22px;line-height:1.5}
.when li:before{content:"";position:absolute;left:0;top:.6em;width:9px;height:9px;border-radius:50%;background:#B8622B}
@media (max-width:900px){.when{grid-template-columns:1fr}.when>div,.when>div:nth-child(n+4){grid-column:auto}}
.when a{color:#B8622B}
.acard{display:flex;gap:28px;align-items:center}
.acard .vig{width:210px;flex:none;margin:0}
@media (max-width:700px){.acard{flex-direction:column;align-items:flex-start}.acard .vig{width:100%}}
.trio{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px;margin:28px 0}
.trio figure{margin:0}
.trio img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:6px;border:1px solid #C9C1AF}
.trio figcaption{margin-top:10px;font-size:14px;color:#4A5F61}
.ico{display:block;margin:0 0 14px}
.steps{counter-reset:s}
.steps .card{position:relative}
.steps .card b{display:block;font-family:'Cormorant Garamond',Georgia,serif;font-size:36px;color:#B8622B;line-height:1;margin-bottom:8px}
@media (max-width:700px){.mbar{display:flex;position:fixed;left:0;right:0;bottom:0;gap:8px;padding:10px 16px;background:#F6F3EC;border-top:1px solid #C9C1AF;z-index:10}.mbar a{flex:1;text-align:center;padding:10px 12px;min-height:44px}body{padding-bottom:76px}}
'''
open(OUT+'styles.css','w',encoding='utf-8').write(fonts+css+extra)
logo='<svg width="48" height="60" viewBox="0 0 200 250" aria-hidden="true"><circle cx="100" cy="30" r="9" fill="#B8622B"/><path d="M100 52 V222" stroke="#1F3A3D" stroke-width="14" stroke-linecap="round" fill="none"/><path d="M36 58 C36 150 62 170 100 170 C138 170 164 150 164 58" stroke="#1F3A3D" stroke-width="14" stroke-linecap="round" fill="none"/></svg>'
SUB=[('come-lavoro.html','Come lavoro'),('index.html#percorsi-e-situazioni','Percorsi'),('psicodramma.html','Psicodramma'),('test-sis.html','Il test SIS'),('formazione.html','Formazione e supervisione')]
NAV=[('index.html','Home'),('chi-sono.html','Chi sono'),('SUB','Di cosa mi occupo'),('scritti.html','Scritti'),('internazionale.html','Attività internazionale'),('index.html#faq','FAQ'),('contatti.html','Contatti')]
def header(cur):
    def a(h,t): return f'<a href="{h}"'+(' aria-current="page"' if h==cur else '')+f'>{t}</a>'
    insub=any(h==cur for h,_ in SUB)
    desk=''; mob=''
    for h,t in NAV:
        if h=='SUB':
            desk+='<div class="dd"><button type="button" class="ddt'+(' cur' if insub else '')+'" aria-haspopup="true">'+t+'<span aria-hidden="true"> ▾</span></button><div class="ddm">'+''.join(a(x,y) for x,y in SUB)+'</div></div>'
            mob+='<span class="mh">'+t+'</span>'+''.join(a(x,y).replace('<a ','<a class="ms" ',1) for x,y in SUB)
        else:
            desk+=a(h,t); mob+=a(h,t)
    return (f'<header class="hd"><a class="brand" href="index.html" aria-label="Antonio Cervigni, home">{logo}<span>Dott. Antonio Cervigni</span></a>'
            f'<nav class="nav" aria-label="Menu principale">{desk}</nav>'
            f'<details class="mnav"><summary aria-label="Apri il menu"><span class="bars" aria-hidden="true"></span>Menu</summary><nav aria-label="Menu principale">{mob}</nav></details></header>\n')
footer=f'''<footer class="ft"><div class="in">
<div><h3>Dott. Antonio Cervigni</h3><p>Psicologo, psicoterapeuta, psicodrammatista</p><p>Iscritto all'<a href="{ORD}" target="_blank" rel="noopener">Ordine degli Psicologi del Lazio</a> n. 15877</p><p><a href="test-sis.html">Il test SIS</a> · <a href="formazione.html">Formazione e supervisione</a></p></div>
<div><h3>Studio</h3><p>Contrada Potenza 34, Fraz. Rotelli<br>Pollenza (MC)</p><p><a href="{MAPS}" target="_blank" rel="noopener">Come raggiungermi</a></p></div>
<div><h3>Contatti</h3><p><a href="tel:{TEL}">+39 351 866 6942</a></p><p><a href="{SUBJ}">{MAIL}</a></p><p><a href="{FB}">Facebook</a> · <a href="{IG}">Instagram</a> · <a href="{LI}">LinkedIn</a></p><p><a href="privacy.html">Informativa sulla privacy</a></p></div>
</div></footer>
<div class="mbar"><a class="btn btn1" href="tel:{TEL}">Chiama</a><a class="btn btn2" href="{WA}">WhatsApp</a><a class="btn btn2" href="{SUBJ}">Email</a></div>
'''
import sys; sys.path.insert(0,'.')
from icons import I

import re
from icons import V
VMAP={'india-ponti-persone-orizzonti.html':'india','amore-nome-della-distanza.html':'distanza','sintomi-moderni.html':'sintomi','parola-che-salva.html':'separazione','perturbante.html':'perturbante','amore-che-manca.html':'narcisismo','capriccio.html':'capriccio','notte-dei-morti.html':'morti','notte-dei-bambini.html':'notte_bambini'}

from icons import ci,CI
def contatti_icons(b):
    A_='#B8622B'; C_='#F6F3EC'
    def hh(t,k): return b.replace('<h3>%s</h3>'%t,'<h3 class="chd">'+ci(CI[k],A_,26)+t+'</h3>',1)
    for t,k in [('Studio','pin'),('Orari','clock'),('Recapiti','phone'),('Online','globe')]: b=hh(t,k)
    b=b.replace('>Chiama +39','>'+ci(CI['phone'],C_,18)+'Chiama +39',1)
    b=b.replace('>Scrivimi su WhatsApp<','>'+ci(CI['wa'],'#1F3A3D',18)+'Scrivimi su WhatsApp<',1)
    b=b.replace('>Scrivimi una email<','>'+ci(CI['mail'],'#1F3A3D',18)+'Scrivimi una email<',1)
    b=b.replace('>Compila il modulo<','>'+ci(CI['mail'],'#1F3A3D',18)+'Compila il modulo<',1)
    b=b.replace('>Come raggiungermi<','>'+ci(CI['pin'],'#1F3A3D',18)+'Come raggiungermi<',1)
    b=b.replace('Telefono: <a','Telefono: <a',1)
    for n,k in [('Facebook','fb'),('Instagram','ig'),('LinkedIn','in')]:
        b=b.replace('">%s</a>'%n,'">'+ci(CI[k],'#1F3A3D',20)+n+'</a>',1)
    new_cards=('<div class="card"><h3 class="chd">'+ci(CI['wa'],A_,26)+'WhatsApp</h3><p>Se preferisci scrivere, puoi mandarmi un messaggio: ti rispondo appena posso.</p><p style="margin-top: 14px"><a class="btn btn2" href="'+WA+'">'+ci(CI['wa'],'#1F3A3D',18)+'Apri WhatsApp</a></p></div>\n'
      '<div class="card"><h3 class="chd">'+ci(CI['group'],A_,26)+'Gruppi di psicodramma</h3><p>Tengo gruppi di psicodramma per adolescenti e adulti. Se vuoi partecipare, scrivimi: ci incontriamo, ne parliamo e valutiamo insieme se il percorso fa per te.</p><p style="margin-top: 14px"><a class="btn btn2" href="psicodramma.html">Scopri lo psicodramma</a></p></div>\n')
    i=b.find('<div class="card"><h3 class="chd">'+ci(CI['globe'],A_,26)+'Online')
    assert i>0
    return b[:i]+new_cards+b[i:]
def fb(x): return '<span class="figbox">'+x+'</span>'
def decorate(fname,body):
    if fname=='psicodramma.html': body=body.replace('<div class="eyebrow">Il mio metodo</div>',fb(I['scena_grande'])+'<div class="eyebrow">Il mio metodo</div>',1)
    if fname=='chi-sono.html': body=body.replace('<h1',fb(I['studio'])+'<h1',1)
    if fname=='internazionale.html': body=body.replace('<h1',fb(I['mondo'])+'<h1',1)
    if fname=='contatti.html': body=body.replace('<h1',fb(I['studio_luogo']).replace('class="figbox"','class="figbox sm"')+'<h1',1)
    if fname=='contatti.html': body=contatti_icons(body)
    if fname in VMAP: body=re.sub(r'(Lettura di circa \d+ minuti</p>)',lambda m:m.group(1)+'\n'+V[VMAP[fname]],body,count=1)
    body=body.replace('<h2 class="h2">Parliamone</h2>',fb(I['bolle'])+'<h2 class="h2">Parliamone</h2>')
    return body
def page(fname,title,desc,body,extra_head=''):
    body=decorate(fname,body)
    html=f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#F6F3EC">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="img/antonio.jpg">
<meta name="google-site-verification" content="oAqAZoIw_TDVErMqa6pE4PqYRUx2FD87C9n0qi3HKB4" />
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon.ico" sizes="48x48">
<link rel="icon" href="icon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="stylesheet" href="styles.css">
{extra_head}</head>
<body>
{header(fname)}<main>
{body}</main>
{footer}<script>document.querySelectorAll('.mnav a').forEach(function(a){{a.addEventListener('click',function(){{a.closest('details').open=false}})}})</script>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "899713410b5146bdb18ad4a35535dadb"}}'></script><!-- End Cloudflare Web Analytics -->
<!--Start of Tawk.to Script-->
<script type="text/javascript">
var Tawk_API=Tawk_API||{{}}, Tawk_LoadStart=new Date();
(function(){{
var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
s1.async=true;
s1.src='https://embed.tawk.to/6af773cae8265e3c3e62e6c9/1k7b9ojnq';
s1.charset='UTF-8';
s1.setAttribute('crossorigin','*');
s0.parentNode.insertBefore(s1,s0);
}})();
</script>
<!--End of Tawk.to Script-->
</body>
</html>
'''
    html=html.replace('psicodramma analitico','psicodramma freudiano').replace('Psicodramma analitico','Psicodramma freudiano').replace('psicodramma freudiano freudiano','psicodramma freudiano')
    html=html.replace('FORM_TARGET_EMAIL',MAIL)
    open(OUT+fname,'w',encoding='utf-8').write(html)
steps='''<div class="wrap" style="padding-top: 56px; padding-bottom: 56px">
<h2 class="h2">Come si prende appuntamento</h2>
<div class="grid steps">
<div class="card"><b>1</b><h3>Scrivimi o chiamami</h3><p>Mi basta un breve messaggio o una telefonata: dimmi chi sei e che cosa ti porta a cercare un aiuto. Se si tratta di un figlio, parliamone prima con i genitori.</p></div>
<div class="card"><b>2</b><h3>Il primo colloquio</h3><p>Ci incontriamo nello studio a Pollenza per conoscerci. Racconti la tua storia con i tuoi tempi, io ascolto e ti dico come lavoro, senza alcun impegno.</p></div>
<div class="card"><b>3</b><h3>Decidiamo insieme</h3><p>Se la strada ti convince, definiamo il percorso: colloqui individuali, un gruppo di psicodramma o un lavoro con la famiglia.</p></div>
</div>
</div>
'''
import sys; sys.path.insert(0,'.')
from icons import I
def put(html,pairs):
    for key,ic in pairs: html=html.replace(key,ic+key,1)
    return html
steps=put(steps,[('<b>1</b>',I['passo1']),('<b>2</b>',I['passo2']),('<b>3</b>',I['passo3'])])
band=f'''<div style="background:#1F3A3D;color:#F6F3EC"><div class="wrap" style="align-items:flex-start">
<h2 class="h2">Parliamone</h2>
<p class="p">Se ti riconosci in qualcosa di quanto hai letto, scrivimi o chiamami. Il primo colloquio è un momento per conoscerci e decidere insieme come proseguire.</p>
<div class="btns"><a class="btn btn2" style="background:#F6F3EC;color:#1F3A3D;border-color:#F6F3EC" href="tel:{TEL}">Chiama +39 351 866 6942</a><a class="btn btn2" style="border-color:#F6F3EC;color:#F6F3EC" href="{WA}">Scrivimi su WhatsApp</a><a class="btn btn2" style="border-color:#F6F3EC;color:#F6F3EC" href="{SUBJ}">Email</a></div>
</div></div>
'''
jsonld='<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"Dott. Antonio Cervigni - Psicologo e Psicoterapeuta","description":"Psicologo dello sviluppo e dell\'educazione, psicoterapeuta, psicodrammatista e psicoanalista a Pollenza (Macerata).","telephone":"+393518666942","email":"FORM_TARGET_EMAIL","address":{"@type":"PostalAddress","streetAddress":"Contrada Potenza 34, Fraz. Rotelli","addressLocality":"Pollenza","addressRegion":"MC","addressCountry":"IT"},"sameAs":["'+FB+'","'+IG+'","'+LI+'"]}</script>\n'
# HOME
hero=f'''<div class="wrap" style="padding-top: 48px; padding-bottom: 80px; flex-direction: row; flex-wrap: wrap; align-items: center; gap: 48px"><div style="flex: 1 1 480px; display: flex; flex-direction: column; gap: 28px">
<div class="eyebrow">Psicologo e psicoterapeuta · Pollenza (MC)</div>
<h1 style="margin: 0; max-width: 860px; font-family: 'Cormorant Garamond', Georgia, serif; font-weight: 500; font-size: clamp(40px, 7vw, 64px); line-height: 1.08">Ciò che non si riesce a dire può trovare un luogo dove essere ascoltato.</h1>
<p class="p" style="font-size: 19px">Psicologo, psicoterapeuta a orientamento psicoanalitico e psicodrammatista freudiano. Nel mio studio di Pollenza accolgo bambini, adolescenti, adulti e famiglie. Il primo colloquio serve a conoscerci e a capire insieme se e come posso esserti utile.</p>
<div class="btns"><a class="btn btn1" href="contatti.html">Richiedi un primo colloquio</a><a class="btn btn2" href="tel:{TEL}">Chiama</a></div>
</div>
<img src="img/antonio.jpg" alt="Antonio Cervigni, psicologo e psicoterapeuta" style="flex: 0 1 360px; width: 360px; max-width: 100%; aspect-ratio: 4 / 5; object-fit: cover; object-position: center 18%; border-radius: 6px; display: block">
</div>
'''
perc_h=perc.replace('<h2 class="h2">Percorsi</h2>','<h2 class="h2">Di cosa mi occupo</h2>',1).replace('Qui sotto trovi come funziona.','Scopri come funziona.')
perc_h=put(perc_h,[('<h3>Colloqui psicologici',I['colloqui']),('<h3>Psicoterapia psicoanalitica',I['psicoterapia']),('<h3>Bambini, adolescenti',I['giovani']),('<h3>Gruppi di psicodramma',I['gruppi']),('<h3>Valutazione psicodiagnostica',I['psicodiagnosi']),('<h3>Lavoro e formazione',I['lavoro'])])
perc_h=perc_h.replace('Colloqui e test (tra cui TAT, CAT, WISC e il test SIS) per comprendere il funzionamento di bambini, adolescenti e adulti.','Colloqui e test, in particolare il test SIS (Somatic Inkblot Series), nel quale mi sono formato con il Dr. B.L. Dubey.')
perc_h=perc_h.rstrip()
assert perc_h.endswith('</div>')
perc_h=perc_h[:-6]+'<p class="p"><a href="come-lavoro.html">Scopri come lavoro</a> · <a href="test-sis.html">Il test SIS</a> · <a href="formazione.html">Formazione e supervisione</a> · <a href="psicodramma.html">Scopri lo psicodramma freudiano</a> · <a href="chi-sono.html">Leggi il mio percorso</a></p>\n</div>\n'
from ritratti import LACAN,DOLTO
quotes_h='''<div class="wrap" style="padding-top: 8px; padding-bottom: 24px"><div class="quotes">
<figure>'''+LACAN+'''<div><blockquote>«Il desiderio dell'uomo è il desiderio dell'Altro.»</blockquote><figcaption>Jacques Lacan</figcaption></div></figure>
<figure>'''+DOLTO+'''<div><blockquote>«Il bambino ha sempre l'intuizione della sua storia. Se gli viene detta la verità, questa verità lo costruisce.»</blockquote><figcaption>Françoise Dolto</figcaption></div></figure>
</div></div>
'''
intl_h='''<div style="background:#F1DFCB"><div class="wrap">
<p class="eyebrow">Attività internazionale</p>
<h2 class="h2" style="margin-top:12px">Il mio lavoro oltre i confini</h2>
<p class="p">Il mio lavoro non si ferma allo studio: da anni porto lo psicodramma analitico e la psicologia proiettiva in università, congressi e società scientifiche di diversi Paesi. Qui trovi le tappe più recenti.</p>
<div class="trio">
<figure><img src="img/p2026-intervento.jpg" alt="Antonio Cervigni al podio della conferenza NACIACP, Gautam Buddha University, 2026" loading="lazy"><figcaption>Gautam Buddha University, Greater Noida, aprile 2026</figcaption></figure>
<figure><img src="img/p2020-intervento.jpg" alt="Antonio Cervigni al podio, conferenza sulla psicologia proiettiva, SGT University, 2020" loading="lazy"><figcaption>SGT University, 2020</figcaption></figure>
<figure><img src="img/p2024-workshop.jpg" style="object-position:center 8%" alt="Antonio Cervigni davanti al cartello del workshop di psicodramma analitico, Hindustan Institute, Mathura, 2024" loading="lazy"><figcaption>Hindustan Institute, Mathura, novembre 2024</figcaption></figure>
</div>
<p><a class="btn btn1" href="internazionale.html">Scopri l'attività internazionale</a></p>
</div></div>
'''
when_h='''<div class="wrap" id="percorsi-e-situazioni">
<p class="eyebrow">Quando rivolgersi a me</p>
<h2 class="h2" style="margin-top:12px">Le situazioni in cui posso esserti utile</h2>
<p class="p">Non serve avere un problema preciso per cominciare: spesso si parte da un disagio che non ha ancora un nome. Queste sono le situazioni per cui più spesso le persone mi cercano, ma l'elenco non è chiuso.</p>
<div class="when">
<div><h3>Adulti</h3><ul>
<li>Ansia, attacchi di panico, stress e sensazione di essere sopraffatti</li>
<li>Tristezza, mancanza di slancio, umore depresso</li>
<li>Paure, fobie e situazioni che si tende a evitare</li>
<li>Pensieri che ritornano, rituali, bisogno di controllo</li>
<li>Insonnia e disturbi del corpo legati allo stress</li>
<li>Momenti di passaggio: lavoro, separazioni, lutti, trasferimenti</li>
<li>Autostima, insicurezza, perfezionismo e senso di colpa</li>
<li>Rapporto con il cibo e con il corpo</li>
<li>Esperienze difficili del passato che continuano a farsi sentire</li>
<li>Decisioni importanti, senso di vuoto, domande su di sé</li>
</ul></div>
<div><h3>Preadolescenti e adolescenti</h3><ul>
<li>Difficoltà scolastiche, motivazione e metodo di studio</li>
<li>Scelta della scuola superiore o dell'università</li>
<li>Relazioni con i coetanei, bullismo e cyberbullismo</li>
<li>Gestione delle emozioni e del rapporto con i genitori</li>
<li>Ansia, tristezza, rabbia e sbalzi d'umore</li>
<li>Isolamento, ritiro sociale, rifiuto della scuola</li>
<li>Rapporto con il corpo, con il cibo e con l'immagine di sé</li>
<li>Uso eccessivo di telefono, social e videogiochi</li>
<li>Identità, primi amori e scoperta di sé</li>
</ul></div>
<div><h3>Bambini</h3><ul>
<li>Capricci, rabbia, paure e disturbi del sonno</li>
<li>Ansia da separazione e difficoltà a staccarsi dai genitori</li>
<li>Difficoltà di attenzione e di apprendimento</li>
<li>Timidezza, silenzi, difficoltà con i compagni</li>
<li>Ingresso a scuola e passaggio da un ciclo all'altro</li>
<li>Separazione dei genitori, lutti, nascita di un fratello</li>
<li>Disturbi dell'alimentazione, enuresi, difficoltà nel controllo degli sfinteri</li>
</ul></div>
<div><h3>Coppie</h3><ul>
<li>Conflitti che si ripetono e difficoltà a comunicare</li>
<li>Crisi, distanza, tradimenti e fiducia incrinata</li>
<li>Gelosia, dipendenza affettiva, solitudine a due</li>
<li>Difficoltà nell'intimità e nella sessualità</li>
<li>La nascita di un figlio e i cambiamenti della coppia</li>
<li>Separazione e vita dopo la separazione</li>
<li>Ritrovare un modo di stare insieme, o di lasciarsi con rispetto</li>
</ul></div>
<div><h3>Genitori e famiglie</h3><ul>
<li>Consulenza ai genitori sul modo di accompagnare i figli</li>
<li>Supporto nei momenti di difficoltà con un figlio</li>
<li>Famiglie in crisi, separazioni e famiglie ricomposte</li>
<li>Lutti e malattie in famiglia</li>
<li>Conflitti tra generazioni e rapporto con i genitori anziani</li>
<li>Genitorialità: dubbi, stanchezza, senso di inadeguatezza</li>
</ul></div>
<div><h3>Lavoro, sport e gruppi</h3><ul>
<li>Stress da lavoro, burnout, conflitti nei gruppi di lavoro</li>
<li>Sportelli di ascolto psicologico e formazione per team</li>
<li>Ansia da prestazione e gestione della pressione, anche nello sport</li>
<li>Giovani atleti, genitori e allenatori</li>
<li>Gruppi di psicodramma per adolescenti e adulti: mettere in scena ciò che si vive nelle relazioni</li>
<li>Per partecipare mi scrivi, ci incontriamo e valutiamo insieme se il gruppo fa per te: <a href="psicodramma.html">scopri lo psicodramma</a></li>
</ul></div>
</div>
<p class="p" style="margin-top:20px">Se non ti riconosci in nessuna di queste voci, scrivimi lo stesso: ne parliamo insieme.</p>
<p><a class="btn btn1" href="contatti.html">Chiedi un primo colloquio</a></p>
</div>
'''
faq_h='''<div class="wrap" id="faq">
<p class="eyebrow">Prima di scrivermi</p>
<h2 class="h2" style="margin-top:12px">Le domande che mi fanno più spesso</h2>
<div class="faq">
<details><summary>Come capisco se ho bisogno di uno psicologo?</summary><p>Se senti che qualcosa non va, forse lo sai già. Può essere un sintomo che non riconosci come tuo e che, come un «intimo estraneo», ti sta accanto tutti i giorni: un&#x27;ansia, una tristezza, una paura, un gesto che si ripete senza che tu sappia perché. Non serve un motivo «abbastanza grave»: se qualcosa ti pesa da tempo, vale la pena parlarne. Il primo colloquio serve a questo: capire insieme di che cosa si tratta.</p></details>
<details><summary>Che cosa succede al primo colloquio?</summary><p>Ci conosciamo. Mi racconti ciò che ti porta da me, con i tuoi tempi e le tue parole. Io ascolto, ti spiego come lavoro e vediamo insieme se e come proseguire. Non ti chiedo nessun impegno.</p></details>
<details><summary>Quanto dura un percorso?</summary><p>Non c&#x27;è una durata uguale per tutti. Alcune situazioni richiedono pochi incontri, altre un lavoro più lungo. Lo decidiamo insieme, e ne riparliamo strada facendo.</p></details>
<details><summary>Come funziona se la richiesta riguarda mio figlio?</summary><p>Si comincia dai genitori: ne parliamo prima insieme, con il consenso dei genitori, e poi incontro il bambino o il ragazzo. Ai genitori resta un posto importante, ma lo spazio del figlio rimane suo e riservato.</p></details>
<details><summary>Per lo psicodramma bisogna saper recitare?</summary><p>No, non serve essere attori né saper recitare. Nel gruppo si mette in scena ciò che si vive, con il gioco e con gli altri, e si può cominciare anche solo guardando. Tengo gruppi per adolescenti e adulti nel mio studio. Per partecipare mi scrivi, ci incontriamo, ne parliamo e valutiamo insieme se il percorso fa per te; poi entri nel gruppo.</p></details>
<details><summary>Quello che dico resta riservato?</summary><p>Sì. Il segreto professionale è un obbligo del mio lavoro. Nel modulo di contatto ti chiedo solo il necessario per risponderti: la tua storia la racconti di persona, nel mio studio.</p></details>
</div>
<p class="p" style="margin-top:22px">Hai un'altra domanda? Scrivimi, ti rispondo volentieri.</p>
<p><a class="btn btn1" href="contatti.html">Scrivimi</a></p>
</div>
'''
faq_ld='<script type="application/ld+json">'+'{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "Come capisco se ho bisogno di uno psicologo?", "acceptedAnswer": {"@type": "Answer", "text": "Se senti che qualcosa non va, forse lo sai già. Può essere un sintomo che non riconosci come tuo e che, come un «intimo estraneo», ti sta accanto tutti i giorni: un\'ansia, una tristezza, una paura, un gesto che si ripete senza che tu sappia perché. Non serve un motivo «abbastanza grave»: se qualcosa ti pesa da tempo, vale la pena parlarne. Il primo colloquio serve a questo: capire insieme di che cosa si tratta."}}, {"@type": "Question", "name": "Che cosa succede al primo colloquio?", "acceptedAnswer": {"@type": "Answer", "text": "Ci conosciamo. Mi racconti ciò che ti porta da me, con i tuoi tempi e le tue parole. Io ascolto, ti spiego come lavoro e vediamo insieme se e come proseguire. Non ti chiedo nessun impegno."}}, {"@type": "Question", "name": "Quanto dura un percorso?", "acceptedAnswer": {"@type": "Answer", "text": "Non c\'è una durata uguale per tutti. Alcune situazioni richiedono pochi incontri, altre un lavoro più lungo. Lo decidiamo insieme, e ne riparliamo strada facendo."}}, {"@type": "Question", "name": "Come funziona se la richiesta riguarda mio figlio?", "acceptedAnswer": {"@type": "Answer", "text": "Si comincia dai genitori: ne parliamo prima insieme, con il consenso dei genitori, e poi incontro il bambino o il ragazzo. Ai genitori resta un posto importante, ma lo spazio del figlio rimane suo e riservato."}}, {"@type": "Question", "name": "Per lo psicodramma bisogna saper recitare?", "acceptedAnswer": {"@type": "Answer", "text": "No, non serve essere attori né saper recitare. Nel gruppo si mette in scena ciò che si vive, con il gioco e con gli altri, e si può cominciare anche solo guardando. Tengo gruppi per adolescenti e adulti nel mio studio. Per partecipare mi scrivi, ci incontriamo, ne parliamo e valutiamo insieme se il percorso fa per te; poi entri nel gruppo."}}, {"@type": "Question", "name": "Quello che dico resta riservato?", "acceptedAnswer": {"@type": "Answer", "text": "Sì. Il segreto professionale è un obbligo del mio lavoro. Nel modulo di contatto ti chiedo solo il necessario per risponderti: la tua storia la racconti di persona, nel mio studio."}}]}'+'</script>'

form_h='''<div class="wrap" id="modulo" style="padding-top: 24px; padding-bottom: 8px">
<h2 class="h2">Scrivimi un messaggio</h2>
<p class="p">Compila il modulo e ti rispondo appena possibile. Bastano poche righe: la tua storia la raccontiamo di persona, nel mio studio.</p>
<form class="cform" action="https://formsubmit.co/FORM_TARGET_EMAIL" method="post">
<input type="hidden" name="_subject" value="Richiesta dal sito antoniocervigni.it">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_next" value="https://www.antoniocervigni.it/grazie.html">
<div><label for="f-nome">Nome *</label><input id="f-nome" name="nome" type="text" autocomplete="given-name" required maxlength="80"></div>
<div><label for="f-cognome">Cognome *</label><input id="f-cognome" name="cognome" type="text" autocomplete="family-name" required maxlength="80"></div>
<div><label for="f-email">Email *</label><input id="f-email" name="email" type="email" autocomplete="email" required maxlength="120"></div>
<div><label for="f-tel">Telefono *</label><input id="f-tel" name="telefono" type="tel" autocomplete="tel" required maxlength="40"></div>
<div class="full"><label for="f-tipo">Tipo di richiesta *</label><select id="f-tipo" name="tipo" required>
<option value="" selected disabled>Scegli…</option>
<option>Colloquio individuale per adulti</option>
<option>Colloquio per un adolescente</option>
<option>Colloquio per un bambino</option>
<option>Colloquio di coppia</option>
<option>Consulenza per genitori o famiglia</option>
<option>Gruppo di psicodramma</option>
<option>Lavoro, formazione o collaborazioni</option>
<option>Altro</option></select></div>
<div class="full"><label for="f-msg">Messaggio *</label><textarea id="f-msg" name="messaggio" required maxlength="3000"></textarea></div>
<p class="note full">Non scrivere nel messaggio dettagli clinici o dati sulla tua salute: ne parleremo di persona, con la tutela del segreto professionale.</p>
<div class="hp" aria-hidden="true"><label>Non compilare questo campo<input name="_honey" type="text" tabindex="-1" autocomplete="off"></label></div>
<label class="chk full"><input type="checkbox" name="consenso" value="1" required><span>Ho letto l'<a href="privacy.html" target="_blank" rel="noopener">informativa sulla privacy</a> e acconsento al trattamento dei miei dati per essere ricontattato.</span></label>
<div class="full"><button class="btn btn1" type="submit">Invia il messaggio</button></div>
</form>
</div>
'''
form_h=form_h.replace('FORM_TARGET_EMAIL',MAIL)

grazie_h='''<div class="wrap" style="padding-top: 56px; padding-bottom: 96px; max-width: 760px">
<h1 class="h2" style="font-size: 48px">Messaggio inviato</h1>
<p class="p">Grazie, ho ricevuto il tuo messaggio e ti risponderò appena possibile. Se è urgente, puoi anche chiamarmi al <a href="tel:{TEL}">+39 351 866 6942</a> o scrivermi su <a href="{WA}">WhatsApp</a>.</p>
<p style="margin-top: 28px"><a class="btn btn1" href="index.html">Torna al sito</a></p>
</div>
'''

from icons import W
def how(n,cls,key,title,text):
    return '<div class="how%s">'%cls+W[key]+'<div><span class="n">%s</span><h2>%s</h2><p>%s</p></div></div>\n'%(n,title,text)
come_h='''<div class="wrap" style="padding-top: 40px; padding-bottom: 40px">
<p class="eyebrow">Il mio modo di lavorare</p>
<h1 class="h2" style="font-size: clamp(36px, 8vw, 52px); margin-top: 12px">Come lavoro</h1>
<p class="p lead" style="font-size: 20px; max-width: 780px; margin-bottom: 56px">La psicoanalisi che pratico nasce con Freud ed è stata rinnovata da Jacques Lacan. Dietro i nomi c'è un'idea semplice: <strong>ognuno di noi è diverso da tutti gli altri</strong>, e nessuna ricetta vale per tutti. Per questo non ti propongo un metodo da applicare, ma <strong>un luogo dove essere ascoltato</strong>.</p>
'''+how('1','','persona','Una persona, non un caso',"Non cerco di farti rientrare in una diagnosi o in un manuale. Parole come ansia, tristezza o rabbia hanno <strong>storie diverse in ciascuno di noi</strong>. Il lavoro comincia dal chiederti di raccontare, <strong>con le tue parole e con i tuoi tempi</strong>, che cosa ti porta da me.")+how('2',' r','sintomo','Il sintomo ha qualcosa da dire',"Molte persone arrivano con qualcosa che sentono estraneo: un'ansia, un pensiero che ritorna, un malessere che non si spiega. È come <strong>un ospite che abita in casa tua</strong> senza che tu sappia perché. Non lo tratto soltanto come un nemico da eliminare, lo ascolto come <strong>un messaggio che nessuno ha ancora decifrato</strong>. Capire che cosa dice cambia spesso il modo di viverlo.")+how('3','','parola','La parola che cura',"Quando parliamo, diciamo sempre qualcosa di più di quello che pensiamo di dire: un'esitazione, un lapsus, una frase che ritorna, un sogno. È ciò che chiamiamo <strong>inconscio</strong>. Non è un luogo misterioso, è <strong>ciò che sappiamo senza sapere di saperlo</strong> e che si fa sentire nelle nostre parole. In studio ascolto anche quello che le tue parole dicono senza che tu lo voglia.")+how('4',' r','desiderio','Il desiderio',"Si soffre spesso perché si vive per quello che gli altri si aspettano da noi. Cerchiamo di capire <strong>che cosa desideri davvero</strong>. Il desiderio nasce da una <strong>mancanza</strong>, e sentire che qualcosa manca non è un difetto: è ciò che ci fa muovere, amare, creare. Il lavoro non consiste nel riempire il vuoto, ma nell'imparare a starci in modo meno doloroso.")+how('5','','strada','Nessuna ricetta',"Non ti dico che cosa fare della tua vita e non prometto la felicità. Ti accompagno a <strong>trovare la tua strada</strong>. I tempi non sono uguali per tutti: alcuni percorsi sono brevi, altri più lunghi, e <strong>ne parliamo insieme</strong> strada facendo.")+how('6',' r','studio','In studio',"Incontro adulti e adolescenti nei <strong>colloqui</strong>. Con i bambini <strong>il gioco e il disegno</strong> sono il modo in cui raccontano, e li ascolto così. Nei <strong>gruppi di psicodramma</strong> mettiamo in scena ciò che a parole è difficile dire. <strong>Non serve sapere nulla di psicoanalisi</strong> per cominciare: basta il desiderio di capire che cosa non va.")+'''<p class="p" style="font-size: 20px; margin-top: 8px">Se qualcosa di tutto questo ti parla, scrivimi o chiamami.</p>
<div class="btns" style="margin-top: 20px"><a class="btn btn1" href="contatti.html">Richiedi un primo colloquio</a><a class="btn btn2" href="psicodramma.html">Scopri lo psicodramma</a></div>
</div>
'''

sis_h='''<div class="wrap" style="padding-top: 40px; padding-bottom: 40px">
<p class="eyebrow">Somatic Inkblot Series</p>
<h1 class="h2" style="font-size: clamp(36px, 8vw, 52px); margin-top: 12px">Il test SIS: quando le immagini parlano del corpo</h1>
<p class="p lead" style="font-size: 20px; max-width: 780px; margin-bottom: 56px">Il SIS, Somatic Inkblot Series, è un <strong>test proiettivo</strong>: una serie di immagini a macchie, simili a quelle del più noto test di Rorschach, che ti chiedo semplicemente di guardare. È stato ideato dallo psichiatra americano <strong>Wilfred A. Cassell</strong> e si è diffuso nel mondo grazie al lavoro del <strong>Dr. B.L. Dubey</strong> e della Somatic Inkblot Society.</p>
'''+how('1','','sis_corpo','Che cosa lo rende diverso',"Le sue immagini richiamano il corpo: forme che possono ricordare un volto, un cuore, un abbraccio, una ferita. Per questo fanno emergere con facilità <strong>ciò che il corpo porta e che la parola fatica a nominare</strong>.")+how('2',' r','sis_svolge','Come si svolge',"Guardi le immagini una alla volta e dici che cosa ci vedi. <strong>Non ci sono risposte giuste o sbagliate</strong>, e non serve alcuna preparazione. Esiste in più versioni: una serie di 20 tavole, una di 62 immagini e una in video, che può essere proposta anche a un gruppo.")+how('3','','sis_sogno','A che cosa serve',"Mi aiuta a conoscerti più in fretta e più in profondità di quanto farebbero le sole domande. Ma soprattutto apre la parola: un'immagine che ti colpisce funziona <strong>come un sogno</strong>, e da lì si comincia a raccontare. Lo uso quindi sia per la valutazione sia dentro il percorso.")+how('4',' r','sis_rivista','Perché da me',"Mi sono formato al SIS direttamente con il Dr. B.L. Dubey, che oggi è in Ohio e con cui sono <strong>in stretto contatto</strong>. Sono <strong>l'unico in Italia a rappresentare la Somatic Inkblot Society</strong>, di cui sono direttore nazionale, e sono consulente editoriale del <i>Journal of Projective Psychology &amp; Mental Health</i>.")+'''<p class="p" style="font-size: 20px; margin-top: 8px">Se vuoi saperne di più, o sei un collega interessato alla formazione sul SIS, scrivimi.</p>
<div class="btns" style="margin-top: 20px"><a class="btn btn1" href="contatti.html">Scrivimi</a><a class="btn btn2" href="formazione.html">Formazione per i colleghi</a><a class="btn btn2" href="internazionale.html">Attività internazionale</a></div>
</div>
'''
for_h='''<div class="wrap" style="padding-top: 40px; padding-bottom: 40px">
<p class="eyebrow">Per i colleghi</p>
<h1 class="h2" style="font-size: clamp(36px, 8vw, 52px); margin-top: 12px">Formazione e supervisione</h1>
<p class="p lead" style="font-size: 20px; max-width: 780px; margin-bottom: 56px">Accanto al lavoro clinico, porto ciò che ho imparato a <strong>psicologi, psicoterapeuti e medici</strong>, in Italia e all'estero.</p>
'''+how('1','','for_supervisione','Gruppi di supervisione con lo psicodramma',"Tengo gruppi di supervisione per <strong>psicologi in formazione</strong>. Qui il caso non viene soltanto raccontato: <strong>si mette in scena</strong>. È un modo di imparare il mestiere che passa dall'esperienza, non soltanto dalla teoria.")+how('2',' r','for_scena','Come si svolge',"Chi porta un caso sceglie un momento del lavoro con il paziente che lo interroga: una seduta difficile, un silenzio, una frase che non sa come prendere. Il gruppo lo aiuta a giocarlo. Con il <strong>cambio di ruolo</strong>, chi cura prende per un momento il posto del paziente e sente dall'interno ciò che dal proprio posto non vedeva. Poi se ne parla insieme.")+how('3','','strada','Che cosa si impara',"Giocare un incontro fa vedere ciò che nel racconto sfugge: <strong>la posizione di chi cura</strong>, quello che il paziente gli fa provare, il punto in cui il lavoro si è fermato. Non si cercano ricette né giudizi: ognuno trova <strong>il proprio modo di stare nella relazione di cura</strong>. I casi sono presentati in forma anonima, e ciò che accade nel gruppo resta nel gruppo.")+how('4',' r','for_aula','Workshop sul test SIS',"Tengo <strong>workshop di formazione sulla Somatic Inkblot Series</strong>. Il primo in Italia si è svolto a Pollenza nel 2018, insieme al Dr. B.L. Dubey. <a href=\"test-sis.html\">Scopri che cos'è il test SIS</a>.")+how('5','','for_team','Workshop di psicodramma analitico',"Conduco <strong>workshop dimostrativi e pre-congressuali</strong>, come quelli tenuti nelle università indiane, per far conoscere il metodo a chi non l'ha mai incontrato.")+'''<p class="p" style="font-size: 20px; margin-top: 8px">Se vuoi partecipare a un gruppo di supervisione, scrivimi: ci sentiamo e ti spiego come funziona.</p>
<div class="btns" style="margin-top: 20px"><a class="btn btn1" href="contatti.html">Scrivimi</a><a class="btn btn2" href="psicodramma.html">Scopri lo psicodramma</a></div>
</div>
'''
sis_h=re.sub(r'<p class="p lead"[^>]*>(.*?)</p>', lambda m:'<div class="how r" style="margin-bottom:64px">'+W['sis_tavola']+'<div><p class="lead" style="font-size:20px;line-height:1.65">'+m.group(1)+'</p></div></div>', sis_h, count=1, flags=re.S)
def sec(x,c): return '<div style="background:%s">'%c+x+'</div>'
page('index.html',"Antonio Cervigni · Psicologo, psicoterapeuta e psicodrammatista · Pollenza (Macerata)","Psicologo dello sviluppo e dell'educazione, psicoterapeuta, psicodrammatista e psicoanalista. Studio a Pollenza (Macerata): percorsi per bambini, adolescenti, adulti e famiglie.",sec(hero,'#F6F3EC')+sec(quotes_h,'#ECE6D9')+sec(perc_h,'#DCE7E0')+sec(when_h,'#E7E9F0')+intl_h+sec(steps,'#F6F3EC')+sec(faq_h,'#F2E3DC')+band,jsonld+faq_ld)
# CHI SONO
chi_h=chi.replace('<div style="display: flex; flex-wrap: wrap; gap: 12px"><a href="tel:+393518666942"','<div class="btns"><a href="tel:+393518666942"',1)
m=re.search(r'(<p[^>]*>)Sono Antonio Cervigni,',chi_h); tag=m.group(1)
e=chi_h.index('scrivimi o chiamami.</p>',m.start())+len('scrivimi o chiamami.</p>')
NEW=["Mi chiamo Antonio Cervigni e sono psicologo dello sviluppo e dell'educazione, psicoterapeuta a orientamento psicoanalitico lacaniano e psicodrammatista freudiano. Nel mio studio di Pollenza incontro bambini, adolescenti, adulti e famiglie, in percorsi individuali e in gruppi dove la parola trova la sua strada anche attraverso il gioco e la scena.",
"Il mio percorso nasce dalla clinica con i bambini, al Policlinico Umberto I di Roma, e approda alla psicoanalisi lacaniana e allo psicodramma freudiano, che ho approfondito a Macerata con il Centro Paul Lemoine e con l'ICLES. Da più di quindici anni esercito la libera professione a Pollenza e conduco gruppi di psicodramma analitico.",
"Il filo che tiene insieme il mio lavoro è la parola e lo spazio in cui può nascere: lo studio, il gruppo, la scena. Per questo porto lo psicodramma anche fuori dallo studio: nelle aziende, con lo sportello di ascolto psicologico per i dipendenti di Cosmari e i corsi per team e apprendisti di Confindustria Macerata e Confartigianato.",
"Presiedo l'ASD Macerata Boxing Club e nel mio lavoro integro psicologia e sport: l'allenamento, il gruppo e il confronto con il proprio limite sono spazi in cui la crescita di una persona diventa visibile.",
"Mi sono formato al <a href=\"test-sis.html\">test SIS (Somatic Inkblot Series)</a> con il Dr. B.L. Dubey, presidente della Somatic Inkblot Society. Dal 2018 sono il responsabile italiano, oggi direttore nazionale, della società e consulente editoriale del <i>Journal of Projective Psychology &amp; Mental Health</i>. In India ho portato lo psicodramma analitico, con interventi e workshop nei congressi di psicologia clinica, e il mio impegno è in costante crescita: a novembre 2026 sono ospite a Parigi della SEPT, la Société d'études du psychodrame pratique et théorique, proprio per raccontare questa esperienza. Ne parlo nella pagina <a href=\"internazionale.html\">Attività internazionale</a>.",
"Durante il Covid ho ideato e condotto «Restiamo in contatto», un programma online in diretta: due volte a settimana ospitavo uno psicologo o una psicologa e ci confrontavamo su temi di psicologia. È stato seguitissimo.",
"Se stai pensando di chiedere aiuto, per te o per un figlio, il primo passo è semplice: scrivimi o chiamami."]
chi_h=chi_h[:m.start()]+''.join(tag+t+'</p>\n' for t in NEW)+chi_h[e:]
cv=cv.replace("Ideatore e conduttore di «Restiamo in contatto», programma online in diretta: due volte a settimana ospitavo un collega psicologo o una collega psicologa per parlare di temi di psicologia. La diretta è stata seguitissima.","Ideatore e conduttore di «Restiamo in contatto», programma online in diretta: due volte a settimana ospitavo uno psicologo o una psicologa per parlare di temi di psicologia. Seguitissimo.")
cv=cv.replace('<div class="row"><div class="yr">2018 – oggi</div>','<div class="row"><div class="yr">Periodo Covid</div><div class="tx">Ideatore e conduttore di «Restiamo in contatto», programma online in diretta: due volte a settimana ospitavo un collega psicologo o una collega psicologa per parlare di temi di psicologia. La diretta è stata seguitissima.</div></div>\n<div class="row"><div class="yr">2018 – oggi</div>',1)
page('chi-sono.html',"Chi sono · Antonio Cervigni, psicologo e psicoterapeuta","Il percorso e la formazione del Dott. Antonio Cervigni: psicoanalisi lacaniana, psicodramma freudiano, clinica con bambini, adolescenti e adulti, formazione e attività internazionale.",chi_h+band)
# PSICODRAMMA
psi_h=psi.replace('<div style="font-size: 14px; letter-spacing: 5px; text-transform: uppercase; color: #9A4F20; font-weight: 500">Il mio metodo</div>','<div class="eyebrow">Il mio metodo</div>',1)
psi_h=psi_h.replace('<h2 class="h2">Lo psicodramma','<h1 class="h2">Lo psicodramma',1).replace("che cos'è</h2>","che cos'è</h1>",1)
psi_h=psi_h.replace('a persone in percorsi di cura delle dipendenze, ','')
psi_h=put(psi_h,[('<h3 class="h3">Come si svolge',I['scena']),('<h3 class="h3">Che cosa lo distingue',I['distingue']),('<h3 class="h3">A chi si rivolge',I['rivolge'])])
dove='''<div class="wrap">
<h2 class="h2">Dove lo pratico</h2>
<p class="p">Lo tengo da anni nel mio studio di Pollenza, per adolescenti e adulti. Lo uso anche nella supervisione e nella formazione degli attori all'Accademia Platafisica di Macerata, e nei corsi per team e apprendisti di aziende e associazioni di categoria, per lavorare su comunicazione e gestione dello stress. Ho portato lo psicodramma analitico anche a workshop di formazione per medici e psicologi in India.</p>
<h2 class="h2" style="margin-top:40px">Partecipare a un gruppo</h2>
<p class="p">Tengo sempre dei gruppi di psicodramma. Se vuoi partecipare, scrivimi o chiamami: ci incontriamo, ne parliamo e valutiamo insieme se il percorso fa per te; poi entri nel gruppo.</p>
<div class="btns"><a class="btn btn1" href="{WA}">Scrivimi su WhatsApp</a><a class="btn btn2" href="{SUBJ}">Scrivimi una email</a><a class="btn btn2" href="tel:{TEL}">Chiama</a><a class="btn btn2" href="internazionale.html">Attività internazionale</a></div>
</div>
'''
dove=dove.replace('{WA}',WA).replace('{SUBJ}',SUBJ).replace('{TEL}',TEL)
page('psicodramma.html',"Psicodramma freudiano · Antonio Cervigni","Che cos'è lo psicodramma freudiano (psicoanalitico), come si svolge una seduta e a chi si rivolge. Gruppi a Pollenza (Macerata) con il Dott. Antonio Cervigni.",psi_h+dove+band)
# INTERNAZIONALE
intl=intl.replace("Dal 2018 partecipo a congressi e workshop in India, dove porto lo psicodramma analitico, e in Italia faccio conoscere la Somatic Inkblot Series: queste sono le tappe, con qualche immagine.","Dal 2018 partecipo a congressi e workshop in India, dove ho portato lo psicodramma analitico e dove il mio impegno è in costante crescita. A novembre 2026 sono ospite a Parigi della SEPT, la Société d'études du psychodrame pratique et théorique, proprio per raccontare questa esperienza. In Italia faccio conoscere la Somatic Inkblot Series: queste sono le tappe, con qualche immagine.")
intl=intl.replace('<div class="row" style="border-color: #3D5C5F"><div class="yr" style="color: #E8B48F">Aprile 2026</div>','<div class="row" style="border-color: #3D5C5F"><div class="yr" style="color: #E8B48F">Novembre 2026</div><div class="tx"><b>Parigi (Francia).</b> Ospite della SEPT, la Société d\'études du psychodrame pratique et théorique, per parlare della mia esperienza di psicodramma in India.</div></div>\n<div class="row" style="border-color: #3D5C5F"><div class="yr" style="color: #E8B48F">Aprile 2026</div>',1)

NC='<a href="https://www.nicolecompagnoni.it" target="_blank" rel="noopener">Dott.ssa Nicole Compagnoni</a>'
intl=intl.replace("Dalle Marche all'India","Un lavoro che attraversa i confini",1)
intl=intl.replace("proprio per raccontare questa esperienza. In Italia","proprio per raccontare questa esperienza, insieme alla stimata collega "+NC+". In Italia",1)
intl=intl.replace("per parlare della mia esperienza di psicodramma in India.","per parlare della mia esperienza di psicodramma in India, insieme alla collega "+NC+".",1)
intl=intl.replace("Ho partecipato ai lavori con interventi dal podio e nel dibattito con i giovani psicologi.","Ho partecipato ai lavori con interventi dal podio e nel dibattito con i giovani psicologi, insieme alla collega "+NC+".",1)
intl=intl.replace("Nel programma sono indicato come","Con me c'era la collega "+NC+". Nel programma sono indicato come",1)
intl_h=intl_h.replace("Greater Noida, 2026","Greater Noida, aprile 2026").replace("Mathura, 2024","Mathura, novembre 2024")

import re as _re
intl=_re.sub(r'(<h1 class="h2">Un lavoro che attraversa i confini</h1>\s*)<p class="p">.*?</p>',lambda m:m.group(1)+'<p class="p">Lo psicodramma e le tecniche proiettive mi portano spesso lontano dallo studio, tra congressi, workshop e società scientifiche di Paesi diversi. Qui trovi le tappe di questo cammino, dalla più recente alla più antica, con qualche immagine: prenditi il tempo di scorrerle.</p>',intl,count=1,flags=_re.S)
page('internazionale.html',"Attività internazionale · Antonio Cervigni, SIS Society","Congressi e workshop in India, responsabile italiano della Somatic Inkblot Society: l'attività internazionale del Dott. Antonio Cervigni, con fotografie.",intl)
# CONTATTI
cont=f'''<div class="wrap" style="padding-top: 24px">
<h1 class="h2" style="font-size: 52px">Contatti</h1>
<p class="p">Per un primo colloquio scrivimi o chiamami: ti rispondo appena possibile. Se la richiesta riguarda un figlio, contattami tu come genitore e ne parliamo prima insieme.</p>
<div class="btns"><a class="btn btn1" href="tel:{TEL}">Chiama +39 351 866 6942</a><a class="btn btn2" href="{WA}">Scrivimi su WhatsApp</a><a class="btn btn2" href="{SUBJ}">Scrivimi una email</a><a class="btn btn2" href="#modulo">Compila il modulo</a></div>
<div class="grid" style="margin-top: 24px">
<div class="card"><h3>Studio</h3><p>Contrada Potenza 34, Fraz. Rotelli<br>Pollenza (MC)</p><p style="margin-top: 14px"><a class="btn btn2" href="{MAPS}" target="_blank" rel="noopener">Come raggiungermi</a></p></div>
<div class="card"><h3>Orari</h3><p>Dal lunedì al venerdì, su appuntamento.</p><p style="margin-top: 10px">Se hai bisogno di altri orari, anche il sabato mattina, scrivimi e troveremo insieme una soluzione.</p></div>
<div class="card"><h3>Recapiti</h3><p>Telefono: <a href="tel:{TEL}">+39 351 866 6942</a><br>Email: <a href="{SUBJ}">{MAIL}</a></p></div>
<div class="card"><h3>Online</h3><p><a href="{FB}">Facebook</a><br><a href="{IG}">Instagram</a><br><a href="{LI}">LinkedIn</a></p></div>
</div>
</div>
'''
page('grazie.html',"Messaggio inviato · Antonio Cervigni","Grazie per il tuo messaggio.",grazie_h.replace('{TEL}',TEL).replace('{WA}',WA),'<meta name="robots" content="noindex">')
page('come-lavoro.html',"Come lavoro · Antonio Cervigni, psicoterapeuta a orientamento psicoanalitico","Come lavoro: l'ascolto, il sintomo, la parola e il desiderio nella psicoanalisi, spiegati in modo semplice dal Dott. Antonio Cervigni.",come_h+band)
page('test-sis.html',"Il test SIS (Somatic Inkblot Series) · Dott. Antonio Cervigni","Che cos'è il test SIS, Somatic Inkblot Series, come si svolge e a che cosa serve. Antonio Cervigni è il responsabile italiano della Somatic Inkblot Society.",sis_h+band)
page('formazione.html',"Formazione e supervisione per psicologi · Dott. Antonio Cervigni","Gruppi di supervisione con lo psicodramma per psicologi in formazione, workshop sul test SIS e sullo psicodramma analitico.",for_h+band)
page('contatti.html',"Contatti · Antonio Cervigni, psicologo a Pollenza (Macerata)","Come prendere appuntamento con il Dott. Antonio Cervigni: telefono, email e indirizzo dello studio a Pollenza (Macerata).",cont+form_h+steps)
# PRIVACY (reuse text from previous privacy.html)
priv_body=open(SC+'privacy_body.html',encoding='utf-8').read()
page('privacy.html',"Informativa sulla privacy · Antonio Cervigni","Informativa sul trattamento dei dati personali del sito del Dott. Antonio Cervigni, psicologo e psicoterapeuta.",priv_body)
[os.remove(OUT+x) for x in ('invia.php','test.php') if os.path.exists(OUT+x)]

_pages=sorted(f for f in os.listdir(OUT) if f.endswith('.html') and f!='grazie.html')
_pr={'index.html':'1.0','test-sis.html':'0.8','formazione.html':'0.7','come-lavoro.html':'0.8','chi-sono.html':'0.8','contatti.html':'0.8','psicodramma.html':'0.8'}
open(OUT+'sitemap.xml','w',encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>https://www.antoniocervigni.it/%s</loc><lastmod>2026-11-12</lastmod><priority>%s</priority></url>\n'%('' if f=='index.html' else f,_pr.get(f,'0.6')) for f in _pages)+'</urlset>\n')
open(OUT+'robots.txt','w').write('User-agent: *\nAllow: /\nDisallow: /grazie.html\n\nSitemap: https://www.antoniocervigni.it/sitemap.xml\n')
print('built')

# SCRITTI
import html
lines=open(SC+'art1.txt',encoding='utf-8').read().split('\n')
body_lines=[l.strip() for l in lines[2:] if l.strip() and l.strip()!='AC']
txt=' '.join(body_lines)
txt=txt.replace('che è sarà la cifra','che è la cifra').replace('umana ,','umana,')
starts=['C\'è una poesia italiana','Lacan lo diceva','Felicita non è bella','In quella confessione','Ma c\'è un secondo movimento','Quello che rende questo poemetto','Gozzano usa l\'ironia','Gozzano e Lacan non si sono']
idx=[txt.index(s) for s in starts]+[len(txt)]
paras=[txt[idx[i]:idx[i+1]].strip() for i in range(len(starts))]
esc=html.escape
art=f'''<article class="wrap" style="padding-top: 24px; max-width: 800px">
<p class="eyebrow"><a href="scritti.html" style="color:inherit">Scritti e interventi</a></p>
<h1 class="h2" style="margin-top:12px">L'amore è il nome della distanza</h1>
<p class="p" style="font-style:italic;font-size:20px;margin-top:0">Quel che fingo d'essere e non sono</p>
<p style="font-size:14px;color:#4A5F61;margin:0 0 28px">Testo di Antonio Cervigni · Lettura di circa 6 minuti</p>
'''+''.join(f'<p class="p" style="font-size:19px;line-height:1.75;margin:0 0 22px">{esc(p,quote=False)}</p>' for p in paras)+'''
<p class="p" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:24px;margin-top:32px">Antonio Cervigni</p>
</article>
'''
page('amore-nome-della-distanza.html',"L'amore è il nome della distanza · Antonio Cervigni","Gozzano, La signorina Felicita e Lacan: desiderio, mancanza e distanza in un saggio breve di Antonio Cervigni.",art+band)
scr=f'''<div class="wrap" style="padding-top: 24px">
<p class="eyebrow">Riflessioni</p>
<h1 class="h2" style="margin-top:12px">Scritti e interventi</h1>
<p class="p">Articoli scritti da me, Antonio Cervigni: pagine in cui la psicoanalisi incontra la letteratura, il teatro e la vita di tutti i giorni.</p>
<div class="card" style="margin-top:28px"><h3>La notte dei bambini</h3><p style="margin:6px 0 10px">Sogni e incubi dei bambini: un messaggio da accogliere, non un nemico del sonno.</p><p style="margin-top:14px"><a class="btn btn2" href="notte-dei-bambini.html">Leggi lo scritto</a></p></div>
<div class="card" style="margin-top:20px"><h3>La notte in cui i bambini giocano con la morte</h3><p style="margin:6px 0 10px">Perché i bambini si travestono da scheletri e fantasmi, e che cosa chiedono agli adulti.</p><p style="margin-top:14px"><a class="btn btn2" href="notte-dei-morti.html">Leggi lo scritto</a></p></div>
<div class="card" style="margin-top:20px"><h3>Il capriccio, ovvero la scena in cui si chiede amore</h3><p style="margin:6px 0 10px">Il bambino che urla al supermercato non vuole l'oggetto: chiede la prova di essere desiderato.</p><p style="margin-top:14px"><a class="btn btn2" href="capriccio.html">Leggi lo scritto</a></p></div>
<div class="card" style="margin-top:20px"><h3>L'amore che manca a se stesso</h3><p style="margin:6px 0 10px">Il narcisismo letto con Lacan: non un eccesso d'amore per sé, ma una ferita mascherata da corazza.</p><p style="margin-top:14px"><a class="btn btn2" href="amore-che-manca.html">Leggi lo scritto</a></p></div>
<div class="card" style="margin-top:20px"><h3>Il perturbante: l'ospite che abita la casa</h3><p style="margin:6px 0 10px">Freud, Lacan e il brivido del familiare che ci guarda: l'angoscia nasce quando la mancanza viene a mancare.</p><p style="margin-top:14px"><a class="btn btn2" href="perturbante.html">Leggi lo scritto</a></p></div>
<div class="card" style="margin-top:20px"><h3>Sintomi moderni</h3><p style="font-style:italic;margin:6px 0 10px">L'ansia e gli attacchi di panico come linguaggio del nostro tempo</p><p>Il sintomo non è un guasto da riparare: è un messaggio cifrato che chiede di essere ascoltato.</p><p style="margin-top:14px"><a class="btn btn2" href="sintomi-moderni.html">Leggi lo scritto</a></p></div>
<div class="card" style="margin-top:20px"><h3>La parola che salva: quando i genitori si separano</h3><p style="margin:6px 0 10px">Françoise Dolto e la separazione dei genitori: a ferire il bambino non è la rottura, ma il non-detto.</p><p style="margin-top:14px"><a class="btn btn2" href="parola-che-salva.html">Leggi lo scritto</a></p></div>
<div class="card" style="margin-top:20px"><h3>L'amore è il nome della distanza</h3><p style="font-style:italic;margin:6px 0 10px">Quel che fingo d'essere e non sono</p><p>Gozzano, <i>La signorina Felicita</i> e Lacan: perché il desiderio vive di mancanza e l'amore nasce già nella forma del ricordo.</p><p style="margin-top:14px"><a class="btn btn2" href="amore-nome-della-distanza.html">Leggi lo scritto</a></p></div>
</div>
'''
a2=[l.strip() for l in open(SC+'art2.txt',encoding='utf-8').read().split('\n') if l.strip()]
art2=f'''<article class="wrap" style="padding-top: 24px; max-width: 800px">
<p class="eyebrow"><a href="scritti.html" style="color:inherit">Scritti e interventi</a></p>
<h1 class="h2" style="margin-top:12px">La parola che salva: quando i genitori si separano</h1>
<p style="font-size:14px;color:#4A5F61;margin:0 0 28px">Testo di Antonio Cervigni · Lettura di circa 3 minuti</p>
'''+''.join(f'<p class="p" style="font-size:19px;line-height:1.75;margin:0 0 22px">{html.escape(p,quote=False)}</p>' for p in a2)+'''
<p class="p" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:24px;margin-top:32px">Antonio Cervigni</p>
</article>'''
page('parola-che-salva.html',"La parola che salva: quando i genitori si separano · Antonio Cervigni","Françoise Dolto e la separazione dei genitori: perché a ferire il bambino non è la rottura, ma il non-detto.",art2+band)
a3=[l.strip() for l in open(SC+'art3.txt',encoding='utf-8').read().split('\n') if l.strip()]
art3=f'''<article class="wrap" style="padding-top: 24px; max-width: 800px">
<p class="eyebrow"><a href="scritti.html" style="color:inherit">Scritti e interventi</a></p>
<h1 class="h2" style="margin-top:12px">Sintomi moderni</h1>
<p class="p" style="font-style:italic;font-size:20px;margin-top:0">L'ansia e gli attacchi di panico come linguaggio del nostro tempo</p>
<p style="font-size:14px;color:#4A5F61;margin:0 0 28px">Testo di Antonio Cervigni · Lettura di circa 3 minuti</p>
'''+''.join(f'<p class="p" style="font-size:19px;line-height:1.75;margin:0 0 22px">{html.escape(p,quote=False)}</p>' for p in a3)+'''
<p class="p" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:24px;margin-top:32px">Antonio Cervigni</p>
</article>'''
page('sintomi-moderni.html',"Sintomi moderni · Antonio Cervigni","Ansia e attacchi di panico letti con la psicoanalisi lacaniana: il sintomo come messaggio cifrato e come domanda sul proprio desiderio.",art3+band)
a4=[l.strip() for l in open(SC+'art4.txt',encoding='utf-8').read().split('\n') if l.strip()]
art4=f'''<article class="wrap" style="padding-top: 24px; max-width: 800px">
<p class="eyebrow"><a href="scritti.html" style="color:inherit">Scritti e interventi</a></p>
<h1 class="h2" style="margin-top:12px">Il perturbante: l'ospite che abita la casa</h1>
<p style="font-size:14px;color:#4A5F61;margin:0 0 28px">Testo di Antonio Cervigni · Lettura di circa 3 minuti</p>
'''+''.join(f'<p class="p" style="font-size:19px;line-height:1.75;margin:0 0 22px">{html.escape(p,quote=False)}</p>' for p in a4)+'''
<p class="p" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:24px;margin-top:32px">Antonio Cervigni</p>
</article>'''
page('perturbante.html',"Il perturbante: l'ospite che abita la casa · Antonio Cervigni","Freud, Lacan e il perturbante: quando il familiare ci guarda e la mancanza viene a mancare.",art4+band)
a5=[l.strip() for l in open(SC+'art5.txt',encoding='utf-8').read().split('\n') if l.strip()]
art5=f'''<article class="wrap" style="padding-top: 24px; max-width: 800px">
<p class="eyebrow"><a href="scritti.html" style="color:inherit">Scritti e interventi</a></p>
<h1 class="h2" style="margin-top:12px">L'amore che manca a se stesso</h1>
<p style="font-size:14px;color:#4A5F61;margin:0 0 28px">Testo di Antonio Cervigni · Lettura di circa 3 minuti</p>
'''+''.join(f'<p class="p" style="font-size:19px;line-height:1.75;margin:0 0 22px">{html.escape(p,quote=False)}</p>' for p in a5)+'''
<p class="p" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:24px;margin-top:32px">Antonio Cervigni</p>
</article>'''
page('amore-che-manca.html',"L'amore che manca a se stesso · Antonio Cervigni","Il narcisismo letto con Lacan e Recalcati: non un eccesso d'amore per sé, ma la ferita di chi non sa fare il lutto della propria mancanza.",art5+band)
a6=[l.strip() for l in open(SC+'art6.txt',encoding='utf-8').read().split('\n') if l.strip()]
art6=f'''<article class="wrap" style="padding-top: 24px; max-width: 800px">
<p class="eyebrow"><a href="scritti.html" style="color:inherit">Scritti e interventi</a></p>
<h1 class="h2" style="margin-top:12px">Il capriccio, ovvero la scena in cui si chiede amore</h1>
<p style="font-size:14px;color:#4A5F61;margin:0 0 28px">Testo di Antonio Cervigni · Lettura di circa 3 minuti</p>
'''+''.join(f'<p class="p" style="font-size:19px;line-height:1.75;margin:0 0 22px">{html.escape(p,quote=False)}</p>' for p in a6)+'''
<p class="p" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:24px;margin-top:32px">Antonio Cervigni</p>
</article>'''
page('capriccio.html',"Il capriccio, ovvero la scena in cui si chiede amore · Antonio Cervigni","Il capriccio del bambino letto con Lacan e Dolto: una domanda d'amore, il valore del no e della parola che nomina.",art6+band)
a7=[l.strip() for l in open(SC+'art7.txt',encoding='utf-8').read().split('\n') if l.strip()]
art7=f'''<article class="wrap" style="padding-top: 24px; max-width: 800px">
<p class="eyebrow"><a href="scritti.html" style="color:inherit">Scritti e interventi</a></p>
<h1 class="h2" style="margin-top:12px">La notte in cui i bambini giocano con la morte</h1>
<p style="font-size:14px;color:#4A5F61;margin:0 0 28px">Testo di Antonio Cervigni · Lettura di circa 3 minuti</p>
'''+''.join(f'<p class="p" style="font-size:19px;line-height:1.75;margin:0 0 22px">{html.escape(p,quote=False)}</p>' for p in a7)+'''
<p class="p" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:24px;margin-top:32px">Antonio Cervigni</p>
</article>'''
page('notte-dei-morti.html',"La notte in cui i bambini giocano con la morte · Antonio Cervigni","Halloween letto con Dolto, Lacan e Mannoni: perché i bambini mettono in scena la morte e come gli adulti possono accoglierli con parole vere.",art7+band)
a8=[l.strip() for l in open(SC+'art8.txt',encoding='utf-8').read().split('\n') if l.strip()]
art8=f'''<article class="wrap" style="padding-top: 24px; max-width: 800px">
<p class="eyebrow"><a href="scritti.html" style="color:inherit">Scritti e interventi</a></p>
<h1 class="h2" style="margin-top:12px">La notte dei bambini</h1>
<p style="font-size:14px;color:#4A5F61;margin:0 0 28px">Testo di Antonio Cervigni · Lettura di circa 3 minuti</p>
'''+''.join(f'<p class="p" style="font-size:19px;line-height:1.75;margin:0 0 22px">{html.escape(p,quote=False)}</p>' for p in a8)+'''
<p class="p" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:24px;margin-top:32px">Antonio Cervigni</p>
</article>'''
page('notte-dei-bambini.html',"La notte dei bambini · Antonio Cervigni","Sogni e incubi dei bambini letti con Françoise Dolto: l'incubo come messaggio da ascoltare, non da zittire.",art8+band)

_NC='<a href="https://www.nicolecompagnoni.it" target="_blank" rel="noopener">Dott.ssa Nicole Compagnoni</a>'
def _P(t): return '<p class="p" style="font-size:19px;line-height:1.75;margin:0 0 22px">'+t+'</p>'
def _Q(t): return '<p class="pq">'+t+'</p>'
def _F(src,alt,cap): return '<figure><img src="img/%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>'%(src,alt,cap)
art9='<article class="wrap art" style="padding-top: 24px; max-width: 800px">\n<p class="eyebrow"><a href="scritti.html" style="color:inherit">Scritti e interventi</a></p>\n<h1 class="h2" style="margin-top:12px">India, ancora una volta: ponti, persone, orizzonti</h1>\n<p style="font-size:14px;color:#4A5F61;margin:0 0 28px">Testo di Antonio Cervigni · Lettura di circa 4 minuti</p>\n'+''.join([
_P("Ci sono luoghi nel mondo che senti già tuoi prima ancora di attraversarne la soglia. L'India, per me, è uno di questi. Ogni volta che vi ritorno, qualcosa si riaccende: un senso di appartenenza a un dialogo più ampio, che va ben oltre i confini del mio studio clinico e delle cornici teoriche entro cui lavoro quotidianamente."),
_P("Quest'anno sono tornato per partecipare al NACIACP, il congresso nazionale organizzato presso la Gautam Buddha University, insieme alla mia stimata collega "+_NC+", psicologa di grande valore con cui collaboro stabilmente da anni e che stimo profondamente, sia sul piano professionale che umano. Ad invitarci è stato, come sempre con generosa visione, il Professor B.L. Dubey, figura centrale nella diffusione del Somatic Inkblot System in Asia e nel mondo."),
_F('p2026-intervento.jpg','Antonio Cervigni al podio del congresso NACIACP, Gautam Buddha University, 2026','Gautam Buddha University, 2026'),
_Q("Ogni volta che rincontro il Professor Dubey è come riprendere un discorso lasciato in sospeso nel posto giusto: esattamente lì dove le idee stavano per fiorire."),
_P("È bello, ogni volta, ritrovarlo. C'è in lui una curiosità intellettuale che non conosce stanchezza, una disponibilità all'incontro che rende ogni conversazione densa di possibilità. Ed è proprio da questi incontri, informali quanto produttivi, che nascono proposte nuove, connessioni inaspettate, semi che poi germogliano nel lavoro clinico e nella ricerca."),
_P("Il cuore del mio contributo in questi anni, e anche in questa trasferta, è stato quello di integrare le mie radici psicoanalitiche con il Somatic Inkblot System, di cui sono Responsabile per l'Italia. Il SIS è uno strumento che lavora sull'esperienza somatica e proiettiva, e si presta in modo straordinario a un dialogo con la psicoanalisi: entrambi cercano ciò che è nascosto, ciò che il corpo porta e che la parola fatica a nominare."),
'<h2>Il workshop di psicodramma</h2>',
_P("Quest'anno ho avuto l'opportunità di condurre un workshop dimostrativo di psicodramma per i colleghi psicologi presenti al congresso. È stata un'esperienza che mi ha sorpreso, e commosso, per la qualità dell'attenzione che vi hanno portato."),
_P("Nel dialogo che ha preceduto e seguito la sessione, ho toccato con mano qualcosa che sapevo in astratto ma che vivere dal vivo ha avuto un peso diverso: la psicoanalisi in India è ancora oggi molto poco praticata. Pur avendo una storia che risale all'inizio del Novecento, con la figura pionieristica di Girindrasekhar Bose, che fondò l'Indian Psychoanalytical Society nel 1922 e intrattenne un famoso carteggio con Freud, il pensiero psicoanalitico non è mai davvero entrato nel tessuto diffuso della clinica psicologica indiana. Schiacciata tra la psichiatria biologica, le terapie brevi e un sistema sanitario sotto pressione, la psicoanalisi è rimasta appannaggio di pochi centri nelle grandi città. Fuori da questi contesti, rimane pressoché sconosciuta."),
_P("Per molti dei colleghi presenti al workshop, l'incontro con lo psicodramma è stato dunque doppiamente inedito: non solo come metodo in sé, ma come finestra aperta su una dimensione interpretativa, quella psicoanalitica, che non avevano mai incontrato nella propria formazione. Guardare il gioco scenico dello psicodramma, anche in una sola seduta dimostrativa, e poi ascoltare come quella stessa scena potesse essere letta in chiave simbolica, transferale, relazionale, ha prodotto in molti di loro una sorta di cortocircuito illuminante."),
_F('p2026-domande.jpg','Antonio Cervigni a confronto con i colleghi alla Gautam Buddha University, 2026','Il confronto con i colleghi, Gautam Buddha University, 2026'),
_Q("Vedere la sorpresa nei loro occhi mentre interpretavamo insieme il gioco psicodrammatico all'interno di una scena mi ha ricordato perché faccio questo lavoro: per aprire porte che non sapevamo di avere davanti."),
'<h2>Ponti, persone, orizzonti</h2>',
_P("Questo viaggio, come tutti quelli che l'hanno preceduto, non si esaurisce nel congresso. Si misura anche nei ponti intrecciati lungo il cammino: con ricercatori, clinici, accademici di università diverse che mi hanno rivolto inviti per interventi futuri, aprendo nuove possibilità di scambio e collaborazione scientifica. Ogni incontro ha aggiunto un filo a una rete che cresce anno dopo anno."),
_P("E Nicole, con la sua presenza precisa, generosa e intellettualmente vivace, è stata, come sempre, la compagna ideale di questo cammino. Collaborare con lei significa avere accanto qualcuno che non si limita a condividere un metodo, ma ne abita pienamente il senso. È raro, ed è prezioso."),
_P("Guardando avanti, sono particolarmente emozionato da ciò che si sta profilando all'orizzonte: si stanno aprendo porte concrete in Sri Lanka e in Thailandia, contesti nei quali porto avanti il mio lavoro sull'integrazione tra psicodramma, SIS e pensiero psicoanalitico. Paesi diversi, culture diverse, ma la stessa domanda di fondo che orienta da sempre il mio lavoro clinico: come si fa, davvero, l'incontro tra due esseri umani?"),
_Q("Non si tratta di esportare un metodo. Si tratta di creare ogni volta le condizioni perché qualcosa di autentico possa accadere: tra persone, tra culture, tra saperi."),
_P("L'India mi ha insegnato, ancora una volta, che la conoscenza non si possiede: si costruisce insieme, nel momento in cui ci si incontra. E io, di incontri, non ho ancora finito di fare."),
])+'<p class="p" style="font-family:\'Cormorant Garamond\',Georgia,serif;font-size:24px;margin-top:32px">Antonio Cervigni</p>\n</article>'
page('india-ponti-persone-orizzonti.html',"India, ancora una volta: ponti, persone, orizzonti · Antonio Cervigni","Il ritorno in India per il congresso NACIACP alla Gautam Buddha University: il workshop di psicodramma, l'incontro con il Professor Dubey e i nuovi orizzonti.",art9+band)
page('scritti.html',"Scritti e interventi · Antonio Cervigni","Articoli scritti da Antonio Cervigni: psicoanalisi, letteratura e vita quotidiana.",scr+band)

ARTS=[('india-ponti-persone-orizzonti.html','India, ancora una volta: ponti, persone, orizzonti','','Il ritorno in India per il congresso NACIACP: un workshop di psicodramma, l\'incontro con il Professor Dubey e le porte che si aprono verso nuovi Paesi.'),
('notte-dei-bambini.html','La notte dei bambini','','Sogni e incubi dei bambini: un messaggio da accogliere, non un nemico del sonno.'),
('notte-dei-morti.html','La notte in cui i bambini giocano con la morte','','Perché i bambini si travestono da scheletri e fantasmi, e che cosa chiedono agli adulti.'),
('capriccio.html','Il capriccio, ovvero la scena in cui si chiede amore','','Il bambino che urla al supermercato non vuole l\'oggetto: chiede la prova di essere desiderato.'),
('amore-che-manca.html','L\'amore che manca a se stesso','','Il narcisismo letto con Lacan: non un eccesso d\'amore per sé, ma una ferita mascherata da corazza.'),
('perturbante.html','Il perturbante: l\'ospite che abita la casa','','Freud, Lacan e il brivido del familiare che ci guarda: l\'angoscia nasce quando la mancanza viene a mancare.'),
('sintomi-moderni.html','Sintomi moderni','L\'ansia e gli attacchi di panico come linguaggio del nostro tempo','Il sintomo non è un guasto da riparare: è un messaggio cifrato che chiede di essere ascoltato.'),
('parola-che-salva.html','La parola che salva: quando i genitori si separano','','Françoise Dolto e la separazione dei genitori: a ferire il bambino non è la rottura, ma il non-detto.'),
('amore-nome-della-distanza.html','L\'amore è il nome della distanza','Quel che fingo d\'essere e non sono','Gozzano, <i>La signorina Felicita</i> e Lacan: perché il desiderio vive di mancanza e l\'amore nasce già nella forma del ricordo.')]
cards=''.join(f'<div class="card acard" style="margin-top:20px">{V[VMAP[h]]}<div><h3>{t}</h3>'+(f'<p style="font-style:italic;margin:6px 0 10px">{s}</p>' if s else '')+f'<p>{d}</p><p style="margin-top:14px"><a class="btn btn2" href="{h}">Leggi lo scritto</a></p></div></div>' for h,t,s,d in ARTS)
scr=f'''<div class="wrap" style="padding-top: 24px">
<p class="eyebrow">Riflessioni</p>
<h1 class="h2" style="margin-top:12px">Scritti e interventi</h1>
<p class="p">Articoli scritti da me, Antonio Cervigni: pagine in cui la psicoanalisi incontra la letteratura, il teatro e la vita di tutti i giorni.</p>
{cards}
</div>
'''
page('scritti.html',"Scritti e interventi · Antonio Cervigni","Articoli scritti da Antonio Cervigni: psicoanalisi, letteratura e vita quotidiana.",scr+band)
