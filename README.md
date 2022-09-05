
# GESTIONE FUMETTERIA

## AUTORI

- Davide Santurbano - [@Ser4ld](https://www.github.com/Ser4ld)
- Alessandro Seghini - [@AlessandroS01](https://github.com/AlessandroS01)
- Giampaolo Marino - [@giamp109](https://github.com/giamp109)
## DESCRIZIONE GENERALE  

Il software è stato sviluppato in Python ed è provvisto di interfaccia grafica. Attraverso il `Login`
l'amministratore può accedere al menu e navigare tra le seguenti sezioni e compiere le seguenti azioni:

- `Gestione magazzino`

    - visualizzazione di tutti i prodotti presenti;
    - ricerca dei prodotti;
    - inserimento e modifica dei prodotti;
    - inserimento dell'offerta per un prodotto. 
(La modifica di un prodotto e l'inserimento dell'offerta avviene successivamente alla ricerca).

- `Gestione Account`
    - modifica nome utente; 
    - modifica password. 

- `Gestione Abbonamenti`
    - Visualizzazione di tutti i clienti abbonati;
    - Visualizzazione dei clienti con un abbonamento attivo; 
    - Visualizzazione dei prodotti che hanno un offerta per abbonati; 
    - Modifica del prezzo dell'abbonamento;
    - Ricerca di un abbonamento; 
    - Modifica dei dati relativi ad un cliente (questa operazione può essere effetuata solo successivamente alla ricerca);
    - Rinnovare un abbonamento già esistente;
    - Visualizzazione delle statistiche relative agli abbonamenti (visualizzazione di quanti abbonamenti sono stati emessi durante una giornata).

- `Gestione Vendite`
    - Registrazione di un acquisto;
    - Registrazione di un abbonamento; 
    - Visualizzazione delle vendite in una giornata;
    - Visualizzazione dell'incasso totale di una giornata.

Per lo sviluppo della GUI è stato utilizzato `PyQt5` che è un set completo di collegamenti Python per Qt v5. Di seguito verranno dettagliate le varie operazioni che consente di eseguire il Software. 
Tutti i dati del software vengono memorizzati all'interno dei file. (per installare PyQt5 andare su prompt dei comandi e digitare `pip install pyqt5`)
## Gestione Fumetteria - Home

<p align="center">
  <img  src="https://github.com/AlessandroS01/GestioneFumetteria/blob/main/Mockup%20png/Homep.png?raw=true">
</p>

Qui sopra è mostrata la schermata `Home` raggiungibile dopo aver effettuato il `Login`. Da questa schermata l'Amministratore della fumetteria può navigare tra le diverse sezioni e effettuare tutte le operazioni.

## Gestione Fumetteria - Gestione Magazzino

<p align="center">
  <img  src="https://github.com/AlessandroS01/GestioneFumetteria/blob/main/Mockup%20png/GestioneMagazzinoPrincipale.png?raw=true">
</p>

Qui sopra è mostrata la schermata `Gestione magazzino` raggiungibile dopo aver cliccato su Gestione Magazzino nella `Home`

Nella sezione Gestione Magazzino è possibile:
- **Visualizzare il magazzino:** cliccando su `visualizza magazzino` viene aperta una schermata dove è presente una tabella con tutte le informazioni relative ai prodotti presenti nel magazzino. 
- **Ricercare i prodotti presenti nel magazzino:** cliccando su `ricerca prodotto` sarà possibile effettuare la ricerca di un prodotto all'interno del magazzino. Quest ultima avviene tramite il codice seriale del prodotto. Una volta inserito il codice seriale, se il prodotto è presente nel magazzino viene aperta una schermata con tutti i dettagli, in caso contrario viene stampato un messaggio di errore.
- **Inserire e modificare i prodotti:** cliccando su `aggiungi prodotto` si apre una finestra dove è possibile inserire tutte le informazioni riguardanti il prodotto e completare l'operazione. Per modificare un prodotto bisogna invece effettuare prima la ricerca e poi successivamente cliccare sul pulsante `modifica` e scegliere le informazioni che si vogliono modificare.
- **Aggiungere un offerta per un prodotto:** per aggiungere un offerta bisogna effettuare prima la ricerca, poi successivamente cliccare su `aggiungi offerta`, se il prodotto presenta già un offerta verrà visualizzato un messaggio di errore, in caso contrario sarà possibile scegliere il tipo di offerta che si vuole aggiungere (generale o abbonati), il prezzo che verrà applicato al prodotto con l'offerta e la data di scadenza dell'offerta. Nel caso in cui un prodotto presenta già un offerta è possibile modificarla effettuando la ricerca e cliccando su modifica prodotto.

## Gestione Fumetteria - Gestione Account

<p align="center">
  <img  src="https://github.com/AlessandroS01/GestioneFumetteria/blob/main/Mockup%20png/Gestione%20Account.png?raw=true">
</p>

Qui sopra è mostrata la schermata `Gestione Account` raggiungibile dopo aver cliccato su Gestione Account nella `Home`

Nella sezione Gestione Account è possibile: 
- **Modificare il nome utente:** cliccando su `modifica nome utente`, e inserendo le informazioni necessarie si puo modificare il nome utente con cui si effettua il login al software. 
- **Modificare la password:** cliccando su `modifica password`, e inserendo le informazioni necessarie si puo modificare la passwrod con cui si effettua il login al software.

## Gestione Fumetteria - Gestione Abbonamenti 

Qui sopra è mostrata la schermata `Gestione Abbonamenti` raggiungibile dopo aver cliccato su Gestione Abbonamenti nella `Home`

<p align="center">
  <img  src="https://github.com/AlessandroS01/GestioneFumetteria/blob/main/Mockup%20png/GestioneAbbonamenti.png?raw=true">
</p>

Nella sezione Gestione Abbonamenti è possibile: 
- **Visualizzare tutti i clienti abbonati:** cliccando su `visualizza clienti abbonati` verrà aperta una finestra con una tabella con tutte le informazioni relative agli abbonamenti (attivi e non attivi).
- **Visualizzare tutti i clienti con un abbonamento attivo:** cliccando su `visualizza abbonamenti attivi` verrà aperta una finestra con tutte le informazioni relative agli abbonamenti e ai clienti che hanno un abbonamento attivo, overro un abbonamento non ancora scaduto (ogni abbonamento ha una data di scadenza).
- **Visualizzare i prodotti per abbonati:** cliccando su `visualizza prodotti per abbonati` verrà visualizzata una tebaella con tutte le informazioni relative ai prodotti che presentano un offerta per soli abbonati attiva.
- **Modificare il prezzo dell'abbonamento:** cliccando su `modifica prezzo abbonamento` sarà possibile impostare un nuovo prezzo per l'abbonamento.
- **Ricercare un abbonamento:** cliccando su `ricerca abbonamento` sarà possibile effettuare una ricerca tramite il codice abbonamento e nel caso in cui l'abbonamento esista verranno visualizzate tute le informazioni relative all'abbonamento e al cliente che usufruisce di quest ultimo, in caso contrario verrà visualizzato un messaggio di errore.
- **Modificare i dati di un cliente che usufruisce di un abbonamento**: per effettuare questa operazione è necessario prima effettuare una ricerca, una volta trovato l'abbonamento verranno visualizzate tutte le informazioni relative all'abbonamento e al cliente. In questa schermata cliccando su `modifica` si potrà scegliere quali informazioni riguardanti il cliente si vuole modificare e procedere con la modifica.
- **Rinnovare un abbonamento:** per effettuare il rinnovo di un abbonamento è necessario effetuare prima una ricerca e una volta trovato l'abbonamento verranno visualizzate tutte le informazioni relative ad esso e al cliente. In questa schermata cliccando su `rinnova abbonamento` verrà automaticamente aggiornata la data di scadenza.
- **Visualizzare le statistiche relative agli abbonamenti:** cliccando su `visualizza abbonamenti` verrà visualizzata una schermata nella quale sarà possibile inserire la data. Una volta inserita, verrà visualizzata una tabella con tutte le informazioni relative agli abbonamenti emessi in tale data.

## Gestione Fumetteria - Gestione Vendite

Qui sopra è mostrata la schermata `Gestione Vendite` raggiungibile dopo aver cliccato su Gestione Vendite nella `Home`

<p align="center">
  <img  src="https://github.com/AlessandroS01/GestioneFumetteria/blob/main/Mockup%20png/GestioneVenditePrincipale.png?raw=true">
</p>

Nella sezione Gestione Vendite è possibile: 
- **Registrare un acquisto:** cliccando su `registrazione acquisto` verrà visualizzata una finestra nella quale sarà possibile inserire un codice abbonamento, utilizzato per applicare eventuali offerte per i clienti abbonati (l'inserimento del codice è facoltativo). Una volta inserito il codice (o dopo aver proseguito senza inserirlo) si aprirà una schermata contenente una tabella con tutti i prodotti e le relative informazioni. In questa schermata sarà possibile effettuare una ricerca dinamica all'interno della tabella e selezionare i prodotti acquistati dal cliente. Una volta selezionati, cliccando su `aggiungi acquisto`, si aprirà una schermata con le seguenti informazioni: data corrente, lista di prodotti selezionati con relativa quantità e prezzo con annesse eventuali offerte. Da questa schermata, cliccando su `registrazione scontrino`, verrà effettuata correttamente la registrazione dell'acquisto. 
- **Acquistare un abbonamento:** cliccando su `acquisto abbonamento` verrà visualizzata una schermata nella quale poter inserire tutte le informazioni relative al cliente che sta effettuando l'acquisto. Da quest schermata, cliccando su `inserisci`, nel caso in cui il cliente non abbia già un abbonamento sarà registrato l'abbonamento acquistato.
- **Visualizzare le vendite in una determinata giornata:** cliccando su `visualizza vendite giornata` verrà visualizzata una finestra nella quale inserire una data. Una volta inserita, verrà visualizzata una tabella contenente tutti i prodotti e le relative quantità vendute in quella data.
- **Visualizzare l'incasso totale di una giornata:** cliccando su `visualizza incasso giornata` verrà visualizzata una finestra nella quale inserire una data. Una volta inserita, verrà visualizzato l'incasso totale in quella data.
