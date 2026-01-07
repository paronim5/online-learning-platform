# SPSE Ječná – Testovací případ

**ID testu:** FUN_01  
**Vytvořil test:** Pavlo Kosov  
**Název testu:** Základní workflow – Registrace & Zápis do kurzu  
**Stručný popis:** Ověření kompletního průběhu registrace nového studenta, vytvoření kurzu a zápisu studenta do kurzu pomocí transakce.  
**Předpoklady:** Aplikace je spuštěná, databáze je inicializovaná.  
**Závislosti a požadavky:** Žádné.

| Krok | Testovací kroky                                          | Testovací data                                      | Očekávaný výsledek                                              | Poznámky |
|------|----------------------------------------------------------|-----------------------------------------------------|------------------------------------------------------------------|----------|
| 1    | Vytvořte nového lektora přes „Správa lektorů“            | Jméno: `Test Prof`<br>Email: `prof@test.com`<br>Hodnocení: `5.0` | Lektor úspěšně vytvořen. Zobrazí se ID.                         |          |
| 2    | Vytvořte nový kurz přes „Správa kurzů“                   | Název: `Test 101`<br>Cena: `100`<br>Úroveň: `Začátečník` | Kurz úspěšně vytvořen. Zobrazí se ID.                           |          |
| 3    | Přejděte do „Pokročilé operace“ a vyberte „Registrace nového studenta & Zápis“ | Jméno: `Nový Student`<br>Email: `new@student.com`   | Systém vyzve k výběru kurzu                                     |          |
| 4    | Dokončete transakční zápis do kurzu                      | Vyberte ID kurzu z kroku 2                          | „Student byl úspěšně zaregistrován a zapsán do kurzu.“          |          |
| 5    | Ověřte vytvoření studenta přes „Správa studentů“         | Vyberte „Zobrazit všechny studenty“                 | V seznamu se objeví „Nový Student“                              |          |
| 6    | Ověřte zápis do kurzu přes „Správa zápisů“               | Vyberte „Zobrazit všechny zápisy“                   | „Nový Student“ je uveden u kurzu „Test 101“ s postupem 0 %     |          |
| 7    | Pokus o duplicitní registraci (test zpracování chyby)    | Stejná data jako v kroku 3                          | Systém zobrazí chybu (Duplicitní záznam / Transakce selhala), ale nespadne |          |