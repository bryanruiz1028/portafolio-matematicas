# 📖 Guía de estudio — Clase 03: Ecuaciones Exponenciales con Bases Iguales

> [!info] 📌 Conceptos clave
> 1. **Definición de ecuación exponencial**: Es aquella igualdad donde la incógnita o variable se encuentra ubicada específicamente en el exponente de una potencia.
> 2. **Propiedad fundamental**: La regla de oro nos dice que si logramos establecer que $a^m = a^n$, entonces obligatoriamente los exponentes deben ser iguales: $m = n$.
> 3. **Requisito indispensable**: ¡Atención aquí! No podemos igualar los exponentes si las bases no son exactamente iguales en ambos lados de la ecuación.
> 4. **Técnica de descomposición**: Para números grandes como **8**, **27**, **64** o **243**, utilizamos la descomposición en factores primos (trazando una línea vertical y sacando mitad, tercera, etc.) para convertirlos en potencias de una base común (**2**, **3**, **5**).

---

## 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación Exponencial** | Una igualdad matemática donde la incógnita aparece en el exponente. |
| **Propiedad de Bases Iguales** | Si $a^x = a^y \implies x = y$. Es el "puente" para eliminar las bases. |
| **Potencia de una Raíz** | $\sqrt[n]{a^m} = a^{\frac{m}{n}}$. El índice de la raíz se convierte en el denominador. |
| **Exponente Negativo** | $\frac{1}{a^n} = a^{-n}$. Se usa para mover bases del denominador al numerador. |

---

## 3. EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A — Caso con base 3
**Ejercicio:** Resolver $3^{2x-1} = 27$

1. **Descomposición y base común:** ¡Ojo aquí! Para que las bases coincidan, debemos expresar **27** como potencia de **3**. Si hacemos la descomposición vertical: **27 | 3**, **9 | 3**, **3 | 3**, **1**. Así, vemos que **27 = $3^3$**.
   $3^{2x-1} = 3^3$
2. **Igualar exponentes:** Como ya tenemos la misma base (**3**), aplicamos la propiedad y trabajamos solo con lo de arriba:
   $2x - 1 = 3$
3. **Despejar la incógnita:**
   $2x = 3 + 1$
   $2x = 4$
   $x = \frac{4}{2}$
   **$x = 2$**
4. **Verificación:** Sustituimos el **2** en la ecuación original: $3^{2(2)-1} = 3^{4-1} = 3^3$. Como **$3^3 = 27$**, ¡el resultado es correcto!

✅ **Resultado:** **$x = 2$**
```

```ad-example
title: Ejemplo B — Aplicación real $USD
**Problema:** Una inversión duplica su valor cada año siguiendo la fórmula $2^x = 64$. ¿En cuántos años el saldo pasará de **1 USD** a **64 USD**?

1. **Igualar bases:** Recuerda que nuestro objetivo es que el **64** tenga base **2**. Al descomponerlo (**2 · 2 · 2 · 2 · 2 · 2**), obtenemos que **64 = $2^6$**.
   $2^x = 2^6$
2. **Aplicar propiedad:** Al ser las bases idénticas, igualamos directamente:
   **$x = 6$**
3. **Verificación:** Si elevamos la base **2** a la potencia **6**, obtenemos **2 · 2 · 2 · 2 · 2 · 2 = 64**. Se cumple la igualdad.

✅ **Resultado:** **6 años**.
```

---

## 4. EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Nivel: Fácil
Resuelve identificando la base común y aplicando la propiedad directa:
1. $2^x = 32$
2. $5^x = 125$
3. $3^x = 81$
```

```ad-abstract
title: 🟡 Nivel: Medio
Resuelve aplicando operaciones algebraicas en el exponente después de igualar bases:
1. $2^{x+2} = 16$
2. $5^{3x-1} = 125$
3. $10^{2x} = 1000$
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Aplicación con $USD
**Situación:** Una criptomoneda triplica su valor siguiendo una tasa de crecimiento de raíz cuadrada mensual. Si hoy vale **1 USD**, ¿en cuántos meses valdrá **243 USD**?
1. Usa la ecuación: $3^{\frac{x}{2}} = 243$.
2. **Pista del Profe:** Primero convierte **243** a base **3** ($3^5$). Luego, iguala el exponente fraccionario $\frac{x}{2}$ con el exponente resultante. ¡No olvides que el **2** que divide pasará a multiplicar!
```

---

## 5. CONSEJO DE ESTUDIO

> [!tip] 💡 Consejo de estudio
> ¡Hola, estudiante! Para resolver estas ecuaciones con la velocidad de un experto, te recomiendo memorizar las potencias básicas de los números **2**, **3** y **5**. 
> - Si ves un **8**, piensa en **$2^3$**.
> - Si ves un **81**, piensa en **$3^4$**.
> - Si ves un **25**, piensa en **$5^2$**.
>
> Al reconocer estos números visualmente, evitarás perder tiempo haciendo la descomposición manual y podrás saltar directamente a igualar los exponentes. ¡La práctica hace al maestro!