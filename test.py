from openai import OpenAI
import os
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

completion = client.chat.completions.create(
    model="o1-mini",
    messages=[
        
        {
            "role": "user",
            "content": """formattami questo trascrizione, formattata e strutturata bene, con evidenziati chi sta parlando in questo momento. NON TRALASCIARE NULLA, NON RIASSUMERE NULLA, RIPORTAMI TUTTE LE PAROLE DETTE. correggi solo la punteggiatura, e alcune parole senza senso, se devi farli fai dei cambiamenti MINIMALI, e cerca di capire sempre chi sta parlando in quel momento.


trascrizione: 0:02
tii della Camera dei Deputati l'ordine del giorno reca l'audizione in videoconferenza del Presidente della Regione Siciliana e Commissario
0:09
straordinario per la valorizzazione energetica e la gestione del ciclo dei rifiuti nella medesima regione Renato Schifani che saluto e ringrazio della
0:17
presenza il presidente Schifani accompagnato l'ingegner Salvatore Cocina dirigente generale del Dipartimento
0:23
della Protezione Civile della Regione Siciliana e dirigente responsabile dell'ufficio speciale per la valutazione energetica e la gestione del Cico di
0:29
rifiuti D l'avvocato Gaetano armao esperto del presidente e dell'ingegner
0:35
Giovanna piccone consulente del presidente a cui vanno anche i miei ringraziamenti per la presenza ricordo
0:40
che all'istituto odierna si svolge nelle forme di audizione libera ed è aperta la partecipazione del remoto dei componenti della commissione averti noti il nostro
0:47
ospite che della presente audizione sarà redatto un resoconto stenografico segnalo altresì che poiché l'audizione odierna si svolgerà in videoconferenza
0:54
non sarà possibile sottoporre al regime di segretezza in quanto tale regime implicherebbe la sospensione di tutti i collegamenti remot oltre che della
1:00
trasmissione diretta sui obiettivi della Camera dei Deputati Pertanto se il nostro ospite dovesse ritenere opportuno essere audito n stuta segreta la
1:06
commissione potrà valutare tempistiche modalità di prosecuzione de lavori compatibili con la segretezza della seduta ricordo sì che la commissione è
1:12
chiamata a svolgere indagini atte a far luce sull'attività leita connesse al cico dei rifiuti su altri Leti ambientali e agroalimentari con
1:17
particolare riguardo alla verifica dei comportamenti leciti nell'ambito della pubblica amministrazione centrale periferica ovvero da parte di soggetti
1:23
pubblici o privati operanti nella gestione del ciclo dei rifiuti con l'obiettivo specifico di individuare eventuali connessioni tra Tale attività
1:28
lecite altre attività economiche compreso il traffico di rifiuti all'interno dei territori comunali provinciali nonché tra le regioni tra
1:34
diverse regioni anche tenendo conto del divario della dotazione di impianti Inoltre Con riferimento specifico alle
1:40
tematiche della dizione odierna ricordo che rientrano tra le competenze della commissione senza Attiva legge
1:45
istitutiva verificare l'eventuale sussistenza di attività lecite relative ai siti inquinanti e alle attività di
1:51
bonifica nonché verificare la correttezza attuazione normativa vigenti in materia ambientale più precisamente l'audizione odierna rientra nell'ambito
1:57
del fino di inchieste riguardan il sistema di smaltimento e rifuti in Sicilia nonché il monitoraggio degli appalti relativi alla gestione dei
2:03
rifiuti solidi urbani e delle conseguenze incendi e accadimenti di natura criminale della mesima regione già avviato per decisione dell'ufficio
2:09
di presidente inato presidente dei gruppi a riguardo ricordo che le delegazioni della commissione sono recate in ben tre occasioni in missione
2:15
in Sicilia la prima volta nella provincia di Catania caltan set nella giornata del 26 27 e 28 marzo 2024 con
2:21
svolgimento sopralluoghi della discarica in contrada di timpazzo del comune di Gela al Sin di Gela alla discarica della
2:27
Contrada codavolpe e all'attiguo sito di stagio presso Catania una seconda volta a Palermo ed in provincia di Messina il
2:33
22-23 luglio 2024 con svolgimento di sopralluoghi a discarica di bello Lampo e a qu di Mazzara Del del Sant'Andrea
2:39
una terza volta il 24 settembre 2024 in provista di Ragusa in contrada Perciata
2:45
nel comune di Vittoria Dove è stato rilevato il grave problema dei roghi illegali di rifiuti le cosiddette
2:51
fumarole e dell'abbandono di rifiuti provenien dal coltivazioni agricole alla luce dell'attività fin qui condotta in
2:57
particolare è di particolare interesse per la commissione acquisire informazioni riguardanti tra gli altri
3:03
temi il piano rifiuti della Regione Siciliana e relativo allo stato di attuazione la condizione delle discariche degli impianti gli aspetti
3:09
illeciti legati al fenomeno dei rghi di rifiuti la condizione di indebitamento degli exato e le percentuali di
3:15
riscossione delle tasse sui rifiuti della Regione nonché le iniziative avviate e programmate dal Presidente delel suo ruolo di Commissario
3:21
straordinario invito il nostro ospite a contenere se possibile il proprio intervento e quelli dei propri accompagnatori in 30 minuti complessivi
3:28
lasciando poi at spazio per le domande Fermo restando che ulteriori richieste potranno poi eventualmente essere poste
3:34
per iscritto cedo dunque la parola al presidente Schifani Per lo svolgimento della sua relazione introduttiva al termine della quale i colleghi
3:40
parlamentari potranno rivolgere eventuali domande o richieste di chiarimento ho parlato in precedenza col
3:46
presidente ehm so che ha un impegno alle 14:50 quindi lo ringrazio per la presenza lo
3:53
lascio alla sua relazione Dopodiché avremo un periodo per fare un tempo per fare le domande a cui chiedo
3:58
naturalmente provvederò a raccoglierle Dopodiché lascerò la parola per la risposta qualsiasi domanda non sia stata
4:05
risposta nel tempo che abbiamo verrà risposta successivamente dal Presidente o dei suoi fici presidente grazie ancora
4:12
per la presenza e scusi per la mia voce ma ho un calo di no no ma si figuri grazie grazie presidente un saluto ai
4:19
componenti della commissione e l'occasione di questa audizione mi
4:24
consente presidente di Illustrare le iniziative intraprese sul sistema di smaltimento dei rifiuti in Sicilia dal
4:32
governo regionale che mi onorò di presiedere Qual è nella qualità anche di Commissario straordinario sin dall'insediamento del marzo scorso la
4:40
relazione sono allegate signor presidente a compendio delle considerazioni che seguiranno schede e
4:46
prospetti che meglio possono offrire dati e riferimenti all'inchiesta che codesta commissione sta conducendo
4:52
monitorando gli appalti relativi alla gestione dei rifiuti solidi urbani e delle conseguenze di Inc di accadimenti
5:00
di natura criminale nella regione una considerazione signor presidente mi
5:05
corre l'obbligo di svolgere all'apertura di questa seduta il settore alla raccolta il trasporto la gestione il
5:13
recupero dello smaltimento dei rifiuti speciali pericolosi e non pericolosi in Sicilia a partire da quello delle
5:19
discariche ha manifestato e per taluni aspetti manifesta ancora purtroppo
5:25
profili di rilevante infiltrazione alla criminalità organizzata come peraltro rilevato dalla stessa
5:32
Commissione nei sopralluoghi svolti in alcune province siciliane le influenze
5:37
della criminalità nel settore le inerzie verso la modernizzazione del sistema dei rifiuti in Sicilia Sono alla base delle
5:44
molte carenze dei ritardi che siamo costretti ad affrontare e Cercheremo di risolvere carenza di impianti adeguati e
5:51
progressiva saturazione delle discariche esportazione dei rifiuti con costi assai
5:56
elevati bassa percentuale di raccolta zata nei grandi centri abitati ritardi
6:02
negli investimenti correlati alla circostanza che la Sicilia è purtroppo la seconda ragione in Italia per numero
6:07
di illeciti penali Purtroppo nel ciclo dei rifiuti tutto ciò ha reso chiaro sin
6:14
dall'insediamento del governo regionale del mio governo regionale l'assoluta priorità che occorreva riconoscere al
6:21
radicale riassetto del sistema che affrontasse in termini drastici le risalenti radicate criticità che sempre
6:27
più si trasformano in pregiudizio irrimediabili per l'ambiente e in costi spropositati per i nostri cittadini la
6:34
presenza signor presidente della criminalità mafiosa e del malaffare in particolare del settore delle discariche
6:41
è ampiamente comprovata Dalle indagini di settore ma soprattutto dai provvedimenti dell'autorità giudiziaria
6:48
in taluni casi anche molto recenti a conferma di ciò e come Riferirò in
6:54
seguito ved da rilevare signor presidente come ben due società operanti del settore
7:00
sottoposti a misure di prevenzione Antimafia e di pochi mesi fa la pronuncia di confisca da parte del
7:05
tribunale di Catania che facevano quindi parte allo stesso gruppo imprenditoriale
7:11
abbiano intrapreso un contenzioso giudiziario contro la struttura commissariale per ottenere
7:17
l'annullamento accompagnato da domanda di sospensione dell'ordinanza che
7:22
approva il piano rifiuti cioè della mia ordinanza che approvando il piano rifiuti consente lo smobilizzo della
7:27
previsione de termovalizzatore è un piano regolatore rifiuti signor presidente cò dimostrare che al di là
7:33
della piena regolarità dei ricorsi avallati dai custodi giudiziari e a
7:39
tutela dei valori patrimoniali dell'aziende confiscata che i custodi giudiziari mi insegna sono cose ben diverse dei mafiosi che erano
7:45
proprietari il settore sia soggetto a Forte inquinamento della criminalità mafiosa questo impone tuttavia di andare
7:52
avanti spediti verso la progressiva trasformazione di un sistema ormai inefficiente e dannoso ben sapendo che i
7:59
di ostacoli e reazioni striscianti come palesi di alcuni settori che hanno goduto di una rendita parassitaria sui
8:07
ritardi del sistema alle iniziative di modernizzazione non si fanno non si faranno attendere come avrò modo di
8:13
illustrare con la forte collaborazione delle istituzioni della Repubblica signor presidente e ringrazio la
8:18
commissione per l'opportunità che ha offerto oggi di Illustrare le criticità frenate le iniziative assunte quelle in
8:25
corso di adozione il percorso già avviato potrà conseguire obiettivi prefissati per liberare la Sicilia dalla
8:31
morsa di un uso irrazionale dei rifiuti per trasformare in risorse produttiva ed energetica tutelando l'ambiente quel che
8:39
ancora oggi ha un costo ed un peso per la collettività come noto signor
8:44
presidente il decreto legge dicembre 2023 1881 convertito con la legge di conversione specialmente l'articolo 14
8:50
quater lei Saprà sicuramente i componenti si è previsto che con decreto del Presidente del Consiglio dei
8:56
Ministri il Presidente della Regione Sicilia fosse nominato commissario straordinario per la valorizzazione
9:01
energetica e la gestione del ciclo dei rifiuti nella regione siciliana la gestione commissariale ha l'obbligo e
9:08
l'obiettivo di accelerare in via d'urgenza In conformità a quanto stabilito agli articoli 179 82 e 182 bis
9:15
del codice dell'ambiente il completamento della rete impiantistica regionale favorire il recupero
9:20
energetico e garantite garantire la sostenibilità ambientale nel rispetto della normativa europea e Nazionale
9:26
sulla gestione dei rifiuti e sull'economia circolare la norma frutto di un proficuo confronto tra governo
9:32
nazionale e regionale ha peraltro contemplato la scelta della realizzazione di termovalorizzatori ed
9:37
iniziativa pubblica per la valorizzazione energetica la gestione del ciclo dei rifiuti nella regione
9:43
siciliana lo stanziamento di 800 milioni di euro derivanti dal fondo sviluppo e
9:48
coesione quale finanziamento pubblico per garantire un più basso de cittadini
9:54
della modernizzazione e razione del sistema io ho firmato con le premier Meloni si fa fsc che Conoscete tutti
10:01
naturalmente all'interno del quale è stata prevista misura è condivisa dal governo nazionale cioè fondi pubblici
10:07
per tenere basse le tariffe Naturalmente per gli utenti il dpcm 22 febbraio 24 ha
10:13
consentito il mio insediamento quale commissario straordinario con l'obiettivo di garantire il completamento della rete impiantistica
10:19
integrata e il conseguimento nell'ambito di un'adeguata pianificazione regionale il sistema di gestione rifiuti il
10:25
recupero energetico bruciamo ma creiamo energia la riduzione dei movimenti dei
10:30
rifiuti e l'adozione di Metodi e tecnologie più idonee a garantire un alto grado di protezione dell'ambiente e
10:35
della salute pubblica sono seguiti l'istituzione dell'ufficio speciale per la valorizzazione energetica la gestione
10:42
del ciclo dei rifiuti nella regione struttura regionale a supporto del Commissario straordinario per la
10:47
valorizzazione energetica e la gestione del ciclo rifiuti Tutto a spese della Regione l'approvazione con ordinanza
10:53
commissariale presidente del 21 novembre 24 segnalo l'importanza di questo passaggio signor presidente
11:00
a seguito di un iter l'ordinanza diciamo di adozione del Piano rifiuti a seguito però di un iter accelerato e previa
11:06
Acquisizione della valutazione ambientale e strategica secondo le modalità previste dall'articolo 14
11:11
decreto legislativo 152/2006 e la consultazione degli enti territoriali e della società civile è
11:18
stato approvato il piano regionale di gestione rifiuti il quale prevede appunto la realizzazione di due impianti
11:24
di valorizzazione energetica cosiddetti term valorizzatori TMV da ubicar Sii rispettivamente presso i comuni di
11:30
Palermo e di Catania Gi ricordare che nel contesto di questa procedura sono stati acquisiti Ecco i percorsi signor
11:36
presidente la risoluzione ottobre 24 trasmessa con nota eccetera con la quale la quarta Commissione Ambiente
11:42
dell'assemblea regionale ha espresso il proprio apporto consultivo la determinazione della conferenza
11:47
permanente regione autonomie locali della regione siciliana ma soprattutto signor presidente il parere espresso il
11:53
5 novembre 2024 numero 257 reso dal consiglio di giustizia amministrativa
11:59
per la Regione Siciliana e la sezione siciliana del Consiglio di Stato naturalmente dalla sezione consultiva
12:05
quindi abbiamo seguito signor presidente un iter normale Anche se questo commissario poteva adottare poteva
12:12
avvalersi dei poteri speciali da riconosciuti dal governo Nazionale Noi abbiamo preferito per l'adozione di
12:17
questo piano seguire un iter ordinario e normale quindi acquisire pareri della regione del governo della assemblea
12:23
regionale e il parere anche del consiglio di giustizia amministrativa come parere consultivo noi abbiamo il cg
12:28
anziché Consiglio di Stato credo che sia notorio a tutti i componenti della commissione che saluto come ricordavo
12:34
signor presidente la gestione dei rifiuti rappresenta una delle sfide ambientali più rilevanti per la Regione Siciliana caratterizzata da una storica
12:41
dipendenza delle discariche da un sistema impiantistico non adeguatamente sviluppato in questo contesto la
12:48
realizzazione dei termovalorizzatori nei comuni di Palermo e Catania si inserisce come un'azione strategica volta a modernizzare il ciclo dei rifiuti
12:54
garantendo una riduzione significativa del conferimento in discarica e un efficiente recupero energetico
13:00
l'obiettivo primario di questi impianti è quello di incrementare la sostenibilità ambientale della gestione
13:05
dei rifiuti ridurre i costi di smaltimento e assicurare una maggiore autonomia energetica per la Regione
13:11
questa iniziativa si allinea alle direttive europee e nazionali in materia di economia circolare e riduzione
13:16
dell'impatto ambientale derivante dalla gestione dei rifiuti urbani in un contesto globale orientato verso
13:22
l'economia circolare il recupero energetico dei rifiuti tramite la realizzazione degli impianti di termovalorizzazione va considerato Quale
13:29
elemento di compo completamento che consente di evitare il conferimento in discarica e mentre favorisce la
13:35
generazione di energia consentendo di inverare il principio per il quale al concetto di rifiuto si sostituisce
13:42
quello di risorse a favore di persone territori contenitori sociali Il PRG
13:47
adottato prevede In conformità a quanto disposto all'articolo 14 quater cioè la nomina la realizzazione di due
13:53
termovalorizzatori da ubic carsi nelle zone delle quali avevamo citato i termovalorizzatori verranno progettati
13:59
garantendo le seguenti prestazioni capacità di trattamento di 300.000 tonnellate allanno di scarti
14:05
circa 38 tonnellate l'ora dalle opzioni di PR trattamento nelle piattaforme
14:12
regionali di rifiuti indifferenziati della frazione secca di rifiuti differenziati potenza elettrica inastata
14:17
25 MW costituiscono quindi elementi chiave per raggiungere l'obiettivo di
14:23
ridurre drasticamente la percentuale dei rifiuti destinati alle discariche come richiesto dalla direttiva Ue 2018 850
14:31
che prevede un limite massimo del 10% di rifiuti conferiti in discarica entro il 2035 poi consentiranno superare le
14:39
condizioni di fragilità del sistema di gestione dei rifiuti urbani della Regione Siciliana assicurare il
14:44
completamento della rete impiantistica integrata nel rispetto alle migliori tecniche disponibili smaltire la fase
14:50
residuale proveniente dalla gestione dei rifiuti compresi quelli generati nell'ambito dell'attività di riciclaggio
14:56
di recupero che non più recuperabili ridurre i movimenti di rifiuti azzerando del tutto il
15:01
trasferimento fuori regione adottare Metodi e tecnologie pidone a garantire un alto grado di protezione D della
15:08
salute pubblica le aree scelte per la realizzazione termovalizzatore sono le seguenti Palermo nell'area di bellolampo
15:14
già sede di un impianto di trattamento meccanico biologico riducendo così i costi logistici Catania all'interno
15:20
della zona industriale di Pantano d'arci area strategicamente collegata alle principali reti infrastrutturali per la
15:27
gestione ottimale del bacino di rifiuti sono aree signor presidente sia la prima che la seconda di proprietà pubblica
15:33
quindi sostanzialmente sosterremo un onere abbastanza contenuto Per fortuna il crono programma signor presidente
15:39
prevede la realizzazione dei moralizzatori e la consegna dell'inizio dei lavori di costruzione entro la fine
15:45
del 2026 Questo è il nostro CR programma All'inizio dei lavori considerata
15:51
l'importanza strategica dei due termovalizzatore nella gestione del ciclo rifiuti in tutto il territorio della Regione Siciliana e per la
15:56
completa attuazione Il commissario ha ritenuto di doversi avvalere dell'agenzia nazionale per l'attrazione
16:02
degli investimenti e lo sviluppo di Impresa spa in Vitalia praticamente in qualità di centrale di committenza
16:09
mediante la sottoscrizione di apposita convinzione che ho firmato il 15 gennaio 25 con l'amministratore delegato dottor
16:16
Mattarella presidente Mattarella al fine di accelerare la realizzazione dei suddetti nuovi nuovi termizzato e questo
16:24
questo contratto Naturalmente supporterà il commissario nello svolgimento con particolare solicitud Stud di Quali
16:29
attività in Italia farà procedura sopra Soglia comunitaria per l'affidamento dei progetti di fattibilità
16:35
tecnico-economica dei termizzato procedura sopras Soglia comunitaria per l'affidamento dei servizi di verifica
16:41
della progettazione Avent ad oggetto il progetto di fattibilità tecnica economica il progetto esecutivo oppure
16:46
tmb procedure di affidamento sopras soglie tramite appalto integrato per la realizzazione dei termovalorizzatori e
16:53
della conseguente gestione Quindi abbiamo inteso presidente dare ad Invitalia che una struttura di
16:59
naturalmente di dominio pubblico per la sua competenza affidabilità trasf initalia questa grande funzione questa
17:04
con grande questa responsabilità per le procedure di cui sopra è stata avviata positivamente
17:09
l'interlocuzione anche con l'autorità Nazionale anticorruzione per attivare la vigilanza collaborativa di
17:15
quell'articolo 222 terzo comma lettera h del Codice dei Contratti Pubblici sicuramente di notoria conoscenza da
17:21
parte di vostri compresa anche in Vitalia Naturalmente la sottoscrizione del protocollo di vigilanza è prevista
17:27
entro questo mese quella con con l'anac ma abbiamo già attivato le procedure con
17:33
decreto del commissario del 5 agosto 24 è stato approvato il Piano Triennale della prevenzione della corruzione della
17:39
trasparenza ptcp del Commissario straordinario per la valorizzazione energetica la gestione del ciclo rifiuti
17:44
volto alla prevenzione del rischio corruttivo e più In generale dei fenomeni cosiddetti di mala amministrazione accezione in cui è
17:51
possibile di comprendere le situazione ove pur non rinvenendosi fatti penalmente rilevanti viene configurarsi
17:57
una distorsione D Ativa dovuta all'esercizio delle funzioni pubbliche per fini privati per gli afferenti di
18:03
cui SOA si applicheranno quali misure per legalità Patto di integrità stabilisce la reciproca formale
18:09
obbligazione del Commissario straordinario dei partecipanti alla procedura di affidamento in oggetto di conformare i propri comportamenti e
18:15
principi di realtà trasparenza e correttezza nonché l'Espresso impegno anticorruzione di non offrire accettare
18:21
o richiedere somme di denaro qualsiasi altra ricompensa vantaggio o beneficio sia direttamente che indirettamente
18:27
attraverso Inter intermar tra gli obblighi previsti del documento l'affidatario si impegna a osservare a
18:33
far osservare i propri collaboratori a qualsiasi titolo avuto riguardo al ruolo e all'attività svolta gli obblighi di
18:38
condotta previsti dal dpr 62/2013 e il codice di comportamento dei pubblici dipendenti e dal codice di comportamento
18:45
della Regione Siciliana e di enti relativi l'applicazione del protocollo di legalità accordo quadro Carlo Alberto
18:52
alla chiesa stipulato il 12 luglio 2005 fra la Regione Siciliana il Ministro degli Interni e la prefettura dell'isola
18:58
il precedente piano regionale di gestione dei rifiuti urbani approvato nel 2021 quindi presidente presente ha
19:04
fissato linea con le direttive europee obiettivi di miglioramento del riciclo e di riduzione dello smaltimento in
19:09
discarica Tuttavia I risultati ottenuti fino ad oggi non sono stati pienamente raggiunti i risultati relativi alla
19:17
raccolta differenziata sono stati in generale Nel tempo inferiori alle aspettative e Comunque al di sotto del
19:23
65% nonostante un progressivo aumento la percentuale di raccolta differenziata
19:28
media annuale in Sicilia è passata dal 51% nel 2022 dati Ispra al
19:34
55.20 nel 2023 dati isper 5578 fino al settembre 2024 allego presidente alla
19:42
mia relazione che mi pregò di inviarvi Immediatamente dopo la mia Diciamo la mia relazione la mia audizione in Man
19:49
tale che i colleghi abbiano lo screening delle delle varie città questo lo faccio per economia temporale rispetto nei
19:55
confronti della commissione quindi la anche l'obiettivo di ridurre i rifiuti
20:00
smaltiti in discarica non è stato raggiunto la quantità di rifiuti destinati alle discariche è rimasta
20:05
elevata 70% con una riduzione rispetto al dato iniziale insufficiente per avvicinarsi all'obiettivo del 10 questo
20:13
ha comportato notevoli criticità nel sistema impiantistico evidenziato la necessità di migliorare la gestione e la
20:19
realizzazione degli impianti intermedi in relazione a livello di approfondimento dei flussi e dei fabbisogni acquisiti nell'ambito della
20:26
redazione del rapporto preliminare ambientale degli obiettivi inv indicati frutto di ampia concertazione con i
20:31
soggetti a vario titoli coinvolti nel settore nel mese di marzo del 2024 è stato completato L'aggiornamento del
20:38
piano regionale di gestione dei rifiuti stralcio rifiuti urbani attualmente la
20:43
volumetria disponibile nelle sedi scariche autorizzate delle quali quattro
20:49
pubbliche e due private all'abbonamento di rifiuti urbani per retratti a monta a
20:55
781.2 m c posti per tra l'avvio del ciclo di
21:00
gestione dei rifiuti indifferenziati e la chiusura dello stesso vi sono degli impianti intermedi destinati a
21:05
raggruppare rifiuti raccolti in matrici merceologiche omogenee al fine di favorire la valorizzazione degli stessi
21:11
impianti di trattamento meccanico TM dotati di sezione di stabilizzazione biologica della frazione organica le
21:19
Regione Siciliana sono operativi presente 8 tmb dei quali cinque pubblici tre privati aventi una potenzialità pari
21:26
a 18.5 409 tonnellata lan al fine di cercare di
21:32
fronteggiare questa criticità emergente già nel 2018 con l'ordinanza del capo del Dipartimento della Protezione Civile
21:38
dell'epoca è stato avviato l'iter per la realizzazione di due interventi di ampliamento delle discariche esistenti
21:44
quali la settima vasca di bellolampo a Palermo e la discarica di Contrada borran a Trapani suddivisa in
21:52
due interventi distinti per complessivi 161.000 M C tali interventi attualmente
21:58
in corso di completamento sono da riferire da interesse strategico in quanto consentiranno di frenare nel breve periodo l'emergenza per la Città
22:05
Metropolitana di Palermo e per la provincia di Trapani Inoltre al fine di ridurre il ricorso allo smaltimento al
22:11
di fuori del territorio regionale rifiuti trattati dall'unico TMV attivo per le province di Messina caternia e
22:17
Siracusa peraltro gestione privata nel piano regionale di gestione dei rifiuti è stata prevista la realizzazione di diversi impianti pubblici di selezione
22:24
recupero e raffinazione infatti Al fine di colmare la disomogeneità età della distribuzione regionale degli impianti
22:30
intermedi nella programmazione regionale per la Sicilia Orientale è prevista la realizzazione di sei piattaforme di
22:36
selezione recupero raffinazione pubbliche di potenzialità pari a 500.000 tonnellate nel medio lungo periodo
22:42
complessivamente il piano regionale di gestione rifiuti contempla l'ampliamento di discariche esistenti non nuove tali
22:49
interventi strategici garantiranno l'abb ANC meno dei rifiuti pretrattati tenendo conto della progressiva riduzione della
22:56
quantità di rifiuti conferiti in discarica finalizzata al raggiungimento dell'obiettivo europeo fissato al 10%
23:01
del 2035 Inoltre tenendo conto della prossima realizzazione dei due
23:06
termovalorizzatori gli interventi programmati garantiranno la capacità di Abbano necessaria allo smaltimento degli
23:13
scarti dei termovalorizzatori andiamo alle discariche oggetto di sopralluoghi da parte della commissione
23:19
ringrazio la commissione per avermi anticipato Quali erano i temi oggetto delle vostre visite che noi conoscevamo
23:25
comunque ma giusto rispondere all la piattaforma bello la piattaforma impiantistica di
23:30
bellolampo a Palermo gestita dalla società Rab risorse ambiente Palermo Quindi è pubblica del comune risulta
23:36
costituita da una discarica per rifiuti non pericolosi cosiddetta sesta vasca in fase di chiusura una discarica per
23:43
rifiuti non pericolosi cosiddetta settima vasca in fase di messa in esercizio un impianto di trattamento
23:48
meccanico biologico tmb fisso da 365.000 tonnellate l'anno la piattaforma
23:54
impiantistica nel suo complesso generale vista circa 10 km dal centro di Palermo e 2 km in linea d'aria dei due grossi
24:00
agglomerati Urbani ad alta densità edilizia piattaforma impiantistica timpazzo
24:06
Gela la società per la regolamentazione del servizio di gestione rifiuti srat 4
24:12
Caltanissetta è stata costituita in data 17 ottobre 2012 e comuni di buttera
24:18
Delia gelia Mazzarino Niscemi Riesi Sommatino Piazza Armerina e della provincia regionale di Caltanissetta e
24:24
successivamente modificata con atto repertorio numero 14300
24:29
la società dato Caltanissetta provincia Sud per raggiungere il proprio scopo sociale ha costituito quale socio unico
24:35
la società Enus impianti srr auto di Caltanissetta provincia e Sud Srl la
24:40
società ha come scopo lo svolgimento dell attività di progettazione realizzazione e gestione della sezione
24:45
impiantistica legata al ciclo integrato del recupero e smaltimento dei rifiuti solidi urbani del servizio di raccolta
24:51
porta a porta la società svolge la gestione operativa dell'impianto D tmb
24:56
aff fardata dal primo giugno 2020 della vasca in ampliamento della discarica denominata vasca e del 27 luglio 2020 la
25:04
società ha conseguito il rilascio delle necessarie certificazioni la struttura territoriale impiantistica è così
25:10
composta impianto di trattamento meccanico biologico tmb un impianto di
25:15
selezione a mano di recupero del rur rifiuto Urbano residuo e nello stesso
25:21
tempo sorge nelle aree immediatamente limitrofe alle vasche esistenti in esercizio della discarica contr Contrada
25:26
di impazzo nel comune di Gela sito che resta nelle previsioni dell'attuale srr come un'area dove si è realizzato un
25:32
vero e proprio Polo Tecnologico la discarica vasca vasca e del per RSU per
25:38
un volume utile di 790.000 m c è ubicata in contrada timpazzo ed è adiacente
25:44
all'impianto tmb in atto risulta una capacità residua di circa 20.000 tonnellate ma in fase di rilascio
25:50
un'autorizzazione per ulteriori 200.000 tonnellate per una riprofilatura dei volumi a bancar nell fsc fondo sociale
25:58
ie è stato previsto un finanziamento per la realizzazione di nuove vasche per un volume pari a 2 milioni di Met cu Ma la
26:05
soci ficato che prevederà un aumento diura pari ad 1 milione Met cu oltre
26:11
opere connesse al recupero di energia o di materia prodotta al combustibile solido secondario la regione ha già in
26:17
corso l'autorizzazione per l'utilizzo del combustibile solido secondario presso i cementifici e ci si auspica in
26:23
breve di potere sgravare la vasca da una risorsa che ancora oggi al pari di un rifiuto Inoltre si sta prevedendo la
26:30
realizzazione di opere di compensazione per il superamento D leicità legate al fatto che le discariche insistono su
26:35
Area sic cioè siti di interesse comunitario zps zone di protezione
26:40
speciale la commissione di camerale in visita presso il sito di timpazzo ha
26:45
chiesto la verifica di alcune ottemperanze relative all'Aia del 2012 in capo al precedente soggetto gestore e
26:51
risulta dagli atti in possesso della regione che sono state ottemperate l'ampliamento della discarica di
26:56
timpazzo si indispensabile al fine di garantire la vita utile del tmb e della piattaforma in quanto il precedente
27:03
governo ha utilizzato l'attuale vasca in esercizio per tamponare l'emergenza rifiuti si Rammenta che la società ha
27:09
vinto un ricorso al TAR per il non accoglimento della quantità Imposta della Regione durante l'emergenza oltre
27:14
i limiti giornalieri ad oggi i conferimenti si sono ridotti per tutelare la vita della discarica in
27:20
vista della realizzazione della nuova vasa ai sensi dell'articolo 15 della legge regionale 8 aprile 2010 numero 9
27:27
il servizio gestione integrata dei rifiuti affidato All srr In nome e per conto dei comuni
27:32
consorziati salvo quanto previsto Al comma 2 ter dell'articolo 5 esercita le funzioni previste agli articoli 200 202
27:40
203 del decreto legislativo 152 il servizio riguarda lo spazzamento la raccolta il trasporto allo smaltimento
27:46
dei rifiuti Solid urbani differenziati e indifferenziati la discarica rimessa di Contrada zuppa nel comune di Mazzara
27:53
Sant'Andrea la discarica ad oggi risulta non Attiva ed è in corso un progetto di
27:58
messa in sicurezza chiusura e riqualificazione delle aree relative alla discarica dimessa attraverso il
28:04
piano d'azione Per la riqualificazione dei siti orfani a valere sulla misura di finanziamento missione 2 componente 4
28:11
più specificamente Per quanto concerne la questione riguardante il sito di Mazzarrà Sant'Andrea si ricorderà che a
28:16
seguito dell'incendio Accorso in data 25 giugno 2024 comportante la distruzione di gran parte della rete di capitazione
28:22
del biogas delle tubazioni che conducevano al percolato alle vasche di accumulo costituite da da 21 Pozzi della
28:29
rete elettrica e dei quadri di comando a servizio dei pozzi oltre che di circa il 30% del Telo di copertura il comune di
28:36
mazzarra sant'andre è stato autorizzato la Regione Siciliana quale soggetto beneficiario del contributo straordinario X legge regionale 32024 di
28:43
importo pari a €54 ad utilizzare tali somme per far fronte alle prime opere emergenziali
28:49
utili per la messa in pristino dello Stato dei luogi successivamente si è provveduto ad effettuare un sopralluogo
28:55
congiunto con il dipartimento regionale di Protezione Civile il Genio Civile di Messina il comandante de Vigili del
29:00
Fuoco territorialmente competente l'amministrazione comunale Il curatore fallimentare della Tirreno ambiente in
29:06
liquidazione presso la discarica in argomento nella cui occasione è stata accertata la presenza dell'attività di
29:11
Piroli pirolisi all'interno dei luoghi in tale sede verificata la consistenza
29:16
dei luoghi danneggiati a causa dell'incendio si è convenuto di attivare un percorso conducente a finanziare gli
29:21
interventi ritenuti necessari con l'impiego e l'utilizzo del contributo pari a 1 Mil milione e mezzo di cui alla
29:27
legge regionale 2 524 pertanto preso atto della impossibilità da parte del soggetto
29:32
attuatore Già individuato nella srr Messina provincia di provvedere all'attività a queste rimesse i pretti
29:38
adempimenti sono stati rimessi in capo al dipartimento regionale acqua e rifiuti già responsabile unico
29:43
dell'attuazione con l'onere di assolvere con diretta titolarità il ruolo di soggetto Totore e stazione appaltante
29:49
tempestivamente nominato il rup nella persona ingegnere capo dell'ufficio del Genio Civile di Messina si è proceduto
29:55
successivamente all'autorizzazione per l'affidamento l'incarico di progettazione e adeguamento del preziario Per la realizzazione degli
30:01
interventi riguardanti la messa in sicurezza e ripristino ambientale del sito da ultimo il commissario delegato
30:07
per lo stato di crisi di emergenza regionale per il sito alla discarica ha sollecitato il comune di Mazzara Sant'Andrea la trasmissione del progetto
30:14
esecutivo agli interventi realizzati Sicula trasporti signor presidente Adesso entro su un territorio diverso e
30:20
cioè che tocca le società che hanno gestito diciamo una buona parte del
30:26
mondo dei rifiuti Sicilian la sigura trasporti e Spy è una società che si occupa di trattamento rifiuti
30:33
indifferenziati per circa 350 400.000 tonnellate all'anno circa Quindi il 50%
30:39
dei rifiuti prodotti in Sicilia il gruppo imprenditoriale sottoposto alle misure di prevenzione a seguito della
30:45
recente sentenza della terza sezione del tribunale di Catania è stato oggetto di confisca delle società coinvolte che
30:52
sono state condannate al pagamento di ingenti somme pecuniarie l'impianto di trattamento l'impianto di trattamento è
30:59
situato a Lentini in contrada Coda volpe provincia di Siracusa e dispone di un sito di discarica esausta pertanto la
31:06
sigula trasporti si occupa esclusivamente del trattamento meccanico e biologico dei rifiuti cioè il tmb
31:12
l'impianto di trattamento meccanico per il trattamento dei rifiuti urbani non pericolosi è stato autorizzato con
31:17
decreto Aia 248 del 2009 per la potenzialità di un milione di tonnellate
31:24
l'an l'impianto opera un trattamento meccanico triturazione e selezione preliminare al conferimento in discarica
31:31
dei rifiuti urbani non pericolosi l'impianto costa di quattro linee indipendenti ciascun delle quali opera
31:37
una fase di preselezione costituita da una triturazione una vagliatura primaria separazione dai metalli ferrosi e non
31:43
una fase di raffinazione rifiuto organico costituita da una vagliatura secondaria produzione sottovaglio ad
31:48
avviare stabilizzazione svalo ad avviare a parziale recupero mediante separazione balistica e separazione di infrarossa
31:55
quasi la totalità dei rifiuti trattati decad dal tmb della sigola trasporto signor presidente vengono conferiti al
32:01
di fuori del territorio regionale A questo riguardo vanno segnalate le molteplici iniziative
32:07
processuali avviate dalle società del gruppo Sicula trasporti e Gesac della quale parleremo avverso il nuovo piano
32:14
regionale di gestione rifiuti verso il piano regionale adottato dal sottoscritto Nella qualità nel mese di
32:20
novembre dello scorso anno Infatti attualmente sono pendenti presso i tribunali amministrativi del Lazio e
32:26
della Sicilia le cui domande cautelari saranno trattate alle camere di consiglio del 13 prossimo 21 Palermo 19
32:34
Roma profili sui quali si innestano altre iniziative giudiziarie delle quali si è occupata la stampa negli articoli
32:40
che mi permettono di allegare alla relazione acqu adesta commissione sono istanze presidente
32:45
cautelari nel senso che si chiede la sospensione con questi ricorsi si chiede la sospensione della mia ordinanza cioè
32:51
dell'adozione piano rifiuti quindi si determinerebbe accolta Io sarà la magistratura a decidere la paralisi
32:58
della nostra iniziativa per realizzare termovalizzatore Però naturalmente ascolt CD Noi abbiamo dato mandato
33:04
all'avvocatura e Loo stato Naturalmente come nostro dovere per difenderci il gruppo sigula trasporti è stato
33:10
sottoposto a misure di prevenzione ed è attualmente affidato a tre amministratori giudiziari tutti designati dal tribunale di Catania
33:16
sezione misure di prevenzione con provvedimento del 29 maggio 2020 cons sentenza del tribunale di Catania
33:22
sezione terza Penale del 18 luglio è minata la confisca del gruppo sicola trasporti nell' del processo condotto
33:29
alla condanna degli Imprenditori Leonardi e dipendenti privati e pubblici la pronuncia ha statuito anche la
33:34
condanna per le società facenti parte del gruppo imprenditoriale di ingenti pene pecuniarie ravalico e risarcimento
33:40
del danno nei confronti delle parti civili la pronuncia evidenziato Tra l'altro il perdurante sistematico
33:46
illecito smaltimento dei rifiuti solidi urbani provenienti da oltre 200 comuni siciliani nonché una gestione della
33:53
discarica orientata all'esclusivo perseguimento di utili attraverso il mantenimento delle convenzioni con gli
33:59
enti locali Pur non essendo gli impianti nelle condizioni di poter più adempiere alle prescrizioni fissate
34:04
dell'autorizzazione amministrativa Val altresì segnalato signor presidente si tratta di profilo di evidente rilievo
34:11
che a seguito di provvedimenti cautelari richiesti A metà gennaio da parte della procura della Repubblica di Messina per
34:17
vicende inerenti la gestione di un'azienda sequestrata alla mafia di Barcellona Pozzo di Gotto nei confronti
34:23
di uno dei tre commissari del gruppo Sicula quindi uno dei tre componenti commissario giudiziario il gruppo siqua
34:29
della quale abbiamo parlato è stato sottoposto a misura restrittiva ed è per
34:35
reati diciamo connessi naturalmente all criminalità mafiosa e diciamo nomina dal tribunale
34:42
presidente ed è presidente rzo dell'Ordine commercialisti di Catania presidente D capogruppo della siur
34:48
trasporti questi naturalmente subito dopo l'arresto si è dimesso da presidente del CdA D siura trasporti
34:54
prendono dei ricorsi come le dicevo un ricorso alla sigula trasporti al TAR Lazio del 27 settembre 24 contro il mio
35:02
decreto e ci stiamo difendendo attraverso l'avvocatura L'udienza è
35:07
fissata per il Dunque per il diciamo il 19 gennaio per questo
35:16
ricorso seguito alla proposizione motivi aggiunti a verso nuovo peratore è stata fissata udienza 19 dove viene chiesto
35:22
non da noi Certo noi ci difenderemo in calcolare la sospensione del nostro piano rifiuto a questo ricorso ci
35:28
aggiunge quello della Gesac società del messimo gruppo avverso il nuovo piano regolatore dei rifiuti regionale dei
35:34
rifiuti pendente presso il TAR Palermo Sicilia la cui domanda cautelare sarà discussa nella camera di consiglio del
35:40
prossimo 13 gennaio 2025 Entrambe le domande cautelari chiedono appunto la sospensione alleghiamo copia degli
35:47
articoli a farsi sulla Stampa coloran diciamo così perché la la commissione ne abbia
35:55
cognizione fermo restando signor presidente che che sono ricorsi promossi naturalmente dai nuovi custodi
36:00
giudiziari quindi è evidente che ci troviamo dinanzi un altro interlocutore Ovviamente non è che si può minimamente
36:06
supporre un minimo di sospetto in capo ai nuovi commissari giudiziari e vi è Naturalmente la prospettazione
36:12
evidentemente resa davanti gli organi di controllo e probabilmente lamentando l'eventuale perdita di patrimonialità di
36:19
queste aziende che avevano però iniziato un'attività che poi è stata dichiarata illecita fino al primo grado Poi ci
36:26
saranno le sentenze di conferma Siamo in un mondo naturalmente di di garantismo però ecco il dato che che emerge è che
36:34
queste due aziende che hanno fatto ricorso erano caratterizzate da presenze estremamente inquinanti e che
36:41
naturalmente hanno insistito correttamente attraverso una nuova compagine che è quella della commissione
36:46
giudiziaria della commissione appunto del commissari giudiziari Allora in
36:52
merito mi accingo a chiudere presidente in merito ai roghi dei rifiuti dell'assessorato all'energia e servizi pub
36:58
chiesto all'ARPA al comando del Corpo Forestale dei Vigili del Fuoco il proprio contributo tali dati non
37:03
comprendono numerosi interventi dei vigili del fuoco scusi saltato una cosa presidente chiedo
37:10
scusa aspetti illeciti legati al fenomeno dei roghi dei rifiuti fenomeni fumarole nella fascia trasformata in
37:18
merito a questi roghi l'assessorato all'energia e servizi di pubblica utilità ha richiesto all'ARPA al comando
37:23
del corpo forestale e ai vigili del fuoco il proprio contributo in particolare questi ultimi hanno
37:28
evidenziato che dal primo gennaio 22 al mese di settembre 24 si sono verificati 56 roghi in 50 in in discarica e
37:36
impianti di trattamento rifiuti tali dati non comprendono i numerosi interventi di vigili del fuoco per la
37:41
combustione di materiali vari legati al fenomeno diffuso e l'am mando de rifiuti arpa Sicilia ha riferito in merito
37:46
all'attività di monitoraggio ambientale Seguita a seguito dell'incendio di bellolampo avvenuto in data 24 luglio 23
37:52
un ulteriore evento avvenuto 17 giugno 24 lungo la scarpata della cosiddetta settimana vasca in data 2 Giugno 24 Si è
37:59
verificato un incendio presso la discarica sita in contrada zuppa del comune di Mazzara Sant'Andrea cui si ha
38:04
fatto Cerno precedentemente Oltre agli incendi presso gli impianti di scarica sopr indicati arpa Sicilia ha riferito
38:10
su altri eventi incendiari particolarmente rilevanti che hanno riguardato in data 20 gennaio 24 l'impianto di trattamento rifiuti della
38:16
ditta Omnia S in contrada bugiades del comune di Licata in data 22 agosto 22 l'impianto della dita ecomac smaltimenti
38:24
srl la pratica illegale della combusione signor presidente del materiale plastico
38:29
derivante dalla rifunzionalizzazione delle Serre cosiddette fumarole è purtroppo diffusa nei territori delle
38:36
province di caltanissette Ragusa per sopperire a tale annoso problema è stato inserito l'articolo 256 bis del decreto
38:43
legislativo 152 del 2006 e similare e modifiche tale articolo prevede pene
38:50
severe per chiunque app picchi il fuoco a rifiuti abbandonati che vengono inasprite in caso di Delitto commesso
38:55
nell'ambito dell'attività di impresa o comunque di un'attività organizzata pertanto lo strumento repressivo signor
39:02
presidente esiste e può e deve essere applicato dagli enti territoriali deputati al controllo del
39:09
territorio condizione di indebitamento degli atomi cengo veramente a concludere in Sicilia legge regionale 8 aprile 2010
39:15
gestione integrata dei rifiuti ha posto in liquidazione le autorità d' ambito territoriale ottima leato sancendo il
39:20
passaggio del servizio di gestione integrata dei rifiuti per ogni ato a una società Consortile di capitali
39:26
costituita da dalla provincia E dai comuni ricompresi in ciascun ambito territoriale ottimale una ricognizione
39:32
pur se dagli esiti parziali su 27 ato ha evidenziato una situazione debitoria di circa 800 milioni di euro ed inoltre che
39:40
il processo liquidatorio ad oggi non si è potuto concludere per effetto della mancata approvazione dei relativi
39:45
bilanci da parte dei comuni soci e per la presenza di moltiplici
39:50
contenziosi sensibilizzazione della cittadinanza sulle tematiche legate alla raccolta differenziata piano di
39:56
comunicazione appare opportuno S presente evidenziare che ai sensi dell'articolo 180 comma2 decreto
40:01
legislativo 152 del 2006 lo sviluppo e il supporto delle Campagne di informazione Per sensibilizzare alla
40:07
riduzione della produzione di rifiuti alla prevenzione della loro dispersione è una prerogativa del programma nazionale di gestione dei rifiuti
40:13
adottato dal Mase Inoltre ai sensi dell'articolo 8 comma 4 la legge regionale 9 2010 le srr hanno lo
40:21
specifico compito di attuare le attività di informazione nell'ambito del PR fers
40:26
2127 la la Regione Siciliana Ha individuato specifiche fonti di finanziamento volte all'implementazione
40:31
di campagne di informazione e sensibilizzazione sul tema della prevenzione della produzione dei rifiuti
40:38
e del riuso programmando una spesa pari a 2. 823.81 sull'azione
40:45
2.6.1 concludo il quadro signor presidente signori componenti della
40:51
commissione che si è pur sinteticamente delineato ha evidenziato molteplici
40:56
criticità risalenti nel tempo che hanno motivato la gestione commissariale con l'inizio dell'attività
41:03
si è Giunti all'approvazione del nuovo piano come dicevo signor presidente al finanziamento dei termovalorizzatori
41:10
all'organizzazione della struttura all'avvio delle procedure ad evidenza pubblica Naturalmente per la
41:16
realizzazione dei nuovi impianti occorre concludo veramente un cambiamento
41:22
epocale nel settore dei rifiuti nella nostra regione tutelare
41:27
l'ambiente valorizzare una risorsa sprecata abbattere i costi dei cittadini garantire la legalità in questo senso
41:35
essenziale contenuto offerto anche dalla vostra commissione parlamentare alla quale confermo la massima collaborazione
41:42
mia e di tutte le strutture regionali Naturalmente perché Sono fermamente convinto Lo sono sempre stato che la
41:48
cooperazione tra istituzioni statali e regionali ma anche comunali potrà consentire di conseguire questi
41:54
risultati nell'osso che il presidente del principio principio dettato in costituzione della collaborazione e
42:00
cooperazione tra vari enti dello stato di vario livello questo dice la nostra Costituzione ed è un principio
42:05
sacrosanto che è uno dei fondamentali naturalmente assiomi della funzionalità
42:11
di un paese la solidarietà e la collaborazione in questo noi puntiamo chiediamo collaborazione siamo pronti a
42:18
darla Naturalmente perché ci muoviamo in un settore estremamente complesso e delicato dove la nostra sfida la sfida
42:25
del mio governo è quella di tenendo spunto dalla dalla possibilità di un finanziamento cospico di carattere
42:30
Nazionale l' fsc contiamo di risolvere una pruta per sempre la soluzione
42:36
dell'emergenza rifiuti con le motivazioni e le proiezioni che mi sono permesso di darvi grazie signor
42:41
presidente grazie presidente lascio subito la parola ai colleghi chiedo di
42:47
raccogliere le domande Magari anche di appuntarsi prego primo mano lorefice
42:58
Sì grazie presidente grazie al presidente Schifani che dopo oltre un
43:03
anno di richiesta ci dà come dire l'onore di essere
43:08
audito mi permetto di fare questa sottolineatura Anche perché ripeto i lavori parlamentari di una commissione
43:15
di inchiesta sono stati fortemente rallentati dall indisponibilità reiterata più volte da
43:22
parte del presidente Schifani detto questo cerco di andare
43:27
direttamente ai tanti temi perché a Valle della relazione che ancora la
43:33
commissione non ha ricevuto e che leggeremo con attenzione per invi la sto per inviare la sto per inviare la sto in
43:40
contestuale alla fine del mio intervento la sto per inviare Sì presidente ma non avremo modo di leggerla e formulare
43:47
Comunque abbiamo ho cercato di prendere a puna corretto inviarla dopo la mia dopo la mia relazione non prima Queste
43:54
sono almeno le regole che io ricordo anche in Parlamento nazionale perfetto presidente lei le regole Io non
44:00
gliele devo insegnare avendo fatto per oltre 20 anni il parlamentare Pertanto è lei che è un
44:07
professore a riguardo Allora arrivando a noi io mi permetto di dire di chiedere
44:14
fare una serie di domande anche se da quello che ho capito lei tra 5 minuti dovrà lasciare la riunione pertanto le
44:22
risposte le avremo successivamente Allora il tema della gestione rifiuti in
44:27
Sicilia è complesso e le radici del dei vari problemi chiaramente non sono
44:33
ascrivibili alla sua gestione ma tutte le diciamo le precedenti compreso la sua
44:39
visto che lei è già in carica da oltre 2 anni e da quasi un anno e anche commissario con poteri
44:46
straordinari nello specifico Io vorrei capire meglio perché ci sono alcune cose
44:52
a me non proprio chiare se è possibile poi avere Successivamente in particolare
44:59
sul Per quanto attiene le discariche lei ha fatto riferimenti a le discariche
45:05
operative in Sicilia quelle di tipo pubblico su quelle private non ci ha dato informazioni io mi permetto di dire
45:13
bello lampo siamo stati con la bicamera di inchiesta a fare un sopralluogo in quell'occasione rispetto al alla
45:20
situazione da girone dantesco della gestione periodo Musumeci abbiamo
45:26
trovato una discarica che aveva un tmb non
45:31
funzionante un impianto mobile in avaria e un altro impianto mobile a noleggio
45:38
che funzionava per la gestione parziale dei rifiuti in arrivo pertanto da quando
45:44
siamo arrivati noi come commissione ad oggi se ci volete aggiornare sul quadro se il tmb quello
45:53
diciamo non quello mobile o non quelli provvisori a noleggio sono pienamente
45:58
operativi E se tutta la piattaforma adesso correlato compreso le varie Aie
46:06
per la maturazione della parte organica Comunque tutte le varie componenti operative ora sono funzionanti Anche
46:14
perché io mi permetto di dire Palermo e Catania i due i due più grandi Poli siciliani sono la palla al piede della
46:20
Regione Anche perché sono Cenerentola gli ultimi Per quanto riguarda percentuali di raccolta differenziata
46:28
sempre sul tema discariche Mazzarrà Sant'Andrea oggetto di Vabbè una discarica in gestione postmortem lei ha
46:36
fatto dei riferimenti con a due leggi regionali che hanno dato risorse per
46:43
359.000 in due tranche 174.000 per il 2014 185.000 per il 2015
46:51
assegnate direttamente al Comune di Mazzarrà Sant'Andrea Almeno così sono ho capito io è 1 milione e mezzo però lei
46:59
ha parlato che queste risorse Sono a disposizione del sindaco e non del della
47:05
srr almeno così ho inteso e neanche all nella disponibilità del commissario in
47:12
quella discarica ad oggi mi risulta che oltre il 40% della superficie il capping
47:18
è inesistente ogni volta che piove l'acqua si infiltra e perciò va ad alimentare
47:27
quello che è la produzione per colato perciò uno spreco di risorse con le risorse assegnate alla Regione Siciliana
47:33
Il Comune si è soltanto limitato ad assumere quattro guardiani che a turno
47:39
fanno la sorveglianza Pertanto se ci volete far sapere quali atti e quali
47:45
azioni reali di come dire interventi emergenziali sono stati posti in essere
47:53
per limitare o eliminare quelli che sono gli inquinamenti ambientali lo spreco e
48:00
tutta quella che è la gestione Poi altra cosa io solo trovato Notizie
48:05
giornalistiche Ma lei ci ha detto qualcosa è stato raggiunto stilato un
48:11
accordo di programma Col il Ministero dell'Ambiente per il progetto di
48:16
bonifica di mazzarra Sant'Andrea se poi ci potete fornire nel dettaglio se avete
48:22
l'accordo di programma copia l'accordo di programma e tutti i documenti corre
48:28
E va bene andando avanti sempre sul questione sulla questione di scariche So
48:33
che lì c'è pure la responsabile del dell'impianto di timpazzo
48:39
Gela in quell'impianto quando noi siamo venuti in a fare una visita un
48:45
sopralluogo già c'erano messe in evidenza alcune vasche
48:51
ancora di competenza dell'ex ato cl2 in liquidazione come lei ha avuto modo di
48:57
dire dal 2010 ad oggi in Regione Siciliana Noi abbiamo 27 ato con i
49:04
relativi liquidatori che però non hanno prodotto nulla Noi continuiamo a pagare
49:11
personale per gestire cosa perché in alcuni casi non sono non operano da
49:18
liquidatori ma gestiscono materialmente anche impianti tipo l'atto cl2 agela è
49:23
proprietario di un impianto di compostaggio che è fermo da oltre un anno non operativo Ma continua a
49:31
impegnare a spendere soldi per un impianto non operativo e anche in merito
49:37
al gestione post morem al progetto di gestione delle vasche del lato cl2 se
49:45
ci potete dare chiaramente informazioni su cosa si
49:51
sta facendo sempre su timpazzo lei ha parlato di CSS l'impianto di timpazzo
49:58
che ha un tmb operativo a noi in occasione della visita c'è stato pure
50:05
detto che quello è un impianto che riesce a far uscire CSS cioè combustibile solido secondario
50:13
certificato solo che il CSS nonostante di alta qualità e certificato viene
50:20
smaltito in discarica pertanto Noi abbiamo un prodotto che potrebbe essere
50:26
tra virgolette venduto utilizzato in impianti di cementerie di valorizzazione
50:32
mediante gassificazione o altro ma da quello che mi risulta ad oggi viene
50:39
trattato e messo in discarica altra cosa mi può dare informazioni in merito
50:46
al ordinanze contingibili e urgenti per Abbano di materiale comunque la parte
50:54
organica stabilizzata anche se non rispetta gli indici
51:02
respirometria Regione Siciliana permette anche l'abbonamento in discarica in
51:07
deformità alle norme vigenti Spero possa smentire questa
51:17
informazione presidente Poi in merito al alla parte relativa agli inceneritori
51:23
con recupero energia Quello che lei li ha citati più cosiddetti termovalorizzatori
51:29
lei ha parlato di un un accordo con Invitalia se ci può
51:35
fornire l'accordo tra la Regione Siciliana e Invitalia in modo da poterlo leggere io sul sito di Invitalia ho
51:42
trovato una nota stampa dove si dice che voi Avete firmato questo accordo vedo un valore di
51:49
16 milioni di euro Pertanto se ci fornite la
51:55
documentazione avremo modo di vedere nel dettaglio poi anche in merito agli
52:00
inceneritori lei ha fatto riferimento a alcune scadenze da quello che ho capito io se va bene
52:07
l'iter per completare progettazione esecutiva e fare bandi e fine
52:15
2026 quali sono poi i tempi relativi alla realizzazione Cioè da quando
52:21
pensate che saranno operativi perché il problema della gestione rifiuti che da
52:27
quello che ho capito io volete risolvere con gli inceneritori in buona parte ad
52:32
oggi non risolveranno niente da qua a quanti anni perché noi abbiamo degli impegni e abbiamo la necessità di
52:40
risolverli Ora lei con i poteri speciali da commissario in un anno cosa è riuscita a fare e per accelerare singoli
52:48
progetti io le faccio un esempio l'impiantistica poi avere un quadro chiaro all'impiantistica c'è il
52:54
cosiddetto impianto di calat ambiente che ha avuto è stato incendiato oltre 2
53:02
anni fa per quell'impianto anzi tre anni fa per quell'impianto ci sono due decreti regionali uno che risale al
53:11
2000 22 e un altro recentissimo Cioè dopo 3 anni e mezzo per vari ritardi non
53:19
si è riusciti neanche a mettere a terra quello che era un progetto di 15 milioni di euro e rimettere in funzione un
53:25
impianto uno pochi impianti che operavano bene in Sicilia Al di là che è oggetto
53:32
anche di indagine giudiziaria Però io le posso dire con dati alla mano avendo
53:38
anche i documenti che poi fornirò anche alla commissione Che calat ambiente Dopo
53:44
varie richieste dopo oltre un anno non riesce a ad avere neanche l'anticipo di €80.000
53:53
per onorare un tratto che ha stilato dopo oltre 2 anni e mezzo e con in
54:02
quanto poggiati prima a Fondi fesd ora a Fondi poc con il solito giochetto dei
54:08
trasferimenti da un fondo all'altro dopo quasi 4 anni abbiamo un impianto fermo e
54:15
mi dispiace dirlo dati alla mano la Regione Siciliana non sta dimostrando né di essere capace né celere nel risolvere
54:23
i problemi se ci può dare informazioni di dettaglio sull'impianto calat E ora
54:29
per ora chiudo dicendo soltanto chiedendo l'informazione in merita all'ARPA l'arpa Sicilia Noi abbiamo
54:36
sentito il direttore e abbiamo soltanto capito che l'arpa Sicilia negli anni ha
54:42
solo perso personale non ha una struttura adeguata a poter effettuare
54:47
controlli sistematici efficaci ed efficienti pertanto io le chiedo per
54:54
quanto riguarda il personale di arpa che è una diretta espressione uno strumento
55:00
tecnico della Regione Siciliana dipende da voi state mettendo risorse state
55:07
predisponendo dato mettendo in condizioni l'arpa di fare i concorsi perché senza personale l'arpa
55:14
potrà solo come dire annaspare arrancare e non risolvere nessun problema neanche
55:20
poter esercitare in maniera adeguata la sua attività di controllo pertanto sulla
55:27
che lei chiaramente forse non l' avevano anticipato o non era oggetto delle domande anticipate vorremmo capire senza
55:35
un organo tecnico come quello dotato adeguatamente di risorse economiche
55:41
tecniche e di personale in che modo la Regione Siciliana pensa di gestire
55:47
quella Mola di procedimenti e di controlli legati alle tante emergenti
55:52
ambientali che non solo solo del comparto rifiuti ultima cosa Ultima
55:57
domanda filone dei rifiuti legati ai fanghi di depurazione se su questo ci
56:04
può fornire una relazione di dettaglio presidente Avrei tanto altro però
56:10
nonostante sono sintetico non riesco con ulteriore
56:15
sintesi Sintetico ma ben dettagliato Onor Marino Grazie presidente grazie al
56:21
presidente Schifani per averci relazionato ovviamente anch'io
56:28
mi allego alla la polemica del polemica
56:33
Non polemica verità richiesta legittima del senatore lorefice avevamo richiesto
56:39
questo suo intervento molto prima anche perché purtroppo in Sicilia lo ha detto pure lei all'inizio della sua relazione
56:44
abbiamo carenze gravi dovute anche a infiltrazioni mafiose e io mi pongo una
56:49
domanda le tante che dovevo farle le ha fatte il senatore quindi è inutile a ripeterle però le le ne pongo una
56:56
importante a lei è stato dato un incarico di commissario come mai ha ritenuto opportuno dopo che c'è questa
57:02
carenza e queste problematiche grossissime che mettono a rischio serio la salute della gente che vive ai
57:09
territori di optare per un per un procedimento
57:14
ehm ordinario e non commissariale che le avrebbe dato la possibilità di accelerare tutti i tempi e quindi poter
57:22
anche incidere in maniera concreta sulle problematiche che attanagliano tutte le
57:27
discariche tra cui in maniera veramente grave quella di Bella lampo dove siamo stati a fare un ispezione
57:35
dico certi poteri vengono dati non solo per prendere
57:41
risorse statali che regionali che potevano servire anche ad altro ma per accelerare i tempi vorrei capire il
57:47
perché ovviamente oggi non sarà non Potrà darci risposta anche perché pure
57:53
Noi purtroppo siamo con i tempi limitati però Volevo anche dirle ha intenzione
58:00
di per progettare questi termovalorizzatori per portare le bonifiche nelle varie discariche di cui
58:08
si è parlato perdere ulteriore tempo e portare il tutto fra 2 anni oppure
58:13
subito sin da subito mettersi a lavorare perché credo che noi siciliani abbiamo il diritto di vivere in una terra pulita
58:19
e e soprattutto quando si ha la consapevolezza che ci sono infiltrazioni
58:24
mafiose che Le carenze sono veramente tante di dare la la giusta attenzione
58:30
consideri che lei dopo un anno ha presentato il piano di intervento sui rifiuti quindi solo questo volevo dirle
58:37
grazie grazie Ci sono altre domande non vedo altre domande Io ne ho alcune che
58:44
però preferisco inviare per iscritto a questo punto perché il tempo stringe in quanto lei mi aveva disponibilità più o
58:50
meno fino alle ore 1500 quindi non la dilungo se vuole replicare per pochi
58:55
minuti qualcuna qualcuna presente posso rispondere le mieie possono essere inviate per iscritto quindi provvederò
59:02
per iscritto mandagli prego a lei la parola Presidente No a qualcuna sono in grado di rispondere ad altre mi riserva
59:07
La ringrazio la disponibilità la commissione risponderemo analiticamente per iscritto su Mazzarrà l'accordo
59:13
sottoscritto dalla PQ di 32 milioni faremo forniremo naturalmente alla commissione copia del del dell'intesa e
59:22
trasmetteremo anche l'accordo sottoscritto con con invitare del quale ho fatto cenno sono atti di trasparenza
59:30
massima Ci mancherebbe su Arpa Stiamo procedendo a investimenti per nuove assunzioni assicuro l'evo l'orefice di
59:38
questo i tempi di definizione dal momento dell'aggiudicazione della della
59:45
gara previsti secondo il nostro cronoprogramma sono 580 giorni dall'aggiudicazione dall'inizio dei
59:51
lavori e sul sulla procedura che ho seguito presidente Per la piano rifiuti
59:58
Sì Avrei potuto accelerare In che senso perché ho omesso di riferire alla
1:00:03
commissione che io ho ottenuto che in tempi velocissimi si potesse seguire l'iter
1:00:10
ordinario ugualmente e quindi l'acquisizione di pareri della dell'assemblea regionale del consiglio
1:00:16
di amministrativa e con la disponibilità istituzionale devo dire che ringrazio
1:00:21
sia dell'assemblea regionale che del consiglio amministrativa di velocizzare questi AR eri in un senso o nell'altro E
1:00:27
l'ho fatto per porre presidente al riparo da eventuali eventuali impugnative di terzi che avrebbero
1:00:33
potuto eccepire che io avessi utilizzato male i miei poteri speciali Allora
1:00:39
siccome diciamo il l'obiettivo di questa presidenza è quello di realizzare i
1:00:44
termovalizzatore evitare impugnative possono esserci ma spesso magari possono essere strumentali o meno mi sono dato
1:00:51
questa regola coniugando rigore trasparenza rispetto alle regole quindi rispondendo allaa deputata posso
1:00:57
assicurare che i tempi sono stati estremamente veloci ugualmente poi relazionerà alla deputata ai tempi
1:01:04
attuati per acquisire questi pareri sono veramente estremamente brevi Se non ricordo male il CGA ci ha dato il parere
1:01:11
nell'ambito dei 45 giorni massimo anche l'assemblea regionale quindi di questo
1:01:17
io naturalmente vado fiero alle considerazioni allella collega Io non lavoro F fa parte della dialettica
1:01:23
politica Naturalmente io eh ne prendo atto sono mi ritengo in pace con la mia coscienza perché stiamo
1:01:30
investendo in risorse umane notevoli abbiamo costituito un ufficio proprio a
1:01:36
spese di Palazzo orlean per la realizzazione di termovalizzatore è una grande scommessa signor presidente e
1:01:42
credo che si è passato in passato Si c'è provato adesso ci stiamo provando abbiamo la risorsa pubblica abbiamo la
1:01:48
provvista abbiamo la volontà per Add divenire all una a una svolta Speriamo
1:01:54
ocale della nostra regione di concerto anche con i vostri stimoli dei quali naturalmente terremo conto e ai quali
1:02:01
risponderemo analiticamente Grazie Presidente Grazie Presidente quindi noi
1:02:08
avremo modo di confrontarci invieremo quelle che sono le domande quindi invito anche gli altri commissari che non sono
1:02:13
intervenuti oggi a far prevenire alla segreteria eventuali domande che invieremo al presidente attendendo
1:02:19
risposta nelle prossime missioni poi magari Chiederemo anche di andare in visita in Regione Sicilia e magari avere
1:02:24
un confronto anche visavì grazie Io ringrazio il presidente Schifani
1:02:32
ringrazio gli altri ospiti e per la disponibilità e dichiaro conclusa l'audizione Grazie"""
        }
    ]
)

print(completion.choices[0].message)