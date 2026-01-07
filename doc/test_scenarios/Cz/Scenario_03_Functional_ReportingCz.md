# SPSE Ječná – Testovací případ

**ID testu:** FUN_02  
**Vytvořil test:** Pavlo Kosov  
**Název testu:** Reporty & Hromadný import dat  
**Stručný popis:** Ověření možnosti hromadného importu dat z různých formátů a generování agregovaných reportů o výkonnosti.  
**Předpoklady:** Aplikace je spuštěná. Datové soubory (`students.csv`, `instructors.json`, `courses.xml`) existují ve složce `data/`.  
**Závislosti a požadavky:** Oprávnění ke čtení složky `data/`.

| Krok | Testovací kroky                                          | Testovací data                  | Očekávaný výsledek                                           | Poznámky |
|------|----------------------------------------------------------|---------------------------------|--------------------------------------------------------------|----------|
| 1    | Přejděte do menu „Import dat“                            | Vyberte volbu `6`               | Zobrazí se možnosti importu (CSV, JSON, XML)                 |          |
| 2    | Import studentů z CSV souboru                            | Soubor: `data/students.csv`     | Hlášení: „Úspěšně importováno X studentů“                    |          |
| 3    | Import lektorů z JSON souboru                            | Soubor: `data/instructors.json` | Hlášení: „Úspěšně importováno X lektorů“                     |          |
| 4    | Import kurzů z XML souboru                               | Soubor: `data/courses.xml`      | Hlášení: „Úspěšně importováno X kurzů“                       |          |
| 5    | Vygenerujte „Report výkonnosti kurzů“ přes „Pokročilé operace“ | Vyberte volbu `5`               | Tabulka zobrazí agregovaná data (průměrné skóre, min, max) pro kurzy |          |
| 6    | Ověřte zobrazení „Nejlépe hodnocené kurzy“               | Vyberte volbu `7` (Pokročilé)   | Tabulka zobrazí kurzy seřazené podle hodnocení lektora       |          |
| 7    | Test zpracování chyby konfigurace (simulovaný)           | Přejmenujte `.env` na `.env.neco` a restartujte aplikaci | Aplikace zobrazí chybu připojení srozumitelně, žádný surový stack trace |          |