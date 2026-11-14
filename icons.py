G='#1F3A3D'; A='#B8622B'; SAND='#E3D9C6'; SAGE='#C9D8D0'; APR='#EBC9AE'; CREAM='#F6F3EC'
def svg(inner,vb='0 0 64 64',w=60,h=60,cls='ico',stroke=G,sw=2.6):
    return ('<svg class="%s" viewBox="%s" width="%d" height="%d" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>')%(cls,vb,w,h,stroke,sw,inner)
def f(x):
    return x.replace('{G}',G).replace('{A}',A).replace('{S}',SAND).replace('{E}',SAGE).replace('{P}',APR).replace('{C}',CREAM)
I={}
I['colloqui']=svg(f('<path d="M8 12h30a4 4 0 0 1 4 4v14a4 4 0 0 1-4 4H22l-8 7v-7H8a4 4 0 0 1-4-4V16a4 4 0 0 1 4-4z" fill="{E}"/><path d="M46 24h10a4 4 0 0 1 4 4v14a4 4 0 0 1-4 4h-2v7l-8-7H34a4 4 0 0 1-4-4v-4" fill="{P}"/><circle cx="14" cy="23" r="1.7" fill="{A}" stroke="none"/><circle cx="23" cy="23" r="1.7" fill="{A}" stroke="none"/><circle cx="32" cy="23" r="1.7" fill="{A}" stroke="none"/>'))
I['psicoterapia']=svg(f('<circle cx="24" cy="26" r="16" fill="{E}" fill-opacity=".75"/><circle cx="40" cy="26" r="16" fill="{P}" fill-opacity=".75" stroke="{A}"/><circle cx="32" cy="41" r="16" fill="{S}" fill-opacity=".55"/><circle cx="32" cy="31" r="2.4" fill="{A}" stroke="none"/>'))
I['giovani']=svg(f('<circle cx="20" cy="14" r="6" fill="{E}"/><path d="M12 54V32a8 8 0 0 1 16 0v22z" fill="{E}"/><circle cx="46" cy="30" r="4.5" fill="{P}" stroke="{A}"/><path d="M40 54V43a6 6 0 0 1 12 0v11z" fill="{P}" stroke="{A}"/><path d="M28 40l6 1"/>'))
I['gruppi']=svg(f('<circle cx="32" cy="10" r="4.5" fill="{E}"/><circle cx="53" cy="26" r="4.5" fill="{E}"/><circle cx="45" cy="52" r="4.5" fill="{E}"/><circle cx="19" cy="52" r="4.5" fill="{E}"/><circle cx="11" cy="26" r="4.5" fill="{E}"/><circle cx="32" cy="32" r="6" stroke="{A}" fill="{P}"/>'))
I['psicodiagnosi']=svg(f('<rect x="11" y="6" width="42" height="52" rx="6" fill="{C}"/><path d="M32 22C26 15 17 19 19 27c-4 5 1 12 7 10 0 6 4 8 6 6 2 2 6 0 6-6 6 2 11-5 7-10 2-8-7-12-13-5z" fill="{G}" stroke="none"/><path d="M32 18v32" stroke="{A}" stroke-dasharray="2 4" stroke-width="1.8"/><circle cx="19" cy="50" r="1.8" fill="{A}" stroke="none"/><circle cx="45" cy="50" r="1.8" fill="{A}" stroke="none"/>'))
I['lavoro']=svg(f('<rect x="6" y="20" width="52" height="34" rx="5" fill="{S}"/><path d="M22 20v-5a4 4 0 0 1 4-4h12a4 4 0 0 1 4 4v5"/><path d="M6 34h52"/><rect x="28" y="30" width="8" height="8" rx="2" stroke="{A}" fill="{P}"/>'))
I['passo1']=svg(f('<rect x="18" y="6" width="28" height="52" rx="6" fill="{E}"/><path d="M28 12h8"/><circle cx="32" cy="50" r="2" fill="{A}" stroke="none"/><path d="M6 24c4 0 6-3 6-7M58 24c-4 0-6-3-6-7" stroke="{A}"/>'))
I['passo2']=svg(f('<path d="M12 56V30a8 8 0 0 1 8-8h8v34z" fill="{E}"/><path d="M12 44h24"/><path d="M40 56V36h12v20z" fill="{P}"/><path d="M40 44h12"/><circle cx="46" cy="26" r="4" stroke="{A}" fill="{P}"/><circle cx="20" cy="14" r="3.5" fill="{E}"/>'))
I['passo3']=svg(f('<path d="M32 58V30"/><path d="M32 30C32 20 20 20 14 12M32 30c0-10 12-10 18-18"/><path d="M8 18l6-6 2 8M44 20l6-8 8 2" stroke="{A}"/><circle cx="32" cy="58" r="2" fill="{A}" stroke="none"/>'))
I['scena']=svg(f('<path d="M6 10h52v6H6z" fill="{P}"/><path d="M10 16c0 18-2 30-4 40M54 16c0 18 2 30 4 40M22 16c-2 12-6 24-8 40M42 16c2 12 6 24 8 40"/><path d="M6 56h52"/><circle cx="32" cy="42" r="4" stroke="{A}" fill="{P}"/><path d="M26 56v-6a6 6 0 0 1 12 0v6z" stroke="{A}" fill="{P}"/>'))
I['distingue']=svg(f('<circle cx="24" cy="32" r="16" fill="{E}" fill-opacity=".8"/><circle cx="40" cy="32" r="16" stroke="{A}" fill="{P}" fill-opacity=".7"/><path d="M32 20v24" stroke-dasharray="2 4"/>'))
I['rivolge']=svg(f('<circle cx="32" cy="14" r="5" stroke="{A}" fill="{P}"/><path d="M22 36a10 10 0 0 1 20 0v6H22z" stroke="{A}" fill="{P}"/><circle cx="12" cy="24" r="4" fill="{E}"/><path d="M4 44v-6a8 8 0 0 1 12-6" fill="{E}"/><circle cx="52" cy="24" r="4" fill="{E}"/><path d="M60 44v-6a8 8 0 0 0-12-6" fill="{E}"/><path d="M8 54h48"/>'))

# ---- grandi scene (320x220) ----
def big(inner,stroke=G,w=320,h=220,cls='fig'): return svg(f(inner),'0 0 320 220',w,h,cls,stroke,2.4)
def chair(x,y):
    return f'<g><rect x="{x-9}" y="{y-30}" width="18" height="24" rx="4" fill="{{E}}"/><rect x="{x-13}" y="{y-8}" width="26" height="7" rx="3" fill="{{P}}"/><path d="M{x-10} {y-1}v12M{x+10} {y-1}v12"/></g>'
I['studio']=big('''<ellipse cx="160" cy="196" rx="146" ry="10" fill="{S}" stroke="none"/>
<rect x="18" y="24" width="86" height="168" rx="6" fill="{S}"/><path d="M18 72h86M18 118h86M18 160h86"/>
<rect x="28" y="40" width="9" height="32" fill="{E}"/><rect x="39" y="46" width="9" height="26" fill="{P}"/><rect x="50" y="38" width="10" height="34" fill="{A}" fill-opacity=".75"/><rect x="62" y="44" width="9" height="28" fill="{E}"/><rect x="73" y="50" width="11" height="22" fill="{P}"/>
<rect x="30" y="86" width="12" height="32" fill="{P}"/><rect x="44" y="92" width="9" height="26" fill="{E}"/><rect x="55" y="84" width="10" height="34" fill="{E}"/><path d="M70 118l10-30 8 4-10 28z" fill="{A}" fill-opacity=".75"/>
<rect x="30" y="128" width="10" height="32" fill="{E}"/><rect x="42" y="134" width="12" height="26" fill="{A}" fill-opacity=".75"/><rect x="56" y="130" width="9" height="30" fill="{P}"/>
<circle cx="86" cy="146" r="10" fill="{E}"/>
<rect x="150" y="26" width="64" height="48" rx="3" fill="{C}"/><circle cx="196" cy="42" r="6" fill="{P}" stroke="{A}"/><path d="M150 66l20-14 14 10 12-8 18 12" stroke="{A}"/>
<path d="M142 108a14 14 0 0 1 14-14h60a14 14 0 0 1 14 14v52H142z" fill="{E}"/>
<rect x="122" y="124" width="30" height="58" rx="12" fill="{E}"/><rect x="206" y="124" width="30" height="58" rx="12" fill="{E}"/>
<rect x="136" y="142" width="86" height="34" rx="12" fill="{P}"/>
<path d="M132 182v12M228 182v12"/>
<path d="M274 194V86"/><path d="M256 86h36l-8-30h-20z" fill="{P}"/><ellipse cx="274" cy="194" rx="16" ry="4" fill="{G}" stroke="none"/><path d="M262 104l-10 14M286 104l10 14" stroke="{A}" stroke-dasharray="2 5"/>''')
I['scena_grande']=big('''<ellipse cx="160" cy="168" rx="148" ry="38" fill="{S}" stroke="none"/>
<path d="M160 6L94 160h132z" fill="{A}" fill-opacity=".10" stroke="none"/>
'''+chair(48,150)+chair(92,188)+chair(228,188)+chair(272,150)+'''
<circle cx="160" cy="62" r="13" fill="{P}"/><path d="M142 150q0-62 18-62t18 62z" fill="{E}"/><path d="M144 112l-22-18M176 112l22-30"/>
<path d="M100 74a16 12 0 1 1 8 10l-8 6z" fill="{C}"/><circle cx="104" cy="72" r="1.5" fill="{A}" stroke="none"/><circle cx="110" cy="72" r="1.5" fill="{A}" stroke="none"/><circle cx="116" cy="72" r="1.5" fill="{A}" stroke="none"/>
<path d="M214 48a18 13 0 1 0-9 11l9 6z" fill="{C}" stroke="{A}"/>
<path d="M208 128q8-22 22-12" stroke="{A}" stroke-dasharray="2 5"/>''')
I['mondo']=big('''<circle cx="160" cy="112" r="82" fill="{E}"/>
<path d="M80 112h160M92 76q68 14 136 0M92 148q68-14 136 0"/><ellipse cx="160" cy="112" rx="36" ry="82"/><path d="M160 30v164"/>
<path d="M142 86Q176 20 208 112" stroke="{A}" stroke-dasharray="3 6"/>
<g fill="{A}" stroke="{G}"><path d="M142 98c-9-12-14-18-14-24a14 14 0 0 1 28 0c0 6-5 12-14 24z"/><path d="M208 128c-9-12-14-18-14-24a14 14 0 0 1 28 0c0 6-5 12-14 24z"/></g>
<circle cx="142" cy="74" r="4.5" fill="{C}" stroke="none"/><circle cx="208" cy="104" r="4.5" fill="{C}" stroke="none"/>
<path d="M240 40l8 4-8 4-3 8-3-8-8-4 8-4 3-8z" fill="{P}" stroke="{A}"/><circle cx="52" cy="60" r="3" fill="{A}" stroke="none"/><circle cx="278" cy="150" r="3" fill="{A}" stroke="none"/>''')
I['studio_luogo']=big('''<defs><clipPath id="cl"><rect width="320" height="220" rx="14"/></clipPath></defs><rect width="320" height="220" rx="14" fill="{C}" stroke="none"/>
<g clip-path="url(#cl)">
<circle cx="262" cy="52" r="22" fill="{P}" stroke="{A}"/>
<path d="M0 124Q70 86 140 112T320 100V220H0z" fill="{E}" stroke="none"/>
<path d="M0 154Q90 116 180 144T320 134V220H0z" fill="#B3C7BC" stroke="none"/>
<path d="M0 176Q110 140 200 168T320 158V220H0z" fill="{S}" stroke="none"/>
<path d="M0 124Q70 86 140 112T320 100M0 154Q90 116 180 144T320 134M0 176Q110 140 200 168T320 158"/>
<ellipse cx="46" cy="146" rx="7" ry="30" fill="{G}" stroke="none"/><ellipse cx="64" cy="152" rx="6" ry="24" fill="{G}" stroke="none"/><ellipse cx="288" cy="140" rx="7" ry="28" fill="{G}" stroke="none"/>
<path d="M156 186H178L204 222H128z" fill="{C}" stroke="none"/>
<ellipse cx="166" cy="186" rx="68" ry="7" fill="{G}" fill-opacity=".15" stroke="none"/>
<rect x="198" y="84" width="12" height="26" fill="{S}"/>
<rect x="118" y="116" width="96" height="70" fill="{C}"/>
<path d="M106 120L166 74L226 120z" fill="{A}"/>
<rect x="154" y="146" width="24" height="40" rx="3" fill="{P}"/><circle cx="173" cy="168" r="1.8" fill="{G}" stroke="none"/>
<rect x="128" y="132" width="18" height="18" fill="{P}"/><path d="M137 132v18M128 141h18"/>
<rect x="186" y="132" width="18" height="18" fill="{P}"/><path d="M195 132v18M186 141h18"/>
<g transform="translate(166 70) scale(.82) translate(-166 -66)"><path d="M166 66c-14-16-22-24-22-36a22 22 0 0 1 44 0c0 12-8 20-22 36z" fill="{A}"/><circle cx="166" cy="30" r="8" fill="{C}" stroke="none"/></g>
<path d="M60 52q5-7 10 0q5-7 10 0M96 34q4-6 8 0q4-6 8 0" /></g>
<rect width="320" height="220" rx="14" fill="none"/>''')
I['bolle']=big('''<path d="M34 30h130a12 12 0 0 1 12 12v50a12 12 0 0 1-12 12H84l-30 26v-26H34a12 12 0 0 1-12-12V42a12 12 0 0 1 12-12z" fill="{G}" fill-opacity=".0"/>
<path d="M170 96h110a12 12 0 0 1 12 12v44a12 12 0 0 1-12 12h-14v26l-30-26h-66a12 12 0 0 1-12-12v-44a12 12 0 0 1 12-12z" fill="#1F3A3D"/>
<circle cx="60" cy="68" r="5" fill="{A}" stroke="none"/><circle cx="92" cy="68" r="5" fill="{A}" stroke="none"/><circle cx="124" cy="68" r="5" fill="{A}" stroke="none"/>
<circle cx="204" cy="130" r="3.5" fill="#F6F3EC" stroke="none"/><circle cx="225" cy="130" r="3.5" fill="#F6F3EC" stroke="none"/><circle cx="246" cy="130" r="3.5" fill="#F6F3EC" stroke="none"/>''',stroke='#F6F3EC',cls='fig figl')

# ---- vignette per gli articoli (320x220, riquadro con sfondo) ----
def vig(inner,bg=SAND,stroke=G):
    return big('<defs><clipPath id="vc"><rect width="320" height="220" rx="14"/></clipPath></defs><rect width="320" height="220" rx="14" fill="%s" stroke="none"/><g clip-path="url(#vc)">'%bg+inner+'</g>',stroke=stroke,cls='vig')
V={}
V['distanza']=vig('''<path d="M0 170Q60 110 130 150Q160 172 170 220H0z" fill="{E}"/><path d="M150 220Q165 172 190 150Q260 100 320 140V220z" fill="{E}"/>
<circle cx="58" cy="98" r="8" fill="{P}"/><path d="M48 136q0-28 10-28t10 28z" fill="{C}"/>
<circle cx="260" cy="87" r="8" fill="{P}"/><path d="M250 125q0-28 10-28t10 28z" fill="{C}"/>
<path d="M68 90Q160 14 252 80" stroke="{A}" stroke-dasharray="3 7"/>
<path d="M160 54c-8-9-12-13-12-18a7 7 0 0 1 12-3 7 7 0 0 1 12 3c0 5-4 9-12 18z" fill="{A}" stroke="{G}"/>
<path d="M104 40q5-7 10 0q5-7 10 0M206 30q5-7 10 0q5-7 10 0"/><circle cx="270" cy="34" r="12" fill="{P}" stroke="{A}"/>''')
V['sintomi']=vig('''<path d="M150 158C98 122 98 72 128 72c12 0 20 8 22 16 2-8 10-16 22-16 30 0 30 50-22 86z" fill="{P}"/>
<path d="M30 118H108l10-26 14 52 12-34 8 8H290" stroke="{A}" stroke-width="3"/>
<rect x="206" y="22" width="76" height="54" rx="16" fill="{C}"/><path d="M222 76l-8 18 22-18" fill="{C}"/>
<path d="M238 40a8 8 0 1 1 11 7q-6 3-6 8" stroke="{A}"/><circle cx="243" cy="63" r="1.8" fill="{A}" stroke="none"/>
<path d="M44 52l10 6M40 70l12 2M56 36l6 10" stroke="{A}"/>''')
V['separazione']=vig('''<ellipse cx="160" cy="186" rx="140" ry="10" fill="{E}" stroke="none"/>
<circle cx="50" cy="104" r="11" fill="{E}"/><path d="M36 182q0-44 14-44t14 44z" fill="{E}"/>
<circle cx="270" cy="104" r="11" fill="{E}"/><path d="M256 182q0-44 14-44t14 44z" fill="{E}"/>
<circle cx="160" cy="138" r="8" fill="{P}" stroke="{A}"/><path d="M150 182q0-26 10-26t10 26z" fill="{P}" stroke="{A}"/>
<path d="M64 152Q108 168 150 164M256 152Q212 168 170 164" stroke="{A}" stroke-dasharray="3 6"/>
<ellipse cx="96" cy="84" rx="20" ry="13" fill="{C}"/><circle cx="88" cy="84" r="1.6" fill="{A}" stroke="none"/><circle cx="96" cy="84" r="1.6" fill="{A}" stroke="none"/><circle cx="104" cy="84" r="1.6" fill="{A}" stroke="none"/>
<ellipse cx="224" cy="84" rx="20" ry="13" fill="{C}"/><circle cx="216" cy="84" r="1.6" fill="{A}" stroke="none"/><circle cx="224" cy="84" r="1.6" fill="{A}" stroke="none"/><circle cx="232" cy="84" r="1.6" fill="{A}" stroke="none"/>
<path d="M160 118c-6-6-9-9-9-13a5 5 0 0 1 9-2 5 5 0 0 1 9 2c0 4-3 7-9 13z" fill="{A}" stroke="none"/>''')
V['perturbante']=vig('''<rect x="14" y="190" width="292" height="3" fill="{G}" stroke="none"/>
<path d="M200 48h52v142h-52z" fill="{G}"/><path d="M200 48L172 58v128l28 4z" fill="{E}"/><circle cx="188" cy="124" r="2.5" fill="{A}" stroke="none"/>
<circle cx="226" cy="92" r="10" fill="{E}" fill-opacity=".45" stroke="none"/><path d="M210 190q0-60 16-60t16 60z" fill="{E}" fill-opacity=".45" stroke="none"/>
<path d="M200 190h52l50 22H172z" fill="{P}" fill-opacity=".55" stroke="none"/>
<path d="M52 122a12 12 0 0 1 12-12h50a12 12 0 0 1 12 12v52H52z" fill="{E}"/><rect x="38" y="138" width="24" height="40" rx="10" fill="{E}"/><rect x="116" y="138" width="24" height="40" rx="10" fill="{E}"/><rect x="50" y="154" width="80" height="24" rx="10" fill="{P}"/><path d="M46 178v12M132 178v12"/>
<path d="M30 40h36l-6-22H36z" fill="{P}" transform="translate(-4 0)"/><path d="M44 40V104" transform="translate(-4 0)"/>''')
V['narcisismo']=vig('''<ellipse cx="160" cy="104" rx="70" ry="92" fill="{P}"/><ellipse cx="160" cy="104" rx="58" ry="80" fill="{C}"/>
<circle cx="160" cy="84" r="17" stroke="{A}" stroke-dasharray="3 6"/><path d="M122 160q0-38 38-38t38 38" stroke="{A}" stroke-dasharray="3 6"/>
<path d="M160 26l-8 28 14 18-10 24" stroke="{G}"/>
<path d="M120 196l-14 14M200 196l14 14"/><path d="M52 40l4 10 10 4-10 4-4 10-4-10-10-4 10-4z" fill="{A}" stroke="none"/><path d="M270 150l3 7 7 3-7 3-3 7-3-7-7-3 7-3z" fill="{A}" stroke="none"/>''')
V['capriccio']=vig('''<rect x="14" y="178" width="292" height="3" fill="{G}" stroke="none"/>
<circle cx="122" cy="124" r="15" fill="{P}"/><ellipse cx="122" cy="128" rx="4" ry="5" fill="{G}" stroke="none"/><path d="M104 176q0-34 18-34t18 34z" fill="{E}"/><path d="M110 148L84 112M134 148l24-38"/>
<path d="M106 136q-4 8-2 12M138 136q4 8 2 12" stroke="{A}"/>
<rect x="78" y="20" width="88" height="52" rx="16" fill="{C}"/><path d="M110 72l6 16 8-16" fill="{C}"/>
<path d="M122 58c-12-10-18-15-18-22a9 9 0 0 1 18-4 9 9 0 0 1 18 4c0 7-6 12-18 22z" fill="{A}" stroke="none"/>
<circle cx="242" cy="78" r="14" fill="{P}"/><path d="M220 178q0-62 22-62t22 62z" fill="{E}"/><path d="M226 134Q196 148 170 158" stroke="{G}"/>
<ellipse cx="276" cy="48" rx="20" ry="13" fill="{C}"/><circle cx="268" cy="48" r="1.6" fill="{A}" stroke="none"/><circle cx="276" cy="48" r="1.6" fill="{A}" stroke="none"/><circle cx="284" cy="48" r="1.6" fill="{A}" stroke="none"/>
<circle cx="52" cy="164" r="13" fill="{P}" stroke="{A}"/>''')
V['morti']=vig('''<path d="M0 176Q80 150 160 170T320 168V220H0z" fill="#2B4F52" stroke="none"/>
<circle cx="268" cy="46" r="22" fill="{C}" stroke="none"/><circle cx="278" cy="40" r="19" fill="{G}" stroke="none"/>
<path d="M40 40l3 8 8 3-8 3-3 8-3-8-8-3 8-3zM96 24l2 5 5 2-5 2-2 5-2-5-5-2 5-2zM214 28l2 5 5 2-5 2-2 5-2-5-5-2 5-2z" fill="{A}" stroke="none"/>
<path d="M130 190V104a30 30 0 0 1 60 0v86q-7-10-15 0-7-10-15 0-7-10-15 0-7-10-15 0z" fill="{C}"/>
<ellipse cx="148" cy="106" rx="4" ry="6" fill="{G}" stroke="none"/><ellipse cx="172" cy="106" rx="4" ry="6" fill="{G}" stroke="none"/><ellipse cx="160" cy="124" rx="4" ry="5" fill="{G}" stroke="none"/>
<path d="M190 132L214 146" stroke="{C}"/><circle cx="218" cy="158" r="20" fill="{P}" fill-opacity=".35" stroke="none"/><rect x="211" y="150" width="14" height="18" rx="2" fill="{P}" stroke="{C}"/><path d="M213 150q5-8 10 0" stroke="{C}"/>
<ellipse cx="82" cy="176" rx="24" ry="19" fill="{A}" stroke="{C}"/><path d="M82 157q0-8 6-10" stroke="{C}"/>''',bg=G,stroke=CREAM)
V['notte_bambini']=vig('''<rect x="206" y="24" width="82" height="100" rx="41" fill="{G}"/><circle cx="256" cy="62" r="13" fill="{C}" stroke="none"/><circle cx="262" cy="58" r="11" fill="{G}" stroke="none"/><path d="M226 90l2 5 5 2-5 2-2 5-2-5-5-2 5-2z" fill="{A}" stroke="none"/>
<rect x="30" y="152" width="190" height="30" rx="6" fill="{E}"/><path d="M34 182v14M216 182v14"/>
<path d="M62 152q0-26 30-26h128v26z" fill="{P}"/><ellipse cx="78" cy="140" rx="24" ry="10" fill="{C}"/><circle cx="88" cy="132" r="12" fill="{P}" stroke="{A}"/><path d="M82 134q4 3 8 0" stroke="{A}" stroke-width="1.8"/>
<circle cx="96" cy="114" r="3" fill="{C}"/><circle cx="104" cy="102" r="5" fill="{C}"/>
<ellipse cx="134" cy="62" rx="52" ry="30" fill="{C}"/><ellipse cx="108" cy="54" rx="22" ry="16" fill="{C}" stroke="none"/><ellipse cx="160" cy="52" rx="24" ry="18" fill="{C}" stroke="none"/>
<path d="M118 84c-4-8 0-22 16-22s20 14 16 22z" fill="{E}"/><circle cx="127" cy="72" r="2" fill="{G}" stroke="none"/><circle cx="141" cy="72" r="2" fill="{G}" stroke="none"/><path d="M129 78q5 4 10 0" stroke-width="1.8"/>''')

# --- Contatti: nuova illustrazione dello studio (interno) e icone ---
I['studio_luogo']=big('''<defs><clipPath id="cl"><rect width="320" height="220" rx="14"/></clipPath></defs><rect width="320" height="220" rx="14" fill="{C}" stroke="none"/>
<g clip-path="url(#cl)">
<rect x="0" y="158" width="320" height="62" fill="{S}" stroke="none"/><path d="M0 158H320"/>
<ellipse cx="165" cy="190" rx="118" ry="13" fill="{P}" fill-opacity=".6" stroke="none"/>
<defs><clipPath id="wc"><rect x="26" y="20" width="92" height="76" rx="4"/></clipPath></defs>
<rect x="26" y="20" width="92" height="76" rx="4" fill="#DCE9E4"/>
<g clip-path="url(#wc)"><circle cx="96" cy="42" r="12" fill="{P}" stroke="{A}"/>
<path d="M20 80Q50 56 78 74T130 70V100H20z" fill="{E}"/>
<path d="M20 92Q56 74 92 88T130 84V100H20z" fill="#B3C7BC"/></g>
<rect x="26" y="20" width="92" height="76" rx="4"/><path d="M72 20v76M26 58h92" stroke-width="2"/>
<rect x="20" y="96" width="104" height="8" rx="2" fill="{S}"/>
<rect x="142" y="38" width="46" height="36" rx="3" fill="{P}"/>
<path d="M165 66V52M156 50q0 8 9 8t9-8" stroke="{A}" stroke-width="2.4"/><circle cx="165" cy="47" r="2" fill="{A}" stroke="none"/>
<path d="M286 96v64"/><path d="M272 96l6-24h16l6 24z" fill="{P}"/><path d="M278 160h16"/>
<path d="M63 104a8 8 0 0 1 8-8h34a8 8 0 0 1 8 8v36H63z" fill="{E}"/>
<rect x="55" y="132" width="66" height="22" rx="8" fill="#B3C7BC"/>
<path d="M62 154v10M114 154v10"/>
<path d="M211 104a8 8 0 0 1 8-8h34a8 8 0 0 1 8 8v36H211z" fill="{P}" stroke="{A}"/>
<rect x="203" y="132" width="66" height="22" rx="8" fill="{S}" stroke="{A}"/>
<path d="M210 154v10M262 154v10" stroke="{A}"/>
<ellipse cx="165" cy="142" rx="17" ry="4.5" fill="{S}"/><path d="M165 146v18M155 165h20"/>
<path d="M158 138l2-12h10l2 12z" fill="{A}"/>
<path d="M165 126c-8-3-9-12-4-15 1 6 3 8 4 15zM165 126c8-3 9-12 4-15-1 6-3 8-4 15z" fill="{E}"/>
</g>
<rect width="320" height="220" rx="14" fill="none"/>''')
def ci(inner,c=G,w=22):
    return svg(inner,'0 0 24 24',w,w,'ci',c,1.8)
CI={
'pin':'<path d="M12 21s-6.5-6-6.5-11a6.5 6.5 0 0 1 13 0c0 5-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/>',
'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
'phone':'<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
'mail':'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
'wa':'<path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3z"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5l1-1.5-2-1-1 .8a4 4 0 0 1-2-2l.8-1-1-2z"/>',
'globe':'<circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3 12h18"/>',
'fb':'<path d="M13.5 21v-8h2.6l.4-3h-3V8.2c0-.9.3-1.4 1.5-1.4H16.6V4.1A18 18 0 0 0 14.4 4C12 4 10.5 5.400 10.5 8v2H8v3h2.5v8z"/>',
'ig':'<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.2" cy="6.8" r=".9" fill="currentColor"/>',
'in':'<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10.500V16M8 7.500v.1M12 16v-5.500M12 12.500c0-1.500 1-2.500 2.500-2.500s2.500 1 2.500 2.500V16"/>',
'group':'<circle cx="8" cy="9" r="3"/><circle cx="17" cy="10" r="2.500"/><path d="M2.500 19c.5-3.500 3-5 5.500-5s5 1.500 5.500 5M14.500 14.500c2.500-.5 5 .5 6 4"/>',
}

I['passo1']=svg(f('<rect x="5" y="16" width="22" height="42" rx="5" fill="{E}"/><path d="M12 22h8"/><circle cx="16" cy="51" r="1.8" fill="{A}" stroke="none"/><path d="M33 6h22a4 4 0 0 1 4 4v14a4 4 0 0 1-4 4H46l-7 7v-7h-6a4 4 0 0 1-4-4V10a4 4 0 0 1 4-4z" fill="{P}" stroke="{A}"/><circle cx="39" cy="17" r="1.8" fill="{A}" stroke="none"/><circle cx="45" cy="17" r="1.8" fill="{A}" stroke="none"/><circle cx="51" cy="17" r="1.8" fill="{A}" stroke="none"/><path d="M31 44c3.500 0 6 2.500 6 6M31 52c1.500 0 3 1 3 3" stroke="{A}" stroke-width="2"/>'))
I['passo3']=svg(f('<circle cx="16" cy="14" r="6.500" fill="{E}"/><path d="M5 56V36a11 11 0 0 1 22 0v20z" fill="{E}"/><circle cx="48" cy="14" r="6.500" fill="{P}" stroke="{A}"/><path d="M37 56V36a11 11 0 0 1 22 0v20z" fill="{P}" stroke="{A}"/><circle cx="32" cy="40" r="10" fill="{C}"/><path d="M26.500 40l4 4 7.500-8.500" stroke="{A}" stroke-width="3.200"/>'))

# --- Come lavoro: sei vignette ---
def _vg(i,inner,bg):
    return vig(inner,bg).replace('id="vc"','id="vw%d"'%i).replace('url(#vc)','url(#vw%d)'%i)
def per(x,y,head,body,s=1.0,extra=''):
    r=9*s; w=13*s; h=38*s; t=y+r+3*s
    return '<circle cx="%g" cy="%g" r="%g" fill="%s"%s/><path d="M%g %gq0-%g %g-%gt%g %gz" fill="%s"%s/>'%(x,y,r,head,extra,x-w,t+h,h,w,h,w,h,body,extra)
W={}
# 1. Una persona, non un caso
W['persona']=_vg(1,'''<ellipse cx="160" cy="176" rx="150" ry="12" fill="{C}" fill-opacity=".7" stroke="none"/>
<g stroke-opacity=".45">'''+per(32,104,'{C}','{C}')+per(80,104,'{C}','{C}')+per(240,104,'{C}','{C}')+per(288,104,'{C}','{C}')+'''</g>
<circle cx="160" cy="112" r="54" fill="{P}" fill-opacity=".55" stroke="{A}" stroke-dasharray="3 7"/>
'''+per(160,84,'{P}','{E}',1.35)+'''
<path d="M160 142c-6-6.500-9-9.500-9-13a5 5 0 0 1 9-2.500 5 5 0 0 1 9 2.500c0 3.500-3 6.500-9 13z" fill="{A}" stroke="none"/>
<path d="M236 34l5 2.500-5 2.500-2 5.500-2-5.500-5-2.500 5-2.500 2-5.500z" fill="{C}" stroke="{A}" stroke-width="1.800"/>
<circle cx="74" cy="44" r="3" fill="{A}" stroke="none"/><circle cx="262" cy="66" r="2.500" fill="{A}" stroke="none"/>''','#E3D9C6')
# 2. Il sintomo ha qualcosa da dire
W['sintomo']=_vg(2,'''<rect x="0" y="176" width="320" height="44" fill="{S}" stroke="none"/><path d="M0 176H320"/>
<rect x="52" y="86" width="216" height="62" rx="16" fill="#B3C7BC"/>
<rect x="44" y="122" width="232" height="38" rx="12" fill="{C}"/>
<rect x="36" y="110" width="26" height="52" rx="10" fill="#B3C7BC"/><rect x="258" y="110" width="26" height="52" rx="10" fill="#B3C7BC"/>
<path d="M62 162v12M258 162v12"/>
<circle cx="120" cy="72" r="11" fill="{P}"/><path d="M103 126q0-40 17-40t17 40z" fill="{C}"/>
<g stroke="{A}" stroke-dasharray="4 5"><circle cx="196" cy="72" r="11" fill="{P}" fill-opacity=".35"/><path d="M179 126q0-40 17-40t17 40z" fill="{P}" fill-opacity=".35"/></g>
<path d="M214 18h62a10 10 0 0 1 10 10v24a10 10 0 0 1-10 10H236l-16 12 3-12h-9a10 10 0 0 1-10-10V28a10 10 0 0 1 10-10z" fill="{C}" stroke="{A}"/>
<circle cx="230" cy="40" r="2.600" fill="{A}" stroke="none"/><circle cx="245" cy="40" r="2.600" fill="{A}" stroke="none"/><circle cx="260" cy="40" r="2.600" fill="{A}" stroke="none"/>
''','#DCE7E0')
# 3. La parola che cura
W['parola']=_vg(3,'''<ellipse cx="160" cy="196" rx="150" ry="11" fill="{C}" fill-opacity=".7" stroke="none"/>
<rect x="134" y="50" width="150" height="86" rx="18" fill="{E}" stroke="{A}" stroke-dasharray="4 5"/>
<path d="M118 34h132a18 18 0 0 1 18 18v50a18 18 0 0 1-18 18H132l-30 24 8-24a18 18 0 0 1-10-16V52a18 18 0 0 1 18-18z" fill="{C}"/>
<path d="M126 62h116M126 78h92M126 94h60" stroke-opacity=".55"/>
<path d="M226 128q7-7 14 0t14 0t14 0" stroke="{A}"/>
'''+per(62,128,'{E}','{C}',1.15)+per(286,146,'{P}','{C}',.95)+'''
<path d="M300 132q8 4 6 14" stroke="{A}" stroke-width="2"/><path d="M306 126q12 6 9 22" stroke="{A}" stroke-width="2"/>''','#F1DFCB')
# 4. Il desiderio
W['desiderio']=_vg(4,'''<path d="M0 170Q80 120 160 160T320 150V220H0z" fill="{E}"/>
<path d="M0 198Q100 164 200 192T320 186V220H0z" fill="#B3C7BC"/>
<circle cx="234" cy="70" r="24" fill="{C}" fill-opacity=".8" stroke="none"/>
<circle cx="234" cy="70" r="32" stroke="{A}" stroke-width="5" stroke-dasharray="168 33" transform="rotate(150 234 70)"/>
<path d="M190 104l4 2-4 2-1.500 4.500-1.500-4.500-4-2 4-2 1.500-4.500z" fill="{A}" stroke="none"/>
'''+per(96,92,'{P}','{C}')+'''
<path d="M106 112l20-14" /><path d="M130 94Q160 74 196 78" stroke="{A}" stroke-dasharray="3 7"/>
<path d="M40 50q5-7 10 0q5-7 10 0M68 30q4-6 8 0q4-6 8 0"/>''','#E3D9C6')
# 5. Nessuna ricetta
W['strada']=_vg(5,'''<path d="M0 120Q70 84 150 108T320 96V220H0z" fill="{E}" stroke="none"/>
<circle cx="52" cy="46" r="18" fill="{P}" stroke="{A}"/>
<path d="M40 232C70 170 190 190 170 140S90 100 150 70S250 62 264 34" stroke="{C}" stroke-width="24"/>
<path d="M40 232C70 170 190 190 170 140S90 100 150 70S250 62 264 34" stroke="{A}" stroke-width="2" stroke-dasharray="2 9"/>
<path d="M264 36V12" /><path d="M264 12l18 6-18 6z" fill="{A}"/>
'''+per(118,142,'{P}','{C}',.8)+per(144,136,'{E}','#B3C7BC',.8)+'''
<path d="M236 150q5-7 10 0q5-7 10 0"/><path d="M262 172v-16M262 156c-8-2-10-10-6-14 4 2 6 8 6 14zM262 160c8-2 10-10 6-14-4 2-6 8-6 14z" fill="{E}"/>''','#E4ECE7')
# 6. In studio
W['studio']=_vg(6,'''<rect x="0" y="172" width="320" height="48" fill="{C}" fill-opacity=".6" stroke="none"/>
<path d="M214 0h72l34 172H180z" fill="{C}" fill-opacity=".55" stroke="none"/>
<ellipse cx="250" cy="172" rx="70" ry="13" fill="{C}" stroke="none"/>
'''+chair(206,160)+chair(234,146)+chair(266,146)+chair(294,160)+'''
<g transform="rotate(-7 86 110)"><rect x="34" y="42" width="106" height="132" rx="5" fill="{C}"/>
<rect x="62" y="104" width="44" height="34" stroke="{A}" fill="{P}"/><path d="M56 106l28-24 28 24" stroke="{A}"/><rect x="78" y="118" width="12" height="20" stroke="{A}" fill="{C}"/>
<circle cx="116" cy="68" r="9" stroke="{A}" fill="{P}"/><path d="M116 52v-5M128 56l4-4M132 68h5M104 56l-4-4" stroke="{A}" stroke-width="2"/>
<path d="M44 152q8-7 16 0t16 0t16 0t16 0t16 0"/></g>
<g transform="rotate(24 150 186)"><rect x="118" y="181" width="54" height="10" rx="3" fill="{A}"/><path d="M172 181l10 5-10 5z" fill="{C}"/></g>
<g transform="rotate(-14 60 196)"><rect x="34" y="191" width="50" height="10" rx="3" fill="#B3C7BC"/><path d="M84 191l10 5-10 5z" fill="{C}"/></g>''','#E3D9C6')

V['india']=vig('''<rect x="0" y="172" width="320" height="48" fill="{E}" stroke="none"/>
<path d="M0 186q20-6 40 0t40 0t40 0t40 0t40 0t40 0t40 0t40 0" stroke="{C}" stroke-opacity=".8"/>
<circle cx="250" cy="48" r="18" fill="{P}" stroke="{A}"/>
<path d="M0 150Q40 128 84 150V220H0z" fill="#B3C7BC"/><path d="M236 150Q280 128 320 150V220H236z" fill="#B3C7BC"/>
<path d="M28 138v-18l12-9 12 9v18z" fill="{C}"/><path d="M36 138v-9h8v9"/>
<path d="M268 136v-12q0-12 12-20q12 8 12 20v12z" fill="{P}" stroke="{A}"/><path d="M280 104v-8" stroke="{A}"/><path d="M262 136h36" stroke="{A}"/>
<path d="M72 150Q160 92 248 150" stroke="{C}" stroke-width="11"/><path d="M72 145Q160 87 248 145M72 155Q160 97 248 155"/>
<path d="M104 136v36M132 124v48M160 121v51M188 124v48M216 136v36" stroke-width="2"/>
'''+per(146,82,'{P}','{C}',.7)+per(172,82,'{E}','{C}',.7)+'''
<path d="M52 104Q160 20 270 92" stroke="{A}" stroke-dasharray="3 7"/>
<path d="M96 52q5-7 10 0q5-7 10 0M190 40q4-6 8 0q4-6 8 0"/>''')

# --- Pagine "Il test SIS" e "Formazione e supervisione" ---
_HB='M0-30C14-34 22-20 16-10C30-8 34 8 22 14C30 26 16 36 6 28C4 34 2 36 0 36Z'
def blot(cx,cy,s,fill='{G}',op=1):
    return '<g fill="%s" fill-opacity="%s" stroke="none"><path transform="translate(%g %g) scale(%g)" d="%s"/><path transform="translate(%g %g) scale(-%g %g)" d="%s"/></g>'%(fill,op,cx,cy,s,_HB,cx,cy,s,s,_HB)
def seat(x,y,head,body,s=1.0):
    return per(x,y,head,body,s)
W['sis_tavola']=_vg(11,'''<ellipse cx="160" cy="186" rx="130" ry="11" fill="{C}" fill-opacity=".7" stroke="none"/>
<g transform="rotate(-5 160 104)"><rect x="76" y="40" width="168" height="124" rx="10" fill="#D5CAB4" stroke="none" transform="translate(6 7)"/>
<rect x="76" y="40" width="168" height="124" rx="10" fill="{C}"/>
'''+blot(160,100,1.35)+'''<path d="M160 52v100" stroke="{A}" stroke-dasharray="2 6" stroke-width="1.800"/>
<circle cx="92" cy="150" r="2.500" fill="{A}" stroke="none"/><circle cx="228" cy="150" r="2.500" fill="{A}" stroke="none"/></g>
<path d="M268 44l5 2.500-5 2.500-2 5.500-2-5.500-5-2.500 5-2.500 2-5.500z" fill="{C}" stroke="{A}" stroke-width="1.800"/><circle cx="50" cy="56" r="3" fill="{A}" stroke="none"/>''','#E3D9C6')
W['sis_corpo']=_vg(12,'''<ellipse cx="160" cy="196" rx="120" ry="10" fill="{C}" fill-opacity=".7" stroke="none"/>
<circle cx="160" cy="54" r="18" fill="{P}"/><path d="M130 190q0-110 30-110t30 110z" fill="{C}"/>
<path d="M160 136c-10-11-15-16-15-22a8 8 0 0 1 15-4 8 8 0 0 1 15 4c0 6-5 11-15 22z" fill="{A}" stroke="none"/>
'''+blot(62,78,.62,'{G}',.85)+blot(258,70,.56,'{A}',.8)+blot(70,150,.5,'{A}',.8)+blot(254,150,.6,'{G}',.85)+'''
<path d="M84 86Q116 100 142 112M236 78Q204 96 178 112M90 146Q118 136 142 126M232 146Q204 136 178 126" stroke="{A}" stroke-dasharray="3 6" stroke-width="1.800"/>''','#DCE7E0')
W['sis_svolge']=_vg(13,'''<rect x="0" y="170" width="320" height="50" fill="{C}" fill-opacity=".6" stroke="none"/>
'''+per(70,84,'{E}','{C}',1.25)+per(252,84,'{P}','{C}',1.25)+'''
<rect x="36" y="150" width="248" height="14" rx="5" fill="{S}"/><path d="M64 164v30M256 164v30"/>
<g transform="rotate(-4 160 122)"><rect x="126" y="96" width="68" height="52" rx="6" fill="{C}"/>'''+blot(160,121,.55)+'''</g>
<path d="M92 26h52a9 9 0 0 1 9 9v18a9 9 0 0 1-9 9h-26l-14 11 3-11h-15a9 9 0 0 1-9-9V35a9 9 0 0 1 9-9z" fill="{C}" stroke="{A}"/>
<path d="M106 44c0-6 4-9 8-9s8 3 8 7-5 6-6 9" stroke="{A}" stroke-width="2.200" stroke-opacity="0"/><circle cx="104" cy="44" r="2.600" fill="{A}" stroke="none"/><circle cx="118" cy="44" r="2.600" fill="{A}" stroke="none"/><circle cx="132" cy="44" r="2.600" fill="{A}" stroke="none"/>''','#F1DFCB')
W['sis_sogno']=_vg(14,'''<g transform="rotate(-6 84 132)"><rect x="40" y="96" width="88" height="70" rx="8" fill="{C}"/>'''+blot(84,130,.75)+'''</g>
<path d="M134 110Q160 84 184 84" stroke="{A}" stroke-dasharray="3 7"/>
<circle cx="146" cy="100" r="3" fill="{C}"/><circle cx="162" cy="90" r="4.500" fill="{C}"/>
<g fill="{C}"><circle cx="208" cy="76" r="22"/><circle cx="238" cy="60" r="26"/><circle cx="266" cy="80" r="22"/><circle cx="236" cy="92" r="24"/></g>
<g fill="{C}" stroke="none"><circle cx="208" cy="76" r="20"/><circle cx="238" cy="60" r="24"/><circle cx="266" cy="80" r="20"/><circle cx="236" cy="92" r="22"/></g>
<path d="M246 56a16 16 0 1 0 10 28 13 13 0 0 1-10-28z" fill="{A}" stroke="none"/>
<path d="M218 70l3 1.500-3 1.500-1.200 3.500-1.200-3.500-3-1.500 3-1.500 1.200-3.500z" fill="{A}" stroke="none"/><circle cx="226" cy="96" r="2" fill="{A}" stroke="none"/>
<ellipse cx="160" cy="196" rx="130" ry="10" fill="{C}" fill-opacity=".6" stroke="none"/>''','#E3D9C6')
W['sis_rivista']=_vg(15,'''<ellipse cx="160" cy="190" rx="130" ry="11" fill="{C}" fill-opacity=".7" stroke="none"/>
<path d="M160 70Q120 52 62 62V168Q120 158 160 176z" fill="{C}"/><path d="M160 70Q200 52 258 62V168Q200 158 160 176z" fill="{C}"/><path d="M160 70V176"/>
'''+blot(111,112,.6)+'''
<path d="M178 86q30-8 62-6M178 102q30-8 62-6M178 118q30-8 62-6M178 134q22-6 44-5" stroke-opacity=".5"/>
<circle cx="262" cy="46" r="20" fill="{E}"/><path d="M242 46h40M262 26c-9 8-9 32 0 40M262 26c9 8 9 32 0 40" stroke-width="1.800"/>
<path d="M256 44c-4-5-6-8-6-11a6 6 0 0 1 12 0c0 3-2 6-6 11z" fill="{A}" stroke-width="1.600"/>''','#E4ECE7')
def _aud(xs):
    return ''.join('<circle cx="%g" cy="%g" r="10" fill="%s"/><path d="M%g %gq0-22 17-22t17 22z" fill="%s"/>'%(x,y,c,x-17,y+36,c2) for x,y,c,c2 in xs)
W['for_aula']=_vg(16,'''<rect x="52" y="24" width="150" height="98" rx="8" fill="{C}"/>'''+blot(127,72,.95)+'''<path d="M127 122v14M104 136h46"/>
'''+per(246,72,'{P}','{C}',1.15)+'''<path d="M232 100l-22-14"/>
'''+_aud([(50,176,'{E}','#B3C7BC'),(104,182,'{P}','{C}'),(160,176,'{E}','#B3C7BC'),(216,182,'{P}','{C}'),(270,176,'{E}','#B3C7BC')]),'#E3D9C6')
W['for_scena']=_vg(17,'''<path d="M110 0h100l60 180H50z" fill="{C}" fill-opacity=".5" stroke="none"/><ellipse cx="160" cy="180" rx="112" ry="16" fill="{C}" stroke="none"/>
'''+chair(60,150)+chair(92,132)+chair(228,132)+chair(260,150)+per(138,98,'{P}','{C}',1.2)+per(184,98,'{E}','#B3C7BC',1.2)+'''
<path d="M150 82q10-12 22 0" stroke="{A}"/><path d="M168 78l5 4-6 3" stroke="{A}"/>''','#DCE7E0')
W['for_supervisione']=_vg(18,'''<ellipse cx="160" cy="124" rx="126" ry="74" fill="{C}" fill-opacity=".55" stroke="{A}" stroke-dasharray="3 7"/>
'''+per(60,62,'{E}','{C}',.72)+per(116,34,'{P}','{C}',.72)+per(204,34,'{E}','{C}',.72)+per(260,62,'{P}','{C}',.72)+per(52,136,'{P}','{C}',.72)+per(268,136,'{E}','{C}',.72)+per(134,112,'{P}','{E}',1.05)+per(186,112,'{E}','{P}',1.05)+'''
<path d="M146 98q14-16 28 0" stroke="{A}"/><path d="M170 93l5 5-7 2" stroke="{A}"/>
<path d="M174 176q-14 14-28 0" stroke="{A}"/><path d="M150 181l-5-5 7-2" stroke="{A}"/>''','#F1DFCB')
W['for_team']=_vg(19,'''<ellipse cx="160" cy="150" rx="104" ry="34" fill="{C}"/>
'''+per(84,70,'{P}','{C}',1.0)+per(160,54,'{E}','#B3C7BC',1.0)+per(236,70,'{P}','{C}',1.0)+'''
<ellipse cx="160" cy="150" rx="104" ry="34" fill="{C}"/>
<path d="M160 150v-16M160 138c-8-2-10-10-6-14 4 2 6 8 6 14zM160 142c8-2 10-10 6-14-4 2-6 8-6 14z" fill="{E}"/><path d="M152 152h16l-2 10h-12z" fill="{A}"/>
<rect x="96" y="146" width="30" height="20" rx="3" fill="{S}" transform="rotate(-8 111 156)"/><rect x="196" y="146" width="30" height="20" rx="3" fill="{S}" transform="rotate(8 211 156)"/>
<path d="M24 28h44a8 8 0 0 1 8 8v14a8 8 0 0 1-8 8H52l-10 9 2-9H24a8 8 0 0 1-8-8V36a8 8 0 0 1 8-8z" fill="{C}" stroke="{A}"/><path d="M28 40h34M28 48h22" stroke="{A}" stroke-width="1.800"/>
<path d="M252 20h44a8 8 0 0 1 8 8v14a8 8 0 0 1-8 8h-20l2 9-10-9h-16a8 8 0 0 1-8-8V28a8 8 0 0 1 8-8z" fill="{C}"/><path d="M256 32h34M256 40h22" stroke-width="1.800"/>''','#E4ECE7')
