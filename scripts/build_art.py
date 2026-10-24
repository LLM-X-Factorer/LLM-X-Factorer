#!/usr/bin/env python3
"""Build self-contained profile SVGs. Python standard library only."""
from pathlib import Path
import base64
import html
import random

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'assets'
IMAGE = 'data:image/webp;base64,' + base64.b64encode((ART / 'workshop.webp').read_bytes()).decode()

# Original 5 x 7 bitmap alphabet: SVG paths keep the pixel display independent of fonts.
GLYPHS = {
    'A':[14,17,17,31,17,17,17], 'B':[30,17,17,30,17,17,30],
    'C':[15,16,16,16,16,16,15], 'D':[30,17,17,17,17,17,30],
    'E':[31,16,16,30,16,16,31], 'F':[31,16,16,30,16,16,16],
    'G':[15,16,16,23,17,17,15], 'H':[17,17,17,31,17,17,17],
    'I':[31,4,4,4,4,4,31], 'J':[7,2,2,2,18,18,12],
    'K':[17,18,20,24,20,18,17], 'L':[16,16,16,16,16,16,31],
    'M':[17,27,21,21,17,17,17], 'N':[17,25,21,19,17,17,17],
    'O':[14,17,17,17,17,17,14], 'P':[30,17,17,30,16,16,16],
    'Q':[14,17,17,17,21,18,13], 'R':[30,17,17,30,20,18,17],
    'S':[15,16,16,14,1,1,30], 'T':[31,4,4,4,4,4,4],
    'U':[17,17,17,17,17,17,14], 'V':[17,17,17,17,17,10,4],
    'W':[17,17,17,21,21,21,10], 'X':[17,17,10,4,10,17,17],
    'Y':[17,17,10,4,4,4,4], 'Z':[31,1,2,4,8,16,31],
    '0':[14,17,19,21,25,17,14], '1':[4,12,4,4,4,4,14],
    '2':[14,17,1,2,4,8,31], '3':[30,1,1,14,1,1,30],
    '4':[2,6,10,18,31,2,2], '5':[31,16,16,30,1,1,30],
    '6':[14,16,16,30,17,17,14], '7':[31,1,2,4,8,8,8],
    '8':[14,17,17,14,17,17,14], '9':[14,17,17,15,1,1,14],
    "'":[4,4,8,0,0,0,0], '.':[0,0,0,0,0,12,12],
    '/':[1,2,2,4,8,8,16], '-':[0,0,0,31,0,0,0],
    '+':[0,4,4,31,4,4,0], ':':[0,12,12,0,12,12,0],
    '>':[16,8,4,2,4,8,16], ' ':[0]*7,
}


def pixel(text, x, y, size=3, color='#e8e6f2'):
    commands=[]
    for char in text.upper():
        for row,bits in enumerate(GLYPHS[char]):
            for col in range(5):
                if bits & (1 << (4-col)):
                    commands.append(f'M{x+col*size:g} {y+row*size:g}h{size:g}v{size:g}h{-size:g}z')
        x += size*6
    return f'<path fill="{color}" d="{"".join(commands)}"/>'


def text(value,x,y,size=20,color='#c0bfd2',extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" {extra}>{html.escape(value)}</text>'


def rect(x,y,w,h,fill,extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" {extra}/>'


def cross(x,y,color='#9ee4c2',scale=1):
    return f'<g transform="translate({x} {y}) scale({scale})">'+rect(4,0,4,12,color)+rect(0,4,12,4,color)+'</g>'


def sprite(kind,x,y,s=4,color='#a8edca'):
    maps={
        'bot':['....XX......','.....X......','..XXXXXXXX..','.X........X.','.X.XX..XX.X.','.X.XX..XX.X.','.X........X.','..XXXXXXXX..','....XXXX....','..XXXXXXXX..','..X.XXXX.X..','....X..X....'],
        'doc':['..XXXXXX....','..X....XX...','..X.....XX..','..X.XXX..X..','..X......X..','..X.XXXX.X..','..X......X..','..X.XXXX.X..','..X......X..','..XXXXXXXX..'],
        'quest':['.....XX.....','.....XX.....','.....XX.....','.....XX.....','.....XX.....','.....XX.....','............','.....XX.....','.....XX.....'],
    }
    commands=[]
    for row,line in enumerate(maps[kind]):
        for col,v in enumerate(line):
            if v=='X': commands.append(f'M{col} {row}h1v1h-1z')
    return f'<g transform="translate({x} {y}) scale({s})"><path fill="{color}" d="{"".join(commands)}"/></g>'


def shell(w,h,title,desc,body,style=''):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Arial,sans-serif">
<title id="title">{html.escape(title)}</title>
<desc id="desc">{html.escape(desc)}</desc>
{f'<style>{style}</style>' if style else ''}
{body}
</svg>\n'''


def hero(theme='dark',mobile=False,still=False):
    light=theme=='light'
    bg='#f3f0e7' if light else '#171a2c'
    border='#d1d1ca' if light else '#393d57'
    ink='#292c43' if light else '#f3eedf'
    muted='#58616a' if light else '#adb5cb'
    mint='#22735f' if light else '#a8edca'
    grid='#d9dfd5' if light else '#292e44'
    w,h=(720,900) if mobile else (1200,650)
    body=rect(0,0,w,h,bg,'rx="18"')
    body+=f'<defs><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{grid}" stroke-width=".6"/></pattern></defs>'
    body+=rect(16,16,w-32,h-32,'url(#grid)','rx="10" opacity=".55"')
    body+=rect(1,1,w-2,h-2,'none',f'rx="18" stroke="{border}" stroke-width="2"')
    body+=rect(32,32,8,8,mint)+pixel('LLM-X-FACTORER',52,30,2,mint)
    body+=pixel('OPEN WORKSHOP',w-211,31,1.8,muted)
    body+=f'<path d="M32 64H{w-32}" stroke="{border}"/>'
    rng=random.Random(42)
    for i in range(24):
        x=rng.randrange(35,w-35); y=rng.randrange(85,h-80)
        body+=f'<g class="spark s{i%4}">'+rect(x,y,3,3,mint, 'opacity=".35"')+'</g>'
    if mobile:
        body+=pixel("LET'S BUILD",48,100,6,ink)
        body+=pixel('SOMETHING USEFUL.',48,161,5.6,mint)
        body+=text('AI agents, tools & open experiments.',48,239,23,muted)
        body+=f'<g class="float"><image href="{IMAGE}" x="65" y="245" width="590" height="590"/></g>'
        body+=cross(615,303,mint,1.6)+cross(62,515,'#bdb0e9',1.3)
        floor=852
    else:
        body+=pixel("LET'S BUILD",52,142,7,ink)
        body+=pixel('SOMETHING',52,213,7,ink)
        body+=pixel('USEFUL.',52,284,7,mint)
        body+=text('AI agents, practical tools,',54,385,25,muted)
        body+=text('and a few open experiments.',54,420,25,muted)
        body+=pixel('EXPLORE. TINKER. CONTRIBUTE.',54,477,1.75,mint)
        body+=f'<g class="float"><image href="{IMAGE}" x="635" y="72" width="500" height="500"/></g>'
        body+=cross(1104,134,mint,1.8)+cross(585,340,'#bdb0e9',1.5)
        floor=598
    body+=f'<path d="M32 {floor-20}H{w-32}" stroke="{border}"/>'
    body+=pixel('IDEA',42,floor,1.8,muted)+pixel('TOOL',180,floor,1.8,muted)+pixel('SHARE',318,floor,1.8,muted)
    body+=f'<path d="M101 {floor+6}H163M239 {floor+6}H301" stroke="{muted}" stroke-dasharray="3 6" opacity=".5"/>'
    body+=f'<g class="packet">'+rect(105,floor+3,6,6,mint)+'</g>'
    body+=pixel('PULL REQUESTS WELCOME',w-291,floor+1,1.6,mint) if not mobile else pixel('COME BUILD',w-161,floor,1.8,mint)
    style='''
@keyframes float { 0%,100% {transform:translateY(0)} 50% {transform:translateY(-7px)} }
@keyframes spark {0%,100% {opacity:.3} 50% {opacity:1} }
@keyframes travel {0% {transform:translateX(0);opacity:0} 15% {opacity:1} 85% {opacity:1} 100% {transform:translateX(52px);opacity:0} }
@media (prefers-reduced-motion: no-preference) {
 .float {animation:float 8s ease-in-out infinite}
 .spark {animation:spark 5s ease-in-out infinite}
 .s1 {animation-delay:-1.3s} .s2 {animation-delay:-2.6s} .s3 {animation-delay:-3.9s}
 .packet {animation:travel 3s linear infinite}
}
''' if not still else ''
    return shell(w,h,"LLM-X-Factorer's open workshop — let's build something useful",'An original pixel-art developer workshop with an Agent robot, research notebooks, screens and a document printer. Links to projects and collaboration are below.',body,style)


ZONES=[('agent','01','AGENT BAY','RUNTIMES / EVALUATION','bot','#a8edca'),('workflows','02','WORKFLOW SHELF','RESEARCH / DOCUMENTS / MEDIA','doc','#c8b6f0'),('quests','03','QUEST BOARD','SMALL TASKS. REAL CONTRIBUTIONS.','quest','#f1c78d')]

def icon(title,kind,color):
    body=rect(0,0,48,48,'#202438','rx="6"')+sprite(kind,6,6,3,color)
    return shell(48,48,title,'',body)


def nav(title,kind,color):
    # No fake in-image button interaction: README wraps the whole asset in a real anchor.
    body=rect(0,0,300,88,'#171a2c','rx="8"')+rect(1,1,298,80,'#252a40',f'rx="7" stroke="{color}" stroke-width="1.5"')
    body+=sprite(kind,12,19,3,color)+pixel(title,61,31,2.25,color)+pixel('>',276,33,2,color)
    return shell(300,88,title,f'Navigate to {title.lower()}.',body)


def main():
    for theme in ['light','dark']:
        for mobile in [False,True]:
            for still in [False,True]:
                name=f'hero-{theme}'+('-mobile' if mobile else '')+('-still' if still else '')+'.svg'
                (ART/name).write_text(hero(theme,mobile,still))
    for name,num,title,sub,kind,color in ZONES:
        (ART/f'icon-{name}.svg').write_text(icon(title,kind,color))
        (ART/f'nav-{name}.svg').write_text(nav(title,kind,color))
    print('Built 8 hero variants and 6 navigation/section assets.')


if __name__=='__main__':
    main()
