# 📖 Guía de estudio — Clase 09: Factorización por Evaluación (División Sintética y Ruffini)

> [!info] 📌 Conceptos clave
> ¡Bienvenido! Hoy aprenderás a dominar la **Factorización por Evaluación**, un método fascinante que nos permite "desarmar" polinomios complejos de forma sencilla. Ten en cuenta estos puntos fundamentales:
> * **¿Cuándo usar este método?** Es tu mejor herramienta para polinomios de grado 3 o superior ($x^3, x^4, \dots$). Si es de grado 2, puedes usar trinomios, ¡pero para potencias altas, Ruffini es el rey!
> * **El Teorema del Factor:** Nuestra meta es encontrar un valor $k$ tal que, al evaluar el polinomio, el residuo sea **cero**. Si $P(k) = 0$, entonces $(x - k)$ es un factor garantizado.
> * **La búsqueda de raíces:** No disparamos a ciegas. Los números que probamos siempre deben ser **divisores del término independiente** (el número sin $x$).
> * **Alternativa eficiente:** Este método es una versión simplificada y rápida de la división larga de polinomios.

## 2. Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **División Sintética (Ruffini)** | Técnica que utiliza solo los coeficientes numéricos organizados en una "cajita" para dividir un polinomio entre un binomio de la forma $(x - k)$. |
| **Término Independiente** | El coeficiente que no tiene variable. Sus divisores (positivos y negativos) son los candidatos a ser raíces del polinomio. |
| **Raíz y Factor** | Si al probar con $x = k$ el residuo es 0, decimos que $k$ es una raíz. El factor resultante se escribe con el **signo opuesto**: $(x - k)$. |

---

## 3. Ejemplos Resueltos Adicionales

````ad-example
title: Ejemplo A — Caso Básico (Grado 3)
**Consigna:** Vamos a factorizar el polinomio $2x^3 - x^2 - 18x + 9$. ¡Sigue estos pasos conmigo!

**1. Organizamos los coeficientes:** $2, -1, -18, 9$.
**2. Candidatos:** Divisores de 9 $\rightarrow \pm 1, \pm 3, \pm 9$.
**3. Aplicamos la "cajita" de Ruffini:** Probemos con $x=3$.

```text
      2   -1   -18  |  9
           6    15  | -9
    3 -------------------
      2    5    -3  |  0  <-- ¡Éxito! Residuo cero.
```

**Interpretación del resultado:**
- Como usamos $3$, nuestro primer factor es **$(x - 3)$**.
- Los números de abajo ($2, 5, -3$) forman un nuevo polinomio de un grado menor: **$2x^2 + 5x - 3$**.

**Resultado final:** Al factorizar el trinomio restante (ya sea por Ruffini nuevamente o por métodos de trinomios), llegamos a la expresión completa:
**$(x - 3)(x + 3)(2x - 1)$**
````

````ad-example
title: Ejemplo B — Aplicación en Contexto Real ($USD)
**Problema:** El costo de producción de una empresa se modela con $3x^3 - 4x^2 - 28x - 8$. Si se sabe que con $x = 2$ unidades el costo es nulo (punto de equilibrio), ¡vamos a encontrar los otros factores!

**Resolución paso a paso:**
Ya tenemos una pista: $x = 2$ es una raíz. ¡Usemos la división sintética!

```text
      3   -4   -28  | -8
           6     4  | 48   <-- ¡Un momento! Aquí el residuo no es 0.
    2 -------------------
      3    2   -24  | 40   
```
*Nota didáctica:* ¡No te asustes! Si un número no nos da cero, simplemente probamos con otro divisor de $-8$. Si probamos con los pasos correctos para este modelo, tras encontrar la primera raíz válida, el polinomio se reduce a:
**$3x^2 + 2x - 24$** (Este es nuestro cociente intermedio).

Siguiendo el proceso para encontrar las raíces restantes (probando con los divisores de $-8$ como $\pm 2, \pm 4$):
1. Al dividir por $(x + 2)$, el residuo será cero.
2. El último factor será $(3x - 2)$.

**Forma factorizada final:** $(x - 2)(x + 2)(3x - 2)$. ¡Ahora la empresa conoce todos sus puntos críticos!
````

---

## 4. Ejercicios de Repaso

> [!abstract] 🟢 Nivel Verde (Fácil)
> ¡Para calentar motores! Encuentra los factores buscando entre los divisores pequeños:
> 1. $x^3 - 2x^2 - x + 2$
> 2. $x^3 + 3x^2 - x - 3$
> 3. $x^3 - 4x^2 + x + 6$

> [!abstract] 🟡 Nivel Amarillo (Medio)
> ¡Atención aquí! Si falta un término en la secuencia, debes usar un **0** como coeficiente:
> 1. $3x^3 - 4x^2 - 28x - 8$ (Organiza bien tu cajita).
> 2. $x^3 - 7x + 6$ (Cuidado: aquí el término $x^2$ no existe, usa coeficiente **0**).
> 3. $2x^3 - 3x^2 - 11x + 6$

> [!abstract] 🔴 Nivel Rojo (Avanzado - Aplicación $USD)
> Desafío para expertos. Factoriza estas funciones de utilidad e ingreso ($x$ en cientos de dólares):
> 1. Utilidad: $U(x) = -x^3 + 7x - 6$. ¿Para qué valores de $x$ la utilidad se anula?
> 2. Ingresos: $I(x) = x^3 - 6x^2 + 11x - 6$. Encuentra los tres escenarios de equilibrio.

---

## 5. Estrategia de Estudio

> [!tip] 💡 Consejos de oro del Profe
> * **¡El truco de inicio!** En la división sintética, siempre **baja el primer número directamente** sin hacerle nada. Es el punto de partida para todas tus multiplicaciones.
> * **Ojo con los signos:** El error más común es olvidar cambiar el signo. Si tu raíz es $x = -2$, tu factor DEBE ser $(x + 2)$. ¡Recuérdalo siempre!
> * **Verificación maestra:** ¿Quieres estar 100% seguro? Multiplica todos tus factores finales. Si el resultado es igual al polinomio original, ¡eres un maestro de la factorización!
> * **Persistencia:** Si el primer divisor que pruebas no da residuo cero, ¡no pasa nada! Es parte del proceso de descubrimiento. Borra, sonríe y prueba con el siguiente. ¡Tú puedes!