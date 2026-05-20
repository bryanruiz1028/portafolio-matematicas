# 📖 Guía de estudio — Clase 02: Despeje de Ecuaciones

> [!info] 📌 Conceptos clave
> 1. **Prioridad de movimiento**: Si la variable está acompañada por varios elementos, primero debemos trasladar los términos que suman o restan. Solo después nos ocupamos de los factores que multiplican o dividen.
> 2. **Regla del cambio de signo**: Al mover un término al otro lado de la igualdad, realiza su operación inversa: lo que suma pasa a restar y lo que resta pasa a sumar.
> 3. **Tratamiento de exponentes y la "Trampa de la Raíz"**: Para despejar una potencia cuadrada, usamos la raíz cuadrada. **¡Cuidado!** Según el Profe Alex, no puedes cancelar una raíz con exponentes si dentro hay una suma (ej: $\sqrt{b^2 + c^2}$ no es igual a $b + c$).
> 4. **Variable negativa**: Si al final tu variable queda negativa (ej: $-x = 5$), multiplica toda la ecuación por $-1$ para invertir los signos y obtener el valor positivo de la incógnita ($x = -5$).

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Despejar** | Proceso algebraico para dejar la variable totalmente sola en un lado del signo igual. |
| **Término** | Cada una de las partes de una expresión separadas por los signos de suma (+) o resta (-). |
| **Operación Inversa** | El método de trasladar valores al lado opuesto ejecutando la acción contraria (ej: de potencia a raíz). |

## Ejemplos Resueltos Adicionales

```ad-example
title: **Ejemplo A — Caso básico**
**Ecuación:** $2 - x = y$
**Objetivo:** Despejar $x$

1. **Identificar términos:** El lado izquierdo tiene el término $2$ (que es positivo, aunque no tenga signo visible) y el término $-x$.
2. **Mover el término independiente:** El $2$ está sumando, por lo que pasa al otro lado restando.
   - $-x = y - 2$
3. **Corregir el signo de la variable:** Como la $x$ no puede ser negativa, multiplicamos todo por $-1$ (cambiamos el signo de cada elemento de la ecuación).
   - $x = -y + 2$

✅ **Resultado:** $x = -y + 2$
```

```ad-example
title: **Ejemplo B — Aplicación real $USD**
**Contexto:** Un repartidor cobra una tarifa fija ($v_i$) más un costo por kilómetro ($a \cdot t$). La fórmula es $v = v_i + at$.
**Objetivo:** Despejar el "Costo por kilómetro" ($a$).

1. **Mover términos:** Primero aislamos el bloque donde está nuestra incógnita. La tarifa fija ($v_i$) está sumando, así que pasa restando.
   - $v - v_i = at$
2. **Despejar el factor:** La distancia ($t$) está multiplicando a nuestra incógnita ($a$). Al pasar al otro lado, debe dividir a **toda la expresión** resultante del paso anterior.
   - $\frac{v - v_i}{t} = a$

✅ **Resultado:** $a = \frac{v - v_i}{t}$
```

## Ejercicios de Repaso

```ad-abstract
title: 🟢 Fácil
Realiza los siguientes despejes directos:
1. Despejar $x$ en: $x - 2 = y$
2. Despejar $a$ en: $a^2 = 25$
3. Despejar $m$ en: $y = mx$
```

```ad-abstract
title: 🟡 Medio
Aplica dos pasos para resolver:
1. Despejar $x$ en: $2x + 8 = 20$
2. Despejar $v_i$ en: $v = v_i + at$
3. Despejar $b$ en la fórmula: $a^2 = b^2 + c^2$ (Recuerda dejar la raíz expresada).
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
**Problema:** Una empresa eléctrica instalará un cable desde la punta de un poste hasta un punto en el suelo. Usamos el Teorema de Pitágoras ($a^2 = b^2 + c^2$), donde:
- $a$ es la longitud del cable.
- $c$ es la altura del poste ($6$ metros).
- $b$ es la distancia en el suelo ($8$ metros).

**Tarea:**
1. Despeja la variable $a$ (longitud del cable) de la fórmula original.
2. Calcula el valor numérico de $a$ (recuerda resolver las potencias y la suma antes de sacar la raíz).
3. Si cada metro de cable cuesta **$15 USD**, ¿cuál es el costo total del cable necesario?
```

> [!tip] 💡 Consejo de estudio
> **¡No te saltes pasos!** Antes de empezar a mover variables, resuelve todas las operaciones pendientes entre números conocidos (como $3 \times 2$ o $4 + 5$). 
> 
> **Nota sobre la barra de división:** Si ves una expresión como $\frac{3y - 5}{4}$, la barra larga actúa como un paréntesis. Esto significa que el denominador ($4$) afecta a todo y debe moverse **antes** que el $-5$. Si la barra es corta, como en $\frac{3y}{4} - 5$, primero mueves el $-5$. ¡El orden lo cambia todo!