# Builds Cozy Crockpot Dinners (A4, 7 pages) -> cozy-crockpot-dinners.html / .pdf
import subprocess, glob, os
HERE = os.path.dirname(os.path.abspath(__file__))

R = [
 dict(n=1, emoji="🌮", title="Salsa Pulled Chicken", tag="3 ingredients · tacos, bowls & wraps", serves="6", prep="5 min",
  slow="LOW 6 h · HIGH 3–4 h", ip="12 min + 10 min release", color="#FBE6DA", diet="Gluten-free",
  ing=["900 g (2 lb) chicken breasts or thighs","1 jar salsa (450 g / 16 oz)","1 tbsp taco seasoning","Juice of 1 lime","Salt to taste"],
  slow_steps=["Put the chicken in the pot and sprinkle with taco seasoning.","Pour the salsa over the top.","Cook until the chicken shreds easily.","Shred with two forks, stir in the lime juice and taste for salt."],
  ip_steps=["Add ½ cup (120 ml) water to the pot, then the chicken and seasoning.","Pour the salsa on top. <b>Don't stir</b>, so you won't get a burn warning.","Pressure cook on HIGH for 12 min, then let the pressure release naturally for 10 min.","Shred, add the lime juice and stir."],
  serve="Warm tortillas, rice bowls with corn and avocado, or nachos with melted cheese.",
  left="Keeps 4 days in the fridge. Roll it into a wrap with rice and cheese for tomorrow's lunch."),
 dict(n=2, emoji="🍝", title="Creamy Tuscan Chicken", tag="sun-dried tomatoes · spinach · parmesan", serves="4", prep="10 min",
  slow="LOW 4–5 h · HIGH 2–3 h", ip="10 min + 5 min release", color="#FBF0D6", diet="Gluten-free",
  ing=["700 g (1½ lb) chicken breasts","1 cup (240 ml) chicken broth","4 garlic cloves, minced","½ cup sun-dried tomatoes, chopped","1 tsp Italian seasoning · salt & pepper","<i>To finish:</i> 1 cup (240 ml) heavy cream","½ cup grated parmesan","2 big handfuls of spinach"],
  slow_steps=["Season the chicken and place it in the pot.","Add the broth, garlic, sun-dried tomatoes and Italian seasoning.","Cook until tender. Chicken breasts dry out, so don't cook longer!","Stir in the cream, parmesan and spinach. Cover for 15 min until the spinach wilts."],
  ip_steps=["Add the broth, then the chicken, garlic, tomatoes and seasoning.","Pressure cook on HIGH for 10 min, then natural release for 5 min.","Take out the chicken. Switch to <b>Sauté</b>.","Stir in the cream, parmesan and spinach and simmer 2–3 min. Return the chicken."],
  serve="Pasta, rice or mashed potatoes, and crusty bread for the sauce.",
  left="Keeps 3 days in the fridge. Slice the chicken and toss it with pasta and the sauce."),
 dict(n=3, emoji="🥧", title="Chicken Pot Pie Soup", tag="all the comfort, none of the pastry work", serves="6", prep="15 min",
  slow="LOW 6–7 h · HIGH 3–4 h", ip="10 min + 10 min release", color="#E6EEE3", diet="",
  ing=["500 g (1 lb) chicken breasts","1 onion, chopped","3 carrots, sliced","2 celery stalks, sliced","2 potatoes, cubed","2 garlic cloves, minced","4 cups (1 l) chicken broth","1 tsp dried thyme · salt & pepper","<i>To finish:</i> 1 cup (240 ml) milk or cream","3 tbsp flour","1 cup frozen peas"],
  slow_steps=["Put the chicken, vegetables, garlic, broth and thyme in the pot.","Cook until the vegetables are soft.","Take out the chicken, shred it and put it back.","Whisk the flour into the milk, stir it in with the peas. Cook 20–30 min more on HIGH until thick."],
  ip_steps=["Add everything except the milk, flour and peas.","Pressure cook on HIGH for 10 min, then natural release for 10 min.","Shred the chicken. Switch to <b>Sauté</b>.","Whisk the flour into the milk, stir it in with the peas and simmer 3–5 min until thick."],
  serve="Puff pastry squares baked until golden, biscuits or a slice of bread.",
  left="Keeps 4 days in the fridge. It thickens overnight, so add a splash of broth when reheating."),
 dict(n=4, emoji="🍆", title="Ajapsandali", tag="Georgian vegetable stew", serves="4–6", prep="20 min",
  slow="LOW 6–7 h · HIGH 3–4 h", ip="6 min + 10 min release", color="#F1E6EE", diet="Vegan",
  ing=["2 eggplants, cubed","3 potatoes, cubed","2 carrots, sliced","2 bell peppers (red + green), chopped","2 onions, chopped","4 tomatoes, chopped (or 1 can, 400 g)","2 tbsp tomato paste","5 garlic cloves, minced","1 small chili (optional)","1 tsp ground coriander · 2 bay leaves · salt","4 tbsp oil","<i>To finish:</i> fresh cilantro, basil & parsley"],
  slow_steps=["Fry the eggplant, onions and peppers in the oil for 5–7 min until golden. This gives the stew its flavor.","Put them in the pot with the potatoes, carrots, spices and chili.","Add the tomatoes and tomato paste on top.","Cook until everything is soft. Stir in the garlic and herbs before serving."],
  ip_steps=["On <b>Sauté</b>, fry the eggplant, onions and peppers in the oil for 5–7 min.","Add the potatoes, carrots, spices and ½ cup (120 ml) water.","Add the tomatoes and paste <b>on top, don't stir</b>.","Pressure cook on HIGH for 6 min, natural release 10 min. Stir in the garlic and herbs."],
  serve="Fresh bread and a piece of salty cheese. In Georgia it's often eaten warm or at room temperature.",
  left="Tastes even better the next day! Keeps 4 days in the fridge."),
 dict(n=5, emoji="🫘", title="Lobio", tag="Georgian bean stew", serves="4–6", prep="10 min",
  slow="LOW 6–8 h · HIGH 4 h", ip="30 min + 15 min release", color="#F6E4D3", diet="Vegan",
  ing=["400 g (2 cups) dried red kidney beans, soaked overnight","1 onion, finely chopped","4 garlic cloves, minced","1 tbsp tomato paste","1 tsp ground coriander","½ tsp blue fenugreek (utskho suneli), optional","½ tsp chili flakes · 1 bay leaf · salt","1 tbsp oil","<i>To finish:</i> ½ cup crushed walnuts (optional), fresh cilantro"],
  slow_steps=["<b>Important:</b> boil the soaked beans hard in a regular pot for 10 min first. Red kidney beans aren't safe if cooked only at low heat.","Drain and put them in the slow cooker with the onion, spices, tomato paste and oil.","Cover with water by 3 cm (1 inch) and cook until very soft.","Mash about a third of the beans. Stir in the garlic, walnuts and cilantro. Season with salt."],
  ip_steps=["Drain the soaked beans and add them with the onion, spices, tomato paste and oil.","Cover with water by 3 cm (1 inch).","Pressure cook on HIGH for 30 min, then natural release for 15 min.","Mash a third of the beans, then stir in the garlic, walnuts, cilantro and salt."],
  serve="Cornbread, pickles and a fresh tomato & cucumber salad.",
  left="Short on time? Use 3 cans of beans (drained): slow cooker 3–4 h on LOW or Instant Pot 5 min."),
]

CSS = """
@font-face{font-family:Fraunces;font-weight:700;src:url(fonts/Fraunces-700.ttf)}
@font-face{font-family:Fraunces;font-weight:500;src:url(fonts/Fraunces-500.ttf)}
@font-face{font-family:Nunito;font-weight:400;src:url(fonts/Nunito-400.ttf)}
@font-face{font-family:Nunito;font-weight:600;src:url(fonts/Nunito-600.ttf)}
@font-face{font-family:Nunito;font-weight:700;src:url(fonts/Nunito-700.ttf)}
@font-face{font-family:Nunito;font-weight:800;src:url(fonts/Nunito-800.ttf)}
@page{size:A4;margin:0}
*{box-sizing:border-box}
:root{--cream:#F3E6D3;--paper:#FAF2E6;--ink:#3A2A1F;--muted:#7A6453;--sage:#9C7350;--sage-l:#EEDFCA;--terra:#B65D35;--mustard:#C9963F;--line:#E0CDB3;--dark:#2E2018}
body{margin:0;font-family:Nunito,sans-serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;overflow:hidden;position:relative;background:var(--paper);padding:14mm 15mm 12mm;page-break-after:always;display:flex;flex-direction:column}
.page:last-child{page-break-after:auto}
.kick{font-weight:800;font-size:9.5pt;letter-spacing:.18em;color:var(--terra);text-transform:uppercase}
h1,h2,h3{font-family:Fraunces,serif;font-weight:700;margin:0}
.foot{position:absolute;left:15mm;right:15mm;bottom:8mm;display:flex;justify-content:space-between;font-size:8pt;color:var(--muted)}
.foot b{font-family:Fraunces,serif;font-size:9.5pt;color:var(--ink)}
/* recipe page */
.rh{border-radius:6mm;padding:7mm 8mm;display:flex;gap:6mm;align-items:center;background:var(--dark);color:var(--paper)}
.rh .tg{color:#D8C3A8 !important}.rh .num{color:#E39A68 !important}
.rh .em{font-size:44pt;line-height:1}
.rh .ph{width:62mm;height:44mm;border-radius:4mm;background-size:cover;background-position:center;flex:none;margin:-3mm 0 -3mm -3mm}
.rh .num{font-weight:800;font-size:9pt;letter-spacing:.16em;color:var(--terra)}
.rh h2{font-size:28pt;line-height:1.05;margin:1mm 0 1.5mm}
.rh .tg{font-size:11pt;font-weight:600;color:var(--muted)}
.meta{display:flex;gap:2.5mm;margin:4mm 0 4mm;flex-wrap:wrap}
.chip{border:1.4px solid var(--line);border-radius:99px;padding:1.8mm 4mm;font-size:9.5pt;font-weight:700;background:var(--cream)}
.chip span{color:var(--muted);font-weight:600}
.chip.diet{background:var(--sage);color:#fff;border-color:var(--sage)}
.cols{display:grid;grid-template-columns:62mm 1fr;gap:7mm}
.ing{background:var(--sage-l);border-radius:5mm;padding:6mm 5.5mm}
.ing h3,.how h3{font-size:14pt;margin-bottom:3mm}
.ing ul{list-style:none;padding:0;margin:0}
.ing li{font-size:10.6pt;line-height:1.35;padding:1.15mm 0 1.15mm 6mm;position:relative;border-bottom:1px dashed rgba(47,59,47,.15)}
.ing li:last-child{border:0}
.ing li:before{content:"";position:absolute;left:0;top:2.7mm;width:2.6mm;height:2.6mm;border:1.4px solid var(--sage);border-radius:1mm;background:var(--paper)}
.how .m{margin-bottom:7mm}
.how .mt{display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid var(--ink);padding-bottom:1.5mm;margin-bottom:2.5mm}
.how .mt h3{margin:0;font-size:13pt}.how .mt span{font-size:9.5pt;font-weight:800;color:var(--terra)}
.how ol{margin:0;padding:0;list-style:none;counter-reset:s}
.how li{counter-increment:s;font-size:10.8pt;line-height:1.45;padding:1.3mm 0 1.3mm 8mm;position:relative}
.how li:before{content:counter(s);position:absolute;left:0;top:1.5mm;width:5.2mm;height:5.2mm;border-radius:50%;background:var(--ink);color:#fff;font-size:8pt;font-weight:800;display:flex;align-items:center;justify-content:center}
.tips{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin-top:4mm}
.tip{border-radius:4mm;padding:4mm 5mm;font-size:10.3pt;line-height:1.4;background:#F6EBDB;border:1.4px solid var(--line)}
.tip b{display:block;font-family:Fraunces,serif;font-size:11pt;margin-bottom:1mm}
.notes{margin-top:4mm;border:1.4px dashed var(--line);border-radius:4mm;padding:3mm 5mm;flex:1;min-height:12mm;margin-bottom:5mm;font-size:9pt;font-weight:800;letter-spacing:.12em;color:var(--muted)}
"""

def foot(p): return f'<div class="foot"><b>MadaraMakes</b><span>Cozy Crockpot Dinners · page {p}</span><span>© 2026 MadaraMakes · personal use only</span></div>'

def photo(r):
    f = glob.glob(os.path.join(HERE, "photos", f"{r['n']}-*.jpg"))
    if f:
        return f'<div class="ph" style="background-image:url(photos/{os.path.basename(f[0])})"></div>'
    return f'<div class="em">{r["emoji"]}</div>'

def recipe(r, p):
    li = "".join(f"<li>{x}</li>" for x in r["ing"])
    s = "".join(f"<li>{x}</li>" for x in r["slow_steps"])
    i = "".join(f"<li>{x}</li>" for x in r["ip_steps"])
    diet = f'<div class="chip diet">{r["diet"]}</div>' if r["diet"] else ""
    return f'''<div class="page">
<div class="rh">{photo(r)}<div><div class="num">RECIPE {r["n"]} OF 5</div><h2>{r["title"]}</h2><div class="tg">{r["tag"]}</div></div></div>
<div class="meta"><div class="chip"><span>Serves</span> {r["serves"]}</div><div class="chip"><span>Prep</span> {r["prep"]}</div><div class="chip">🐢 <span>Slow cooker</span> {r["slow"]}</div><div class="chip">⚡ <span>Instant Pot</span> {r["ip"]}</div>{diet}</div>
<div class="cols"><div class="ing"><h3>Ingredients</h3><ul>{li}</ul></div>
<div class="how"><div class="m"><div class="mt"><h3>🐢 Slow cooker</h3><span>{r["slow"]}</span></div><ol>{s}</ol></div>
<div class="m"><div class="mt"><h3>⚡ Instant Pot</h3><span>{r["ip"]}</span></div><ol>{i}</ol></div></div></div>
<div class="tips"><div class="tip"><b>Serve it with</b>{r["serve"]}</div><div class="tip"><b>Leftovers</b>{r["left"]}</div></div>
<div class="notes">MY NOTES</div>
{foot(p)}</div>'''

def cover_photos():
    fs = sorted(glob.glob(os.path.join(HERE, "photos", "*.jpg")))
    return "".join(f'<div style="background:url(photos/{os.path.basename(f)}) center/cover;border-radius:3mm"></div>' for f in fs[:5])

cover = f'''<div class="page" style="background:var(--dark);color:var(--paper);padding:0">
<div style="display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:43mm 43mm;gap:2.5mm;padding:12mm 12mm 0;height:100mm" class="cg"><style>.cg div:first-child{{grid-row:span 2}}</style>{cover_photos()}</div>
<div style="padding:9mm 16mm 0">
<div class="kick" style="color:#E39A68">Slow cooker & Instant Pot</div>
<h1 style="font-size:46pt;line-height:1;margin:3mm 0 4mm;color:var(--paper)">Cozy Crockpot <span style="color:#E39A68">Dinners</span></h1>
<p style="font-size:12.5pt;font-weight:600;color:#D8C3A8;max-width:150mm;margin:0 0 7mm">5 easy dump-and-go dinners for busy weeks, with 2 cozy recipes from Georgia, where my family lives.</p>
<div style="display:grid;gap:2.5mm;max-width:150mm">
{"".join(f'<div style="display:flex;align-items:center;gap:4mm;background:rgba(250,242,230,.07);border:1px solid rgba(250,242,230,.2);border-radius:4mm;padding:2.8mm 5mm;font-weight:800;font-size:11.5pt"><span style="font-size:16pt">{r["emoji"]}</span>{r["title"]}<span style="margin-left:auto;font-weight:600;font-size:9.5pt;color:#D8C3A8">page {r["n"]+2}</span></div>' for r in R)}
<div style="display:flex;align-items:center;gap:4mm;background:#B65D35;border-radius:4mm;padding:2.8mm 5mm;font-weight:800;font-size:11.5pt"><span style="font-size:16pt">🛒</span>Shopping lists & weekend prep<span style="margin-left:auto;font-weight:600;font-size:9.5pt;opacity:.85">page 8</span></div>
</div></div>
<div style="position:absolute;left:16mm;bottom:12mm;font-family:Fraunces,serif;font-size:13pt;color:#D8C3A8">MadaraMakes</div></div>'''
howto = f'''<div class="page">
<div class="kick">Before you start</div><h1 style="font-size:30pt;margin:2mm 0 6mm">How to use this guide</h1>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:5mm">
<div class="tip" style="background:var(--sage-l);border:0"><b>🐢 Slow cooker (Crockpot)</b>Low and slow. Put everything in before work and come home to dinner. LOW is gentler, HIGH is about twice as fast.</div>
<div class="tip" style="background:#F1D9BC;border:0"><b>⚡ Instant Pot / pressure cooker</b>Fast. "Natural release" means you leave the valve closed and let the pressure drop on its own.</div>
</div>
<h3 style="font-size:15pt;margin:8mm 0 3mm">5 golden rules</h3>
<div style="display:grid;gap:3mm">
{"".join(f'<div style="display:flex;gap:5mm;align-items:flex-start;background:var(--cream);border-radius:4mm;padding:4mm 5mm"><div style="font-family:Fraunces,serif;font-size:22pt;color:var(--terra);line-height:1;width:8mm">{i}</div><div style="font-size:10.5pt;line-height:1.45"><b style="font-size:11.5pt">{a}</b><br>{b}</div></div>' for i,(a,b) in enumerate([
 ("Fill it halfway to three-quarters.","Too empty and food dries out, too full and it won't cook evenly."),
 ("Don't lift the lid.","Every peek lets the heat out and can add up to 20–30 minutes to the cooking time."),
 ("Dairy goes in at the end.","Cream, cheese and milk can split if they cook for hours. Stir them in during the last 15–30 minutes."),
 ("Tomatoes on top in the Instant Pot.","Thick sauces on the bottom can trigger the burn warning. Layer them on top and don't stir before cooking."),
 ("Herbs and garlic last.","Fresh herbs and a little raw garlic at the end make every stew taste brighter."),],1))}
</div>
<div class="tip" style="margin-top:8mm"><b>Good to know</b>Cooking times are a guide and can vary depending on your appliance and the size of your pieces. Chicken is safe to eat at 74 °C (165 °F). Most dishes keep 3–4 days in the fridge or up to 3 months in the freezer (except the creamy ones).</div>
{foot(2)}</div>'''

shop = [("🌮 Salsa Pulled Chicken",["Chicken breasts or thighs · 900 g (2 lb)","Salsa · 1 jar (450 g / 16 oz)","Taco seasoning","Lime · 1"]),
 ("🍝 Creamy Tuscan Chicken",["Chicken breasts · 700 g (1½ lb)","Chicken broth · 1 cup","Sun-dried tomatoes · ½ cup","Heavy cream · 1 cup","Parmesan · ½ cup grated","Spinach · 2 handfuls","Italian seasoning"]),
 ("🥧 Chicken Pot Pie Soup",["Chicken breasts · 500 g (1 lb)","Carrots · 3 · celery · 2 stalks","Potatoes · 2","Chicken broth · 4 cups (1 l)","Milk or cream · 1 cup","Frozen peas · 1 cup","Dried thyme · flour"]),
 ("🍆 Ajapsandali",["Eggplants · 2","Potatoes · 3 · carrots · 2","Bell peppers · 2","Tomatoes · 4 (or 1 can)","Small chili (optional)","Fresh cilantro, basil & parsley"]),
 ("🫘 Lobio",["Dried red kidney beans · 400 g (or 3 cans)","Walnuts · ½ cup (optional)","Blue fenugreek (optional)","Fresh cilantro"]),
 ("🧂 Pantry basics (used in several)",["Onions & garlic","Oil · salt · pepper","Tomato paste","Ground coriander · bay leaves","Chili flakes"])]
def shop_item(x):
    return ('<div style="display:flex;gap:2.5mm;align-items:center;font-size:9.8pt;padding:1.1mm 0;border-bottom:1px dashed var(--line)">'
            '<span style="width:3mm;height:3mm;border:1.4px solid var(--sage);border-radius:1mm;flex:none"></span>' + x + '</div>')
shop_html = "".join('<div style="break-inside:avoid;margin-bottom:4.5mm"><h3 style="font-size:12.5pt;margin-bottom:1.5mm">' + h + '</h3>'
                    + "".join(shop_item(x) for x in items) + '</div>' for h, items in shop)
shopping = f'''<div class="page">
<div class="kick">Pick 2 or 3 for this week</div><h1 style="font-size:30pt;margin:2mm 0 2mm">Shopping lists</h1><p style="font-size:10.5pt;color:var(--muted);margin:0 0 5mm">Check the pantry basics first, then add the lists for the recipes you want to cook this week.</p>
<div style="columns:2;column-gap:7mm">
{shop_html}
</div>
<div style="background:var(--ink);color:var(--cream);border-radius:5mm;padding:6mm 7mm;margin-top:auto;margin-bottom:8mm">
<h3 style="font-size:15pt;margin-bottom:3mm">🗓️ 30-minute weekend prep</h3>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:2mm 7mm;font-size:9.8pt;line-height:1.4">
<div>1. Pick 2–3 recipes for the week.</div><div>2. Chop the onions and mince the garlic for all of them.</div>
<div>3. Slice the carrots, celery and peppers.</div><div>4. Making lobio? Soak the beans the night before.</div>
<div>5. Pack each recipe's veggies in its own labeled box or bag.</div><div>6. On cooking day: open, dump, switch on. Done! 🎉</div>
</div></div>
{foot(8)}</div>'''

pages = [cover, howto] + [recipe(r, i+3) for i, r in enumerate(R)] + [shopping]
html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Cozy Crockpot Dinners</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
open(os.path.join(HERE, "cozy-crockpot-dinners.html"), "w").write(html)
ch = sorted(glob.glob("/opt/pw-browsers/chromium-*/*/chrome"))[0]
subprocess.run([ch, "--headless", "--no-sandbox", "--disable-gpu", "--allow-file-access-from-files", "--no-pdf-header-footer",
  "--virtual-time-budget=4000", f"--print-to-pdf={HERE}/cozy-crockpot-dinners.pdf", f"file://{HERE}/cozy-crockpot-dinners.html"], stderr=subprocess.DEVNULL)
