# 📖 Guía de estudio — Clase 02: Progresiones Aritméticas

> [!info] 📌 Conceptos clave
> - **Progresión Aritmética:** Es una sucesión de números donde cada término se obtiene sumando o restando una cantidad constante (llamada diferencia) al término anterior.
> - **Diferencia ($d$):** Es el valor constante que determina cuánto aumenta o disminuye la secuencia. Se calcula restando un término menos el anterior ($a_n - a_{n-1}$).
> - **Término General ($a_n$):** Es la "fórmula maestra" que nos permite encontrar cualquier número en la secuencia si conocemos su posición ($n$).
> - **Posición ($n$):** Representa el lugar que ocupa un número en la lista (siempre es un número entero positivo: 1, 2, 3...).

## Fórmulas y Definiciones Importantes

| Término / Variable | Definición / Fórmula Matemática |
| :--- | :--- |
| **Diferencia ($d$)** | El valor constante de cambio: $d = a_{n} - a_{n-1}$. |
| **Término General ($a_n$)** | **Método 1 (Corrección):** $a_n = d \cdot n \pm \text{corrección}$. *(Ideal para cálculos rápidos)*.<br>**Método 2 (Fórmula):** $a_n = a_1 + (n-1)d$. *(Método algebraico formal)*. |
| **Posición ($n$)** | El número de orden del término ($n = 1, 2, 3, \dots$). |
| **Primer Término ($a_1$)** | El valor que inicia la progresión. |
| **Suma de términos ($S_n$)** | $S_n = \frac{(a_1 + a_n) \cdot n}{2}$. Se necesita el primer y el último término del rango a sumar. |

---

## Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — Caso básico (Encontrar el término general)
**Enunciado:** Hallar el término general de una progresión donde el primer término ($a_1$) es 5 y la diferencia ($d$) es 2.

**Paso 1:** Escribir la diferencia multiplicada por la posición:
$2n$

**Paso 2:** Realizar la "corrección" probando con la posición 1 ($n=1$):
$2 \cdot (1) = 2$
Para que el resultado sea igual a nuestro primer término (5), debemos sumarle 3:
$2 + 3 = 5$

**Paso 3:** Construir la fórmula final uniendo ambos pasos:
$a_n = 2n + 3$

✅ **Resultado:** $a_n = 2n + 3$
```

```ad-example
title: Ejemplo B — Caso con aplicación real $USD (Ahorro)
**Enunciado:** Un estudiante ahorra $10 la primera semana ($a_1$) e incrementa el monto en $3 cada semana siguiente ($d=3$). ¿Cuánto ahorrará específicamente en la semana 20 ($a_{20}$)?

**Paso 1:** Identificar los datos del problema:
$a_1 = 10$, $d = 3$, $n = 20$.

**Paso 2:** Sustituir todos los valores en la fórmula del término general:
$a_{20} = 10 + (20 - 1) \cdot 3$

**Paso 3:** Resolver las operaciones respetando la jerarquía:
$a_{20} = 10 + (19) \cdot 3$
$a_{20} = 10 + 57$
$a_{20} = 67$

✅ **Resultado:** En la semana 20 ahorrará $67.
```

---

## Ejercicios de Repaso

```ad-abstract
title: 🟢 Fácil
1. Identifica la diferencia ($d$) y los siguientes dos términos en: $3, 7, 11, 15...$
2. Identifica la diferencia ($d$) y los siguientes dos términos en: $12, 14, 16, 18...$
3. Identifica la diferencia ($d$) y los siguientes dos términos en: $10, 5, 0, -5...$
```

```ad-abstract
title: 🟡 Medio
1. Encuentra el término general ($a_n$) si se sabe que $a_5 = 23$ y $d = 4$.
2. Encuentra el término general ($a_n$) si se sabe que $a_7 = 12$ y $d = -2$.
3. Encuentra el término general ($a_n$) si se sabe que $a_{10} = 40$ y $d = 3$.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. Una persona comienza un plan de ahorro donde la primera semana deposita $5 y cada semana aumenta $4 respecto a la anterior. Calcula la **suma total** ahorrada al cabo de 10 semanas ($S_{10}$).  
*(Pista: Primero debes encontrar el valor del término $a_{10}$ usando la fórmula del término general).*

2. Si una cuenta bancaria tiene un saldo inicial de $100 y cada semana se retiran $5 de forma constante, ¿cuál será el saldo al llegar a la semana 10?

3. Calcula el término general y el valor del término 30 ($a_{30}$) para una sucesión de dinero que inicia en $1 y aumenta $3 cada periodo.
```

---

> [!tip] 💡 Consejo de estudio
> Para dominar este tema, es vital practicar la **suma y resta de números enteros**, ya que de esto depende que el "número de corrección" sea correcto. 
> 
> **Tip extra:** Recuerda que si el coeficiente de $n$ es 1, generalmente no se escribe. Por ejemplo, $1n + 8$ se debe expresar simplemente como $n + 8$. ¡Mantén tu notación limpia y profesional!