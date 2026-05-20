# 📖 Guía de estudio — Clase 05: División de Polinomios

> [!info] 📌 Conceptos clave
> Para realizar una división de polinomios de forma exitosa, es fundamental seguir estas reglas de oro:
> *   **Ordenación obligatoria:** Antes de operar, se deben ordenar los términos tanto del dividendo como del divisor de mayor a menor exponente (orden descendente).
> *   **Respetar espacios vacíos:** Si en el polinomio dividendo falta algún grado intermedio (por ejemplo, si pasamos de $x^3$ a $x^1$), se debe dejar un espacio en blanco o completar con cero para mantener la alineación de las columnas.
> *   **Cambio de signo (El inverso aditivo):** Al trasladar los productos resultantes debajo del dividendo, es obligatorio **cambiarles el signo**. Pedagógicamente, esto se hace para realizar la resta de polinomios mediante el uso del inverso aditivo.
> *   **Proceso cíclico:** El algoritmo es repetitivo: buscar la expresión necesaria para igualar términos, multiplicar, cambiar signos, restar y bajar el siguiente término.

---

### FÓRMULAS Y DEFINICIONES IMPORTANTES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Dividendo** | Es el polinomio que se va a dividir (se ubica en el numerador de una fracción o dentro de la galera de división). |
| **Divisor** | Es el polinomio que divide al dividendo (se ubica en el denominador o fuera de la galera). |
| **Grado del exponente** | El valor numérico que indica la potencia a la que está elevada la variable; determina el orden del término en el polinomio y el número de raíces posibles. |
| **Residuo** | Es la expresión sobrante que queda al final de la operación cuando el grado del resto es menor al grado del divisor. |

---

### EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A — División de trinomio por binomio
**Ejercicio:** $(3x^2 + 2x - 8) \div (x + 2)$

**Pasos detallados:**
1. **Ordenar:** La expresión ya se encuentra en orden descendente.
2. **Buscar término:** ¿Por cuánto multiplico a $x$ para obtener $3x^2$? El resultado es $3x$.
3. **Multiplicar y cambiar signos:** 
   * $3x \cdot x = 3x^2 \to$ se anota como $-3x^2$.
   * $3x \cdot 2 = 6x \to$ se anota como $-6x$.
4. **Reducir y bajar:** 
   * $3x^2 - 3x^2 = 0$.
   * $2x - 6x = -4x$.
   * Bajamos el siguiente término: $-8$.
5. **Repetir el ciclo:** Buscamos un término para que $x$ iguale a $-4x$. Multiplicamos por $-4$.
   * $-4 \cdot x = -4x \to$ se anota como $+4x$.
   * $-4 \cdot 2 = -8 \to$ se anota como $+8$.
   * Al operar, el residuo es $0$.

**Resultado final:** $3x - 4$
```

```ad-example
title: Ejemplo B — Aplicación de costos $USD
**Problema:** Una empresa tiene un presupuesto total representado por el polinomio $2x^2 - 15x + 25$ dólares. Si se desea dividir este presupuesto entre $x - 5$ unidades de producción, ¿cuál es el costo unitario?

**Resolución:**
1. **Buscar término:** Dividimos el primer término del dividendo por el primero del divisor: $2x^2 \div x = 2x$.
2. **Multiplicar y cambiar signos:** 
   * $2x \cdot x = 2x^2 \to$ se anota como $-2x^2$.
   * $2x \cdot -5 = -10x \to$ se anota como $+10x$.
3. **Reducir y bajar:** 
   * $-15x + 10x = -5x$. 
   * Bajamos el término constante: $+25$.
4. **Repetir el ciclo:** Dividimos $-5x$ entre $x$, lo que nos da $-5$.
5. **Multiplicar y cambiar signos:** 
   * $-5 \cdot x = -5x \to$ se anota como $+5x$.
   * $-5 \cdot -5 = +25 \to$ se anota como $-25$.
6. **Finalización:** El residuo es $0$.

**Resultado final:** El costo por unidad es de $2x - 5$ dólares.
```

---

### EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Fácil
**Enunciado:** Resuelve la siguiente división básica para afianzar el algoritmo:
$(x^2 + 5x + 6) \div (x + 2)$
*Sugerencia: Encuentra el término que, multiplicado por $x$, iguale exactamente a $x^2$.*
```

```ad-abstract
title: 🟡 Medio
color: 255, 200, 0
**Enunciado:** Realiza la división de los siguientes polinomios:
$(-a^5 - 3a^2 - a + 1) \div (a^2 + 2a + 1)$
**Nota técnica:** Al organizar el dividendo, es estrictamente necesario dejar los espacios físicos para los términos de grado $a^4$ y $a^3$, ya que aparecerán productos en esas posiciones durante la operación.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
color: 255, 0, 0
**Enunciado:** En un modelo de proyección financiera, los coeficientes de la siguiente operación representan flujos de caja en USD, mientras que los exponentes literales actúan como "factores de escala temporal". Resuelve:
$(a^{2x} + 2a^{2x-1} - 4a^{2x-2} + 5a^{2x-3} - 2a^{2x-4}) \div (a^x + a^{x-1} + a^{x-2})$
**Recordatorio pedagógico:** Al multiplicar potencias de igual base, se deben sumar los exponentes literales. Por ejemplo: $a^x \cdot a^x = a^{x+x} = a^{2x}$. Mantén un control riguroso de la ley de signos y los términos semejantes.
```

---

> [!tip] 💡 Consejo de estudio
> Para evitar confusiones en los procesos largos, sigue la recomendación del "Profe Alex": utiliza un **color distinto (como el rojo)** exclusivamente para marcar el cambio de signo cuando traslades los productos para restar. Este apoyo visual reduce drásticamente los errores comunes de signos y facilita la eliminación correcta de los términos.