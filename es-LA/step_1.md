Si deseas encontrar texto ubicado entre caracteres específicos o secuencias de caracteres, puedes usar el módulo de Python `re` y el método `findall()`.

- Supongamos que tienes la siguiente cadena:

    ```python
    texto = 'inicio Aquí hay una línea final'
    ```

- Imagina que quieres encontrar todo el texto entre `'inicio'` y `'final'`. Aquí está la búsqueda de regex que puedes usar para hacerlo:

    ```python
    import re
    texto = 'inicio Aquí hay una línea final'
    coincidencias = re.findall(r'inicio.*final', texto)
    ```

- Si ahora revisas la variable `coincidencias` en el intérprete, verás que es una lista de las coincidencias que Python ha encontrado:

    ```python
    >>> coincidencias
    ['inicio Aquí hay una línea final']
    ```

- ¿Qué pasa si hay más de una coincidencia, como en el ejemplo de abajo?

    ```python
    import re
    texto = 'inicio Aquí hay una línea final inicio y aquí hay otra final'
    coincidencias = re.findall(r'inicio.*final', texto)
    ```

    ```python
    >>> coincidencias
    ['inicio Aquí hay una línea final inicio y aquí hay otra final']
    ```

- Eso no era lo que queríamos. Esto es porque esta expresión regular se describe como **codiciosa**. Esto significa que busca toda la cadena antes de devolver la coincidencia, y luego devuelve todos los caracteres entre el primer `'inicio'` y el último `'final'`.

- Para hacer que el **regex** no sea codicioso, debes usar un `.*?` en lugar de `.*`.

    ```python
    import re
    texto = 'inicio Aquí hay una línea final inicio y aquí hay otra final'
    coincidencias = re.findall(r'inicio.*?final', texto)
    ```

    ```python
    >>> coincidencias
    ['inicio Aquí hay una línea final', 'inicio y aquí hay otra final']
    ```

- Ahora la lista contiene dos elementos.

- Si no quieres que Python incluya las palabras `inicio` y `final` en los resultados, entonces tienes que decirle al **regex** que **mire hacia adelante** y **mire hacia atras**. Hay dos elementos regex que harán eso:

- `?<=` significa **mirar hacia adelante**. Úsalo para buscar texto **despues** de la coincidencia.

- `?=` significa **mirar hacia atras**. Úsalo para buscar texto **antes** de la coincidencia.

- Para que estos elementos funcionen, necesitas rodearlos y el patrón que estás buscando entre paréntesis:

    ```python
    coincidencias = re.findall(r'(?<=inicio).*?(?=final)', texto)
    ```

    ```python
    >>> coincidencias
    [' Aquí hay una línea ', ' y aquí hay otra ']
    ```

- ¿Qué sucede con las cadenas distribuidas en múltiples líneas, como la de abajo?

    ```python
    import re
    texto = '''
    inicio
    Aquí hay una línea
    final
    inicio
    y aquí hay otra
    final'''

    coincidencias = re.findall(r'(?<=inicio).*?(?=final)', texto)
    ```

    ```python
    >>> coincidencias
    []
    ```

- Eso no era lo que queríamos. El problema es que las nuevas líneas (`\n`) detienen la búsqueda de expresiones regulares. Sin embargo, añadir una `bandera` a la búsqueda puede resolverla:

    ```python
    import re

    texto = '''
    inicio
    Aquí hay una línea
    final
    inicio
    y aquí hay otra
    final'''

    coincidencias = re.findall(r'(?<=inicio).*?(?=final)', texto, flags=re.DOTALL)
    ```

    ```python
    >>> coincidencias
    ['\nAquí hay una línea\n', '\ny aquí hay otra\n']
    ```

