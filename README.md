
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
    - modifica nome utente e password. 

- `Gestione Abbonamenti`
    - Visualizzazione di tutti i clienti Abbonamenti;
    - Visualizzazione dei clienti con un abbonamento attivo; 
    - Visualizzazione dei prodotti che hanno un offerta per abbonati; 
    - Modifica del prezzo dell'abbonamento;
    - Ricerca di un abbonamento; 
    - Modifica dei dati relativi ad un cliente (questa operazione può essere effetuata solo successivamente alla ricerca);
    - Visualizzazione delle statistiche relative agli abbonamenti (visualizzazione di quanti abbonamenti sono stati emessi durante una giornata).

- `Gestione Vendite`
    - Registrazione di un acquisto
    - Registrazione di un abbonamento 
    - Visualizzazione delle vendite in una giornata
    - Visualizzazione dell'incasso totale di una giornata

Per lo sviluppo della GUI è stato utilizzato `PyQt5` che è un set completo di collegamenti Python per Qt v5. Di seguito verranno dettagliate le varie operazioni che consente di eseguire il Software.
Tutti i dati del software vengono memorizzati all'interno dei file. 
## Gestione Fumetteria - Home

<p align="center">
  <img  src="https://github.com/AlessandroS01/GestioneFumetteria/blob/main/Mockup%20png/Homep.png?raw=true">
</p>

Qui sopra è mostrata la schermata `Home` raggiungibile dopo aver effettuato il `Login`. Da questa schermata l'Amministratore della fumetteria può navigare tra le diverse sezioni e effettuare tutte le operazioni.

## Gestione Fumetteria - Gestione Magazzino

<p align="center">
  <img  src="https://github.com/AlessandroS01/GestioneFumetteria/blob/main/Mockup%20png/GestioneMagazzinoPrincipale.png?raw=true">
</p>

Nella sezione Gestione Magazzino è possibile:
- **Visualizzare il magazzino:** viene aperta una schermata dove è presente una tabella con tutti i prodotti presenti nel magazzino. 
- **Ricercare i prodotti presenti nel magazzino:** la ricerca all'interno del magazzino avviene tramite il codice seriale del prodotto. Una volta inserito il codice seriale, se il prodotto è presente nel magazzino viene aperta una schermata con tutti i dettagli, in caso contrario viene stampato un messaggio di errore.
- **Inserire e modificare i prodotti:** una volta cliccato su aggiungi prodotto si apre una finestra dove è possibile inserire tutte le informazioni riguardanti il prodotto e completare l'operazione. Per modificare un prodotto bisogna invece effettuare prima la ricerca e poi successivamente cliccare sul pulsante modifica e scegliere le informazioni che si vogliono modificare.
- **Aggiungere un offerta per un prodotto:** per aggiungere un offerta bisogna effettuare prima la ricerca, poi successivamente cliccare su aggiungi offerta, se il prodotto presenta già un offerta verrà visualizzato un messaggio di errore, in caso contrario sarà possibile scegliere il tipo di offerta che si vuole aggiungere (generale o abbonati), il prezzo che verrà applicato al prodotto con l'offerta e la data di scadenza dell'offerta. Nel caso in cui un prodotto presenta già un offerta è possibile modificarla effettuando la ricerca e cliccando su modifica prodotto.

