# Beat Producer HQ: šablona struktūra

Šī ir "būvēšanas instrukcija" pirmajai versijai.
Šablons pašā Notion būs **angliski** (starptautiskais tirgus), tāpēc nosaukumi te ir angliski.

> **Princips:** maz, bet labi. Labāk 3 datubāzes, kas strādā perfekti, nekā 12, kas biedē.
> Viss, kas atzīmēts ar *(v2)*, nāk vēlāk, ne pirmajā versijā.

## Kam tas ir?
Beatmakeriem un producentiem (iesācējiem un vidēja līmeņa), kam ir simtiem beatu
mapēs, nav skaidrs, kas pabeigts, kas pārdots un kam, un kas pazaudē idejas.

**Viena teikuma solījums:** *"Know where every beat is: from idea to sold."*

## Datubāzes

### 1. 🎹 Beats (galvenā)
Katrs beats ir viena rinda.

| Property | Tips | Piezīmes |
|---|---|---|
| Name | Title | Beata nosaukums |
| Status | Status | 💡 Idea → 🎛️ In Progress → 🎚️ Mixing → ✅ Finished → 💰 Sold |
| Genre | Multi-select | Trap, Lo-fi, Drill, R&B, Afro, Pop… |
| BPM | Number | |
| Key | Select | C min, F# maj… |
| Mood | Multi-select | Dark, Chill, Energetic, Sad… |
| Rating | Select | ⭐ līdz ⭐⭐⭐⭐⭐ (cik labs, pēc tavām domām) |
| File link | URL | Saite uz Google Drive / Dropbox |
| Date created | Created time | Automātiski |
| Collaborators | Relation → Contacts | |
| Sales | Relation → Sales | |
| Total earned | Rollup | Sales → Price, sum |
| Notes | Text | |

**Views:**
- 🗂️ **Board by Status** (kanban): galvenais skats, redzams, kur katrs beats atrodas
- 📋 **All Beats** (tabula): ar filtriem pa žanru, BPM, key
- 🔥 **Ready to Sell**: filtrs Status = Finished
- 💡 **Idea Vault**: tikai idejas, lai nekas nepazūd
- 🖼️ **Gallery** *(v2)*: ar cover art

### 2. 💰 Sales & Licenses
Katra pārdošana vai licence ir viena rinda.

| Property | Tips | Piezīmes |
|---|---|---|
| Sale | Title | piem. "Midnight – Basic Lease – @artistname" |
| Beat | Relation → Beats | |
| Buyer | Relation → Contacts | |
| License type | Select | Basic Lease, Premium Lease, Unlimited, Exclusive |
| Price | Number (€/$) | |
| Date | Date | |
| Platform | Select | BeatStars, Airbit, Direct, Instagram… |
| Contract sent | Checkbox | |

**Views:**
- 📋 Visas pārdošanas
- 📅 Šis mēnesis (filtrs pēc datuma)
- 📊 Pa licences tipiem (grupēts)

### 3. 👥 Contacts
Mākslinieki, pircēji, kolaboranti.

| Property | Tips | Piezīmes |
|---|---|---|
| Name | Title | |
| Role | Multi-select | Artist, Buyer, Producer, Engineer |
| Instagram / Email | Text / Email | |
| Beats | Relation → Beats | |
| Purchases | Relation → Sales | |
| Total spent | Rollup | |
| Last contact | Date | Lai zinātu, kam uzrakstīt atkal |

## Galvenā lapa (Dashboard)

```
🎧 BEAT PRODUCER HQ
──────────────────────────────
[Quick add: + New beat idea]

📌 Start here (instrukcija, 5 min)

🎛️ In progress        💰 This month
(Beats board view)     (Sales, šis mēnesis)

🔥 Ready to sell       👥 Contacts
```

Visas daļas ir "linked views" uz tām pašām 3 datubāzēm.

## "Start here" lapa (svarīgi pārdošanai!)
1. Kā nokopēt šablonu (Duplicate)
2. Kā izdzēst parauga datus
3. Kā pievienot pirmo beatu (ar bildi/GIF)
4. Kā atzīmēt pārdošanu
5. Saite uz video instrukciju

## Parauga dati
Ielikt ~8 izdomātus beatus dažādos statusos, 3 pārdošanas, 4 kontaktus,
lai pircējs, atverot šablonu, uzreiz redz "dzīvu" sistēmu.

## Nākamajām versijām *(v2+)*
- 🗓️ Content planner: ko likt TikTok/IG/YouTube par katru beatu
- 🎯 Goals: "100 beats this year", "€500 this month" ar progresa joslu
- 🧪 Sample & Drum kit library
- 📝 Collab split sheets (kurš ir autors cik %)
- 💸 Expenses: plugini, sample pakas, abonementi → peļņa = ienākumi − izdevumi

## Atvērti jautājumi
- [ ] Vai producentiem patiešām vajag "Contacts", vai pietiek ar teksta lauku pirmajā versijā?
- [ ] Viena cena vai divi līmeņi (Basic / Pro ar v2 funkcijām)?
- [ ] Nosaukums: "Beat Producer HQ"? "Beat Vault"? "The Beat Catalog"?
