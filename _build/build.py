"""Builds the Via Pulchritudinis pages from one shared layout.
Run from the repository root:  python3 _build/build.py
Text blocks reused across pages live in _build/pages/_*.html."""
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=lambda n: open(os.path.join(ROOT,'_build','pages',n)).read()
SITE='https://liquid1188.github.io/Via-pulchritudinis/'

NAV=[('lookbook.html','The Lookbook'),('how-it-works.html','How It Works'),('liturgical-year.html','The Liturgical Year'),
     ('beauty-and-faith.html','Beauty &amp; Faith'),('st-pier-giorgio.html','St. Pier Giorgio'),('directory.html','The Directory')]

def lic(name,url): return f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'
ART={
 'nd':('Notre-Dame de Paris, nave and choir','Ibex73',lic('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'https://commons.wikimedia.org/wiki/File:Nave_of_Notre-Dame_de_Paris_towards_the_chancel,_2024_(6).jpg'),
 'sp':('St. Paul Outside the Walls, nave','Herbert Weber, Hildesheim',lic('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),'https://commons.wikimedia.org/wiki/File:San_Paolo_fuori_le_mura-2.jpg'),
 'fa':('Fra Angelico, Crucifixion with St. Dominic, San Marco','jacquemart',lic('CC0','https://creativecommons.org/publicdomain/zero/1.0/'),'https://www.flickr.com/photos/26602223@N00/55152966795'),
 'co':('Cosmatesque pavement, Santa Maria Maggiore','Nicholas Hartmann',lic('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),'https://commons.wikimedia.org/w/index.php?curid=97352923'),
}
def cr(k): t,by,l,src=ART[k]; return f'Photo by {by} · {l} · <a href="{src}" target="_blank" rel="noopener">source</a>'

def layout(fname,title,desc,body,page,scripts=True):
    nav=''.join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==fname else ""}>{t}</a></li>' for h,t in NAV)
    full=f'{title} | Via Pulchritudinis' if page!='home' else 'Via Pulchritudinis | The Beauty of Cathedrals in Everyday Fashion'
    url=SITE+('' if fname=='index.html' else fname)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>try{{if(localStorage.getItem('vp-desktop')==='1')document.querySelector('meta[name=viewport]').setAttribute('content','width=1280')}}catch(e){{}}</script>
<title>{full}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Via Pulchritudinis">
<meta property="og:title" content="{'Via Pulchritudinis' if page=='home' else title+' | Via Pulchritudinis'}">
<meta property="og:description" content="The Beauty of Cathedrals in Everyday Fashion">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F7F3EC">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body data-page="{page}">
<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
  <a class="brand" href="index.html" aria-label="Via Pulchritudinis, home"><b>VIA PULCHRITUDINIS</b><span>A Catholic Journal of Style and Beauty</span></a>
</header>
<div class="navbar">
  <div class="in">
    <a class="mini" href="index.html" aria-label="Via Pulchritudinis, home"><b>VIA PULCHRITUDINIS</b><span>A Catholic Journal of Style and Beauty</span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu<i aria-hidden="true"></i></button>
    <nav class="nav" id="nav" aria-label="Main">
      <ul>{nav}</ul>
      <div class="nav-extra"><button type="button" class="vp-toggle">View desktop version</button></div>
    </nav>
  </div>
</div>
<main id="main">
{body}
</main>
<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        <div class="brand"><b>VIA PULCHRITUDINIS</b><span>A Catholic Journal of Style and Beauty</span></div>
        <p>Via Pulchritudinis explores the relationship between sacred architecture, personal style, and the Catholic understanding of beauty. Through its architectural lookbook, theological reflections, and curated resources, the journal invites readers to discover new ways of appreciating the Church’s artistic inheritance.</p>
        <p>Curated by Andrew Likoudis, a Catholic writer and editor whose work on St. Pier Giorgio Frassati and personal style appeared in the <em>National Catholic Register</em>.</p>
      </div>
      <nav aria-label="Footer"><span class="label">The Journal</span><ul>{''.join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV[:3])}</ul></nav>
      <nav aria-label="Footer, more"><span class="label">More</span><ul>{''.join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV[3:])}<li><a href="sources-and-credits.html">Sources &amp; Credits</a></li></ul></nav>
    </div>
    <div class="base"><span>Photos are used under Creative Commons licenses or are in the public domain, credited on each page and in <a href="sources-and-credits.html" style="color:inherit">Sources &amp; Credits</a>.</span><button type="button" class="vp-toggle">View desktop version</button><span class="amdg">Ad maiorem Dei gloriam</span></div>
  </div>
</footer>
<button type="button" class="vp-back">View mobile version</button>
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Photo viewer" hidden>
  <button type="button" class="lb-x" id="lbX">Close <span aria-hidden="true">✕</span></button>
  <button type="button" class="lb-nav lb-p" id="lbP" aria-label="Previous photo">←</button>
  <figure><img id="lbImg" alt=""><figcaption><b id="lbCap"></b><span id="lbCredit"></span><span class="lb-n" id="lbN"></span></figcaption></figure>
  <button type="button" class="lb-nav lb-nx" id="lbNx" aria-label="Next photo">→</button>
</div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="data.js"></script>
<script src="assets/site.js"></script>
</body>
</html>
'''

def head(no,label,h1,*paras,extra=''):
    ps=''.join(f'<p class="lede">{p}</p>' for p in paras)
    return f'''<div class="wrap page-head">
  <div class="intro"><h1>{h1}</h1><div>{ps}{extra}</div></div>
</div>'''

HINT='<p class="swipe-hint" aria-hidden="true">Swipe for more →</p>'

PAGES={}
# ---------------- HOME ----------------
TOC=[('lookbook.html','I','The Lookbook','Fifty churches, each with its own palette and a contemporary outfit.','img/sm/ext/siena.jpg|img/sm/look/siena-v2.jpg'),
 ('how-it-works.html','II','How It Works','From stone and glass to five colors to a wardrobe.','img/sm/ext/st-marks.jpg'),
 ('liturgical-year.html','III','The Liturgical Year','The colors of the Church’s seasons, worn lightly.','img/int/saint-denis.jpg'),
 ('beauty-and-faith.html','IV','Beauty &amp; Faith','What the popes and the Church have said about beauty and dress.','img/art/san-paolo-nave.jpg'),
 ('st-pier-giorgio.html','V','St. Pier Giorgio','The saint who dressed well and gave his clothes away.','img/art/fra-angelico-st-dominic.jpg'),
 ('directory.html','VI','The Directory','Catholic makers, stylists, publications, and books.','img/sm/ext/vezelay.jpg')]
def _im(im):
  if '|' in im: return '<div class="im two">'+''.join(f'<img loading="lazy" src="{x}" alt="">' for x in im.split('|'))+'</div>'
  st=' style="object-position:center 88%"' if 'angelico' in im else ''
  return f'<div class="im"><img loading="lazy" src="{im}" alt=""{st}></div>'
toc=''.join(f'<li><a href="{h}">{_im(im)}<h3>{t}</h3><p>{d}</p></a></li>' for h,n,t,d,im in TOC)
PAGES['index.html']=('Home','Via Pulchritudinis draws inspiration from the world’s great Catholic cathedrals, basilicas, and shrines, translating their architectural beauty into contemporary personal style.','home',f'''
<section class="hero" id="hero" data-zoom-group aria-roledescription="carousel" aria-label="Featured churches and looks">
  <div class="h-panel h-church zp"><img class="kb" alt="" data-zoom tabindex="0" role="button"><img class="kb" alt="" data-zoom tabindex="-1" role="button" aria-hidden="true"></div>
  <div class="h-pal" id="hPal" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
  <div class="h-panel h-look zp"><img class="kb" alt="" data-zoom tabindex="0" role="button"><img class="kb" alt="" data-zoom tabindex="-1" role="button" aria-hidden="true"></div>
  <div class="h-copy">
    <h1 id="cover-h">The Beauty of Cathedrals in Everyday Fashion</h1>
    <div class="ctas"><a class="btn solid light" href="lookbook.html">Explore the Lookbook</a><a class="btn ghost" href="how-it-works.html">Discover the Concept</a></div>
  </div>
  <div class="h-now" aria-live="polite">
    <div class="h-count"><b id="hNo">01</b><span>/ <span id="hOf">06</span></span></div>
    <a class="h-name" id="hOpen" href="lookbook.html"><b id="hTitle"></b><span id="hSub"></span></a>
    <div class="h-ctrl"><button type="button" id="hPrev" aria-label="Previous church">←</button><span class="h-prog"><i id="hProg"></i></span><button type="button" id="hNext" aria-label="Next church">→</button></div>
  </div>
</section>

<section class="statement wrap rv-group" aria-label="About the journal">
  <p class="big">From the marble of Rome’s great basilicas to the stained glass of Gothic cathedrals, sacred architecture offers an extraordinary vocabulary of color, texture, and form.</p>
  <p class="lede">Via Pulchritudinis draws inspiration from the world’s great Catholic cathedrals, basilicas, and shrines, translating their architectural beauty into contemporary personal style.</p>
  <div class="today" id="today" hidden><span class="today-sw" id="todaySw"></span><div><span class="label">Today in the liturgical year</span><b id="todayName"></b><span id="todayNote"></span></div><a class="more" href="liturgical-year.html">The Liturgical Year</a></div>
</section>

<section class="contents" aria-labelledby="toc-h">
  <div class="wrap">
    <div class="sec-h"><div><h2 id="toc-h">Six Ways In</h2></div><p>Begin with the lookbook, or start with the ideas behind it. Each part of the journal stands on its own.</p></div>
    <ol class="toc" role="list">{toc}</ol>{HINT}
  </div>
</section>

<section class="sec marquee-sec" aria-labelledby="rail-h">
  <div class="wrap">
    <div class="sec-h"><div><h2 id="rail-h">Fifty Churches, Fifty Looks</h2></div><p>Every church has its own visual language. Hover to pause, or select any look to see its church, palette, and outfit. <a class="more" href="lookbook.html" style="margin-left:6px">Open the Lookbook</a></p></div>
  </div>
  <div class="marquee" id="marquee"><div class="mq-track" id="mqA"></div></div>
  <div class="marquee rev" id="marquee2"><div class="mq-track" id="mqB"></div></div>
</section>

<figure class="interlude">
  <img data-zoom tabindex="0" role="button" data-cap="Notre-Dame de Paris, the nave and choir" src="img/art/notre-dame-nave.jpg" width="1920" height="1280" loading="lazy" decoding="async" alt="The vaulted nave and choir of Notre-Dame de Paris, with stained glass at the far end">
  <figcaption class="wrap"><span class="label">Notre-Dame de Paris</span><p>Restored and reopened in December 2024. Pale limestone, a little gold, and colored light from the glass. A palette can be that simple.</p><small>{cr('nd')}</small></figcaption>
</figure>

<section class="sec">
  <div class="wrap quote-teaser">
    <blockquote>“This world in which we live needs beauty in order not to sink into despair.”</blockquote>
    <cite class="label">Paul VI, address to artists, 8 December 1965</cite>
    <div class="ctas" style="justify-content:center"><a class="btn" href="beauty-and-faith.html">Read Beauty &amp; Faith</a></div>
  </div>
</section>''')

# ---------------- LOOKBOOK ----------------
PAGES['lookbook.html']=('The Lookbook','Fifty contemporary looks drawn from the colors and materials of Catholic cathedrals, basilicas, and shrines.','lookbook',
head('I','The Lookbook','Sacred Spaces. Personal Style.',
 'Every church has its own visual language, shaped by centuries of artistic imagination, local tradition, and religious devotion. Explore contemporary looks inspired by the colors and materials of sacred architecture.',
 'Select a look to see the church that inspired it, its palette, and how those colors become a wardrobe.')+'''
<div class="wrap">
  <div class="filters" id="filters" role="search" aria-label="Filter looks">
    <div class="seg" id="segWho" role="group" aria-label="Show looks for"><button type="button" aria-pressed="true" data-v="all">All</button><button type="button" aria-pressed="false" data-v="her">Women</button><button type="button" aria-pressed="false" data-v="him">Men</button></div>
    <button type="button" class="f-toggle" id="fToggle" aria-expanded="false" aria-controls="fMore">Filters<span id="fCount"></span></button>
    <div class="f-more" id="fMore">
      <div class="colors" id="colorF" role="group" aria-label="Filter by color"></div><span class="color-name" id="colorName" aria-hidden="true">Any color</span>
      <label><span class="sr">Architectural style</span><select id="styleF"></select></label>
      <label><span class="sr">Region</span><select id="regionF"></select></label>
      <div class="search"><label style="display:contents"><span class="sr">Search looks</span><input id="q" type="search" placeholder="Search church, city, or region" autocomplete="off"></label><button type="button" class="clear" id="clearF" disabled>Clear</button></div>
    </div>
  </div>
  <p class="result-count" id="resultCount" aria-live="polite"></p>
  <div class="grid" id="grid"></div>
  <p class="empty" id="empty" hidden>No looks match your current selection. Try a different search or adjust the filters.</p>
</div>
<div class="detail" id="detail" role="dialog" aria-modal="true" aria-labelledby="dTitle" hidden>
  <div class="detail-bar">
    <button class="btn small" id="dClose">← All Looks</button>
    <div class="detail-step"><button id="dPrev" aria-label="Previous look">←</button><span id="dIdx"></span><button id="dNext" aria-label="Next look">→</button></div>
  </div>
  <article class="detail-body" id="dBody" data-zoom-group></article>
</div>''')

# ---------------- HOW IT WORKS ----------------
PAGES['how-it-works.html']=('How It Works','How each look moves from a church’s architecture to a five-color palette to a contemporary outfit.','how',
head('II','How It Works','From Sacred Architecture to Personal Style',
 'Every look begins with a place. The architecture of a church, its materials, colors, and atmosphere, becomes the starting point for a contemporary wardrobe.',
 'These churches are sacred places before they are sources of inspiration. They were built for prayer and worship, and the looks here are a small tribute to their beauty, not a substitute for visiting them.')+f'''
<section class="wrap" aria-label="Three steps">
  <ol class="steps" role="list">
    <li class="step"><span class="n">01</span><h3>The Architecture</h3><p>Each look begins with a church. Its exterior and interior reveal a distinctive harmony of stone, stained glass, wood, metal, and ornament.</p></li>
    <li class="step"><span class="n">02</span><h3>The Palette</h3><p>Five colors are drawn from the building’s architectural character, capturing something of its atmosphere and visual identity.</p></li>
    <li class="step"><span class="n">03</span><h3>The Wardrobe</h3><p>Those colors become the inspiration for a contemporary outfit, bringing the beauty of sacred architecture into the art of everyday dress.</p></li>
  </ol>{HINT}
</section>
<section class="sec">
  <div class="wrap method">
    <figure id="methodFig"></figure>
    <div>
      <h2 style="margin:0 0 18px">How a Look Is Chosen</h2>
      <p>Each palette is measured from an exterior and an interior photograph, then checked by eye so it reflects the building’s real stone, glass, wood, and metal rather than the accident of a cloudy day or a camera’s color cast.</p>
      <p>The outfit is chosen first for its own beauty and good taste. A color-match score in each look shows how closely the clothes follow the palette, but it is a guide, not a verdict.</p>
      <p>Photographs of churches and clothing are used under Creative Commons licenses or are in the public domain, and every image is credited.</p>
      <div class="ctas"><a class="btn solid" href="lookbook.html">Explore the Lookbook</a></div>
    </div>
  </div>
</section>''')

# ---------------- LITURGICAL YEAR ----------------
PAGES['liturgical-year.html']=('The Liturgical Year','The colors of the Church’s liturgical seasons as a quiet source of inspiration for personal style.','ly',
head('III','The Liturgical Year','Dressing with the Seasons of the Church',
 'The Church marks the passage of the year through a changing language of color. Violet accompanies Advent and Lent, white and gold mark great celebrations, red recalls the Holy Spirit and the witness of the martyrs, and green characterizes Ordinary Time.')+f'''
<section class="wrap" aria-label="The seasons">
  <div class="seasons" id="seasonsGrid"></div>{HINT}
  <p class="season-note">The seasons above describe the colors of the Church’s liturgy. The wardrobe notes are optional suggestions for personal devotion, not rules of dress.</p>
</section>
<section class="sec">
  <div class="wrap feature-row">
    <figure class="zp" style="margin:0"><img data-zoom tabindex="0" role="button" data-cap="Basilica of Saint-Denis, interior" src="img/int/saint-denis.jpg" alt="The Rayonnant nave of the Basilica of Saint-Denis with its stained glass" style="width:100%;aspect-ratio:4/3;object-fit:cover"></figure>
    <div class="read">
      <p class="lede">These colors belong first to the Church’s liturgical worship, but they can also provide a quiet source of inspiration for personal style. A tie, a scarf, or a carefully chosen accessory can acknowledge the rhythm of the Christian year without turning the wardrobe into an extension of the sanctuary.</p>
      <p class="lede">Mary Harper’s <em>Liturgical Style</em> explores this relationship between clothing, the Church calendar, and the habits of everyday life.</p>
      <div class="ctas"><a class="btn" href="https://liturgicalstyle.com" target="_blank" rel="noopener">Explore Liturgical Style</a></div>
    </div>
  </div>
</section>''')

# ---------------- BEAUTY & FAITH ----------------
PAGES['beauty-and-faith.html']=('Beauty &amp; Faith','What the popes and the Church have said about beauty, art, modesty, and dress.','bf',f'''
<figure class="nave-band">
  <img data-zoom tabindex="0" role="button" data-cap="Basilica of St. Paul Outside the Walls, Rome" src="img/art/san-paolo-nave.jpg" width="1920" height="1032" decoding="async" alt="The long colonnaded nave of the Basilica of St. Paul Outside the Walls, with the apse mosaic at the far end">
  <figcaption><div><h1>The Way of Beauty</h1></div><small>St. Paul Outside the Walls, Rome. {cr('sp')}</small></figcaption>
</figure>
<div class="wrap page-head" style="padding-top:clamp(40px,6vw,80px)">
  <div class="intro">
    <div class="read"><p class="lede">The Christian tradition has long recognized beauty as a means of awakening the human person to truth and goodness. From the architecture of great churches to the dignity of the human body, beauty has a place in the Church’s understanding of creation, worship, and everyday life.</p>
    <p class="lede">The Latin expression <em>via pulchritudinis</em>, or “way of beauty,” gives this journal its name. It also provides a broader framework for considering how we dress, how we present ourselves, and how the material world can reflect something of the dignity of the human person.</p></div>
    <div class="read"><p class="lede">Clothing occupies a modest but meaningful place in the wider human experience of beauty. Through color, proportion, material, and craftsmanship, it can express personality, cultural inheritance, and respect for an occasion. The Church’s artistic tradition offers a rich source of inspiration for this everyday art, without prescribing a particular fashion or aesthetic.</p>
    <p class="lede">The phrase became a pastoral program in 2006, when the Pontifical Council for Culture proposed beauty as a path toward God in <a class="link" href="https://www.vatican.va/roman_curia/pontifical_councils/cultr/documents/rc_pc_cultr_doc_20060327_plenary-assembly_final-document_en.html" target="_blank" rel="noopener"><em>The Via Pulchritudinis, Privileged Pathway for Evangelisation and Dialogue</em></a>.</p></div>
  </div>
</div>
<section class="sec" style="padding-top:0" aria-labelledby="popes-h">
  <div class="wrap">
    <div class="sec-h"><div><h2 id="popes-h">The Popes on Beauty</h2></div><p>Across generations, the popes have spoken of beauty as an expression of human creativity, a reflection of truth, and a means of drawing the human heart toward God.</p></div>
    {P('_popes.html')}{HINT}
  </div>
</section>
<section class="sec" aria-labelledby="dress-h">
  <div class="wrap">
    <div class="sec-h"><div><h2 id="dress-h">The Church on Dress</h2></div><p>Six passages from the Catechism, the Council, and St. John Paul II on modesty, reverence, the body, and noble beauty. Open each to read it.</p></div>
    <div class="teach">{P('_teach.html')}</div>
  </div>
</section>''')

# ---------------- FRASSATI ----------------
PAGES['st-pier-giorgio.html']=('St. Pier Giorgio Frassati','St. Pier Giorgio Frassati on personal style, simplicity, and generosity, with perspectives from the National Catholic Register.','fr',f'''
<div class="wrap page-head">
  <div class="fr-top">
    <figure class="fr-art"><div class="im zp"><img data-zoom tabindex="0" role="button" data-cap="Fra Angelico, Crucifixion with St. Dominic, Convent of San Marco, Florence" src="img/art/fra-angelico-st-dominic.jpg" width="420" height="795" alt="Detail of Fra Angelico’s fresco of St. Dominic kneeling at the foot of the Cross"></div>
      <figcaption>Fra Angelico, <em>Crucifixion with St. Dominic</em>, Convent of San Marco, Florence. Frassati was a lay Dominican.<br><span class="cr">{cr('fa')}</span></figcaption></figure>
    <div>
      <h1>A Life of Faith, Friendship, and Generosity</h1>
      <p class="dates">St. Pier Giorgio Frassati, 1901–1925. Canonized September 7, 2025.</p>
      <div class="read">
        <p class="lede">St. Pier Giorgio Frassati belonged to one of Turin’s most prominent families, yet his life was distinguished by an extraordinary generosity toward the poor and a profound devotion to Christ.</p>
        <p class="lede">Photographs of the young saint reveal a man equally at ease in tailored suits, university attire, and the practical clothing of a mountaineer. His sense of style reflected the conventions of his time and social circumstances, but his attachment to material possessions was remarkably slight. He gave clothing and shoes to those in need, continued wearing garments that had been repaired repeatedly, and placed the needs of others before his own comfort.</p>
        <p class="lede">Frassati’s example offers a compelling perspective on the relationship between personal style and Christian virtue. His elegance was compatible with simplicity, his social standing with humility, and his appreciation for appropriate dress with a freedom from material possessions.</p>
        <p class="lede">In August 2025, Andrew Likoudis explored this dimension of Frassati’s life for the <em>National Catholic Register</em>, drawing on interviews with Catholic designers, writers, and advocates who reflected on the spiritual significance of his wardrobe.</p>
        <div class="ctas"><a class="btn" href="https://www.ncregister.com/features/frassati-tailored-for-holiness" target="_blank" rel="noopener">Read “Patron Saint of Fashion?” in the Register</a></div>
      </div>
      {P('_themes.html')}{HINT}
    </div>
  </div>
</div>
<section class="sec" style="padding-top:0" aria-labelledby="voices-h">
  <div class="wrap">
    <div class="sec-h"><div><h2 id="voices-h">Perspectives on Frassati</h2></div><p>Six people interviewed for the <em>Register</em> on what his clothing reveals about his character. Quotations are reproduced as published.</p></div>
    {P('_fqs.html')}{HINT}
  </div>
</section>''')

# ---------------- DIRECTORY ----------------
PAGES['directory.html']=('The Directory','Catholic designers, stylists, publications, and books on faith, beauty, and everyday life.','dir',
head('VI','The Directory','People, Books, and Ideas Worth Discovering',
 'A curated selection of designers, stylists, writers, publications, and books exploring the relationship between Catholic faith, beauty, and everyday life.',
 'Some approach the subject through clothing and craftsmanship. Others begin with theology, the home, the liturgical year, or the example of the saints.')+f'''
<section class="wrap" aria-label="Directory">
  <div class="sub-h"><h2>Makers and Stylists</h2><p>Designers and stylists making clothing with Catholic faith in mind.</p></div>
  <div class="makers">{P('_makers.html')}</div>{HINT}
  <div class="sub-h"><h2>Writing and Culture</h2><p>Publications and apostolates on faith, beauty, and everyday life.</p></div>
  <div class="makers">{P('_culture.html')}</div>{HINT}
  <div class="sub-h" id="library"><h2>The Library</h2><p>A reading list on the theology of beauty, the dignity of the human person, Catholic culture, and personal style.</p></div>
  <div class="shelf">{P('_books.html')}</div>
</section>''')

# ---------------- CREDITS ----------------
artp=''.join(f'<p><b>{ART[k][0]}.</b> {cr(k)}.</p>' for k in ('nd','sp','fa'))
PAGES['sources-and-credits.html']=('Sources &amp; Credits','Primary sources and photo credits for Via Pulchritudinis.','credits',
head('','Sources &amp; Credits','Sources and Credits','Primary sources quoted in the journal, and the photographers whose work appears here under Creative Commons licenses or in the public domain.').replace('<span class="label no"> · ','<span class="label no">')+f'''
<section class="wrap" aria-label="Sources">
  <div class="sub-h"><h2>Primary Sources</h2></div>
  {P('_src.html')}
  <div class="sub-h"><h2>Photo Credits</h2><p>Brand names belong to their owners.</p></div>
  <div id="artCredits" hidden>{artp}</div>
  <div class="photo-credits" id="photoCredits"></div>
</section>''')

for fname,(title,desc,page,body) in PAGES.items():
    open(os.path.join(ROOT,fname),'w').write(layout(fname,title,desc,body,page))
print('built',len(PAGES),'pages')
