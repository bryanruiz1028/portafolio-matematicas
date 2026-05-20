# 📖 Guía de estudio — Clase 06: Factorización de un Trinomio Cuadrado Perfecto por Adición o Sustracción

> [!info] 📌 Conceptos clave
> La factorización por adición o sustracción es un método de "reparación" algebraica. Se utiliza cuando un trinomio tiene el potencial de ser un Trinomio Cuadrado Perfecto (TCP) porque sus extremos tienen raíces cuadradas exactas, pero su término central no cumple con la regla del "doble producto".
> 
> *   **Verificación inicial:** Primero, extraemos las raíces de los extremos y calculamos cuál debería ser el término central ideal (multiplicando las raíces por 2). Si el término central del ejercicio es diferente, debemos ajustarlo.
> *   **Objetivo de la adición/sustracción:** Sumamos o restamos una cantidad al término central original para transformarlo en el valor ideal que complete el TCP.
> *   **Compensación:** Para no alterar la expresión, si sumamos una cantidad, debemos restar esa misma cantidad al final. Es como sumar un "cero" inteligente.
> *   **Paso final:** El trinomio se convierte en una **Diferencia de Cuadrados**. Este es el paso crucial: el término que restamos para compensar debe ser un cuadrado perfecto para poder terminar la factorización satisfactoriamente.

---

## 2. Sección: Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Raíz cuadrada de una potencia** | Se divide el exponente entre 2 ($x^n \rightarrow x^{n/2}$). *Ejemplo: $\sqrt{x^4} = x^2$*. |
| **Trinomio Cuadrado Perfecto (TCP)** | Estructura donde el centro es el doble producto de las raíces: $a^2 \pm 2ab + b^2 = (a \pm b)^2$. |
| **Diferencia de Cuadrados** | Dos términos restándose, ambos con raíz cuadrada: $a^2 - b^2 = (a + b)(a - b)$. |
| **Términos semejantes** | Tienen misma letra y exponente. *Semejantes: $3x^2$ y $5x^2$. No semejantes: $5x^2$ y $5x^3$*. |

---

## 3. Sección: Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A (Caso Básico) — Factorizar $4a^4 + 8a^2b^2 + 9b^4$

**Paso 1: Extraer raíces de los extremos.**
- $\sqrt{4a^4} = 2a^2$
- $\sqrt{9b^4} = 3b^2$

**Paso 2: Calcular el término central ideal.**
Multiplicamos las raíces por 2: $2 \times (2a^2) \times (3b^2) = 12a^2b^2$.
Como el ejercicio original solo tiene $8a^2b^2$, nos faltan $4a^2b^2$ para llegar a 12.

**Paso 3: Sumar y restar la diferencia.**
$(4a^4 + 8a^2b^2 + 9b^4) + 4a^2b^2 - 4a^2b^2$
Operando el centro: $(4a^4 + 12a^2b^2 + 9b^4) - 4a^2b^2$

**Paso 4: Factorización en dos etapas.**
1. **Factorizar el TCP:** $(2a^2 + 3b^2)^2 - 4a^2b^2$
2. **Factorizar la Diferencia de Cuadrados:** 
   Raíces: $(2a^2 + 3b^2)$ y $2ab$.
   Resultado: $(2a^2 + 3b^2 + 2ab)(2a^2 + 3b^2 - 2ab)$

**Resultado final ordenado (descendente respecto a 'a'):**
$(2a^2 + 2ab + 3b^2)(2a^2 - 2ab + 3b^2)$
```

```ad-example
title: Ejemplo B (Aplicación Práctica) — Análisis de Costos en USD

**Contexto:** Un modelo de costos de producción está representado por $c^4 - 45c^2 + 100$. Factorizar esta expresión permite encontrar los "puntos de equilibrio" donde el costo se simplifica, facilitando el análisis de márgenes de ganancia.

**Paso 1: Raíces y término ideal.**
- $\sqrt{c^4} = c^2$; $\sqrt{100} = 10$.
- Centro ideal: $2 \times (c^2) \times (10) = 20c^2$. 

**Paso 2: Decisión didáctica.**
Tenemos $-45c^2$ y queremos llegar a $-20c^2$ (que es el centro del TCP). Para esto, sumamos $25c^2$. Elegimos este camino porque $25$ es un **cuadrado perfecto**, lo que permitirá completar el proceso.

**Paso 3: Compensación.**
$(c^4 - 45c^2 + 100) + 25c^2 - 25c^2$
$(c^4 - 20c^2 + 100) - 25c^2$

**Paso 4: Factorización final.**
1. **TCP:** $(c^2 - 10)^2 - 25c^2$
2. **Diferencia de cuadrados:** $(c^2 - 10 + 5c)(c^2 - 10 - 5c)$

**Resultado ordenado:**
$(c^2 + 5c - 10)(c^2 - 5c - 10)$
```

---

## 4. Sección: Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel Fácil
Factoriza el siguiente trinomio completando el término central:
$a^4 + 2a^2 + 9$
*(Pista: El término central ideal es $6a^2$. Debes sumar y restar $4a^2$)*.
```

```ad-abstract
title: 🟡 Nivel Medio
Factoriza la siguiente expresión organizada de forma **ascendente** (tal como aparece en la práctica del video):
$4 - 108x^2 + 121x^4$
*(Pista: Las raíces son 2 y $11x^2$. Busca llegar a un centro de $44x^2$ sumando $64x^2$)*.
```

```ad-abstract
title: 🔴 Nivel Avanzado — Aplicación Contable ($USD)
Un sistema contable genera la expresión de balance: $121x^4 - 125x^2y^2 + 4y^4$.
1. **Verificación:** Confirma que no existe un factor común para los tres términos.
2. **Proceso:** Calcula el término central ideal y determina qué cantidad debes sumar y restar (recuerda que el sustraendo debe tener raíz exacta).
3. **Orden:** Entrega el resultado final ordenado de forma descendente respecto a la variable $x$.
```

---

## 5. Sección: Consejo de Estudio

> [!tip] 💡 Consejo de estudio
> Antes de escribir todo el procedimiento, realiza una "prueba rápida" con lápiz: resta el término que tienes del término que necesitas. **¡La clave está en el resultado de esa resta!** Si el número que vas a restar para compensar no tiene raíz cuadrada exacta (como 4, 9, 16, 25, 36, 49, 64, 81, 100...), entonces el método de adición y sustracción no funcionará o habrás cometido un error en el cálculo del doble producto. ¡Verifica esto primero y ahorrarás mucho tiempo!