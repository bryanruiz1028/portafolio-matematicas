# 📖 Guía de estudio — Clase 02: Potencias con exponente fraccionario y Radicales

> [!info] 📌 Conceptos clave
> Para dominar las potencias y raíces, debemos entender que son dos caras de la misma moneda. Basándonos en las enseñanzas del **Profe Alex**, aquí tienes los pilares fundamentales:
> 1. **La conexión vital**: Una potencia fraccionaria es una raíz disfrazada ($a^{m/n} = \sqrt[n]{a^m}$). ¡Recuerda! El **denominador** es el índice (el "jefe" de la raíz) y el **numerador** es el exponente.
> 2. **Índices y Signos (¡Mucho cuidado!)**: 
>    - Si el índice es **impar**, la vida es fácil: puedes cancelar la raíz y el exponente manteniendo el signo original ($\sqrt[n]{(-a)^n} = -a$).
>    - Si el índice es **par**, ¡alerta! El resultado siempre debe ser positivo porque buscamos la **raíz principal**. Por eso, usamos el **valor absoluto**: $\sqrt[n]{(-a)^n} = |a|$.
> 3. **Radicales Semejantes ("Perritos con perritos")**: Solo puedes sumar o restar raíces que sean idénticas (mismo índice y mismo radicando). Si tienes $3\sqrt{2}$ y $5\sqrt{2}$, tienes 8 "perritos" de clase $\sqrt{2}$. Si son diferentes, no se tocan... a menos que puedas simplificarlos.
> 4. **Simplificación**: La herramienta secreta es la **descomposición en factores primos**. Agrupamos los factores en **parejas** (si es raíz cuadrada) o **tríos** (si es raíz cúbica) para poder sacarlos de la raíz.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Potencia Fraccionaria** | $a^{m/n} = \sqrt[n]{a^m}$. También puedes usar la **"Forma Fácil"**: $(\sqrt[n]{a})^m$. Es mejor sacar la raíz primero para trabajar con números pequeños. |
| **Índice Impar (Base Negativa)** | Si $n$ es impar: $\sqrt[n]{(-a)^n} = -a$. Ejemplo: $\sqrt[3]{(-2)^3} = -2$. |
| **Índice Par (Base Negativa)** | Si $n$ es par: $\sqrt[n]{(-a)^n} = \|a\|$. Esto es vital con variables: $\sqrt{x^2} = \|x\|$, porque no sabemos si $x$ era positivo o negativo. |
| **Radicales Semejantes** | Sumamos "perritos con perritos": $k\sqrt[n]{a} \pm j\sqrt[n]{a} = (k \pm j)\sqrt[n]{a}$. |

---

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Conversión y Cálculo Básico
**Problema:** Calcular el valor de $8^{1/3}$.
1. **Transformar a raíz:** El denominador 3 es el índice: $\sqrt[3]{8^1}$.
2. **Descomposición:** $8 = 2 \cdot 2 \cdot 2$, es decir, $2^3$. La expresión es $\sqrt[3]{2^3}$.
3. **Simplificación:** Como el índice (3) y el exponente (3) son iguales, se cancelan.
✅ **Resultado:** 2.
```

```ad-example
title: Ejemplo B — Simplificación aplicada a Finanzas ($USD)
**Enunciado:** Un ahorro genera $\sqrt{12}$ USD y otro $\sqrt{27}$ USD. ¿Cuál es el total?
1. **¡Cuidado!** No parecen semejantes, así que descomponemos:
   - $12 = 2 \cdot 2 \cdot 3 = 2^2 \cdot 3$
   - $27 = 3 \cdot 3 \cdot 3 = 3^2 \cdot 3$
2. **Extraer factores:** 
   - $\sqrt{2^2 \cdot 3} = 2\sqrt{3}$
   - $\sqrt{3^2 \cdot 3} = 3\sqrt{3}$
3. **Sumar perritos:** Ahora ambos son términos con $\sqrt{3}$. 
   - $2\sqrt{3} + 3\sqrt{3} = 5\sqrt{3}$.
✅ **Resultado:** $5\sqrt{3}$ USD.
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. Convierte $25^{1/2}$ a raíz y resuélvelo. (Pista: Busca la raíz cuadrada principal).
2. Resuelve la suma: $3\sqrt{2} + 5\sqrt{2}$. Aplica el concepto de "perritos con perritos".
3. Calcula $\sqrt[3]{(-2)^3}$. ¿Se mantiene el signo o cambia?
```

```ad-abstract
title: 🟡 Medio
1. Simplifica $\sqrt{50}$ usando factores primos. Agrupa en parejas (índice 2).
2. Resuelve $\sqrt{12} + \sqrt{75}$. Simplifica ambos términos antes de intentar sumar.
3. Calcula el valor de $(-7)^{2/2}$. **¡Cuidado!** Aplica la regla del índice par y valor absoluto.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación y Técnica
1. **Geometría:** Un terreno cuadrado tiene un área de $\sqrt{5000} \text{ m}^2$. Simplifica esta expresión extrayendo la mayor cantidad de factores posibles (debe quedar $50\sqrt{2}$).
2. **Finanzas:** Si en tu cuenta tienes $10\sqrt{3}$ USD y pierdes $\sqrt{12}$ USD, ¿cuál es tu saldo exacto simplificado?
3. **Análisis de Tríos:** Simplifica $5\sqrt[3]{24}$. 
   - Paso 1: Descompón 24 ($2 \cdot 2 \cdot 2 \cdot 3 = 2^3 \cdot 3$).
   - Paso 2: Identifica el **trío** de doses ($2^3$) para sacarlo de la raíz.
   - Paso 3: Multiplica el factor que sale por el coeficiente externo (5).
```

---

> [!tip] 💡 El "Consejo del Profe Alex"
> Para no sufrir en los exámenes, hay dos trucos que no fallan:
> 1. **La "Forma Fácil"**: Si tienes algo como $9^{3/2}$, no eleves 9 al cubo primero ($9^3 = 729$) porque sacar esa raíz es muy difícil. ¡Hazlo al revés! Saca primero la raíz cuadrada de 9, que es 3, y luego elévalo al cubo ($3^3 = 27$). ¡Mucho más rápido!
> 2. **Descompón siempre**: No intentes adivinar si dos raíces se pueden sumar. Si el número de adentro no es primo, pásalo a factores primos. Agrupa en **parejas** para raíces cuadradas e índices 2, y en **tríos** para raíces cúbicas. ¡Es la única forma de estar seguro!