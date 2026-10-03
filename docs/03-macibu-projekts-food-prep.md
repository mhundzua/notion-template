# Mācību projekts: 🍱 Food Prep plānotājs

**Mērķis:** iemācīties Notion pamatus, uztaisot kaut ko sev noderīgu.
Šis **nav** produkts pārdošanai, tas ir treniņš. Nav jābūt perfektam.

**Laiks:** 1–2 vakari.

> Notion ir angliski, tāpēc pogu nosaukumi te ir angliski, **treknrakstā**.
> Notion laiku pa laikam maina izskatu, tāpēc, ja kāda poga izskatās nedaudz citādi, meklē līdzīgu.

---

## 0. solis: konts

1. Atver [notion.so](https://www.notion.so) un reģistrējies (bezmaksas plāns pilnīgi pietiek).
2. Var strādāt pārlūkā vai lejupielādēt aplikāciju datoram. Aplikācija ir ērtāka, bet pārlūks arī der.
3. Ja Notion piedāvā izvēlēties "kam lietosi", izvēlies "For myself" un izlaid visus piedāvātos šablonus.

---

## 1. solis: pirmā lapa

1. Kreisajā sānjoslā spied **+ New page** (vai **Add a page**).
2. Virsrakstā ieraksti: `Food Prep`
3. Uzbrauc ar peli virs virsraksta un spied **Add icon**, izvēlies 🍱.
4. Spied **Add cover**: augšā parādīsies bilde. Vēlāk to var nomainīt.

✅ *Tu iemācījies: lapas, ikonas, cover bildes.*

---

## 2. solis: recepšu tabula (tava pirmā datubāze!)

**Datubāze** ir gudra tabula: katra rinda ir viena recepte, un katra rinda ir arī atsevišķa lapa, kurā var rakstīt.

1. Lapā zem virsraksta uzraksti `/table` un izvēlies **Table** (dažreiz saucas **Table view** vai **Database – Inline**).
2. Ja Notion jautā par datu avotu, izvēlies **New database** / **New table**.
3. Tabulas nosaukumu (augšā, kur rakstīts "Untitled") nomaini uz `Receptes`.

### Kolonnas (Notion tās sauc par *properties*)

Pirmā kolonna **Name** jau ir, tur būs receptes nosaukums.
Pārējās pievieno, spiežot **+** tabulas galvenes labajā malā. Izvēlies tipu un ieraksti nosaukumu:

| Nosaukums | Tips (ko izvēlēties) | Kam tas ir |
|---|---|---|
| Kategorija | **Select** | Brokastis / Pusdienas / Vakariņas / Uzkoda |
| Laiks (min) | **Number** | Cik ilgi gatavot |
| Porcijas | **Number** | Cik porcijas sanāk |
| Glabājas | **Select** | 1–2 dienas / 3–4 dienas / Var saldēt |
| Birkas | **Multi-select** | ātrs, lēts, veģetārs, daudz proteīna… |
| Saite | **URL** | Ja recepte ir no interneta |
| Izmēģināts | **Checkbox** | ✔ ja jau taisīji |

💡 **Select pret Multi-select:** *Select* = var izvēlēties tikai vienu variantu (recepte ir vai nu brokastis, vai vakariņas).
*Multi-select* = var vairākus (recepte var būt gan "ātra", gan "lēta").

Select varianti rodas, kad šūnā vienkārši ieraksti jaunu vārdu un spied Enter. Notion katram iedod krāsu.

✅ *Tu iemācījies: datubāzes un property tipus. Šī ir 50% no visa, kas vajadzīgs šabloniem!*

---

## 3. solis: receptes iekšpuse

1. Ieraksti pirmo recepti, piemēram, `Vistas rīsi ar dārzeņiem`.
2. Uzbrauc uz rindas ar peli. Parādās poga **Open**: spied to. Atveras receptes lapa.
3. Augšā redzi visas kolonnas (Kategorija, Laiks…), aizpildi tās.
4. Zemāk, tukšajā daļā, raksti:
   - `## Sastāvdaļas` un Enter (sanāk virsraksts)
   - `/todo` (izveido ķeksīšu sarakstu), katra sastāvdaļa savā rindā
   - `## Pagatavošana`
   - `1.` un atstarpe (sanāk numurēts saraksts) soļiem

**Pievieno vismaz 5 receptes**, tās vajadzēs nākamajos soļos. Var būt vienkāršas, pat tikai nosaukums un kolonnas.

✅ *Tu iemācījies: ka katra rinda ir lapa, un "/" komandas.*

---

## 4. solis: skati (views): tie paši dati, cits izskats

Šī ir Notion "maģija". Dati ir tie paši, bet tos var rādīt dažādos veidos.

### Galerija (kartītes ar bildēm)
1. Blakus tabulas nosaukumam spied **+** (vai **Add view**).
2. Izvēlies **Gallery**, nosauc `Galerija`.
3. Katrai receptei var ielikt bildi: atver recepti → **Add cover**.

### Board (kolonnas pa kategorijām)
1. Vēlreiz **+** → **Board**, nosauc `Pa ēdienreizēm`.
2. Augšā labajā stūrī **⋯** → **Group by** (Grupēt pēc) → **Kategorija**.
3. Tagad redzi kolonnas: Brokastis | Pusdienas | Vakariņas. Kartītes var vilkt no vienas uz otru!

### Filtrs: "Ātrās receptes"
1. Izveido vēl vienu **Table** skatu, nosauc `⚡ Ātrās`.
2. Spied **Filter** → izvēlies **Laiks (min)** → nosacījums **≤** (less than or equal to) → `30`.
3. Tagad šis skats rāda tikai receptes līdz 30 minūtēm. Pārējie skati paliek nemainīti!

✅ *Tu iemācījies: views, grupēšanu, filtrus. Šī ir vēl 30% no šablonu prasmēm.*

---

## 5. solis (bonuss): nedēļas plāns ar saitēm uz receptēm

Šis ir nedaudz grūtāks, bet tieši tas atšķir "tabulu" no "sistēmas". Ja iestrēgsti, nekas, atnāc un pajautā.

1. Food Prep lapā (zem receptēm) uzraksti `/table` → **New database**, nosauc `Nedēļas plāns`.
2. Kolonnas:
   | Nosaukums | Tips |
   |---|---|
   | Name | (jau ir) raksti, piem., `Pirmdiena – pusdienas` |
   | Diena | **Select**: Pirmdiena … Svētdiena |
   | Ēdienreize | **Select**: Brokastis / Pusdienas / Vakariņas |
   | Recepte | **Relation** → izvēlies datubāzi **Receptes** |
3. **Relation** ir saite starp divām tabulām. Tagad, spiežot uz šūnas "Recepte", vari izvēlēties kādu no savām receptēm!
4. Kad Notion jautā, vai rādīt saiti arī otrā tabulā (**Show on Receptes**), ieslēdz to. Tad katrā receptē redzēsi, kurās dienās tā ieplānota.
5. Uztaisi **Board** skatu, grupētu pēc **Diena**: tā ir tava nedēļa kolonnās. 🎉

✅ *Tu iemācījies: relations. Tas ir lielākais "aha!" moments Notion.*

---

## 6. solis: iepirkumu saraksts un "glīti"

1. Food Prep lapā pievieno virsrakstu `## 🛒 Iepirkumu saraksts` un zem tā `/todo` sarakstu.
2. Lapas augšā uzraksti `/callout` un ieraksti īsu tekstu, piem., *"Svētdienās gatavoju 3 receptes visai nedēļai"*.
3. Lai sakārtotu lietas blakus: satver bloku aiz **⋮⋮** roktura (parādās pa kreisi, uzbraucot ar peli) un velc to blakus citam blokam. Izveidojas kolonnas.

✅ *Tu iemācījies: lapas izkārtojumu. Tas ir tas, kas padara šablonu skaistu.*

---

## 🎓 Ko tu tagad proti

| Prasme | Kur to izmantos īstā šablonā |
|---|---|
| Datubāzes un properties | Katra šablona pamats |
| Select / Multi-select | Statusi, kategorijas, birkas |
| Views (Table, Board, Gallery) | Tas, kas pircējam "izskatās gudri" |
| Filtri un grupēšana | "Šodien", "Šonedēļ", "Gatavs" skati |
| Relations | Saistītas sistēmas (piem., recepte ↔ nedēļas plāns) |
| Izkārtojums, ikonas, callouts | Skaistums un pirmais iespaids |

Nākamais līmenis (vēlāk): **Rollups** (piem., saskaitīt nedēļas kalorijas no receptēm),
**Formulas**, **Buttons** (poga "Jauna nedēļa"), **Templates** datubāzes iekšienē.

## 📝 Manas piezīmes, lietojot

Lieto savu Food Prep 1–2 nedēļas un pieraksti šeit:
- Kas bija grūti?
- Kas kaitināja?
- Ko gribētos, lai būtu, bet nav?

Šīs piezīmes ir **zelts**: tieši tādas pašas problēmas būs taviem nākotnes pircējiem.

-
-
