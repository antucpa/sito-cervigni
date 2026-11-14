G='#1F3A3D'; A='#B8622B'; SAND='#E3D9C6'; SAGE='#C9D8D0'; APR='#EBC9AE'; CREAM='#F6F3EC'; SK='#F3D9C4'; HAIR='#F1EEE8'
def wrap(i,inner):
    return '<svg class="ritr" viewBox="0 0 200 200" width="200" height="200" fill="none" stroke="%s" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><defs><clipPath id="rc%d"><circle cx="100" cy="100" r="96"/></clipPath></defs>%s</svg>'%(G,i,inner.replace('#RC','url(#rc%d)'%i))
GR='#C4C9C7'; GR2='#E2E4E1'; TW='#55676A'; AMB='#C8853F'; CIG='#7A4A26'
LACAN=wrap(1,f'''<circle cx="100" cy="100" r="96" fill="{SAGE}" stroke="none"/>
<g clip-path="#RC">
<path d="M22 206q4-50 54-58l24 24 24-24q50 8 54 58z" fill="{TW}"/>
<path d="M44 176l6 4M60 166l6 4M52 190l6 4M140 168l6-4M150 182l6-4M134 188l6-4M70 184l6 4M124 178l6-4" stroke="{CREAM}" stroke-opacity=".35" stroke-width="1.600"/>
<path d="M78 148l22 28 22-28-9-9H87z" fill="{CREAM}"/>
<path d="M76 148l14 26M124 148l-14 26" />
<path d="M88 126h24v18q-12 9-24 0z" fill="{SK}"/>
<path d="M100 165l-24-11q-3 11 0 22zM100 165l24-11q3 11 0 22z" fill="{SAND}"/><rect x="95" y="159" width="10" height="12" rx="3" fill="{SAND}"/>
<circle cx="84" cy="163" r="1.300" fill="{G}" stroke="none"/><circle cx="86" cy="169" r="1.300" fill="{G}" stroke="none"/><circle cx="116" cy="163" r="1.300" fill="{G}" stroke="none"/><circle cx="114" cy="169" r="1.300" fill="{G}" stroke="none"/>
<path d="M66 86c-12-4-15 20-2 24M134 86c12-4 15 20 2 24" fill="{SK}"/>
<path d="M66 80c0-28 14-42 34-42s34 14 34 42c0 22-6 40-16 50-6 6-12 9-18 9s-12-3-18-9c-10-10-16-28-16-50z" fill="{SK}"/>
<path d="M64 84c-7-32 4-60 36-62 32 2 43 30 36 62-2-14-5-22-10-28-16 5-36 5-52 0-5 6-8 14-10 28z" fill="{GR}"/>
<path d="M80 30v18M90 25v20M100 24v20M110 25v20M120 30v18M72 40v12M128 40v12" stroke="{GR2}" stroke-width="2.200"/>
<path d="M84 64h32M87 70h26" stroke-width="1.500" stroke-opacity=".35"/>
<path d="M73 79q9-5 19-2M108 77q10-3 19 2" stroke-width="3.400"/>
<rect x="71" y="84" width="25" height="18" rx="8" fill="{CREAM}" fill-opacity=".45" stroke-width="1.500"/><rect x="104" y="84" width="25" height="18" rx="8" fill="{CREAM}" fill-opacity=".45" stroke-width="1.500"/>
<path d="M70 87q13-6 27-1M103 86q14-5 27 1" stroke-width="3.200"/><path d="M96 90q4-3 8 0M70 89l-8-2M130 89l8-2" stroke-width="1.800"/>
<path d="M78 92q6-3 12 0M110 92q6-3 12 0" stroke-width="1.800"/><circle cx="84" cy="94.500" r="2.300" fill="{G}" stroke="none"/><circle cx="116" cy="94.500" r="2.300" fill="{G}" stroke="none"/>
<path d="M100 90c-1 12-7 20-6 25 2 4 10 4 12 0" stroke-width="2.200"/>
<path d="M83 109q-5 8-2 17M118 108q5 8 2 18" stroke-width="1.500" stroke-opacity=".5"/>

<path d="M147 131c9-6 11-15 5-21s-5-15 3-22" stroke="{CREAM}" stroke-width="2.600"/><path d="M156 124c5-5 5-11 1-15" stroke="{CREAM}" stroke-opacity=".75" stroke-width="2.200"/>
<g transform="translate(-5 1)"><path d="M105 119.500Q116 118.500 124 123Q133 128.500 143 129.500Q148 130.500 147.500 134.500Q147 138.500 142 138.500Q131 137.500 122 132Q115 128 105 128.500Z" fill="#8A5A2E" stroke-width="2.200"/>
<path d="M109 122Q117 121.500 123 125Q131 130 139 131.500" stroke="#C08A52" stroke-width="1.600"/>
<path d="M139 129.200Q143.500 129.500 146 130.700Q148 132 147.500 134.500Q147 138.500 142 138.500L138 138.100Z" fill="#DEDDD8" stroke-width="2"/>
<path d="M139.200 129.600L138.200 137.800" stroke="#E2702A" stroke-width="2.400"/>
<path d="M117.500 120.300L122.800 122.300L121.800 131.700L116.500 129.500Z" fill="#E3C36A" stroke-width="1.500"/>
</g>
<ellipse cx="100" cy="125" rx="5" ry="7" fill="{SK}" stroke="none"/>
<path d="M85 123.500q7 3 13 .500q4-2.500 8-2" stroke-width="2.400"/><path d="M84 121.500q-2 2-1 4" stroke-width="1.800"/>
<path d="M94 128.500q5 3.500 11 1.500" stroke-width="2.200"/>
<path d="M105.500 121.300q1.500 4.500 0 8.700" stroke-width="2"/>
</g>
<circle cx="100" cy="100" r="96" stroke="{G}"/>''')
dots=''.join('<circle cx="%g" cy="%g" r="2.700" fill="%s" stroke="none"/>'%(x,y,CREAM) for x,y in [(40,176),(54,166),(52,188),(68,178),(70,196),(84,170),(86,190),(100,180),(114,190),(116,170),(130,178),(132,196),(146,166),(148,188),(160,176),(66,160),(134,160),(100,196)])
DOLTO=wrap(2,f'''<circle cx="100" cy="100" r="96" fill="{APR}" stroke="none"/>
<g clip-path="#RC">
<path d="M18 206q2-50 56-58h52q54 8 56 58z" fill="{G}"/>{dots}
<path d="M76 149q24 20 48 0l-4-6H80z" fill="{G}"/>
<path d="M86 128h28v20q-14 10-28 0z" fill="{SK}"/>
<path d="M56 106c-6 2-10-4-8-10-6-4-6-12-1-16-4-6-2-14 4-17-1-8 4-14 11-15 2-8 9-12 16-11 5-7 14-8 22-4 8-4 17-3 22 4 7-1 14 3 16 11 7 1 12 7 11 15 6 3 8 11 4 17 5 4 5 12-1 16 2 6-2 12-8 10l-10 6-6-34H72l-6 34z" fill="{GR2}"/>
<path d="M60 92c0-28 16-44 40-44s40 16 40 44c0 30-18 48-40 48s-40-18-40-48z" fill="{SK}"/>
<path d="M57 88c-5-30 13-54 43-54s48 24 43 54c-6-17-16-27-30-30-18 5-35 3-45-5-6 8-9 20-11 35z" fill="#EEF0ED"/>
<path d="M66 50q14-14 36-10M90 38q22-6 38 12M60 68q5-12 14-16M132 60q6 6 8 16" stroke-width="1.800" stroke-opacity=".45"/>
<path d="M53 80q-3 8 1 14M147 80q3 8-1 14" stroke-width="1.800" stroke-opacity=".45"/>
<circle cx="70" cy="113" r="7" fill="{A}" fill-opacity=".25" stroke="none"/><circle cx="130" cy="113" r="7" fill="{A}" fill-opacity=".25" stroke="none"/>
<path d="M72 80q9-5 18-2M110 78q9-3 18 2" stroke-width="2" stroke-opacity=".6"/>
<circle cx="82" cy="97" r="16" fill="{CREAM}" fill-opacity=".4" stroke="{AMB}" stroke-width="4.500"/><circle cx="118" cy="97" r="16" fill="{CREAM}" fill-opacity=".4" stroke="{AMB}" stroke-width="4.500"/>
<path d="M97 94q3-3 6 0M66 94l-7-3M134 94l7-3" stroke="{AMB}" stroke-width="4"/>
<path d="M76 95q6-5 12 0M112 95q6-5 12 0" stroke-width="2"/><circle cx="82" cy="98" r="2.600" fill="{G}" stroke="none"/><circle cx="118" cy="98" r="2.600" fill="{G}" stroke="none"/>
<path d="M100 102c-1 6-5 9-4 12 2 2 6 2 8 0" stroke-width="2"/>
<path d="M83 120q17 5 34 0q-17 18-34 0z" fill="#FFFFFF"/><path d="M86 124q14 3 28 0" stroke-width="1.400" stroke-opacity=".5"/>
<path d="M79 118q2 3 4 3M121 118q-2 3-4 3" stroke-width="1.600" stroke-opacity=".6"/>
</g>
<circle cx="100" cy="100" r="96" stroke="{G}"/>''')
if __name__=='__main__':
    open('ritr.html','w').write('<body style="margin:0;background:#ECE6D9;font-family:Georgia,serif;color:#1F3A3D"><div style="display:flex;gap:60px;padding:40px;justify-content:center">'
      +'<figure style="margin:0;text-align:center">'+LACAN.replace('width="200" height="200"','width="260" height="260"')+'<figcaption style="margin-top:12px;font-size:22px">Jacques Lacan</figcaption></figure>'
      +'<figure style="margin:0;text-align:center">'+DOLTO.replace('width="200" height="200"','width="260" height="260"')+'<figcaption style="margin-top:12px;font-size:22px">Françoise Dolto</figcaption></figure></div></body>')

HB='#3B2A20'; BD='#35261D'; JK='#2F3537'
def _antonio():
    SKA='#F0CDB4'
    return wrap(3,f'''<circle cx="100" cy="100" r="96" fill="#DCE7E0" stroke="none"/>
<g clip-path="#RC">
<g fill="{CREAM}" stroke="none" fill-opacity=".85"><circle cx="34" cy="52" r="11"/><circle cx="48" cy="46" r="13"/><circle cx="62" cy="54" r="10"/><rect x="30" y="52" width="36" height="12" rx="6"/><circle cx="150" cy="36" r="9"/><circle cx="162" cy="32" r="11"/><circle cx="174" cy="38" r="8"/><rect x="146" y="36" width="32" height="10" rx="5"/></g>
<path d="M0 150q50-24 100-10t100-12v80H0z" fill="#C3D4CB" stroke="none"/><path d="M0 166q60-16 110-6t90-8v60H0z" fill="#B3C7BC" stroke="none"/>
<path d="M8 212q6-52 62-62h60q56 10 62 62z" fill="{JK}"/>
<path d="M36 182q4-4 8 0M54 198q4-4 8 0M152 178q4-4 8 0M136 196q4-4 8 0M28 200q4-4 8 0M166 194q4-4 8 0M70 176q4-4 8 0M122 172q4-4 8 0" stroke="#4A5153" stroke-width="1.600"/>
<path d="M82 150q18 16 36 0l-18 36z" fill="#17191A"/>
<path d="M80 136h40v16q-20 13-40 0z" fill="{SKA}"/>
<path d="M66 154q-4-13 9-18l11 20-13 8zM134 154q4-13-9-18l-11 20 13 8z" fill="{JK}"/>
<path d="M100 186v30" stroke="#17191A"/><circle cx="107" cy="197" r="2.600" fill="#17191A" stroke="#4A5153" stroke-width="1"/>
<path d="M53 84c-10-4-13 17-2 23M147 84c10-4 13 17 2 23" fill="{SKA}"/><path d="M50 92q3 3 2 8M150 92q-3 3-2 8" stroke-width="1.500" stroke-opacity=".5"/>
<path d="M54 78c0-26 18-43 46-43s46 17 46 43c0 14-1 26-4 36-6 20-22 31-42 31s-36-11-42-31c-3-10-4-22-4-36z" fill="{SKA}"/>
<ellipse cx="71" cy="100" rx="9" ry="6" fill="{A}" fill-opacity=".16" stroke="none"/><ellipse cx="129" cy="100" rx="9" ry="6" fill="{A}" fill-opacity=".16" stroke="none"/>
<path d="M54 86c0 10 2 18 6 22 5 4 11 4 17 2 7-2 14-2 23-2s16 0 23 2c6 2 12 2 17-2 4-4 6-12 6-22 3 40-12 67-46 67S51 126 54 86z" fill="{BD}"/>
<path d="M87 133q13 8 26 0q-2 15-13 17q-11-2-13-17z" fill="#8B7D73" fill-opacity=".6" stroke="none"/>
<path d="M65 118q2 8 6 12M75 127q2 8 6 12M125 127q-2 8-6 12M135 118q-2 8-6 12M92 141v6M108 141v6M100 143v7M84 136q1 5 4 8M116 136q-1 5-4 8" stroke="#6A5545" stroke-width="1.600"/>
<path d="M77 114q6-10 23-8 17-2 23 8-6-3-11-2-6-3-12-1-6-2-12 1-5-1-11 2z" fill="{BD}"/>
<path d="M89 116.500q11 4 22 0q-11 9-22 0z" fill="#DDA890" stroke-width="1.600"/>
<path d="M53 84c-7-32 8-58 47-58s54 26 47 58c-1-10-4-18-8-23-2-8-8-13-15-14-8 2-16 1-24 1s-17 1-24-1c-7 1-13 6-15 14-4 5-7 13-8 23z" fill="{HB}"/>
<path d="M53 84c-2-10-1-19 4-27 2 8 2 17 1 25zM147 84c2-10 1-19-4-27-2 8-2 17-1 25z" fill="#6A5545" stroke="none"/>
<path d="M64 38q6-9 15-7q6-7 15-4q7-5 15 1q8-3 13 5q8 0 12 8" stroke="#6A5545" stroke-width="2.200"/>
<path d="M76 46q8-6 18-6M100 40q10-2 20 4" stroke="#6A5545" stroke-width="1.800" stroke-opacity=".7"/>
<path d="M80 54q20-5 40 0M84 61q16-4 32 0" stroke-width="1.400" stroke-opacity=".3"/><path d="M97 68v6M103 68v6" stroke-width="1.400" stroke-opacity=".35"/>
<path d="M65 73q12-13 27-6l-1 5.500q-12-5-23 4z" fill="{HB}" stroke="none"/><path d="M108 69q15-5 27 5l-3 3.500q-11-7-23-3z" fill="{HB}" stroke="none"/>
<path d="M70 85q8.500-7 17 0q-8.500 5-17 0z" fill="#FFFFFF" stroke-width="1.500"/><path d="M113 85q8.500-7 17 0q-8.500 5-17 0z" fill="#FFFFFF" stroke-width="1.500"/>
<circle cx="78.500" cy="85" r="3.200" fill="#3B2A20" stroke="none"/><circle cx="121.500" cy="85" r="3.200" fill="#3B2A20" stroke="none"/><circle cx="79.500" cy="84" r=".9" fill="#FFFFFF" stroke="none"/><circle cx="122.500" cy="84" r=".9" fill="#FFFFFF" stroke="none"/>
<path d="M69 84q9.500-8.500 19 0M112 84q9.500-8.500 19 0" stroke-width="1.900"/>
<path d="M72 91q7 3 14 0M114 91q7 3 14 0" stroke-width="1.300" stroke-opacity=".35"/>
<path d="M97 82c-1 8-6 13-6 18" stroke-width="2"/><path d="M90 100q4 5 10 3q6 2 10-3" stroke-width="2"/>
</g>
<circle cx="100" cy="100" r="96" stroke="{G}"/>''')
ANTONIO=_antonio()
