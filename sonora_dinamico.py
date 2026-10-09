from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os
from urllib.parse import urlparse, parse_qs, urlencode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import json

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", "5000"))

SEED_TRACKS = [
    {'trackId': -1, 'trackName': 'Miopia', 'artistName': 'SóCiro', 'primaryGenreName': 'BR alternativo', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -2, 'trackName': 'Três da Madrugada', 'artistName': 'Iago O Próprio', 'primaryGenreName': 'BR alternativo', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -3, 'trackName': 'AmarElo', 'artistName': 'Emicida, Majur & Pabllo Vittar', 'primaryGenreName': 'Rap / R&B', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -4, 'trackName': 'Pupila', 'artistName': 'ANAVITÓRIA & Vitor Kley', 'primaryGenreName': 'Pop', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -5, 'trackName': 'Velha Infância', 'artistName': 'Tribalistas', 'primaryGenreName': 'BR alternativo', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -6, 'trackName': 'Do I Wanna Know?', 'artistName': 'Arctic Monkeys', 'primaryGenreName': 'Rock', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -7, 'trackName': '505', 'artistName': 'Arctic Monkeys', 'primaryGenreName': 'Indie / Alt', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -8, 'trackName': 'Sweater Weather', 'artistName': 'The Neighbourhood', 'primaryGenreName': 'Indie / Alt', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -9, 'trackName': 'The Night We Met', 'artistName': 'Lord Huron', 'primaryGenreName': 'Indie / Alt', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -10, 'trackName': 'After Dark', 'artistName': 'Mr.Kitty', 'primaryGenreName': 'Indie / Alt', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -11, 'trackName': 'good 4 u', 'artistName': 'Olivia Rodrigo', 'primaryGenreName': 'Pop', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -12, 'trackName': 'Ocean Eyes', 'artistName': 'Billie Eilish', 'primaryGenreName': 'Pop', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -13, 'trackName': 'Snooze', 'artistName': 'SZA', 'primaryGenreName': 'Rap / R&B', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -14, 'trackName': 'Redbone', 'artistName': 'Childish Gambino', 'primaryGenreName': 'Rap / R&B', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -15, 'trackName': 'Céu Azul', 'artistName': 'Charlie Brown Jr.', 'primaryGenreName': 'Rock', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -16, 'trackName': 'Só os Loucos Sabem', 'artistName': 'Charlie Brown Jr.', 'primaryGenreName': 'Rock', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -17, 'trackName': 'Velha Roupa Colorida', 'artistName': 'Belchior', 'primaryGenreName': 'BR alternativo', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -18, 'trackName': 'Dois Rios', 'artistName': 'Skank', 'primaryGenreName': 'Rock', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -19, 'trackName': 'Space Song', 'artistName': 'Beach House', 'primaryGenreName': 'Indie / Alt', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -20, 'trackName': 'A Noite', 'artistName': 'Tiê', 'primaryGenreName': 'BR alternativo', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -21, 'trackName': 'R U Mine?', 'artistName': 'Arctic Monkeys', 'primaryGenreName': 'Indie / Alt', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -22, 'trackName': 'Little Dark Age', 'artistName': 'MGMT', 'primaryGenreName': 'Indie / Alt', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -23, 'trackName': 'Idiota', 'artistName': 'Jão', 'primaryGenreName': 'Pop', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
    {'trackId': -24, 'trackName': 'Amarelo, Azul e Branco', 'artistName': 'ANAVITÓRIA', 'primaryGenreName': 'Pop', 'collectionName': 'Catálogo inicial', 'artworkUrl100': '', 'previewUrl': '', 'trackViewUrl': ''},
]

HTML = r'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SONORA — Music Discovery Lab</title>
<style>
:root{color-scheme:dark;--bg:#0b0a12;--panel:#14121f;--panel2:#1b1829;--text:#f8f5ff;--muted:#a49bb8;--line:#2a253b;--purple:#a78bfa;--pink:#f472b6;--green:#86efac}*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at 75% -15%,#a78bfa28,transparent 38%),radial-gradient(ellipse at -10% 30%,#f472b615,transparent 32%),var(--bg);color:var(--text);font-family:Inter,system-ui,Segoe UI,sans-serif}.top{height:76px;border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;padding:0 clamp(18px,5vw,76px)}.brand{display:flex;gap:11px;align-items:center;font-weight:900;letter-spacing:.18em}.logo{width:38px;height:38px;border-radius:12px;background:linear-gradient(135deg,var(--purple),var(--pink));display:grid;place-items:center;color:#170f29;font-size:21px}.brand small{display:block;font-size:9px;letter-spacing:.22em;color:var(--muted);margin-top:3px}.status{font-size:12px;color:var(--muted)}main{max-width:1150px;margin:auto;padding:0 22px 45px}.hero{padding:55px 0 32px}.eyebrow{font-size:11px;letter-spacing:.2em;color:var(--purple);font-weight:800}.hero h1{font-size:clamp(42px,6vw,68px);letter-spacing:-.06em;line-height:1;margin:15px 0}.gradient{background:linear-gradient(100deg,#c4b5fd,#f9a8d4 58%,#67e8f9);background-clip:text;color:transparent}.hero p{color:var(--muted);font-size:14px;line-height:1.8;max-width:690px}.layout{display:grid;grid-template-columns:1.1fr .9fr;gap:18px;align-items:start}.panel{background:#14121fee;border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:0 18px 60px #0002}.head{padding:20px 21px 15px;display:flex;justify-content:space-between;align-items:center;gap:10px}.head h2{font-size:16px;margin:0}.sub{color:var(--muted);font-size:12px;margin-top:5px}.count{background:var(--panel2);border:1px solid var(--line);padding:6px 10px;border-radius:99px;color:var(--muted);font-size:11px;white-space:nowrap}.search{margin:0 18px 14px;display:flex;gap:10px;align-items:center;background:var(--panel2);border:1px solid var(--line);border-radius:12px;padding:0 13px}.search input{width:100%;background:none;border:0;outline:none;color:var(--text);padding:14px 0;font-size:13px}.actions{display:flex;gap:8px;margin:0 18px 14px}.btn{border:1px solid var(--line);background:var(--panel2);color:var(--text);border-radius:10px;padding:10px 13px;font-size:12px}.btn.main{background:linear-gradient(105deg,#c4b5fd,#f0abfc);color:#211331;border:0;font-weight:800}.btn:disabled{opacity:.45;cursor:not-allowed}.list{padding:0 10px 12px;display:grid;gap:5px}.track{display:grid;grid-template-columns:46px minmax(0,1fr) auto;gap:11px;align-items:center;padding:9px;border:1px solid transparent;border-radius:13px}.track:hover{background:var(--panel2)}.track.sel{background:#a78bfa13;border-color:#a78bfa55}.cover{width:46px;height:46px;object-fit:cover;border-radius:10px;background:linear-gradient(135deg,#4c3474,#182c49)}.name{font-size:13px;font-weight:750;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.artist{font-size:11px;color:var(--muted);margin-top:4px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.meta{font-size:10px;color:var(--muted);margin-top:5px}.add{width:32px;height:32px;border-radius:10px;border:1px solid var(--line);background:var(--panel);color:var(--muted);font-size:18px}.sel .add{background:var(--purple);color:#1a102c}.right{display:grid;gap:18px}.pad{padding:0 18px 18px}.empty{border:1px dashed var(--line);border-radius:14px;padding:22px 15px;text-align:center;color:var(--muted);font-size:12px;line-height:1.7}.picked{display:grid;gap:7px}.picked .track{background:var(--panel2);border:1px solid var(--line)}.remove{background:none;border:0;color:var(--muted);font-size:20px}.recs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;padding:0 15px 17px}.rec{border:1px solid var(--line);background:var(--panel2);border-radius:14px;padding:11px;min-width:0}.rec img{width:100%;aspect-ratio:1.8;object-fit:cover;border-radius:9px;background:#28213a}.rec h3{font-size:13px;margin:10px 0 4px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.rec .why{font-size:10px;color:var(--muted);line-height:1.5;min-height:30px;margin:8px 0}.rec audio{width:100%;height:32px;margin:5px 0}.small{font-size:10px;color:var(--green);font-weight:800}.notice{font-size:12px;color:var(--muted);padding:0 18px 16px;line-height:1.6}.footer{text-align:center;color:var(--muted);font-size:10px;margin-top:23px}.toast{position:fixed;bottom:20px;left:50%;transform:translate(-50%,20px);background:var(--text);color:var(--bg);padding:12px 18px;border-radius:12px;font-size:12px;opacity:0;transition:.2s;pointer-events:none}.toast.show{opacity:1;transform:translate(-50%,0)}@media(max-width:800px){.layout{grid-template-columns:1fr}.right{grid-row:1}.hero{padding-top:38px}}@media(max-width:480px){main{padding:0 12px 30px}.top{padding:0 13px}.status{font-size:10px}.recs{padding:0 10px 12px;gap:7px}.rec{padding:8px}.head{padding:16px}.hero h1{font-size:43px}}
</style></head><body><header class="top"><div class="brand"><div class="logo">♫</div><div>SONORA<small>MUSIC DISCOVERY LAB</small></div></div><div class="status">● Sem cadastro · Sem chave de API</div></header>
<main><section class="hero"><div class="eyebrow">✦ SUA PRÓXIMA OBSESSÃO COMEÇA AQUI</div><h1>Seu gosto tem<br>uma <span class="gradient">próxima faixa.</span></h1><p>Comece pelas 24 faixas do catálogo inicial ou pesquise músicas e artistas online. Selecione as que você ama e descubra outras parecidas.</p></section>
<div class="layout"><section class="panel"><div class="head"><div><h2>01 / Explore o catálogo</h2><div class="sub">24 faixas iniciais + catálogo online do iTunes.</div></div><span class="count" id="resultCount">Pronto</span></div><label class="search">⌕ <input id="query" placeholder="Ex.: SóCiro, Arctic Monkeys..." autocomplete="off"></label><div class="actions"><button class="btn main" id="searchBtn">Pesquisar músicas</button><button class="btn" id="popularBtn">Descobrir aleatórias</button></div><div class="list" id="results"><div class="empty">Carregando as 24 faixas iniciais…</div></div></section>
<div class="right"><section class="panel"><div class="head"><div><h2>02 / Seu mapa musical</h2><div class="sub">Selecione pelo menos 2 faixas.</div></div><span class="count" id="selectedCount">0 escolhidas</span></div><div class="pad"><div id="picked" class="empty">Suas referências escolhidas aparecerão aqui.</div><button class="btn main" id="recommendBtn" style="width:100%;margin-top:12px" disabled>✦ Encontrar próximas músicas</button></div></section><section class="panel"><div class="head"><div><h2>Seu perfil de escuta</h2><div class="sub">Artistas e estilos das suas escolhas.</div></div></div><div class="pad" id="profile"><div class="empty">Seu perfil aparece quando selecionar músicas.</div></div></section></div></div>
<section class="panel" style="margin-top:18px"><div class="head"><div><h2>03 / Recomendações para você</h2><div class="sub" id="recSubtitle">Resultados do catálogo online.</div></div><span class="count" id="recCount">0 sugestões</span></div><div class="recs" id="recs"><div class="empty" style="grid-column:1/-1">Suas recomendações vão aparecer aqui.</div></div><div class="notice">As prévias normalmente duram cerca de 30 segundos e não estão disponíveis para todas as faixas. A afinidade é uma estimativa baseada em artistas, gêneros e termos semelhantes — não é uma IA generativa.</div></section><div class="footer">SONORA · 24 faixas iniciais + catálogo online do iTunes/Apple.</div></main><div class="toast" id="toast"></div>
<script>
const $=s=>document.querySelector(s);const selected=new Map();let latest=[];let busy=false;
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
function cover(t){return t.artworkUrl100||''}function trackHTML(t){return `<div class="track ${selected.has(t.trackId)?'sel':''}"><img class="cover" src="${esc(cover(t))}" onerror="this.style.visibility='hidden'" alt=""><div><div class="name">${esc(t.trackName)}</div><div class="artist">${esc(t.artistName)}</div><div class="meta">${esc(t.primaryGenreName||'Gênero não informado')} · ${esc(t.collectionName||'')}</div></div><button class="add" data-add="${t.trackId}" title="Selecionar">${selected.has(t.trackId)?'✓':'+'}</button></div>`}
function renderResults(items){latest=items;$('#resultCount').textContent=items.length+' faixas';$('#results').innerHTML=items.map(trackHTML).join('')||'<div class="empty">Nenhuma faixa encontrada. Tente outro termo.</div>'}
function renderSelected(){const items=[...selected.values()];$('#selectedCount').textContent=items.length+' escolhida'+(items.length===1?'':'s');$('#recommendBtn').disabled=items.length<2;$('#picked').className=items.length?'picked':'empty';$('#picked').innerHTML=items.length?items.map(t=>`<div class="track"><img class="cover" src="${esc(cover(t))}" alt=""><div><div class="name">${esc(t.trackName)}</div><div class="artist">${esc(t.artistName)}</div></div><button class="remove" data-remove="${t.trackId}">×</button></div>`).join(''):'Suas referências escolhidas aparecerão aqui.';
const artists={};const genres={};items.forEach(t=>{artists[t.artistName]=(artists[t.artistName]||0)+1;const g=t.primaryGenreName||'Gênero não informado';genres[g]=(genres[g]||0)+1});const top=Object.entries(artists).sort((a,b)=>b[1]-a[1]).slice(0,4);const gs=Object.entries(genres).sort((a,b)=>b[1]-a[1]).slice(0,4);$('#profile').innerHTML=items.length?`<div class="sub">Artistas mais presentes</div><p>${top.map(x=>`<span class="count" style="display:inline-block;margin:4px 3px 0 0">${esc(x[0])} (${x[1]})</span>`).join('')}</p><div class="sub" style="margin-top:15px">Gêneros</div><p>${gs.map(x=>`<span class="count" style="display:inline-block;margin:4px 3px 0 0">${esc(x[0])} (${x[1]})</span>`).join('')}</p>`:'<div class="empty">Seu perfil aparece quando selecionar músicas.</div>';}
async function api(path,params={}){const u=new URL(path,location.origin);Object.entries(params).forEach(([k,v])=>u.searchParams.set(k,v));const r=await fetch(u);const d=await r.json();if(!r.ok)throw Error(d.error||'Erro na consulta');return d;}
async function search(q){if(busy)return;if(!q.trim()){toast('Digite uma música ou artista primeiro.');return}busy=true;$('#searchBtn').disabled=true;$('#results').innerHTML='<div class="empty">Buscando no catálogo online…</div>';try{const d=await api('/api/search',{term:q,limit:30});renderResults(d.results)}catch(e){$('#results').innerHTML=`<div class="empty">${esc(e.message)}<br>Confira sua conexão com a internet e tente novamente.</div>`}finally{busy=false;$('#searchBtn').disabled=false}}
async function popular(){if(busy)return;const terms=['indie alternativo','rock brasileiro','dream pop','rap brasileiro','indie pop','MPB','alternative rock','R&B'];await search(terms[Math.floor(Math.random()*terms.length)])}
async function recommend(){const items=[...selected.values()];if(items.length<2)return;const b=$('#recommendBtn');b.disabled=true;b.textContent='Analisando seu gosto…';$('#recs').innerHTML='<div class="empty" style="grid-column:1/-1">Buscando faixas parecidas…</div>';try{let queries=[];items.slice(0,5).forEach(t=>{queries.push(t.artistName);if(t.primaryGenreName)queries.push(t.primaryGenreName+' similar to '+t.artistName)});const unique=[...new Set(queries)].slice(0,5);const batches=await Promise.all(unique.map(q=>api('/api/search',{term:q,limit:25}).catch(()=>({results:[]}))));let all=batches.flatMap(x=>x.results);const ids=new Set(items.map(t=>t.trackId));all=all.filter(t=>!ids.has(t.trackId));const artistCounts={};const genreCounts={};items.forEach(t=>{artistCounts[t.artistName]=(artistCounts[t.artistName]||0)+1;if(t.primaryGenreName)genreCounts[t.primaryGenreName]=(genreCounts[t.primaryGenreName]||0)+1});const words=items.map(t=>t.trackName.toLowerCase().split(/\W+/).filter(w=>w.length>3)).flat();const uniqueTracks=new Map();all.forEach(t=>{if(!t.trackId)return;let score=0;score+=(artistCounts[t.artistName]||0)*5;score+=(genreCounts[t.primaryGenreName]||0)*3;const name=(t.trackName+' '+t.artistName+' '+(t.primaryGenreName||'')).toLowerCase();score+=words.filter(w=>name.includes(w)).length*.2;score+=t.previewUrl?0.5:0;if(!uniqueTracks.has(t.trackId)||uniqueTracks.get(t.trackId).score<score)uniqueTracks.set(t.trackId,{track:t,score})});const ranked=[...uniqueTracks.values()].sort((a,b)=>b.score-a.score).slice(0,12);$('#recCount').textContent=ranked.length+' sugestões';$('#recSubtitle').textContent='Comparando artistas, gêneros e termos das suas referências.';$('#recs').innerHTML=ranked.map(({track:t,score},i)=>`<article class="rec"><img src="${esc(cover(t))}" alt="Capa de ${esc(t.trackName)}" onerror="this.style.visibility='hidden'"><div class="small">✦ ${Math.min(98,Math.round(60+score*4))}% afinidade estimada</div><h3 title="${esc(t.trackName)}">${esc(t.trackName)}</h3><div class="artist">${esc(t.artistName)}</div><div class="why">${esc(t.primaryGenreName||'Gênero não informado')} · ${score?'Artista ou estilo relacionado às suas escolhas.':'Descoberta complementar.'}</div>${t.previewUrl?`<audio controls preload="none" src="${esc(t.previewUrl)}">Seu navegador não suporta áudio.</audio>`:'<div class="meta">Prévia indisponível</div>'}<button class="btn" style="width:100%;margin-top:8px" data-recadd="${t.trackId}">＋ Usar como referência</button><button class="btn" style="width:100%;margin-top:6px" onclick="window.open('${esc(t.trackViewUrl||'')}','_blank','noopener')">Abrir no iTunes</button></article>`).join('')||'<div class="empty" style="grid-column:1/-1">Não encontramos recomendações desta vez. Tente selecionar outros artistas.</div>';$('#recs').scrollIntoView({behavior:'smooth',block:'nearest'});}catch(e){$('#recs').innerHTML=`<div class="empty" style="grid-column:1/-1">Não foi possível recomendar agora: ${esc(e.message)}</div>`}finally{b.disabled=selected.size<2;b.textContent='✦ Encontrar próximas músicas'}}
function toast(s){const t=$('#toast');t.textContent=s;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2200)}
async function loadCatalog(){try{const d=await api('/api/catalog');renderResults(d.results);$('#resultCount').textContent=d.results.length+' faixas iniciais'}catch(e){$('#results').innerHTML='<div class="empty">Não foi possível carregar o catálogo inicial.</div>'}}
$('#searchBtn').addEventListener('click',()=>search($('#query').value));$('#query').addEventListener('keydown',e=>{if(e.key==='Enter')search($('#query').value)});$('#popularBtn').addEventListener('click',popular);$('#recommendBtn').addEventListener('click',recommend);
loadCatalog();
document.addEventListener('click',e=>{const a=e.target.closest('[data-add]');if(a){const id=Number(a.dataset.add);const t=latest.find(x=>x.trackId===id);if(!t)return;if(selected.has(id))selected.delete(id);else selected.set(id,t);renderResults(latest);renderSelected()}const r=e.target.closest('[data-remove]');if(r){selected.delete(Number(r.dataset.remove));renderSelected();renderResults(latest)}const rec=e.target.closest('[data-recadd]');if(rec){const id=Number(rec.dataset.recadd);const card=rec.closest('.rec');const title=card.querySelector('h3').textContent;const artist=card.querySelector('.artist').textContent;const img=card.querySelector('img').src;const t={trackId:id,trackName:title,artistName:artist,artworkUrl100:img,primaryGenreName:'Recomendação'};selected.set(id,t);renderSelected();toast('Adicionada às suas referências')}});
</script></body></html>'''

class Handler(BaseHTTPRequestHandler):
    def send_json(self, status, obj):
        data = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/':
            data = HTML.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        if parsed.path == '/api/catalog':
            self.send_json(200, {'results': SEED_TRACKS, 'resultCount': len(SEED_TRACKS)})
            return
        if parsed.path == '/api/search':
            params = parse_qs(parsed.query)
            term = params.get('term', [''])[0].strip()
            try:
                limit = max(1, min(50, int(params.get('limit', ['25'])[0])))
            except ValueError:
                limit = 25
            if not term:
                self.send_json(400, {'error': 'Informe um termo de pesquisa.'})
                return
            url = 'https://itunes.apple.com/search?' + urlencode({'term': term, 'entity': 'song', 'limit': limit, 'country': 'br'})
            req = Request(url, headers={'User-Agent': 'SONORA-Music-Discovery/1.0', 'Accept': 'application/json'})
            try:
                with urlopen(req, timeout=15) as response:
                    payload = json.loads(response.read().decode('utf-8'))
                results = []
                for item in payload.get('results', []):
                    if not item.get('trackId') or not item.get('trackName') or not item.get('artistName'):
                        continue
                    results.append({k: item.get(k) for k in ('trackId','trackName','artistName','collectionName','primaryGenreName','artworkUrl100','previewUrl','trackViewUrl','releaseDate','trackTimeMillis')})
                self.send_json(200, {'results': results, 'resultCount': len(results)})
            except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
                self.send_json(502, {'error': 'O catálogo do iTunes não respondeu. Verifique a internet e tente novamente.'})
            return
        self.send_json(404, {'error': 'Rota não encontrada.'})

    def log_message(self, fmt, *args):
        print('%s - %s' % (self.address_string(), fmt % args))

if __name__ == '__main__':
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print('\nSONORA está iniciando!')
    print(f'Endereço local: http://127.0.0.1:{PORT}')
    print(f'Para abrir no celular, conecte-o ao mesmo Wi-Fi e use o IPv4 deste computador: http://SEU-IP:{PORT}')
    print('Para descobrir o IP, abra outro CMD e execute: ipconfig')
    print('Sem Flask, sem chave de API e sem cadastro. Feche com Ctrl+C.\n')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nSONORA encerrado.')
    finally:
        server.server_close()
