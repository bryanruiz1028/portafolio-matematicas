# 📖 Guía de estudio — Clase 06: Solución de problemas con Sistemas de Ecuaciones Lineales 2x2

> [!info] 📌 Conceptos clave
> Para dominar la resolución de problemas mediante sistemas $2 \times 2$, un estudiante de secundaria debe seguir un proceso lógico que garantice no solo el resultado, sino la comprensión del mismo:
> 1. **Estimación mental:** Antes de usar álgebra, intenta "tantear" valores posibles. Según el *profe Alex*, esto desarrolla el sentido numérico y te permite saber si tu respuesta final es coherente.
> 2. **Definición de variables:** Asigna letras representativas (como $n$ para niños o $g$ para gallinas). Esto es una estrategia cognitiva para no confundir qué valor pertenece a cada categoría al final.
> 3. **Traducción algebraica:** Convierte el texto en dos ecuaciones. Recuerda que cada condición del enunciado genera una ecuación distinta.
> 4. **Resolución por Eliminación:** Ajusta las ecuaciones para que, al sumarlas verticalmente, una variable se anule.
> 5. **Verificación doble:** Un resultado solo es correcto si satisface **ambas** condiciones originales del problema.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Incógnita** | Es el valor desconocido. La clave pedagógica es usar letras "sugerentes": $c$ para coches, $m$ para motos. Esto reduce la carga mental al interpretar la solución final. |
| **Diferencia** | Resultado de una resta. Para mantener resultados positivos y facilitar el despeje, siempre planteamos la operación como: $Mayor - Menor = Diferencia$. |
| **Método de Eliminación** | Técnica de sumar ecuaciones en columna para cancelar una variable. Si los coeficientes no coinciden, multiplicamos una ecuación por un factor (generalmente negativo) para crear opuestos. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Problema de números (Caso básico)
**Enunciado:** La suma de dos números es $226$ y su diferencia es $36$. ¿Cuáles son los números?

**Desarrollo paso a paso:**
1. **Definir variables:** Sea $x$ el número mayor e $y$ el número menor.
2. **Plantear el sistema:**
   - Ecuación 1 (Suma): $x + y = 226$
   - Ecuación 2 (Diferencia): $x - y = 36$
3. **Eliminación (Suma vertical):** Alineamos las variables para sumarlas directamente:
   $$\begin{aligned}
   x + y &= 226 \\
   + (x - y &= 36) \\
   \hline
   2x &= 262
   \end{aligned}$$
4. **Resolver:** 
   $x = \frac{262}{2} \Rightarrow x = 131$
   Sustituimos $x$ en la Ecuación 1: $131 + y = 226 \Rightarrow y = 226 - 131 \Rightarrow y = 95$.

✅ **Resultado:** Los números son $131$ y $95$.
```

```ad-example
title: Ejemplo B — Entradas al parque (Aplicación real $USD)
**Enunciado:** $6$ entradas de niños y $5$ de adultos cuestan $\$177$ USD. $3$ entradas de niños y $1$ de adulto cuestan $\$57$ USD. ¿Cuál es el precio de cada una?

**Desarrollo algebraico:**
1. **Variables:** $n$ = precio niño; $a$ = precio adulto.
2. **Ecuaciones:**
   - (1) $6n + 5a = 177$
   - (2) $3n + a = 57$
3. **Estrategia:** Multiplicamos la ecuación (2) por $-5$ para eliminar la variable $a$:
   $-5(3n + a = 57) \Rightarrow -15n - 5a = -285$
4. **Resolución (Suma vertical):**
   $$\begin{aligned}
   6n + 5a &= 177 \\
   + (-15n - 5a &= -285) \\
   \hline
   -9n &= -108
   \end{aligned}$$
   $n = \frac{-108}{-9} \Rightarrow n = 12$.
   Sustituimos $n = 12$ en (2): $3(12) + a = 57 \Rightarrow 36 + a = 57 \Rightarrow a = 21$.

✅ **Resultado:** La entrada de niño cuesta $\$12$ USD y la de adulto $\$21$ USD.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
**Problema:** Hallar dos números cuya suma es $97$ y la diferencia entre el doble del mayor ($2x$) y el menor ($y$) es $131$.
**Pista:** Define $x$ como el mayor y aprovecha que la variable $y$ ya tiene signos opuestos en el enunciado.
**Solución:** Los números son $76$ y $21$.
```

```ad-abstract
title: 🟡 Medio
**Problema:** En un parqueadero hay $65$ vehículos entre coches y motos. Si en total se cuentan $214$ ruedas, calcula cuántos vehículos hay de cada tipo.
**Pista:** Aplica la lógica de "patas de animales" a este caso: cada coche aporta $4$ ruedas y cada moto $2$. Usa $c$ y $m$ para no confundir los tipos de vehículo.
**Solución:** Hay $42$ coches y $23$ motos.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
**Problema:** Claudia paga $\$30.70$ USD por $3$ bolígrafos y $8$ cuadernos. Patricia paga $\$25.40$ USD por $1$ bolígrafo y $7$ cuadernos en la misma tienda. Halla el precio unitario de cada artículo.
**Pista:** Para eliminar los bolígrafos, busca que la segunda ecuación tenga el mismo coeficiente que la primera pero con signo negativo.
**Solución:** Bolígrafo $\$0.90$ USD, Cuaderno $\$3.50$ USD.
```

> [!tip] 💡 Consejo de estudio: El Checklist de Verificación
> No des por terminado un problema sin pasar por esta lista de control. Sustituye tus valores finales en las **dos** ecuaciones originales:
> - [ ] **Condición 1:** ¿Mis resultados sumados/operados dan el primer total del enunciado?
> - [ ] **Condición 2:** ¿Mis resultados cumplen también la segunda restricción?
> 
> *Si solo funciona en una, el planteamiento o un signo en la eliminación están fallando. ¡Vuelve a revisar!*