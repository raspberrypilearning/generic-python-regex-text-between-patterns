Si deseas encontrar texto ubicado entre caracteres específicos o secuencias de caracteres, puedes usar el módulo de Python `re` y el método `findall()`.

- Supongamos que tienes la siguiente cadena:

    ```python
    text = 'start Aqui hay una linea end'
    ```

- Imagina que quieres encontrar todo el texto entre `'start'` y `'end'`. Aquí está la búsqueda de regex que puedes usar para hacerlo:

    ```python
    import re
    text = 'start Aqui hay una linea end'
    coincidencias = re.findall(r'start.*end', text)
    ```

- Si ahora revisas la variable `coincidencias` en el intérprete, verás que es una lista de las coincidencias que Python ha encontrado:

    ```python
    >>> matches
    ['start Aqui hay un fin de linea']
    ```

- ¿Qué pasa si hay más de una coincidencia, como en el ejemplo de abajo?

    ```python
    import re
    text = 'start Aqui hay una linea end start y aqui hay otra end'
    coincidencias = re.findall(r'start.*end', text)
    ```

    ```python
    >>> coincidencia
    ['start Aqui hay una linea end start y aqui hay otra end']
    ```

- Eso no era lo que queríamos. Esto es porque esta expresión regular se describe como **codiciosa**. Esto significa que busca toda la cadena antes de devolver la coincidencia, y luego devuelve todos los caracteres entre el primer `'start'` y el último `'end'`.

- Para hacer que el **regex** no sea codicioso, debes usar un `.*?` en lugar de `.*`.

    ```python
    import re
    text = 'start Aqui hay una linea end start y aqui hay otra end'
    coincidencias = re.findall(r'start.*?end', text)
    ```

    ```python
    >>> coincidencias
    ['start Aqui hay una linea end', 'start y aqui hay otra end']
    ```

- Ahora la lista contiene dos elementos.

- Si no quieres que Python incluya las palabras `start` y `end` en los resultados, entonces tienes que decirle al **regex** que **mire hacia adelante**  y **mire hacia atras**. Hay dos elementos regex que harán eso:

- `?<=` significa **mirar hacia adelante**. Úsalo para buscar texto **despues** de la coincidencia.

- `?=` significa **mirar hacia atras**. Úsalo para buscar texto **antes** de la coincidencia.

- Para que estos elementos funcionen, necesitas rodearlos y el patrón que estás buscando entre paréntesis:

    ```python
    coincidencia = re.findall(r'(?<=start).*?(?=end)', text)
    ```

    ```python
    >>> coincidencia
    ['Aqui hay una linea', 'y aqui hay otra']
    ```

- ¿Qué sucede con las cadenas distribuidas en múltiples líneas, como la de abajo?

    ```python
    import re
    text = '''
    start
    Aqui hay una linea
    end
    start
    y aqui hay otra
    end'''

    coincidencia = re.findall(r'(?<=start).*?(?=end)', text)
    ```

    ```python
    >>> coincidencia
    []
    ```

- Eso no era lo que queríamos. El problema es que las nuevas líneas (`\n`) detienen la búsqueda de expresiones regulares. Sin embargo, añadir una `bandera` a la búsqueda puede resolverla:

    ```python
    import re

    text = '''
    start
    Aqui hay una linea
    end
    start
    y aqui hay otra
    end'''

    coincidencia = re.findall(r'(?<=start).*?(?=end)', text, flags=re.DOTALL)
    ```

    ```python
    >>> coincidencias
    ['\nAqui hay una linea\n', '\ny aqui hay otra\n']
    ```

