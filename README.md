
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
    - Visualizzazione di tutti i clienti Abbonamenti;
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
Tutti i dati del software vengono memorizzati all'interno dei file. 
## Gestione Fumetteria - Home

<p align="center">
  <img style="border-radius:8px" src="https://github.com/AlessandroS01/GestioneFumetteria/blob/main/Mockup%20png/Homep.png?raw=true">
</p>

Qui sopra è mostrata la schermata `Home` raggiungibile dopo aver effettuato il `Login`. Da questa schermata l'Amministratore della fumetteria può navigare tra le diverse sezioni e effettuare tutte le operazioni.

## Gestione Fumetteria - Gestione Magazzino

<p align="center">
  <img style="border-radius:8px" src="https://github.com/AlessandroS01/GestioneFumetteria/blob/main/Mockup%20png/GestioneMagazzinoPrincipale.png?raw=true">
</p>

Qui sopra è mostrata la schermata `Gestione magazzino` raggiungibile dopo aver cliccato su Gestione Magazzino nella `Home`

Nella sezione Gestione Magazzino è possibile:
- **Visualizzare il magazzino:** cliccando su `visualizza magazzino` viene aperta una schermata dove è presente una tabella con tutte le informazioni relative ai prodotti presenti nel magazzino. 
- **Ricercare i prodotti presenti nel magazzino:** cliccando su `ricerca prodotto` sarà possibile effettuare la ricerca di un prodotto all'interno del magazzino. Quest ultima avviene tramite il codice seriale del prodotto. Una volta inserito il codice seriale, se il prodotto è presente nel magazzino viene aperta una schermata con tutti i dettagli, in caso contrario viene stampato un messaggio di errore.
- **Inserire e modificare i prodotti:** cliccando su `aggiungi prodotto` si apre una finestra dove è possibile inserire tutte le informazioni riguardanti il prodotto e completare l'operazione. Per modificare un prodotto bisogna invece effettuare prima la ricerca e poi successivamente cliccare sul pulsante `modifica` e scegliere le informazioni che si vogliono modificare.
- **Aggiungere un offerta per un prodotto:** per aggiungere un offerta bisogna effettuare prima la ricerca, poi successivamente cliccare su `aggiungi offerta`, se il prodotto presenta già un offerta verrà visualizzato un messaggio di errore, in caso contrario sarà possibile scegliere il tipo di offerta che si vuole aggiungere (generale o abbonati), il prezzo che verrà applicato al prodotto con l'offerta e la data di scadenza dell'offerta. Nel caso in cui un prodotto presenta già un offerta è possibile modificarla effettuando la ricerca e cliccando su modifica prodotto.

## Gestione Fumetteria - Gestione Account

<p align="center">
  <img style="border-radius:8px" src="https://github.com/AlessandroS01/GestioneFumetteria/blob/main/Mockup%20png/Gestione%20Account.png?raw=true">
</p>

Qui sopra è mostrata la schermata `Gestione Account` raggiungibile dopo aver cliccato su Gestione Account nella `Home`

Nella sezione Gestione Account è possibile: 
- **Modificare il nome utente:** cliccando su `modifica nome utente`, e inserendo le informazioni necessarie si puo modificare il nome utente con cui si effettua il login al software. 
- **Modificare la password:** cliccando su `modifica password`, e inserendo le informazioni necessarie si puo modificare la passwrod con cui si effettua il login al software.

## Gestione Fumetteria - Gestione Abbonamenti 

Qui sopra è mostrata la schermata `Gestione Abbonamenti` raggiungibile dopo aver cliccato su Gestione Abbonamenti nella `Home`

<p align="center">
  <img style="border-radius:8px" src="https://github.com/AlessandroS01/GestioneFumetteria/blob/main/Mockup%20png/GestioneAbbonamenti.png?raw=true">
</p>

Nella sezione Gestione Abbonamenti è possibile: 
- **Visualizzare tutti i clienti abbonati:** cliccando su `visualizza clienti abbonati` verrà aperta una finestra con una tabella con tutte le informazioni relative agli abbonamenti (attivi e non attivi).
- **Visualizzare tutti i clienti con un abbonamento attivo:** cliccando su `visualizza abbonamenti attivi` verrà aperta una finestra con tutte le informazioni relative agli abbonamenti e ai clienti che hanno un abbonamento attivo, overro un abbonamento non ancora scaduto (ogni abbonamento ha una data di scadenza).
- **Visualizzare i prodotti per abbonati:** cliccando su `visualizza prodotti per abbonati` verrà visualizzata una tebaella con tutte le informazioni relative ai prodotti che presentano un offerta per soli abbonati attiva.
- **Modificare il prezzo dell'abbonamento:** cliccando su `modifica prezzo abbonamento` sarà possibile impostare un nuovo prezzo per l'abbonamento.
- **Ricercare un abbonamento:** cliccando su `ricerca abbonamento` sarà possibile effettuare una ricerca tramite il codice abbonamento e nel caso in cui l'abbonamento esista verranno visualizzate tute le informazioni relative all'abbonamento e al cliente che usufruisce di quest ultimo, in caso contrario verrà visualizzato un messaggio di errore.
- **Modificare i dati di un cliente che usufruisce di un abbonamento**: per effettuare questa operazione è necessario prima effettuare una ricerca, una volta trovato l'abbonamento verranno visualizzate tutte le informazioni relative all'abbonamento e al cliente. In questa schermata cliccando su `modifica` si potrà scegliere quali informazioni riguardanti il cliente si vuole modificare e procedere con la modifica.
