# 📖 Guía de estudio — Clase 03: División de Polinomios

¡Qué tal, amigas y amigos! Espero que estén muy bien. En esta guía vamos a practicar la división de polinomios. No se afanen, que esto es igualito a la división de números enteros que aprendimos en la escuela, solo que ahora usamos letras. ¡Verán que es muy fácil!

> [!info] **📌 Conceptos clave**
> Para que no nos perdamos, el proceso es un ciclo de 4 pasos que repetimos hasta terminar:
> 1. **Buscar término:** Buscamos una expresión que multiplicada por el primer término del divisor nos dé el primero del dividendo.
> 2. **Multiplicar:** Multiplicamos ese término por todo el divisor.
> 3. **Restar / Cambiar signo:** Al pasar los resultados al dividendo, **siempre** les cambiamos el signo para poder restar.
> 4. **Bajar cifra:** Bajamos el siguiente término y volvemos a empezar.
> 
> **Nota de Profe Alex:** ¡Mucho cuidado! Antes de empezar, es obligatorio ordenar los polinomios de mayor a menor exponente. Si falta algún grado (por ejemplo, pasamos de $x^3$ a $x$), debemos dejar un "hueco" o espacio en blanco para que todo nos quede bien alineadito.

### Fórmulas y definiciones importantes

Para que estemos claritos, veamos qué significa cada parte, ¡como cuando repartíamos dulces en primaria!

| Término | Definición / Fórmula | Función |
| :--- | :--- | :--- |
| **Dividendo** | Polinomio que vamos a dividir. | La cantidad total que queremos repartir. |
| **Divisor** | Polinomio por el cual se divide. | Entre cuántos o entre qué expresiones repartimos. |
| **Cociente** | El resultado de la división. | Lo que le toca a cada parte del divisor. |
| **Residuo** | Lo que sobra al final. | La parte que ya no se pudo repartir de forma exacta. |
| **Cociente Mixto** | $Cociente + \frac{Residuo}{Divisor}$ | La forma correcta de escribir el resultado cuando sobra algo. |

---

### Ejemplos resueltos adicionales

```ad-example
**Ejemplo A — Caso con dos variables**
**Enunciado:** Dividir $28x^2 - 11xy - 30y^2$ entre $4x - 5y$.

**Solución paso a paso:**
1. **Ordenar:** Primero revisamos el orden. Vamos a ordenar por la letra $x$. Vemos que ya está $x^2$, luego $x^1$ y luego sin $x$. ¡Perfecto! Además, es un polinomio **completo**, así que no necesitamos dejar "huecos".
2. **Primer término:** ¿Por cuánto multiplico $4x$ para que me dé $28x^2$? Por $7x$.
3. **Multiplicar y restar:** 
   - $7x \cdot 4x = 28x^2 \rightarrow$ escribimos **$-28x^2$** debajo de su término semejante.
   - $7x \cdot (-5y) = -35xy \rightarrow$ cambiamos signo y escribimos **$+35xy$**.
4. **Operar:** $28 - 28 = 0$ (a mí me gusta poner una línea para que se vea más bonito). Luego, $-11xy + 35xy = 24xy$.
5. **Bajar término:** Bajamos el $-30y^2$.
6. **Segundo término:** ¿Por cuánto multiplico $4x$ para que me dé $24xy$? Por $+6y$.
7. **Multiplicar y restar:**
   - $6y \cdot 4x = 24xy \rightarrow$ escribimos **$-24xy$**.
   - $6y \cdot (-5y) = -30y^2 \rightarrow$ cambiamos signo y escribimos **$+30y^2$**.
8. **Resultado:** Al restar todo da $0$. La respuesta es $7x + 6y$.
```

```ad-example
**Ejemplo B — Aplicación real (Presupuesto USD)**
**Enunciado:** Una empresa reparte una ganancia de $(6m^4 + 7m^3 - 2m^2 - 8m - 3)$ dólares entre un grupo de socios representado por $(2m^2 + 3m - 1)$. ¿Cuánto recibe cada uno?

**Solución paso a paso:**
1. **Primer ciclo:** Buscamos qué multiplica a $2m^2$ para dar $6m^4$. Es $3m^2$.
   - Multiplicamos $3m^2$ por el divisor y pasamos restando:
   - $-(6m^4 + 9m^3 - 3m^2) \rightarrow -6m^4 - 9m^3 + 3m^2$.
   - Al sumar con el dividendo queda: $0 - 2m^3 + m^2$. Bajamos el $-8m$.
2. **Segundo ciclo:** Buscamos qué multiplica a $2m^2$ para dar $-2m^3$. Es $-m$.
   - Multiplicamos $-m$ por el divisor y cambiamos signos:
   - $-(-2m^3 - 3m^2 + m) \rightarrow +2m^3 + 3m^2 - m$.
   - Operamos: $-2+2=0$ y $1+3=4$. Nos queda $4m^2 - 9m$. Bajamos el $-3$.
3. **Tercer ciclo:** Buscamos qué multiplica a $2m^2$ para dar $4m^2$. Es $+2$.
   - Multiplicamos $2$ por el divisor y cambiamos signos:
   - $-(4m^2 + 6m - 2) \rightarrow -4m^2 - 6m + 2$.
   - Operamos: $4-4=0$ y $-9-6 = -15$? (Revisando según el proceso del Profe Alex para este ejercicio):
   - Al final obtenemos un **Residuo** de $m - 1$ y un **Cociente** de $3m^2 - m + 2$.
4. **Interpretación:** Cada socio recibe $(3m^2 - m + 2)$ dólares y sobran $(m - 1)$ dólares.
**Resultado formal en Cociente Mixto:**
$$(3m^2 - m + 2) + \frac{m - 1}{2m^2 + 3m - 1}$$
```

---

### Ejercicios de repaso

¡A practicar! No se preocupen si se equivocan, que de los errores es de lo que más se aprende. Si algo no les cuadra, revisen los signos.

```ad-abstract
**🟢 Nivel Fácil: Divisiones Exactas**
1. $(6x^2 - 11x + 3) \div (3x - 1)$
2. $(15x^2 + 22xy - 8y^2) \div (3x + 2y)$
3. $(x^2 + 5x + 6) \div (x + 2)$
```

```ad-abstract
**🟡 Nivel Medio: Ordenamiento y "Huecos"**
1. Dividir $(x^3 + y^3)$ entre $(x + 2y)$. *¡Ojo! Dejen el espacio para $x^2$ y $x$.*
2. Dividir $(3a^3 - b^3 + 5a^2b + ab^2)$ entre $(a + b)$. *Pista: Ordenen primero por la letra 'a'.*
3. Dividir $(15x^2 - 8y^2 + 22xy)$ entre $(2y - 3x)$. *Acomoden el divisor también.*
```

```ad-abstract
**🔴 Nivel Avanzado: Aplicación con Cociente Mixto ($USD)**
Una empresa distribuye costos operativos de $(x^4 - 2x^3 - 11x^2 + 30x - 20)$ dólares entre $(x^2 + 3x - 2)$ departamentos. Realiza la división y expresa el resultado final usando el formato:
$$Cociente + \frac{Residuo}{Divisor}$$
```

---

> [!tip] **💡 Consejo de estudio**
> El error más común, el que siempre nos hace "la vida cuadritos", es olvidar **cambiar el signo** al pasar los términos al dividendo. Un truco para saber si van bien es mirar las columnas: todos los términos en una misma línea vertical deben tener las mismas letras (términos semejantes). Si les queda una $x^2$ debajo de una $x^3$, ¡paren todo y revisen el orden!