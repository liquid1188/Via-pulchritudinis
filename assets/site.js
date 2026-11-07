/* Via Pulchritudinis shared script. Each block runs only when its elements are on the page. */
(function(){
const $=id=>document.getElementById(id);
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const L=window.LOOKS||[];
const WHO={her:'Women',him:'Men'};
function credit(m,label){if(!m)return'';const by=m.creator?(m.creator_url?'<a href="'+esc(m.creator_url)+'" target="_blank" rel="noopener">'+esc(m.creator)+'</a>':esc(m.creator)):'an unnamed photographer';const l=(m.license||'').toLowerCase();const lic=l==='pdm'?'Public domain':(l==='cc0'?'CC0':'CC '+esc(l.toUpperCase())+' '+esc(m.license_version||''));return (label?label+' by ':'Photo by ')+by+' · <a href="'+esc(m.license_url||'#')+'" target="_blank" rel="noopener">'+lic+'</a> · <a href="'+esc(m.landing||'#')+'" target="_blank" rel="noopener">source</a>'}
const sm=src=>src.replace(/^img\/(ext|look)\//,'img/sm/$1/');
const dim=m=>m&&m.w?' width="'+m.w+'" height="'+m.h+'"':'';
const strip=l=>l.palette.map(p=>'<i style="background:'+p.h+'"></i>').join('');
const PERIODS=["Early Christian and Byzantine","Romanesque","Gothic","Renaissance and Baroque","Neoclassical and Revival","Modern"];
const PERIOD_OF={ecb:"st-paul-outside maria-maggiore lateran pantheon st-marks monreale",rom:"trastevere pisa santiago vezelay",got:"minerva florence siena orvieto milan assisi notre-dame-paris saint-denis chartres reims seville toledo burgos cologne vienna st-vitus",ren:"st-peters santa-maria-popolo mexico-city st-louis-nola estrela bom-jesus",neo:"baltimore st-peter-chains st-paul-mn yamoussoukro national-shrine sacre-coeur westminster-cathedral st-louis-basilica lourdes st-patricks sacred-heart-nd notre-dame-montreal madeleine manila las-lajas",mod:"christ-cathedral brasilia sagrada"};
const PK=["ecb","rom","got","ren","neo","mod"];
L.forEach(l=>{const k=PK.find(k=>PERIOD_OF[k].split(' ').includes(l.id));l.period=k?PERIODS[PK.indexOf(k)]:'Other'});
let tt;function toast(m){const t=$('toast');if(!t)return;t.textContent=m;t.classList.add('on');clearTimeout(tt);tt=setTimeout(()=>t.classList.remove('on'),1600)}

/* ---------- desktop or mobile view ---------- */
const small=Math.min(screen.width,screen.height)<760;
const root=document.documentElement;
if(small)root.classList.add('vp-small');
let desk=false;try{desk=localStorage.getItem('vp-desktop')==='1'}catch(e){}
if(desk)root.classList.add('vp-desktop');
document.querySelectorAll('.vp-toggle,.vp-back').forEach(b=>{
 b.textContent=desk?'View mobile version':'View desktop version';
 b.addEventListener('click',()=>{try{desk?localStorage.removeItem('vp-desktop'):localStorage.setItem('vp-desktop','1')}catch(e){}
  const m=document.querySelector('meta[name=viewport]');m.setAttribute('content',desk?'width=device-width, initial-scale=1':'width=1280');location.reload()})});

/* ---------- menu ---------- */
const btn=document.querySelector('.menu-btn'),nav=$('nav');
if(btn&&nav){
 const setOpen=o=>{nav.classList.toggle('open',o);btn.setAttribute('aria-expanded',o);btn.firstChild.textContent=o?'Close':'Menu';document.body.classList.toggle('locked',o)};
 btn.addEventListener('click',()=>setOpen(!nav.classList.contains('open')));
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){setOpen(false);btn.focus()}});
}

/* ---------- photo viewer: every photo opens full and uncropped ---------- */
const lb=$('lb'),lbImg=$('lbImg');let lbSet=[],lbI=0,lbFrom=null;
function lbCredit(im){if(im.dataset.credit)return im.dataset.credit;const c=im.closest('figure');const s=c&&c.querySelector('small,.cr');return s?s.innerHTML:''}
function lbShow(i){lbI=(i+lbSet.length)%lbSet.length;const im=lbSet[lbI];lbImg.src=(im.dataset.full||im.currentSrc||im.src).replace('/img/sm/','/img/');lbImg.alt=im.alt;$('lbCap').textContent=im.dataset.cap||im.alt;$('lbCredit').innerHTML=lbCredit(im);$('lbN').textContent=lbSet.length>1?(lbI+1)+' of '+lbSet.length:'';$('lbP').hidden=$('lbNx').hidden=lbSet.length<2}
function lbOpen(im){const g=im.closest('[data-zoom-group]');lbSet=g?[...g.querySelectorAll('img[data-zoom]')]:[im];lbFrom=document.activeElement;lb.hidden=false;document.body.classList.add('locked');lbShow(lbSet.indexOf(im));$('lbX').focus({preventScroll:true})}
function lbClose(){lb.hidden=true;const d=$('detail');if(!d||d.hidden)document.body.classList.remove('locked');if(lbFrom&&document.contains(lbFrom))lbFrom.focus({preventScroll:true})}
if(lb){
 document.addEventListener('click',e=>{const im=e.target.closest('img[data-zoom]');if(im&&!lb.contains(im)){e.preventDefault();e.stopPropagation();lbOpen(im)}},true);
 document.addEventListener('keydown',e=>{const im=e.target.closest&&e.target.closest('img[data-zoom]');if(im&&(e.key==='Enter'||e.key===' ')){e.preventDefault();lbOpen(im)}});
 $('lbX').onclick=lbClose;$('lbP').onclick=()=>lbShow(lbI-1);$('lbNx').onclick=()=>lbShow(lbI+1);
 lb.addEventListener('click',e=>{if(e.target===lb||e.target.tagName==='FIGURE')lbClose()});
 window.addEventListener('keydown',e=>{if(lb.hidden)return;e.stopImmediatePropagation();if(e.key==='Escape')lbClose();else if(e.key==='ArrowRight')lbShow(lbI+1);else if(e.key==='ArrowLeft')lbShow(lbI-1);else if(e.key==='Tab'){const f=[...lb.querySelectorAll('button')].filter(b=>!b.hidden);const i=f.indexOf(document.activeElement);e.preventDefault();f[(i+(e.shiftKey?-1:1)+f.length)%f.length].focus()}},true);
 let tx=null;lbImg.addEventListener('touchstart',e=>{tx=e.touches[0].clientX},{passive:true});lbImg.addEventListener('touchend',e=>{if(tx===null)return;const dx=e.changedTouches[0].clientX-tx;if(Math.abs(dx)>50)lbShow(lbI+(dx<0?1:-1));tx=null});
}

/* ---------- home: featured triptych and lookbook rail ---------- */
if($('trip')&&L.length){
 const FEAT=L.map((l,i)=>i).filter(i=>L[i].featured).concat(L.map((l,i)=>i)).filter((v,i,a)=>a.indexOf(v)===i).slice(0,6);
 let ti=0,timer;const dots=$('tDots');
 FEAT.forEach((k,j)=>{const b=document.createElement('button');b.type='button';b.setAttribute('aria-label','Show '+L[k].name);b.onclick=()=>{showTrip(j);restart()};dots.appendChild(b)});
 function showTrip(j){ti=j;const l=L[FEAT[j]];
  const set=(id,m,alt)=>{const im=$(id);im.dataset.cap=alt;im.dataset.credit=credit(m);im.style.opacity=0;setTimeout(()=>{im.onload=()=>im.style.opacity=1;im.src=m.src;im.alt=alt},180)};
  set('tExt',l.exterior,l.name+', exterior');set('tLook',l.look,l.look.title+', a look inspired by '+l.name);set('tInt',l.interior,l.name+', interior');
  $('tBar').innerHTML=strip(l);$('tTitle').textContent=l.name;$('tSub').textContent=l.place+' · '+l.look.title;$('tOpen').href='lookbook.html#'+l.id;
  [...dots.children].forEach((b,k)=>b.setAttribute('aria-current',k===j))}
 function restart(){clearInterval(timer);if(!matchMedia('(prefers-reduced-motion: reduce)').matches)timer=setInterval(()=>showTrip((ti+1)%FEAT.length),6500)}
 const trip=$('trip');['mouseenter','focusin','touchstart'].forEach(ev=>trip.addEventListener(ev,()=>clearInterval(timer),{passive:true}));['mouseleave','focusout'].forEach(ev=>trip.addEventListener(ev,restart));
 showTrip(0);restart();
}
if($('homeRail')&&L.length){
 const pick=['siena','st-marks','florence','national-shrine','saint-denis','vezelay','orvieto','las-lajas'];
 $('homeRail').innerHTML=pick.map(id=>L.find(l=>l.id===id)).filter(Boolean).map(l=>'<a class="mini-look" href="lookbook.html#'+l.id+'"><div class="ph"><span><img loading="lazy" src="'+sm(l.exterior.src)+'" alt=""></span><span class="lk"><img loading="lazy" src="'+sm(l.look.src)+'" alt=""></span></div><div class="strip" aria-hidden="true">'+strip(l)+'</div><h3>'+esc(l.name)+'</h3><p>'+esc(l.place)+' · <i>'+esc(l.look.title)+'</i></p></a>').join('');
}
if($('methodFig')&&L.length){const l=L.find(x=>x.id==='siena')||L[0];$('methodFig').innerHTML='<div class="ph" data-zoom-group><span><img data-zoom tabindex="0" role="button" data-cap="'+esc(l.name)+', exterior" data-credit="'+esc(credit(l.exterior))+'" src="'+l.exterior.src+'" alt="'+esc(l.name)+', exterior"></span><span class="chips" aria-hidden="true">'+strip(l)+'</span><span><img data-zoom tabindex="0" role="button" data-cap="'+esc(l.look.title)+'" data-credit="'+esc(credit(l.look))+'" src="'+l.look.src+'" style="object-position:center 22%" alt="'+esc(l.look.title)+'"></span></div><figcaption>'+esc(l.name)+', its palette, and '+esc(l.look.title)+'. <a class="link" href="lookbook.html#'+l.id+'">See the full look</a></figcaption>'}

/* ---------- lookbook ---------- */
const grid=$('grid');
if(grid){
 const FAM=[["blue","#2D6A8C","Blues and greens"],["red","#9E2430","Reds and pinks"],["gold","#C49A3E","Golds and browns"],["neutral","#D8CBB2","Light neutrals"],["dark","#24211E","Darks"]];
 const styleF=$('styleF'),regionF=$('regionF'),colorF=$('colorF'),qEl=$('q'),clearF=$('clearF'),rc=$('resultCount'),colorName=$('colorName');
 styleF.innerHTML='<option>All styles</option>'+PERIODS.filter(p=>L.some(l=>l.period===p)).map(p=>'<option>'+esc(p)+'</option>').join('');
 regionF.innerHTML=["All regions"].concat([...new Set(L.map(l=>l.region))]).map(r=>'<option>'+esc(r)+'</option>').join('');
 colorF.innerHTML='<button type="button" class="all" aria-pressed="true" data-v="all">Any color</button>'+FAM.map(f=>'<button type="button" aria-pressed="false" data-v="'+f[0]+'" style="background:'+f[1]+'" title="'+f[2]+'" aria-label="'+f[2]+'"></button>').join('');
 let fWho='all',fCol='all';
 grid.innerHTML=L.map((l,i)=>'<button type="button" class="card" data-i="'+i+'" aria-label="Explore this look, '+esc(l.look.title)+', inspired by '+esc(l.name)+', '+esc(l.place)+'"><div class="ph"><span class="ch"><img loading="lazy" decoding="async" src="'+sm(l.exterior.src)+'"'+dim(l.exterior)+' alt=""></span><span class="lk"><img loading="lazy" decoding="async" src="'+sm(l.look.src)+'"'+dim(l.look)+' alt=""><span class="tag">'+WHO[l.who]+'</span></span></div><div class="strip" aria-hidden="true">'+strip(l)+'</div><h3>'+esc(l.name)+'</h3><span class="pl">'+esc(l.place)+'</span><span class="lt">'+esc(l.look.title)+'</span></button>').join('');
 let VIS=L.map((l,i)=>i);
 function filter(){const q=qEl.value.trim().toLowerCase(),r=regionF.value,st=styleF.value;let n=0;VIS=[];
  [...grid.children].forEach(el=>{const l=L[+el.dataset.i];const ok=(fWho==='all'||l.who===fWho)&&(fCol==='all'||l.families.includes(fCol))&&(r==='All regions'||l.region===r)&&(st==='All styles'||l.period===st)&&(!q||(l.name+' '+l.place+' '+l.city+' '+l.region+' '+l.style+' '+l.look.title).toLowerCase().includes(q));el.hidden=!ok;if(ok){n++;VIS.push(+el.dataset.i)}});
  rc.textContent=n+(n===1?' look':' looks');$('empty').hidden=n>0;
  const fam=FAM.find(f=>f[0]===fCol);colorName.textContent=fam?fam[2]:'Any color';
  const active=(fCol!=='all')+(r!=='All regions')+(st!=='All styles')+(!!q);
  clearF.disabled=(fWho==='all'&&!active);$('fCount').textContent=active?' ('+active+')':''}
 const press=(g,b)=>[...g.children].forEach(x=>x.setAttribute('aria-pressed',x===b));
 $('segWho').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;fWho=b.dataset.v;press(b.parentNode,b);filter()});
 colorF.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;fCol=b.dataset.v;press(colorF,b);filter()});
 regionF.onchange=filter;styleF.onchange=filter;qEl.oninput=filter;
 clearF.onclick=()=>{fWho='all';fCol='all';qEl.value='';regionF.value='All regions';styleF.value='All styles';press($('segWho'),document.querySelector('#segWho [data-v=all]'));press(colorF,colorF.querySelector('[data-v=all]'));filter()};
 $('fToggle').onclick=()=>{const o=$('filters').classList.toggle('open');$('fToggle').setAttribute('aria-expanded',o)};
 filter();
 grid.addEventListener('click',e=>{const c=e.target.closest('.card');if(c)openDetail(+c.dataset.i)});

 /* look view */
 const detail=$('detail'),dBody=$('dBody');let cur=-1,lastFocus=null;
 const makers=who=>who==='her'?'<a class="link" href="https://www.litanynyc.com" target="_blank" rel="noopener">Litany NYC</a><a class="link" href="https://urbansophisticatecollective.com" target="_blank" rel="noopener">The Urban Sophisticate Collective</a><a class="link" href="https://liturgicalstyle.com" target="_blank" rel="noopener">Liturgical Style</a>':'<a class="link" href="https://catholicmensshop.com" target="_blank" rel="noopener">Catholic Men’s Shop</a><a class="link" href="https://catholicgentleman.com" target="_blank" rel="noopener">The Catholic Gentleman</a><a class="link" href="https://urbansophisticatecollective.com" target="_blank" rel="noopener">The Urban Sophisticate Collective</a>';
 const seq=()=>VIS.includes(cur)&&VIS.length?VIS:L.map((l,i)=>i);
 function step(d){const S=seq();const k=S.indexOf(cur);openDetail(S[(k+d+S.length)%S.length])}
 function openDetail(i,noPush){cur=(i+L.length)%L.length;const l=L[cur];if(detail.hidden)lastFocus=document.activeElement;
  dBody.innerHTML='<div class="trio"><figure class="t-ch"><div class="ph zp"><img data-zoom tabindex="0" role="button" data-cap="'+esc(l.name)+', exterior" data-credit="'+esc(credit(l.exterior))+'" src="'+l.exterior.src+'"'+dim(l.exterior)+' alt="'+esc(l.name)+', exterior"></div><figcaption class="label">The Church</figcaption></figure><figure class="t-pal"><div class="chips" aria-hidden="true">'+strip(l)+'</div><figcaption class="label">The Palette</figcaption></figure><figure class="t-lk"><div class="ph zp"><img data-zoom tabindex="0" role="button" data-cap="'+esc(l.look.title)+', inspired by '+esc(l.name)+'" data-credit="'+esc(credit(l.look))+'" src="'+l.look.src+'"'+dim(l.look)+' alt="'+esc(l.look.title)+'. '+esc(l.look.wear)+'"></div><figcaption class="label">The Look</figcaption></figure></div>'+
  '<p class="credit t-credit">'+credit(l.exterior,'Exterior photo')+'<br>'+credit(l.look,'Look photo')+'</p>'+
  '<div class="d-read"><div class="d-info">'+
   '<span class="label kicker">'+WHO[l.who]+' · '+esc(l.period)+'</span><h2 id="dTitle">'+esc(l.name)+'</h2><p class="label place">'+esc(l.place)+' · '+esc(l.style)+' · '+esc(l.year)+'</p><p class="story">'+esc(l.story)+'</p>'+
   '<figure class="d-int"><div class="ph zp"><img data-zoom tabindex="0" role="button" data-cap="'+esc(l.name)+', interior" data-credit="'+esc(credit(l.interior))+'" loading="lazy" src="'+l.interior.src+'"'+dim(l.interior)+' alt="'+esc(l.name)+', interior"></div><figcaption class="credit"><span class="label">Interior</span> · '+credit(l.interior,'Photo')+'</figcaption></figure>'+
   '<div class="d-sec"><span class="label">The Palette</span><div class="palette">'+l.palette.map(p=>'<button type="button" class="sw" data-hex="'+p.h+'" aria-label="Copy '+esc(p.n)+', '+p.h+'"><i style="background:'+p.h+'"></i><b>'+esc(p.n)+'</b><small>'+p.h+'</small></button>').join('')+'</div><p class="tip">Five colors measured from the exterior and interior photographs. Select a color to copy its value.</p></div>'+
   '<div class="d-sec"><span class="label">The Look</span><h3>'+esc(l.look.title)+'</h3><p class="wear">'+esc(l.look.wear)+'</p></div>'+
   '<div class="d-sec"><span class="label">Architectural Inspiration</span><p class="insp">'+esc(l.inspiration||'')+'</p></div>'+
   '<details class="analysis"><summary><span class="label">Color analysis</span><b>'+l.score+'% palette match</b></summary><div class="inner">'+l.matches.map(m=>'<div class="mrow"><i style="background:'+m.g+'"></i><span>'+esc(m.gl)+'</span><span aria-hidden="true">→</span><i style="background:'+m.p+'"></i><span>'+esc(m.pn)+'</span></div>').join('')+'<p class="tip">Left, colors measured from the outfit photo. Right, the closest color in the church’s palette. The score is a guide, not a verdict on the look.</p></div></details>'+
   '<div class="d-shop"><p>Find pieces like these from Catholic makers.</p><div class="links">'+makers(l.who)+'</div></div>'+
  '</div></div>';
  {const S=seq();$('dIdx').textContent=(S.indexOf(cur)+1)+' of '+S.length}
  detail.hidden=false;document.body.classList.add('locked');detail.scrollTop=0;
  if(!noPush){try{history.replaceState(null,'','#'+l.id)}catch(e){}}
  $('dClose').focus({preventScroll:true})}
 function closeDetail(){detail.hidden=true;document.body.classList.remove('locked');try{history.replaceState(null,'',location.pathname)}catch(e){};if(lastFocus&&document.contains(lastFocus))lastFocus.focus({preventScroll:true})}
 $('dClose').onclick=closeDetail;$('dPrev').onclick=()=>step(-1);$('dNext').onclick=()=>step(1);
 document.addEventListener('keydown',e=>{if(detail.hidden)return;
  if(e.key==='Escape')closeDetail();
  if(e.key==='ArrowRight'&&!e.target.closest('summary'))step(1);
  if(e.key==='ArrowLeft'&&!e.target.closest('summary'))step(-1);
  if(e.key==='Tab'){const f=[...detail.querySelectorAll('a[href],button,summary,[tabindex="0"]')].filter(x=>x.offsetParent!==null);if(!f.length)return;const a=f[0],z=f[f.length-1];if(e.shiftKey&&document.activeElement===a){e.preventDefault();z.focus()}else if(!e.shiftKey&&document.activeElement===z){e.preventDefault();a.focus()}}});
 dBody.addEventListener('click',e=>{const sw=e.target.closest('.sw');if(sw){const h=sw.dataset.hex;try{navigator.clipboard.writeText(h).then(()=>toast(h+' copied'),()=>toast(h))}catch(err){toast(h)}}});
 const route=()=>{const id=location.hash.slice(1);const i=L.findIndex(l=>l.id===id);if(i>=0)openDetail(i,true);else if(!detail.hidden)closeDetail()};
 window.addEventListener('hashchange',route);route();
}

/* ---------- liturgical seasons ---------- */
if($('seasonsGrid')){
 const S=[["Advent","#4B2E6B","Violet and blue-violet","Watchful, quiet tones. Plum knits, a violet scarf, and on Gaudete Sunday a touch of rose."],["Christmas","#F4EEDF","White and gold","Ivory, cream, and gold jewelry from the Nativity through the Baptism of the Lord."],["Ordinary Time","#3F6B47","Green","The long green season of growth. Olive, sage, and forest for everyday wear."],["Lent","#5A3A63","Violet","Penitential and plain. Fewer pieces, darker tones, and rose on Laetare Sunday."],["Easter","#F7F2E4","White and gold","Fifty days of light. Whites, creams, and spring brightness."],["Pentecost & Martyrs","#A1252F","Red","The fire of the Spirit and the blood of witnesses. A red tie, a red lip, a red lining."]];
 $('seasonsGrid').innerHTML=S.map(s=>{const light=['#F4EEDF','#F7F2E4'].includes(s[1]);return '<div class="season"><div class="bar" style="background:'+s[1]+(light?';box-shadow:inset 0 -10px 0 #C2A162':'')+'" aria-hidden="true"></div><div class="txt"><span class="label">'+esc(s[2])+'</span><h3>'+esc(s[0])+'</h3><p>'+esc(s[3])+'</p></div></div>'}).join('');
}

/* ---------- photo credits ---------- */
if($('photoCredits')){
 const art=[...document.querySelectorAll('#artCredits p')].map(p=>p.outerHTML).join('');
 $('photoCredits').innerHTML=art+L.map(l=>'<p><b>'+esc(l.name)+'.</b> '+credit(l.look,'Look')+'. '+credit(l.exterior,'Exterior')+'. '+credit(l.interior,'Interior')+'.</p>').join('');
}

/* ---------- old single-page links ---------- */
if(document.body.dataset.page==='home'&&location.hash){
 const h=location.hash.slice(1);const map={lookbook:'lookbook.html',how:'how-it-works.html','liturgical-year':'liturgical-year.html','beauty-faith':'beauty-and-faith.html',frassati:'st-pier-giorgio.html',directory:'directory.html',library:'directory.html#library',credits:'sources-and-credits.html'};
 if(map[h])location.replace(map[h]);else if(L.some(l=>l.id===h))location.replace('lookbook.html#'+h);
}
window.VP={toast};
})();
