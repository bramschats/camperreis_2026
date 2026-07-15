# -*- coding: utf-8 -*-
import json, re, os
geo = open('route_geo.js','r',encoding='utf-8').read()
def grab(name): return re.search(name+r'=(\[.*?\]);', geo, re.S).group(1)
HEEN=grab('ROUTE_HEEN'); FASE2=grab('ROUTE_FASE2'); TERUG=grab('ROUTE_TERUG')

M=[]
def add(id,naam,type,lat,lng,dag,fase,hond,info,link="",caveat=""):
    M.append(dict(id=id,naam=naam,type=type,lat=lat,lng=lng,dag=dag,fase=fase,hond=hond,info=info,link=link,caveat=caveat))
F1="Met de kinderen"; F2="Met z'n tweeën"
# HEEN
add(1,"Doetinchem — vertrek","stop",51.965,6.288,"do 6 aug",F1,True,"Startpunt. Vertrek 's ochtends.")
add(2,"Châlons-en-Champagne","overnachting",48.957,4.365,"do 6 – vr 7 aug",F1,True,"Aankomst donderdag, 2 nachten in de Champagne. Etappe 1 is 535 km — de enige dag net boven 500, dus vroeg starten met een lunchpauze. Vrijdag de champagnestreek in (Épernay, Reims, wijngaarden). Kathedraal en grachtjes in Châlons zelf.")
add(3,"Sancerre","overnachting",47.331,2.846,"za 8 aug",F1,True,"Zaterdag de volgende etappe: wijndorp op een heuvel boven de Loire. Terras met een glas Sancerre, Max mag mee.")
add(4,"Coulon — Marais Poitevin","overnachting",46.323,-0.588,"zo 9 aug",F1,True,"Laatste tussenstop vóór de kust (1 nacht). 'Groene Venetië': platbodem-tochtje en fietsen door het moeras.")
add(5,"Marais Poitevin — fietsen","fietsen",46.30,-0.68,"zo 9 aug",F1,True,"Vlakke fietsroutes langs de kanalen, prima voor de e-bikes en met Max.")
add(6,"Camping 2 Plages & Océan","overnachting",46.090,-1.082,"ma 10 – zo 16 aug",F1,True,"ANKER — vaste boeking, 7 nachten. 122 av. d'Angoulins, Châtelaillon-Plage. Strand op loopafstand.","https://www.2plages-ocean.com/")
add(7,"Châtelaillon-Plage — strand","water",46.075,-1.085,"10–16 aug",F1,True,"Breed strand. Honden overdag in de zomer verboden — Max vroeg/laat uitlaten.",caveat="Hond: alleen vroeg/laat op het strand")
add(8,"La Rochelle","historie",46.159,-1.152,"10–16 aug",F1,True,"Oude haven met de torens, levendig centrum. ~20 min rijden, hondvriendelijke kades.")
add(9,"Île de Ré — fietsen","fietsen",46.20,-1.37,"10–16 aug",F1,True,"Fietseiland met witte dorpjes en zoutpannen. Dagtrip op de e-bikes.")
# FASE 2
add(10,"San Sebastián / Donostia","overnachting",43.318,-1.981,"ma 17 – di 18 aug",F2,True,"Transit 409 km / 4u20; 2 nachten — CULINAIR zwaartepunt. Pintxos-bars in de Parte Vieja (La Cuchara, Ganbara, Casa Vallés/Gilda), Mercado de la Bretxa, Monte Igueldo, Peine del Viento en kustdagtrips (Getaria, Hondarribia, panoramaweg Jaizkibel). Área Autocaravanas Berio (~€11, water) of gratis Illunbe.","https://sansebastianturismoa.eus/en/come/where-to-park/motorhomes-parking-areas/",caveat="Stadsstranden zomer: Max alleen vroeg/laat")
add(11,"Bilbao — tussenstop","stop",43.263,-2.935,"wo 19 aug",F2,True,"Stevige stop onderweg naar de Picos (geen overnachting meer): Casco Viejo, Mercado de la Ribera, pintxos op Plaza Nueva, Guggenheim van buiten (Puppy), en de Funicular de Artxanda voor het uitzicht. Hondvriendelijke terrassen.")
add(12,"San Vicente de la Barquera","stop",43.395,-4.398,"wo 19 aug",F2,True,"Lunchstop onderweg naar de Picos. Cantabrisch vissersstadje, kasteel, zicht op de bergen.")
add(13,"Cangas de Onís","overnachting",43.351,-5.130,"wo 19 – do 20 aug",F2,True,"Transit 226 km / 2u40. Poort tot het westelijke massief. Romeinse brug over de Sella; goede uitvalsbasis voor Covadonga.")
add(14,"Covadonga — heiligdom","historie",43.308,-5.056,"19–20 aug",F2,True,"Basiliek en de Santa Cueva in een groene bergketel.")
add(15,"Lagos de Covadonga","water",43.273,-4.992,"do 20 aug",F2,True,"Bergmeren Enol & Ercina. In de zomer ALLEEN met de verplichte shuttle (camper >5 m mag de berg niet op). Max mag mee in het bagageruim, aangelijnd.","https://www.turismoasturias.es/en/organiza-tu-viaje/como-llegar/acceso-a-lagos",caveat="Camper niet omhoog — verplichte shuttle; hond aangelijnd in bagageruim")
add(16,"Arenas de Cabrales","overnachting",43.297,-4.815,"vr 21 – za 22 aug",F2,True,"Korte hop 33 km / 0u40. Centraal massief. Cabrales-blauwkaas (kaasgrotten), markt.")
add(17,"Ruta del Cares (Poncebos)","wandeling",43.265,-4.840,"vr 21 aug",F2,True,"De klassieker: spectaculaire kloofwandeling. Hond verplicht kort aangelijnd (geen flexlijn) — steile afgronden zonder reling.","https://www.alltrails.com/trail/spain/asturias/pr-pnpe-3-ruta-del-cares--2",caveat="Hond kort aangelijnd; afgronden")
add(18,"Funicular de Bulnes","kabelbaan",43.246,-4.812,"za 22 aug",F2,True,"Ondergrondse funicular naar het autoloze bergdorp Bulnes, met zicht op de Naranjo de Bulnes; daarna te voet terug naar Poncebos via de Canal del Texu (~1u15, pittig pad met afgronden). ~21,50 € retour.","https://blog.telecable.es/funicular-bulnes/",caveat="Hond in box óf muilkorf+lijn; afdaalpad met afgronden")
add(19,"Potes","overnachting",43.155,-4.629,"zo 23 – ma 24 aug",F2,True,"Transit 53 km / 1u via de Desfiladero de la Hermida. Liébana-vallei. Maandagmarkt valt op 24 aug; orujo op een terras.")
add(20,"Teleférico de Fuente Dé","kabelbaan",43.1442,-4.8122,"zo 23 – ma 24 aug",F2,True,"Kabelbaan naar El Cable (1.823 m), dan te voet terug naar Espinama/Fuente Dé via Chalet Real en Áliva (~10-15 km, ~4,5 u afdaling — dé manier om een kabelbaan te nemen en te lopen). Hond VERPLICHT in gesloten box tijdens de rit (+€10 retour).","https://telefericodefuentede.com/tarifas/",caveat="Rit: hond alleen in box (+€10); of alleen dalwandeling")
add(21,"Mogrovejo","historie",43.166,-4.683,"23–24 aug",F2,True,"Idyllisch steendorpje met toren, zicht op de bergen. Authentiek, weinig toeristen.")
add(22,"Santo Toribio de Liébana","historie",43.150,-4.668,"23–24 aug",F2,True,"Klooster in de bergen, rustige omgeving en uitzicht.")
# binnenland-route naar Rioja
add(23,"Aguilar de Campoo","stop",42.795,-4.262,"di 25 aug",F2,True,"Tussenstop door het BINNENLAND (Montaña Palentina) i.p.v. langs de kust — korter (246 km totaal). Romaans stadje, camperplek, bekend van de koekjes.")
add(24,"Laguardia (Rioja Alavesa)","overnachting",42.554,-2.583,"di 25 aug",F2,True,"Binnenland-transit 246 km (Potes→Aguilar 82 km, Aguilar→Laguardia 164 km). Ommuurd wijnstadje, een van de mooiste van Spanje. Gratis camperplek bij de lift naar het centrum.","https://visitriojaalavesa.com/")
add(25,"Elciego — Marqués de Riscal","historie",42.513,-2.620,"25 aug",F2,True,"Iconische wijnarchitectuur (Gehry), te bekijken van buiten tussen de wijngaarden.")
add(26,"Arguedas — Área Autocaravanas","overnachting",42.179,-1.594,"wo 26 aug",F2,True,"Hop 114 km / 1u35. Gratis camperplek aan de rand van de Bardenas (vrij staan in het park zelf is verboden).","https://bardenasreales.es/turismo/normativa-de-uso-turistico/")
add(27,"Bardenas Reales","fietsen",42.21,-1.50,"wo 26 aug",F2,True,"Woestijnlandschap. Camper mag de onverharde lus (Blanca) op; ook mooi op de e-bike. Castildetierra. Hond aangelijnd (max 3 m), niet vrij overdag bij hitte.",caveat="Hond aangelijnd; hitte/schaduw — rij vroeg")
add(28,"Olite","historie",42.480,-1.650,"do 27 aug",F2,True,"Tussenstop i.p.v. Pamplona: middeleeuws koningskasteel (Palacio Real), klein en authentiek dorp. Past beter bij jullie smaak dan de stadsdrukte van Pamplona.")
add(29,"Ochagavía","overnachting",42.908,-1.080,"do 27 aug",F2,True,"Via Olite (39 + 92 km). Een van de mooiste dorpen van Navarra; poort naar het Irati-woud. Camperplek €4 aan de toegangsweg.")
add(30,"Selva de Irati","wandeling",42.97,-1.10,"do 27 aug",F2,True,"Tweede grootste beukenwoud van Europa. Auto's mogen er niet in — wandelen/fietsen. Dagtoegang €5 (cash). Hond mag mee op de paden.","https://discovernavarra.com/en/irati-forest/")
add(31,"Foz de Lumbier","wandeling",42.658,-1.300,"vr 28 aug",F2,True,"Korte beenstrek onderweg: kloof via een oude spoorbaan met tunnels, gieren. Hondvriendelijk.")
add(32,"Jaca","historie",42.570,-0.549,"vr 28 aug",F2,True,"Stop richting Ordesa: romaanse kathedraal, sterrenfort (Ciudadela). Goede plek voor boodschappen.")
add(33,"Torla-Ordesa","overnachting",42.625,-0.111,"vr 28 – za 29 aug",F2,True,"Transit 164 km / 2u25 (geknipt via Lumbier + Jaca). 2 nachten: bergdorp aan de voet van Ordesa. Camping Río Ara / Camping Ordesa.","https://www.eurocampings.co.uk/spain/aragon/huesca/torla/")
add(34,"Pradera de Ordesa — Cola de Caballo","wandeling",42.638,-0.041,"za 29 aug",F2,True,"Volle hike-dag: met de verplichte shuttle vanuit Torla (hond €2 retour, aangelijnd) het dal in, dan de Cola de Caballo-tocht langs de watervallen.","https://www.ordesamonteperdido.com/en/buses/",caveat="Shuttle verplicht; hond €2, aangelijnd")
# TERUG (3 reisdagen)
add(35,"Brive-la-Gaillarde","overnachting",45.159,1.533,"zo 30 aug",F2,True,"Terugreis dag 1: 461 km via de Bielsa-tunnel — direct noordwaarts vanaf Toulouse. Pleisterplaats in de Corrèze met een mooie oude binnenstad en hondvriendelijke terrasjes.")
add(36,"Reims","overnachting",49.258,4.034,"ma 31 aug",F2,True,"Terugreis dag 2: 618 km (de langste dag, ~6,5 u). Champagnestad met indrukwekkende kathedraal; recht op koers richting huis.")
add(37,"Doetinchem — thuis","stop",51.965,6.288,"di 1 sep",F2,True,"Terugreis dag 3: 494 km via Luxemburg. Thuiskomst dinsdag.")
add(38,"Cabrales-kaas & streekmarkt","markt",43.296,-4.808,"21–22 aug",F2,True,"Beroemde blauwkaas uit de berggrotten; streekmarkt rond Arenas — kaas proeven en kopen bij de bron.")
add(39,"Desfiladero de la Hermida (N-621)","bergpas",43.252,-4.601,"zo 23 aug",F2,True,"21 km diepe kloof met rotswanden tot 600 m op de weg naar Potes; dorpje Lebeña, Mirador de Santa Catalina, afkoelen in de Deva. Camper VOORBEHOUD — nationale weg maar smal (~6 m), rij defensief.",caveat="Camper: smal (~6 m), rij defensief")
add(40,"La Concha — strand San Sebastián","water",43.317,-1.994,"17 aug",F2,True,"Iconisch stadsstrand voor een snelle duik tussen de pintxos door.",caveat="Hond: zomers overdag verboden — alleen vroeg/laat")
add(41,"Champagne in Reims","terras",49.255,4.031,"31 aug",F2,True,"Bakermat van de champagne: een glas op een terras in Reims als feestelijke afsluiter van de reis.")
add(42,"Pintxos — Parte Vieja, San Sebastián","terras",43.324,-1.986,"17 aug",F2,True,"Bar-hoppen langs de pintxos-bars van de oude stad — de culinaire avond van de reis; terrasjes hondvriendelijk.")
add(43,"Wijn op een terras — Rioja Alavesa","terras",42.556,-2.580,"25 aug",F2,True,"Rioja drinken tussen de wijngaarden rond Laguardia; bodegas te kust en te keur, Max mag mee op het terras.")
add(44,"Sancerre — wijnterras","terras",47.330,2.847,"8 aug",F1,True,"Frisse witte Sancerre op een terras met uitzicht over de Loire-wijngaarden.")
add(45,"Maandagmarkt Potes","markt",43.157,-4.631,"ma 24 aug",F2,True,"Sfeervolle streekmarkt in het bergstadje; valt precies goed op maandag 24 aug. Lokale kaas, honing en orujo.")
add(46,"Mercado de la Ribera, Bilbao","markt",43.256,-2.923,"18 aug",F2,True,"Grote overdekte markthal aan de rivier — proeven en boodschappen doen midden in de oude stad.")
add(47,"Épernay — champagnestreek","terras",49.044,3.959,"vr 7 aug",F1,True,"Dagje champagne vanuit Châlons: de Avenue de Champagne met de grote huizen, wijngaarden eromheen en proeven op een terras. Max mag mee naar buiten.")
add(48,"La Cuchara de San Telmo","terras",43.3247,-1.9852,"17–18 aug",F2,True,"Miniatuurkeuken van de Parte Vieja; specialiteit gesmoorde runderwang (carrillera) en gegrilde octopus, à la minute. Hond aangelijnd aan de staanbar.")
add(49,"Ganbara","terras",43.3241,-1.9857,"17–18 aug",F2,True,"Seizoenstempel: schaal wilde paddenstoelen met eidooier en een toonbank vol topklasse pintxos. Drukke bar, hond aangelijnd.")
add(50,"Casa Vallés — de Gilda","terras",43.3179,-1.9840,"17–18 aug",F2,True,"Geboorteplek van de Gilda (olijf-ansjovis-piparra), de iconische pintxo van de stad. Klein terras, hond aangelijnd.")
add(51,"Mercado de la Bretxa","markt",43.3232,-1.9843,"17–18 aug",F2,True,"Centrale stadsmarkt voor Baskische producten (Idiazabal-kaas, conservas, txakoli). Terrassen buiten, hond aangelijnd.")
add(52,"Peine del Viento","uitzichtpunt",43.3157,-2.0175,"17–18 aug",F2,True,"Stalen sculpturen van Chillida tegen de rotsen aan het einde van de baai, met spuitende blaasgaten. Gratis, fotogeniek eindpunt van de kustwandeling.")
add(53,"Monte Igueldo (funicular)","kabelbaan",43.3159,-2.0107,"17–18 aug",F2,True,"Historische kabeltram (1912) naar het klassieke uitzicht over de La Concha-baai; omhoog en langs het pad teruglopen. Hond mag mee (+€2,50).","https://www.monteigueldo.es/en-faq",caveat="Rijd de camper NIET naar boven — parkeer beneden")
add(54,"Jaizkibel — panoramaweg (GI-3440)","bergpas",43.376,-1.860,"dagtrip SS",F2,True,"Een van de mooiste kustwegen van Baskenland: kamweg boven de kliffen tussen Hondarribia en Pasaia, met stop bij het Santuario de Guadalupe. Camper GESCHIKT — volg strikt de GI-3440, niet de smalle dorpsweggetjes.",caveat="Camper: volg de GI-3440 zelf (geschikt)")
add(55,"Getaria — kaap El Ratón","wandeling",43.3045,-2.2015,"dagtrip SS",F2,True,"Authentiek vissersdorp; korte ronde (~2 km) over de muis-kaap (El Ratón) naar de vuurtoren, daarna gegrilde vis en txakoli op een haventerras. Hond aangelijnd.")
add(56,"Hondarribia — oude stad & Marina","historie",43.3620,-1.7930,"dagtrip SS",F2,True,"Ommuurde bovenstad plus kleurrijke vissershuizen in de Marina; txakoli-terrassen. Hondvriendelijk wandelpad langs de Bidasoa.")
add(57,"Pasaia San Juan","historie",43.3245,-1.9235,"dagtrip SS",F2,True,"Pittoresk vissersgehucht aan de voet van de Jaizkibel, huizen boven het water; veerbootje over de baai. Hond aangelijnd.")
add(58,"Monte Ulia — wandeling SS→Pasaia","wandeling",43.3230,-1.9760,"17–18 aug",F2,True,"Groene kustrug (235 m) langs oude walvis-uitkijkposten naar de Faro de la Plata; ~6 km naar Pasaia, terug met de bus. Stevig wandelen met zeezicht, hond aangelijnd.")
add(59,"Funicular de Artxanda (Bilbao)","kabelbaan",43.2637,-2.9270,"wo 19 aug",F2,True,"Korte kabeltram naar het beste panorama over Bilbao en de Nervión-vallei; boven wandelpaden en terras. Hond gratis mee in de huisdiercoupé.")
add(60,"Puerto de San Glorio + Mirador de Llesba","bergpas",43.0667,-4.7667,"Potes",F2,True,"Paspunt 1.609 m met bronzen berenbeeld en panorama over het Centrale Massief. Hoofdpas N-621 camper GESCHIKT (brede weg, ruime bochten); het smalle zijweggetje (2 km) naar het beeld met voorbehoud — evt. beneden parkeren.",caveat="Hoofdpas geschikt; zijweg naar beeld smal")
add(61,"Puerto de Panderruedas + Mirador Piedrashitas","bergpas",43.1291,-4.9804,"Cangas/Potes",F2,True,"Smalle, rustige bergweg naar 1.450 m; 15 min lopen naar panorama over Valle de Valdeón. Camper VOORBEHOUD — rustig rijden, haarspelden, weinig verkeer.",caveat="Camper: smal met haarspelden, kalm rijden")
add(62,"Desfiladero de los Beyos (N-625)","bergpas",43.200,-5.050,"Cangas",F2,True,"12 km Sella-kloof, een van de mooiste kloofwegen van Spanje. Camper VOORBEHOUD — smal, bochtig, natuurlijke tunnels; op drukke zomerdagen zijn tegenliggers lastig.",caveat="Camper: smal/bochtig — voorzichtig")
add(63,"Puerto del Pontón","bergpas",43.147,-5.033,"Cangas/Potes",F2,True,"Brede, comfortabele pas (1.280 m) met zicht over Valle de Sajambre en beukenbossen; parkeerplaats op de top. Camper GESCHIKT.",caveat="Camper geschikt (breed)")
add(64,"Vega de Ario (wandeling)","wandeling",43.276,-4.985,"Cangas",F2,True,"Klim vanaf de meren van Covadonga naar een refugio (~1.630 m), spectaculair balkon tegenover het Centraal Massief en de Cares. ~6,5 km enkel, matig-pittig.",caveat="Via shuttle tot Lagos; hond aangelijnd")
add(65,"Mirador de Ordiales","wandeling",43.270,-4.996,"Cangas",F2,True,"Lange, pittige bergtocht (PR-PNPE 5, ~21 km h/t, 7-8 u) via Vegarredonda naar het graf van Pedro Pidal aan een 1.000 m-afgrond. Alleen voor een volle wandeldag.",caveat="Pittig; shuttle tot Lagos; hond aangelijnd")
add(66,"Río Sella / Deva — zwemwater","water",43.210,-5.030,"Cangas/Potes",F2,True,"Heldere natuurlijke poelen langs de N-625 (Sella) en in de Hermida (Deva) — afkoelen in de augustushitte, hondvriendelijk buiten de strengste parkzones.")
add(67,"Weg naar Sotres / Tresviso","bergpas",43.236,-4.759,"Arenas",F2,True,"Mooie hooggelegen dorpen, MAAR de weg is te smal, steil en plaatselijk kapot voor een 7 m camper. Laat de camper in Arenas/Poncebos en neem een 4x4-taxi.",caveat="Camper VERMIJDEN — te smal/steil")
add(68,"Senda del Oso (vía verde)","fietsen",43.247,-6.000,"Cangas (uithoek)",F2,True,"Vlakke greenway op oud spoor door de Trubia-vallei langs een berenreservaat; ideaal voor e-bikes met brede banden, hond mag mee (karretjes tot 40 kg). ~1-1,5 u rijden — aparte dag.")
add(69,"Faja de Pelay + Cola de Caballo (balkonrondje)","wandeling",42.6408,-0.0800,"Torla/Ordesa",F2,True,"Pittige rondwandeling (~20 km, +650 m) via de Senda de los Cazadores en de adembenemende balkonroute Faja de Pelay, terug langs Cola de Caballo. Voor stevige wandelaars het mooiste van Ordesa.","https://www.rutaspirineos.org/rutas/circular-cola-de-caballo-por-faja-de-pelay",caveat="Pittig (~20 km); hond aangelijnd")
add(70,"Embalse de Irabia (Irati)","water",42.9333,-1.0836,"Ochagavía",F2,True,"Vlakke bosroute langs een spiegelend stuwmeer in het Irati-beukenwoud; schaduw en zwemwater voor Max. Hond aangelijnd.")
add(71,"Puerto de Belagua / Larra (NA-137)","bergpas",42.977,-0.756,"Ochagavía/Isaba",F2,True,"Heerlijke panoramaklim naar 1.765 m met het karstplateau Larra; brede, uitstekend aangelegde weg met 7 haarspelden. Camper GESCHIKT. Let op kuddehonden op de weiden.",caveat="Camper geschikt; kuddehonden op weiden")
add(72,"Telecabina de Panticosa","kabelbaan",42.7181,-0.2739,"Pyreneeën (dagtrip)",F2,True,"De enige echt hond-toegankelijke kabelbaan in de regio (zomer, klein/middelgroot): omhoog en naar beneden wandelen. Open 4 jul–30 aug. Bevestig de hondregel aan de kassa.","https://www.formigal-panticosa.com/preguntas-frecuentes-formigal-panticosa-verano.html",caveat="Bevestig hondregel vooraf (kassa)")
add(73,"Puerto de Somport (N-330)","bergpas",42.7936,-0.5242,"corridor Jaca",F2,True,"Brede, comfortabele Pyreneeën-overgang (ruime tunnel of de oude passweg N-330A over de top) langs het monumentale station van Canfranc. Camper GESCHIKT.",caveat="Camper geschikt (breed)")
add(74,"Cascada del Cubo (Irati)","wandeling",42.920,-1.070,"Ochagavía",F2,True,"Korte familieroute (~20 min) naar een fraaie waterval in het beukenbos; combineert goed met Embalse de Irabia. Hond aangelijnd.")
add(75,"Ujué","historie",42.5119,-1.5017,"Olite-regio",F2,True,"Een van de mooiste dorpen van Navarra: stenen steegjes rond een vestingkerk, weids uitzicht en een authentiek terras. Parkeer onderaan, de kern is voetgangers.")
add(76,"Embalse de Yesa — zwemwater","water",42.6167,-1.150,"corridor Navarra",F2,True,"Groot turquoise stuwmeer; baden toegestaan aan de Aragonese oever (Salvatierra de Esca–Sigües), hondvriendelijk en verfrissend in augustus.")
add(77,"Mirador Foz de Arbayún","uitzichtpunt",42.6558,-1.240,"Lumbier",F2,True,"300 m diepe kalksteenkloof met cirkelende gieren; korte stop met groots uitzicht, combineert met de Foz de Lumbier. Kleine parking — kom vroeg of laat.")
add(78,"Bardenas — Castildetierra & Alto de Aguilares","uitzichtpunt",42.205,-1.428,"Arguedas",F2,True,"Castildetierra is het iconische erosie-monoliet van de Bardenas; Alto de Aguilares geeft het weidse badlands-overzicht. Hond aangelijnd, let op de hitte.")
add(79,"Puerto de Cotefablo (tunnel, N-260)","bergpas",42.6236,-0.2517,"route naar Torla",F2,True,"Kortste route Biescas→Torla, maar de tunnel (683 m) is smal en één rijstrook. Camper VOORBEHOUD — stapvoets, tegenliggers afwachten; alternatief via Fiscal/Sarvisé.",caveat="Smalle tunnel — voorzichtig of omrijden")
add(80,"Cañón de Añisclo-weg (HU-631)","bergpas",42.503,0.030,"Ordesa-sector",F2,True,"Prachtige kloofwandeling, MAAR de eenrichtingsweg is te smal (~4 m doorrijhoogte, steenslag) — campers verboden. Parkeer in Escalona/Sarvisé, of sla de weg over.",caveat="Camper VERBODEN op deze weg")
add(81,"Mirador de Piedrasluengas","bergpas",43.0414,-4.4581,"Potes-corridor",F2,True,"Balkon over de Liébana-vallei op de brede pasweg CL-627 (1.355 m) richting Aguilar de Campoo — de binnenlandroute naar Rioja. Camper GESCHIKT.",caveat="Camper geschikt (breed)")

# ITINERARY
I=[]
def day(phase,date,title,mid,drive,tag,items): I.append(dict(phase=phase,date=date,title=title,mid=mid,drive=drive,tag=tag,items=items))
day(F1,"do 6 – vr 7 aug","Doetinchem → Champagne (2 nachten)",2,"535 km · 5u55","overnachting",
    [("Donderdag: rijden (enige dag net boven 500 km) — vroeg starten, lunchpauze","stop",False,""),
     ("Vrijdag: champagnestreek — Épernay, Reims, wijngaarden, proeverij op een terras","terras",True,"hond mee naar buiten"),
     ("Kathedraal en grachtjes van Châlons zelf","historie",True,"")])
day(F1,"za 8 aug","→ Sancerre (Loire)",3,"305 km · 3u20","overnachting",
    [("Zaterdag verder; wijndorp op de heuvel, glas Sancerre op een terras","terras",True,"hond welkom")])
day(F1,"zo 9 aug","→ Coulon · Marais Poitevin",4,"357 km · 4u10","overnachting",
    [("Laatste tussenstop vóór de kust","stop",False,""),
     ("Platbodem-tochtje in 'Groene Venetië'","water",True,""),
     ("Fietsen langs de kanalen op de e-bikes","fietsen",True,"")])
day(F1,"ma 10 aug","→ Châtelaillon-Plage — ANKER",6,"70 km · 1u00","overnachting",
    [("Inchecken Camping 2 Plages & Océan (t/m 16 aug)","overnachting",True,"vaste boeking")])
day(F1,"ma 10 – zo 16 aug","Gezinsweek aan de kust",6,"lokaal","water",
    [("Strand Châtelaillon — Max vroeg/laat (zomerverbod overdag)","water",True,"hond alleen vroeg/laat"),
     ("La Rochelle: oude haven en torens","historie",True,""),
     ("Île de Ré op de fiets","fietsen",True,"")])
day(F2,"ma 17 – di 18 aug","Châtelaillon → San Sebastián (2 nachten · culinair)",10,"409 km · 4u20","overnachting",
    [("Maandag rijden; dinsdag culinaire dag — pintxos hoppen (La Cuchara, Ganbara, Gilda)","terras",True,"hond aan de bar aangelijnd"),
     ("Peine del Viento, Monte Igueldo (funicular), Mercado de la Bretxa","uitzichtpunt",True,""),
     ("Dagtrip Getaria of Hondarribia + panoramaweg Jaizkibel","bergpas",True,"camper: volg de GI-3440"),
     ("Stadsstranden: Max alleen vroeg/laat","water",True,"hond vroeg/laat")])
day(F2,"wo 19 – do 20 aug","San Sebastián → Bilbao → Cangas de Onís (2 nachten)",13,"≈328 km · 3u55","overnachting",
    [("Onderweg: stevige stop in Bilbao (Casco Viejo, Mercado de la Ribera, Artxanda-uitzicht)","historie",True,""),
     ("Covadonga — basiliek en de Santa Cueva","historie",True,""),
     ("Lagos de Covadonga met de shuttle (camper niet omhoog)","water",True,"shuttle verplicht; hond aangelijnd"),
     ("Wandelbalkon Vega de Ario of Ruta de los Lagos","wandeling",True,"")])
day(F2,"vr 21 – za 22 aug","→ Arenas de Cabrales · Picos centraal (2 nachten)",16,"33 km · 0u40","overnachting",
    [("Ruta del Cares — kloofwandeling, hond kort aangelijnd","wandeling",True,"afgronden, geen flexlijn"),
     ("Bulnes & uitzicht op de Naranjo de Bulnes","wandeling",True,""),
     ("Cabrales-blauwkaas en markt","markt",True,"")])
day(F2,"zo 23 – ma 24 aug","→ Potes · Liébana, Picos oost (2 nachten)",19,"53 km · 1u00","overnachting",
    [("Via de Desfiladero de la Hermida","stop",True,""),
     ("Fuente Dé — dalwandeling (kabelbaan vraagt hondenbox)","wandeling",True,"kabelbaan: hond alleen in box"),
     ("Mogrovejo: idyllisch steendorp + Santo Toribio","historie",True,""),
     ("Maandagmarkt Potes (24 aug) + orujo op een terras","markt",True,"")])
day(F2,"di 25 aug","→ Laguardia · door het BINNENLAND (wijnstop)",24,"246 km · 4u00","overnachting",
    [("Binnenland via de Montaña Palentina i.p.v. de kust","stop",False,""),
     ("Tussenstop Aguilar de Campoo (romaans, koekjes)","historie",True,"82 km"),
     ("Laguardia: ommuurd wijnstadje, wijn op een terras","terras",True,"hond welkom"),
     ("Marqués de Riscal (Elciego) van buiten","historie",True,"")])
day(F2,"wo 26 aug","→ Arguedas · Bardenas Reales",26,"114 km · 1u35","overnachting",
    [("Woestijnlus Blanca met de camper of e-bike","fietsen",True,"hond aangelijnd, hitte"),
     ("Castildetierra — iconische rotsformatie","historie",True,""),
     ("Slapen op de gratis área Arguedas (niet in het park)","overnachting",True,"")])
day(F2,"do 27 aug","→ Olite → Ochagavía · Irati",29,"39 + 92 km · 2u05","overnachting",
    [("Tussenstop Olite: middeleeuws koningskasteel","historie",True,"i.p.v. Pamplona"),
     ("Middag: wandeling in de Selva de Irati","wandeling",True,"hond mag mee; €5 toegang")])
day(F2,"vr 28 aug","Ochagavía → (Lumbier · Jaca) → Torla-Ordesa",33,"164 km · 2u25","overnachting",
    [("Beenstrek: Foz de Lumbier (kloof + tunnels)","wandeling",True,""),
     ("Stop Jaca: kathedraal, sterrenfort, boodschappen","historie",True,""),
     ("Aankomst Torla — 2 nachten","overnachting",True,"")])
day(F2,"za 29 aug","Ordesa — Cola de Caballo (volle hike-dag)",34,"shuttle","wandeling",
    [("Shuttle Torla → Pradera (hond €2, aangelijnd)","stop",True,"shuttle verplicht"),
     ("Cola de Caballo-tocht langs de watervallen","wandeling",True,"hele dag")])
day(F2,"zo 30 aug","Ordesa → Brive-la-Gaillarde (terugreis 1/3)",35,"461 km · 5u40","overnachting",
    [("Via de Bielsa-tunnel en Toulouse, direct noordwaarts","stop",False,""),
     ("Corrèze: oude binnenstad, hondvriendelijk terras","terras",True,"")])
day(F2,"ma 31 aug","Brive → Reims (terugreis 2/3 — langste dag)",36,"618 km · 6u30","overnachting",
    [("De langste dag (~6,5 u), maar recht op huis aan","stop",False,""),
     ("Reims: kathedraal en champagne op een terras","terras",True,"")])
day(F2,"di 1 sep","Reims → Doetinchem (terugreis 3/3, thuis)",37,"494 km · 5u20","stop",
    [("Via Luxemburg naar huis","stop",False,""),
     ("Thuiskomst dinsdag","stop",False,"")])

OVER_HTML = '\n<p class="lead">Een grote lus van ruim drie weken: met het hele gezin langs de Franse westkant omlaag naar een strandweek bij La Rochelle, daarna met z\'n tweeën (en Max) een actieve rondreis door Noord-Spanje met de Picos de Europa als kloppend hart, en via de Pyreneeën direct terug naar huis. Andere wegen heen dan terug, korte ritten ter plekke, en overal de hond mee.</p>\n\n<h3>Heenreis — met de kinderen (6–10 aug)</h3>\n<p>In rustige etappes naar het zuidwesten: een avond in Châlons-en-Champagne, een glas wijn op een terras in Sancerre boven de Loire, en twee nachten ontspannen in het Marais Poitevin — het "Groene Venetië" met platbodems en vlakke fietspaden. Daarna inchecken op de vaste camping in Châtelaillon-Plage.</p>\n\n<h3>Strandweek — La Rochelle (10–16 aug)</h3>\n<p>Zeven dagen kust met het hele gezin. Strand op loopafstand (Max vroeg en laat), dagtripjes naar de oude haven van La Rochelle en het fietseiland Île de Ré. Even geen kilometers maken, gewoon zomer.</p>\n\n<h3>Baskenland — San Sebastián & Bilbao (17–18 aug)</h3>\n<p>Het tweede deel begint culinair: een avond pintxos hoppen door de oude stad van San Sebastián, en de dag erna Bilbao met zijn Casco Viejo, de Mercado de la Ribera en het Guggenheim van buiten. Mooi opwarmertje voor de bergen.</p>\n\n<h3>Het zwaartepunt — Picos de Europa (19–24 aug)</h3>\n<p>Zes nachten, dwars door de drie massieven van west naar oost. <b>Wat te doen:</b> met de shuttle omhoog naar de bergmeren van Covadonga; de spectaculaire kloofwandeling Ruta del Cares; het uitzicht op de Naranjo de Bulnes; dalwandelingen bij Fuente Dé; en de idyllische steendorpjes Mogrovejo en Liébana rond Potes, met de maandagmarkt en een glas orujo. Stevige wandelingen, koele bergnachten en authentieke dorpen — precies waar deze reis om draait.</p>\n\n<h3>Wijn, woestijn en kastelen — La Rioja & Navarra (25–27 aug)</h3>\n<p>Door het binnenland naar Laguardia, een ommuurd wijnstadje midden in de Rioja Alavesa — wijn op een terras tussen de wijngaarden. Daarna het verrassende woestijnlandschap van de Bardenas Reales (per camper of e-bike), en het middeleeuwse koningskasteel van Olite op weg naar het sprookjesachtige beukenwoud Selva de Irati.</p>\n\n<h3>De Pyreneeën — Ordesa (28–29 aug)</h3>\n<p>Via de kloof van Lumbier en het stadje Jaca naar Torla, poort van Nationaal Park Ordesa. Eén volle dag voor de grote tocht: met de shuttle het dal in en wandelen langs de watervallen tot de Cola de Caballo — het bergafscheid van de reis.</p>\n\n<h3>Terugreis — direct naar huis (30 aug–1 sep)</h3>\n<p>In drie reisdagen recht naar het noorden: via Brive-la-Gaillarde en Reims (champagne!) terug naar Doetinchem. Geen omweg, ander deel van Frankrijk dan de heenweg.</p>\n\n<h3>Goed om te weten</h3>\n<p><b>Hond Max:</b> overal mee, maar let op — stranden zijn \'s zomers overdag vaak verboden (vroeg/laat uitlaten), de meren van Covadonga en het Ordesa-dal doe je met de verplichte shuttle (aangelijnd), en voor de kabelbaan Fuente Dé is een transportbox nodig — kies daar de dalwandeling. <b>Reserveren:</b> de gezinscamping staat; boek populaire camperplekken in het hoogseizoen vooruit of kom vóór de middag aan. <b>Hitte:</b> zoek bij warmte rivier- en meerwater op — fijner dan de zee, en hondvriendelijk.</p>\n'
TOTAL_KM = 1267 + 1482 + 1573
NIGHTS = 26
KLEUR={"overnachting":"#1d4ed8","bergpas":"#92400e","kabelbaan":"#db2777","uitzichtpunt":"#ca8a04","wandeling":"#15803d","fietsen":"#0d9488","markt":"#b45309","historie":"#7c3aed","terras":"#be123c","water":"#0284c7","stop":"#64748b"}
LABEL={"overnachting":"Overnachting","bergpas":"Bergpas / weg","kabelbaan":"Kabelbaan","uitzichtpunt":"Uitzichtpunt","wandeling":"Wandelen","fietsen":"Fietsen","markt":"Markt","historie":"Historie / doen","terras":"Terras / wijn","water":"Water / zwemmen","stop":"Stop / transit"}

import urllib.parse
for _m in M:
    _m['maps']='https://www.google.com/maps/search/?api=1&query='+urllib.parse.quote(_m['naam'])

html = """<!DOCTYPE html>
<html lang="nl"><head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Camperreis 2026 — Atlantische kust · Picos de Europa · Pyreneeën</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
:root{--ink:#0f172a;--muted:#64748b;--line:#e2e8f0;--bg:#f8fafc;--card:#fff;}
*{box-sizing:border-box}
html,body{margin:0;padding:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--bg)}
header{padding:18px 22px;background:#fff;border-bottom:1px solid var(--line)}
header h1{margin:0 0 4px;font-size:20px;font-weight:700}
header .meta{color:var(--muted);font-size:13.5px}
header .meta b{color:var(--ink)}
.phasebar{display:flex;gap:18px;margin-top:10px;flex-wrap:wrap;font-size:12.5px}
.phasebar span{display:inline-flex;align-items:center;gap:6px;color:var(--muted)}
.dot{width:18px;height:4px;border-radius:2px;display:inline-block}
.wrap{display:flex;height:calc(100vh - 96px);min-height:520px}
#map{flex:1 1 60%;height:100%}
.side{flex:1 1 40%;max-width:520px;overflow-y:auto;background:var(--bg);padding:14px 16px}
.controls{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}
.chip{font-size:12px;border:1px solid var(--line);background:#fff;border-radius:999px;padding:5px 10px;cursor:pointer;user-select:none;display:inline-flex;align-items:center;gap:6px}
.chip .sw{width:10px;height:10px;border-radius:50%}
.chip.off{opacity:.38}
.phase-h{position:sticky;top:0;background:var(--bg);padding:8px 2px 6px;font-size:13px;font-weight:700;letter-spacing:.02em;text-transform:uppercase;color:#334155;border-bottom:2px solid var(--line);z-index:2;margin-top:6px}
.phase-h .tag{font-weight:600;text-transform:none;letter-spacing:0;font-size:11.5px;color:#fff;border-radius:999px;padding:2px 8px;margin-left:6px}
.card{background:var(--card);border:1px solid var(--line);border-left-width:4px;border-radius:10px;padding:10px 12px;margin:9px 0;cursor:pointer;transition:box-shadow .15s}
.card:hover{box-shadow:0 4px 14px rgba(15,23,42,.09)}
.card .top{display:flex;justify-content:space-between;gap:8px;align-items:baseline}
.card .date{font-size:11.5px;color:var(--muted);font-weight:600;text-transform:uppercase;letter-spacing:.03em}
.card .drive{font-size:11.5px;color:#fff;background:#475569;border-radius:999px;padding:2px 8px;white-space:nowrap}
.card .drive.local{background:#94a3b8}
.card h3{margin:5px 0 7px;font-size:15px}
.card ul{margin:0;padding:0;list-style:none}
.card li{font-size:13px;color:#334155;padding:3px 0 3px 18px;position:relative;line-height:1.35}
.card li:before{content:"";position:absolute;left:2px;top:8px;width:7px;height:7px;border-radius:50%;background:var(--c,#94a3b8)}
.card li .paw{color:#a16207}
.card li .note{color:var(--muted);font-style:italic}
.legend{font-size:12px;color:var(--muted);margin-top:6px;line-height:1.6}
.leaflet-popup-content{font-size:13px;line-height:1.4}
.leaflet-popup-content b.cv{color:#b45309}
.tabs{display:flex;gap:6px;margin-bottom:10px}
#overblad{font-size:13.5px;color:#334155;line-height:1.55}
#overblad h3{font-size:15px;color:#0f172a;margin:16px 0 6px}
#overblad p{margin:0 0 9px}
#overblad .lead{font-size:14px;color:#0f172a;background:#fff;border:1px solid var(--line);border-left:4px solid #15803d;border-radius:10px;padding:11px 13px;margin-bottom:12px}
.tab{flex:1;font-size:13px;font-weight:600;border:1px solid var(--line);background:#fff;border-radius:8px;padding:7px;cursor:pointer;color:#475569}
.tab.active{background:#0f172a;color:#fff;border-color:#0f172a}
.card p.why{margin:0;font-size:13px;color:#334155;line-height:1.4}
.card p.cv{margin:6px 0 0;font-size:12.5px;color:#b45309}
.card a{font-size:12.5px}
.card .paw{color:#a16207}
@media(max-width:820px){.wrap{flex-direction:column;height:auto}#map{height:52vh;flex:none;width:100%}.side{max-width:none;height:auto;flex:none}}
</style></head><body>
<header>
<h1>Camperreis 2026 · Atlantische kust → Picos de Europa → Pyreneeën</h1>
<div class="meta"><b>do 6 aug – di 1 sep 2026</b> · """+str(NIGHTS)+""" nachten · ± <b>"""+f"{TOTAL_KM:,}".replace(',','.')+""" km</b> · grote lus, andere wegen heen dan terug · 🐾 Max altijd mee</div>
<div class="phasebar">
 <span><i class="dot" style="background:#6366f1"></i> Heenreis (met de kinderen)</span>
 <span><i class="dot" style="background:#15803d"></i> Rondreis Spanje (met z'n tweeën)</span>
 <span><i class="dot" style="background:#d97706"></i> Terugreis in 3 dagen (direct via Toulouse)</span>
</div>
</header>
<div class="wrap">
 <div id="map"></div>
 <div class="side">
   <div class="tabs"><button id="tab-plan" class="tab active">Dagplanning</button><button id="tab-poi" class="tab">POI's</button><button id="tab-over" class="tab">Over de reis</button></div>
   <div class="controls" id="filters"></div>
   <div id="timeline"></div>
   <div id="poilist" style="display:none"></div>
   <div id="overblad" style="display:none"></div>
   <div class="legend" id="legend"></div>
 </div>
</div>
<script>
const KLEUR=""" + json.dumps(KLEUR, ensure_ascii=False) + """;
const LABEL=""" + json.dumps(LABEL, ensure_ascii=False) + """;
const MARKERS=""" + json.dumps(M, ensure_ascii=False) + """;
const ITIN=""" + json.dumps(I, ensure_ascii=False) + """;
const OVER=""" + json.dumps(OVER_HTML, ensure_ascii=False) + """;
const ROUTE_HEEN=""" + HEEN + """;
const ROUTE_FASE2=""" + FASE2 + """;
const ROUTE_TERUG=""" + TERUG + """;
const map=L.map('map',{scrollWheelZoom:true});
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{attribution:'© OpenStreetMap-bijdragers',maxZoom:18}).addTo(map);
L.polyline(ROUTE_HEEN,{color:'#6366f1',weight:4,opacity:.75}).addTo(map);
L.polyline(ROUTE_FASE2,{color:'#15803d',weight:4,opacity:.8}).addTo(map);
L.polyline(ROUTE_TERUG,{color:'#d97706',weight:4,opacity:.8}).addTo(map);
const layers={}, byId={};
MARKERS.forEach(s=>{
  const m=L.circleMarker([s.lat,s.lng],{radius:s.type==='overnachting'?8:6,color:'#fff',weight:2,fillColor:KLEUR[s.type]||'#555',fillOpacity:1});
  let pop='<strong>'+s.naam+'</strong>'+(s.hond?' 🐾':'')+'<br><em>'+(s.dag||'')+'</em><br>'+(s.info||'');
  if(s.caveat) pop+='<br><b class="cv">⚠ '+s.caveat+'</b>';
  if(s.link) pop+='<br><a href="'+s.link+'" target="_blank" rel="noopener">Meer info / boeken</a>';
  if(s.maps) pop+='<br><a href="'+s.maps+'" target="_blank" rel="noopener">📍 Google Maps</a>';
  m.bindPopup(pop); m.addTo(map);
  (layers[s.type]=layers[s.type]||[]).push(m); byId[s.id]=m;
});
map.fitBounds(L.latLngBounds(MARKERS.map(s=>[s.lat,s.lng])).pad(0.12));
const fbox=document.getElementById('filters');
const order=['overnachting','bergpas','kabelbaan','wandeling','fietsen','water','uitzichtpunt','markt','historie','terras','stop'];
const state={};
order.forEach(t=>{ if(!layers[t])return; state[t]=true;
  const c=document.createElement('div'); c.className='chip';
  c.innerHTML='<span class="sw" style="background:'+KLEUR[t]+'"></span>'+LABEL[t];
  c.onclick=()=>{state[t]=!state[t]; c.classList.toggle('off',!state[t]); layers[t].forEach(m=> state[t]?m.addTo(map):map.removeLayer(m)); };
  fbox.appendChild(c);
});
const tl=document.getElementById('timeline'); let curPhase=null;
const tagColor={ "Met de kinderen":"#6366f1", "Met z'n tweeën":"#15803d" };
ITIN.forEach(d=>{
  if(d.phase!==curPhase){ curPhase=d.phase;
    const h=document.createElement('div'); h.className='phase-h';
    h.innerHTML='Fase<span class="tag" style="background:'+tagColor[d.phase]+'">'+d.phase+'</span>'; tl.appendChild(h); }
  const card=document.createElement('div'); card.className='card';
  card.style.borderLeftColor=KLEUR[d.tag]||'#94a3b8';
  const local=(d.drive==='lokaal'||d.drive==='—'||d.drive==='shuttle');
  let lis=d.items.map(it=>{const c=KLEUR[it[1]]||'#94a3b8';const paw=it[2]?' <span class="paw">🐾</span>':'';const note=it[3]?' <span class="note">— '+it[3]+'</span>':'';return '<li style="--c:'+c+'">'+it[0]+paw+note+'</li>';}).join('');
  card.innerHTML='<div class="top"><span class="date">'+d.date+'</span><span class="drive'+(local?' local':'')+'">'+d.drive+'</span></div><h3>'+d.title+'</h3><ul>'+lis+'</ul>';
  card.onclick=()=>{ const m=byId[d.mid]; if(m){ map.setView(m.getLatLng(),9,{animate:true}); m.openPopup(); } };
  tl.appendChild(card);
});
// POI's per categorie
const poibox=document.getElementById('poilist');
order.forEach(t=>{ if(!layers[t]) return;
  const items=MARKERS.filter(m=>m.type===t);
  const h=document.createElement('div'); h.className='phase-h';
  h.innerHTML='<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:'+KLEUR[t]+';margin-right:7px"></span>'+LABEL[t]+' <span style="color:#94a3b8;font-weight:500">('+items.length+')</span>';
  poibox.appendChild(h);
  items.forEach(sp=>{
    const card=document.createElement('div'); card.className='card'; card.style.borderLeftColor=KLEUR[t];
    let inner='<div class="top"><span class="date">'+(sp.dag||'')+'</span>'+(sp.hond?'<span class="paw">🐾</span>':'')+'</div><h3>'+sp.naam+'</h3><p class="why">'+(sp.info||'')+'</p>';
    if(sp.caveat) inner+='<p class="cv">⚠ '+sp.caveat+'</p>';
    if(sp.link) inner+='<a href="'+sp.link+'" target="_blank" rel="noopener">Meer info / boeken</a>';
    if(sp.maps) inner+=(sp.link?' \u00b7 ':'')+'<a href="'+sp.maps+'" target="_blank" rel="noopener">📍 Google Maps</a>';
    card.innerHTML=inner;
    card.onclick=(e)=>{ if(e.target.tagName==='A')return; const m=byId[sp.id]; if(m){map.setView(m.getLatLng(),10,{animate:true}); m.openPopup();} };
    poibox.appendChild(card);
  });
});
document.getElementById('overblad').innerHTML=OVER;
const TABS=[['tab-plan','timeline'],['tab-poi','poilist'],['tab-over','overblad']];
function showTab(id){TABS.forEach(function(t){var bt=document.getElementById(t[0]),pe=document.getElementById(t[1]);var on=(t[0]===id);bt.classList.toggle('active',on);pe.style.display=on?'':'none';});}
TABS.forEach(function(t){document.getElementById(t[0]).onclick=function(){showTab(t[0]);};});
showTab('tab-plan');
document.getElementById('legend').innerHTML='Twee tabs: <b>Dagplanning</b> (etappes per dag) en <b>POI per categorie</b> (alle bestemmingen met de reden om er heen te gaan). 🐾 = hond Max welkom; let op de waarschuwingen in de popups (stranden zomer, shuttles, kabelbaan-box). Klik een item of marker om in te zoomen.';
</script>
</body></html>"""
outdir='/sessions/wonderful-nice-fermi/mnt/Claude/Camperreis 2026'; os.makedirs(outdir,exist_ok=True)
out=os.path.join(outdir,'Camperreis-2026-Picos-Pyreneeen.html')
open(out,'w',encoding='utf-8').write(html)
open(os.path.join(outdir,'index.html'),'w',encoding='utf-8').write(html)
print('written',out,'KB',round(os.path.getsize(out)/1024,1),'TOTAL',TOTAL_KM,'markers',len(M),'days',len(I))
