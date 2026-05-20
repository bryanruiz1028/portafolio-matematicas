# 📖 Guía de estudio — Clase 06: División de Polinomios

> [!info] 📌 Conceptos clave
> - **Ordenamiento y Espacios:** Antes de dividir, ordena el dividendo y el divisor de forma descendente (del exponente mayor al menor). Si falta un grado de la variable (ej. de $x^3$ pasa a $x^1$), deja un espacio vacío; esto evita sumar términos que no son "pantalones" iguales.
> - **La Analogía de los "Pantalones":** En suma y resta, tratamos a las letras como objetos. Si tienes $5$ pantalones ($x^2$) y quitas $3$ pantalones ($x^2$), te quedan $2$ pantalones ($x^2$). **Los exponentes no cambian** en la suma/resta.
> - **Pilas con los Signos:** En la suma y resta **no se hace operación de signos** (ej. $-7 - 4 = -11$, no $+11$). Sin embargo, en la división, al multiplicar el cociente por el divisor, debes "darle la vuelta" al signo antes de escribirlo abajo para restar.
> - **Estrategia de "Objetivo" (Exponentes Literales):** Para dividir términos con letras en el exponente, busca qué le falta al divisor para alcanzar al dividendo. Si tienes $x^n$ y quieres llegar a $x^{n+2}$, debes multiplicar por $x^2$, ya que en la multiplicación los exponentes se suman ($n + 2$).

## 2. Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Términos Semejantes** | Aquellos con la misma parte literal (letras y exponentes iguales). Si el coeficiente es $1$, generalmente no se escribe. Solo estos se pueden sumar o restar entre sí. |
| **Ley de Exponentes** | Al multiplicar potencias de la misma base, se mantiene la base y se suman los exponentes: $x^a \cdot x^b = x^{a+b}$. |
| **Cambio de Signo** | Regla operativa: Multiplicas el término del cociente por el divisor y el resultado se anota con el **signo opuesto** debajo del dividendo. |

## 3. Ejemplos Resueltos Adicionales

````ad-example
**Ejemplo A — División de polinomios simple**
**Enunciado:** Dividir $x^2 + xy - 2y^2$ entre $x + 2y$.

**Proceso paso a paso:**
1. **Ordenar:** Ya está ordenado respecto a $x$.
2. **Buscar el primer término:** ¿Por cuánto multiplico a $x$ para que me dé $x^2$? Por $x$.
3. **Multiplicar y cambiar signo:** 
   - $x \cdot x = x^2 \rightarrow$ anotamos $-x^2$.
   - $x \cdot 2y = 2xy \rightarrow$ anotamos $-2xy$.
4. **Operar:** $x^2 - x^2 = 0$. Luego, $1xy - 2xy = -1xy$. (Pilas: aquí no se hace "menos por menos", simplemente se resta).
5. **Bajar y repetir:** Bajamos $-2y^2$. Ahora, ¿por cuánto multiplico $x$ para que dé $-xy$? Por $-y$.
6. **Multiplicar y cambiar signo:**
   - $-y \cdot x = -xy \rightarrow$ anotamos $+xy$.
   - $-y \cdot 2y = -2y^2 \rightarrow$ anotamos $+2y^2$.
7. **Resultado:** Todo se elimina. El cociente es $x - y$.
````

````ad-example
**Ejemplo B — Repartición de costos**
**Enunciado:** Un costo total de producción es $(15m^2 - 8m - 12) \text{ USD}$. Si se produjeron $3m + 2$ artículos, ¿cuál es el costo unitario?

**Resolución:**
1. **Primer término:** $15m^2 \div 3m = 5m$.
2. **Multiplicar y cambiar signo:**
   - $5m \cdot 3m = 15m^2 \rightarrow$ escribimos $-15m^2$.
   - $5m \cdot 2 = 10m \rightarrow$ escribimos $-10m$.
3. **Restar:** El $15m^2$ se elimina. Para los términos en $m$: $-8m - 10m = -18m$.
4. **Segundo término:** ¿Qué multiplicado por $3m$ da $-18m$? El $-6$.
5. **Multiplicar y cambiar signo:**
   - $-6 \cdot 3m = -18m \rightarrow$ escribimos $+18m$.
   - $-6 \cdot 2 = -12 \rightarrow$ escribimos $+12$.
6. **Conclusión:** El residuo es $0$. 
**Costo unitario:** $(5m - 6) \text{ USD}$.
````

## 4. Ejercicios de Repaso

````ad-abstract
**Bloque Verde (Fácil)**
1. Realice la reducción de estos "pantalones": $-10a^2b - 3a^2b + 5a^2b$.
2. Ordene y prepare (dejando espacios si es necesario): $x^2 - 9$ entre $x + 3$.
3. Si al multiplicar el cociente por el divisor obtienes $+7xy^2$, ¿con qué signo debes escribirlo debajo del dividendo?
````

````ad-abstract
**Bloque Amarillo (Medio)**
1. Encuentra el exponente faltante: $x^{n+5} \cdot x^{[ \text{ ? } ]} = x^{2n+8}$.
2. Aplica la estrategia de "Objetivo": ¿Por cuánto multiplicas $m^a$ para que se convierta en $m^{a+3}$?
3. Divide $x^{a+2} + x^a$ entre $x + 1$. (Recuerda que al restar exponentes literales, debes ser cuidadoso con los términos independientes).
````

````ad-abstract
**Bloque Rojo (Avanzado — Aplicación \text{USD})**
1. Un presupuesto de $(15a^3 - 35a^2 + 15a) \text{ USD}$ se reparte entre $3a$ personas. ¿Cuánto recibe cada una?
2. Hallar el valor unitario: Costo total $(x^{2n} + 2x^n - 3) \text{ USD}$ entre $(x^n + 3)$ unidades.
3. El costo de una obra es $(6x^{2a+2} - 11x^{2a+1} + 4x^{2a}) \text{ USD}$. Si se divide entre $(3x^a - 4x^{a-1})$ metros cuadrados, ¿cuál es el costo por metro?
````

> [!tip] 💡 Consejo de estudio
> La clave de la división es la **eliminación**: si el primer término de tu resta no da cero, ¡revisa los signos! Además, si al restar se eliminan **dos términos al mismo tiempo** (doble eliminación), no te asustes: simplemente **baja los siguientes dos términos** del dividendo para poder continuar con la operación. Mantén siempre las columnas alineadas; los "pantalones" con los "pantalones" y las "camisas" con las "camisas".