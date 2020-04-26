Als je tekst tussen specifieke tekens of reeksen tekens wilt vinden, kun je de `re` module van Python en de methode `findall()` gebruiken.

- Stel dat je de volgende tekenreeks hebt:

    ```python
    tekst = 'start Hier is een regel einde'
    ```

- Stel je voor dat je alle tekst tussen `'start'` en `'einde'` wilt vinden. Hier is de regex-zoekopdracht die je hiervoor zou kunnen gebruiken:

    ```python
    import re
    text = 'start Hier is een regel einde'
    overeenkomsten = re.findall(r'start.*einde', tekst)
    ```

- Als je nu de variabele `overeenkomsten` in de interpreter controleert, zul je zien dat het een lijst is met de overeenkomsten die Python heeft gevonden:

    ```python
    >>> overeenkomsten
    ['start Hier is een regel einde']
    ```

- Wat gebeurt er als er meer dan één overeenkomst is, zoals in het onderstaande voorbeeld?

    ```python
    import re
    tekst = 'start Hier is een regel einde start en hier is wat meer einde'
    overeenkomsten = re.findall(r'start.*einde', tekst)
    ```

    ```python
    >>> overeenkomsten
    ['start Hier is een regel einde start en hier is wat meer einde']
    ```

- Dat was niet wat we wilden. Dit komt omdat deze regex wordt beschreven als **hebzuchtig**. Dat betekent dat het de hele reeks doorzoekt voordat de overeenkomsten worden geretourneerd en vervolgens alle tekens tussen de eerste `'start'` en de laatste `'einde'` retourneert.

- Om de **regex** niet hebzuchtig te maken, moet je een `.*?` gebruiken in plaats van `*`.

    ```python
    import re
    tekst = 'start Hier is een regel einde start en hier is wat meer einde'
    overeenkomsten = re.findall(r'start.*?einde', tekst)
    ```

    ```python
    >>> overeenkomsten
    ['start Hier is een regel einde', 'start en hier is wat meer einde']
    ```

- Nu bevat de lijst twee elementen.

- Als je niet wilt dat Python de woorden `start` en `einde` in de resultaten opneemt, moet je de **regex** opdragen **vooruit te kijken** en **achteruit te kijken**. Er zijn twee regex-elementen die dat zullen doen:

- `?<=` betekent **vooruit kijken**. Gebruik dit om naar tekst **te zoeken na** de overeenkomst.

- `? =` betekent **achteruit kijken**. Gebruik het om naar tekst **te zoeken vóór** de overeenkomst.

- Om deze elementen te laten werken, moet je ze en het patroon waarnaar je op zoek bent omringen door haakjes:

    ```python
    overeenkomsten = re.findall(r'(?<=start).*?(?=einde)', tekst)
    ```

    ```python
    >>> overeenkomsten
    ['Hier is een regel', 'en hier is wat meer']
    ```

- Wat gebeurt er met tekenreeksen verspreid over meerdere lijnen, zoals die hieronder?

    ```python
    import re
    text = '''
    start
    Hier is een regel
    einde
    start
    en hier is nog wat
    einde'''

overeenkomsten = re.findall(r'(?<= start).*?(?= einde)', tekst)
    ```

    ```python
    >>> overeenkomsten
    []
    ```

- Dat is niet wat we wilden. Het probleem is dat nieuwe regels (`\n`) het zoeken naar regex stoppen. Het toevoegen van een `vlag` aan de zoekopdracht kan dit echter oplossen:

    ```python
    import re

    text = '''
    start
    Hier is een regel
    einde
    start
    en hier is nog wat
    einde'''

overeenkomsten = re.findall(r'(?<=start).*?(?=einde)', tekst, flags=re.DOTALL)
    ```

    ```python
    >>> overeenkomsten
[   '\nHier is een regel\n', '\nen hier is nog wat\n']
    ```

