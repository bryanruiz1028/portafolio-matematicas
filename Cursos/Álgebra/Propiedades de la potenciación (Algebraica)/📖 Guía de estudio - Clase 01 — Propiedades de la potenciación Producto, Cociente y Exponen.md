# 📖 Guía de estudio — Clase 01: Producto y cociente de potencias con bases iguales

> [!info] 📌 Conceptos clave
> Para dominar las potencias no hace falta memoria, ¡hace falta lógica! Como dice el Profe Alex, si entiendes el "porqué", las fórmulas se cuidan solas.
> 
> 1.  **La Regla de los Gemelos (Bases Idénticas):** Estas propiedades solo funcionan si las bases son exactamente iguales. Si tienes $a^2 \cdot b^3$, ¡ojo! No puedes hacer nada, déjalas tranquilas porque no son "gemelas".
> 2.  **Producto (Suma de fuerzas):** Al multiplicar potencias de igual base, la base se mantiene y los exponentes se **suman**. ¿Por qué? Porque estamos agrupando cuántas veces se multiplica el mismo número en total.
> 3.  **Cociente (La Gran Simplificación):** Al dividir, la base se mantiene y los exponentes se **restan**. Pero no es cualquier resta: siempre es **"el de arriba menos el de abajo"**. 
> 4.  **El Exponente Invisible:** El único exponente que no escribimos es el **1**, pero ahí está siempre pendiente. Si ves una $x$ sola, trátala como $x^1$.
> 5.  **El Misterio del Exponente 0:** Todo número (excepto el 0) elevado a la 0 es igual a **1**. Esto no es magia; surge porque cualquier cosa dividida por sí misma da 1 (ejemplo: $\frac{5}{5}=1$), lo que en potencias es restar exponentes iguales ($n-n=0$).

## Fórmulas y definiciones importantes

| Término | Fórmula | ¿Por qué funciona? (La Lógica) |
| :--- | :--- | :--- |
| **Producto de bases iguales** | $a^m \cdot a^n = a^{m+n}$ | Porque estamos contando el total de veces que la base se multiplica por sí misma. |
| **Cociente de bases iguales** | $\frac{a^m}{a^n} = a^{m-n}$ | Porque las bases de arriba se "cancelan" (simplifican a 1) con las de abajo. |
| **Potencia de exponente cero** | $a^0 = 1$ (si $a \neq 0$) | Porque dividir algo entre sí mismo da 1. **Dato curioso:** $0^0$ no existe porque no se puede dividir entre cero. |

---

## Ejemplos resueltos para crackear el código

```ad-example
title: Ejemplo A — Operaciones Combinadas
**Simplificar:** $\frac{x^5 \cdot x^2}{x^3}$

1. **Paso 1 (Multiplicar arriba):** Sumamos los exponentes de $x^5$ y $x^2$. Tenemos $5 + 2 = 7$. Ahora la expresión es $\frac{x^7}{x^3}$.
2. **Paso 2 (Dividir):** Aplicamos la "Regla de Oro" (arriba menos abajo): $7 - 3 = 4$.

**Visualización lógica:** Imagina que arriba tienes la $x$ multiplicada 7 veces y abajo 3 veces. Tachas 3 de arriba con las 3 de abajo... ¡Te quedan 4 arriba!

✅ **Resultado:** $x^4$
```

```ad-example
title: Ejemplo B — Ahorros en Cripto-Dólares
**Escenario:** Tu cuenta duplica su valor cada mes (base 2). Si tienes $2^3$ USD y recibes un bono que multiplica tu saldo por $2^4$.

1. **Análisis:** Es un producto de bases iguales.
2. **Operación:** Sumamos los exponentes: $3 + 4 = 7$.

✅ **Resultado:** $2^7$ USD. (Si quieres saber cuánto es, multiplica el 2 siete veces: ¡128 dólares!).
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel: Fácil (Para calentar)
1. Resolver $m^8 \cdot m^4$.
2. Resolver $\frac{x^7}{x^3}$.
3. Hallar el resultado de $(5 \cdot 3)^0$. (Pista: ¡No hagas la multiplicación, usa la propiedad del cero!).
```

```ad-abstract
title: 🟡 Nivel: Medio (¡Cuidado con las trampas!)
1. Resolver $a^{10} \cdot a \cdot a^5$. (No olvides al "exponente invisible" en la $a$ solitaria).
2. Resolver $\frac{y^{12}}{y^{15}}$. Realiza la resta $12 - 15$. Si te da negativo, no te asustes, significa que "ganaron" las potencias de abajo.
3. Simplificar $x^3 \cdot x^{-2}$. Suma los exponentes respetando los signos: $3 + (-2)$.
```

```ad-abstract
title: 🔴 Nivel: Avanzado (Reto Profe Alex)
1. Un servidor procesa $10^9$ transacciones. Si la eficiencia cae y procesa $10^4$ veces menos, ¿cuántas procesa ahora? (Pista: "veces menos" indica división).
2. Reparte un presupuesto de $2^{10}$ USD entre $2^3$ departamentos. Expresa el resultado como potencia.
3. Simplifica $\frac{n^5 \cdot n^2}{n^7}$. ¿Ves por qué el resultado es 1? Explícalo usando la resta de exponentes.
```

---

> [!tip] 💡 El Consejo de Oro del Profe Alex
> En la división, grábate esto: **"El de arriba menos el de abajo"**. Siempre. Si el de abajo es negativo, recuerda que menos por menos da más (ejemplo: $2 - (-3) = 5$). 
>
> Y recuerda: si te dan $\frac{a^6}{b^3}$, **¡no se tocan!** Si las bases no son gemelas, la propiedad se va a dormir. ¡Asegúrate de que sean iguales antes de operar!