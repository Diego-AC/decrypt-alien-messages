# Descifrador de mensajes alienígenas

1. [Información general](#información-general)

  1.1. [Contexto](#contexto)

  1.2. [Tecnologías](#tecnologías)

2. [Comentarios](#comentarios)
2. [Aspectos de mejora](#aspectos-de-mejora)

## Información general

El descifrador de mensajes alienígenas es un algoritmo que permite determinar el número de posibles interpretaciones para un patrón de mensajes dado.

### Contexto
Después de años de estudio, los científicos han descubierto una lengua extraterrestre transmitida desde un planeta lejano. El lenguaje alienígena es único en el sentido de que cada palabra es única ya que consta exactamente de **L** letras minúsculas. Además, hay exactamente **D** palabras en este idioma.

Una vez que se construyó el diccionario de todas las palabras en el idioma alienígena, el siguiente avance fue descubrir que los alienígenas han estado transmitiendo mensajes a la Tierra durante la última década. Desafortunadamente, estas señales se debilitan debido a la distancia entre nuestros dos planetas y algunas de las palabras pueden malinterpretarse.

Un patrón consta exactamente de **L** tokens. Cada token es una sola letra minúscula (los científicos están muy seguros de que esta es la letra) o un grupo de letras únicas. Por ejemplo: **(ad)d(dc)** significa que la primera letra es **a** o **d**, la segunda letra es definitivamente **d** y la última letra es **d** o **c**. Por lo tanto, el patrón **(ad)d(dc)** puede representar cualquiera de estas 4 posibilidades: **add, adc, bdd, bdc**.
### Tecnologías

* [Python](https://www.python.org/) Version 3.9.5

## Comentarios
* #### ¿Por qué usar funciones para obtener los datos de entrada?
  Las funciones `get_words()` y `get_cases()` están pensadas con el paradigma de que eventualmente podrían aumentar sus valores iniciales. Según el enunciado, los científicos tienen un diccionario de todas las palabras alienígena, sin embargo no se niega la posibilidad de que este diccionario aumente su cantidad de registros. Lo anterior es más evidente con los casos de pruebas, ***si ya se han recibido mensajes entonces podrían llegar más.***

  Por ello, las funciones `get_words()` y `get_cases()` simulan el resultado de un posible método de obtención de datos a partir de una herramienta de gestión de datos como podría ser una base de datos o un archivo plano.

  Ambas funciones fueron pensadas para que el algoritmo sea preparado para eventualmente aumentar la cantidad de casos de prueba y la cantidad de palabras alienígenas en el diccionario sin afectar su funcionamiento.

* #### El instructivo habla de 3 parametros enteros (L, D, N) ¿Por qué precindir de ellos?
  Esto se decide tras incluir el supuesto comentado en el punto anterior y es que ahora el paradigma habla de que estos números enteros podrían ser variable dependiendo del largo de cada conjunto de datos.

  Lo anterior, explica los parametros *D* y *N*, por ello para *L* hay que realizar una explicación más profunda. Por como está construido el algoritmo, para cada conjunto de posibles palabras de cada patrón, se realiza uno a uno la comparación con el diccionario alienígena de cada posible palabra.

  Esto significa que independiente del largo del patrón, si de la combinación no resulta una palabra correcta, esta no se contabilizará dentro de las palabra favorables de cada conjunto.

* #### Escalabilidad del algoritmo
  A partir de los puntos anteriores, es posible afirmar 3 cosas:
  * El algoritmo funcionará para palabras de largo **L**, donde **L** es un número entero  que puede ir desde el 1 hasta el infinito positivo.

  * El algoritmo funcionará para un conjunto de palabras (cantidad de palabras del diccionario alienígena) de largo **D**, donde **D** es un número entero  que puede ir desde el 0 hasta el infinito positivo.

  * El algoritmo funcionará para un conjunto de patrónes (cantidad de casos de prueba) de largo **N**, donde **N** es un número entero  que puede ir desde el 0 hasta el infinito positivo.

  Por ello te invito a poner a prueba el algoritmo considerando la 3 afirmaciones anteriores.


## Aspectos de mejora

* #### Función `extract_paretheses(args)`:
  Si bien esta función lleva como nombre extraer paréntesis, en la ejecución resulta hacer mucho más que eso, ya que también separa cada token de la palabra y adicionalmente lista cada posible valor de cada token de la palabra.

  Es decir:
  ```
  Extraer paréntesis: (ab)b(cd) => abbcd

  Extraer paréntesis y separar por token: (ab)b(cd) => ['ab', 'b', 'cd']

  Extraer paréntesis, separar por token y listar valores: (ab)b(cd) => [['a', 'b'],['b'], ['c', 'd']]
  ```

  En este caso el nombre de la función describe el primer caso y de manera parcial el segundo y tercer caso. Por lo tanto el aspecto de mejora podrían ser:

  * Renombrar función.
  * **Descomponer función en más funciones**

  *Personalmente prefiero la segunda opción por que nos permite tener funciones auxiliares que podrían reutilizarse en diversos casos.*

* #### Uso de expresiones regulares
  Si bien el uso de los métodos de expresiones regulares permitió cumplir objetivo (comprobar y extraer paréntesis respectivamente), no tuvo un comportamiento satisfactorio. Lo anterior se afirma por que en el caso de la extracción de paréntesis tuvo un inconveniente que obligó a realizar un paso adicional.

  En la función para extraer paréntesis, se esperaba que el uso de regex retornara un listado con el caso de prueba separado por token de la forma `a(bc)d => ['a', 'bc', 'd']`, sin embargo la ejecución tuvo como resultado `a(bc)d => ['a', '', 'bc', '', 'd']` lo que obligó a recorrer el listado quitando los valores vacíos en los índices que lo tuvieran.
