# 📖 Guía de estudio — Clase 07: Factorización del Cubo Perfecto de un Binomio

> [!info] **Conceptos clave**
> ¡Hola! Hoy vamos a dominar el proceso inverso de los productos notables. La factorización del **Cubo Perfecto de un Binomio** es sencilla si aprendes a observar los detalles. Para identificar este caso, la expresión debe cumplir con estas reglas de oro:
> * **Número de términos:** El polinomio debe tener exactamente cuatro términos.
> * **Ordenamiento y Patrón de Letras:** ¡Observa con atención! Antes de empezar, asegúrate de que la expresión esté ordenada. Un truco de experto es mirar las letras: mientras el exponente de una variable disminuye (3, 2, 1, 0), la otra aumenta.
> * **Extremos:** El primer y el cuarto término deben ser cubos perfectos.
> * **Regla de los Exponentes:** Para las letras, simplemente dividimos el exponente entre 3 para hallar su raíz.
> * **Regla de los signos:**
>     * Si todos son **positivos**, el binomio es una **suma** $(+)$.
>     * Si los signos están **intercalados** $(+ , -, + , -)$, el binomio es una **resta** $(-)$.

## Fórmulas y definiciones importantes

Para que un polinomio sea un cubo perfecto, debe superar estas pruebas de verificación. ¡No te confíes y compruébalo siempre!

| Término | Definición / Fórmula |
| :--- | :--- |
| **Primer y cuarto término** | Deben tener raíces cúbicas exactas ($r_1$ y $r_2$). Para las letras: $\text{Exponente} \div 3$. |
| **Segundo término** | Debe ser el triple del cuadrado de la primera raíz por la segunda: $3 \cdot (r_1)^2 \cdot r_2$. |
| **Tercer término** | Debe ser el triple de la primera raíz por el cuadrado de la segunda: $3 \cdot r_1 \cdot (r_2)^2$. |
| **Signo de la respuesta** | Si son todos $(+)$, el resultado es $(r_1 + r_2)^3$. Si son intercalados, es $(r_1 - r_2)^3$. |

---

## Ejemplos resueltos adicionales

```ad-example
**Ejemplo A — Caso Básico ($m^3 + 3m^2n + 3mn^2 + n^3$)**

**Paso 1: Hallar raíces cúbicas de los extremos.**
* Raíz de $m^3$: Dividimos exponente $3 \div 3 = 1 \rightarrow m^1$ (Primera raíz: $m$).
* Raíz de $n^3$: Dividimos exponente $3 \div 3 = 1 \rightarrow n^1$ (Segunda raíz: $n$).

**Paso 2: Verificación aritmética.** (Usamos el triple producto)
* $3 \cdot (m)^2 \cdot (n) = 3m^2n$. (¡Coincide con el segundo término!)
* $3 \cdot (m) \cdot (n)^2 = 3mn^2$. (¡Coincide con el tercer término!)

**Paso 3: Resultado final.**
Como todos los signos son positivos, escribimos el binomio al cubo:
**Resultado:** $(m + n)^3$
```

```ad-example
**Ejemplo B — Aplicación en contexto financiero ($USD)**

**Planteamiento:** Si el valor de una inversión en dólares se comporta según la expresión: $27 - 27x + 9x^2 - x^3$, ¿cuál es su forma factorizada?

**Desarrollo:**
1. **Ordenamiento:** La expresión ya está organizada (los exponentes de $x$ suben: $0, 1, 2, 3$).
2. **Extracción de raíces (Cálculo mental):**
   * $\sqrt[3]{27} = 3$ (porque $3 \cdot 3 \cdot 3 = 27$).
   * $\sqrt[3]{x^3} = x$ (porque $3 \div 3 = 1$).
3. **Verificación de términos medios:**
   * $3 \cdot (3)^2 \cdot (x) = 3 \cdot 9 \cdot x = 27x$. (Correcto)
   * $3 \cdot (3) \cdot (x)^2 = 9x^2$. (Correcto)
4. **Signos:** Observamos que están intercalados ($+ , -, +, -$). ¡Cuidado! Esto nos indica una resta.

**Resultado:** El binomio factorizado que representa la inversión es:
**Resultado:** $(3 - x)^3$
```

---

## Ejercicios de repaso

```ad-abstract
**Práctica de clase**

🟢 **Nivel Fácil (Variables simples y signos positivos):**
1. Factorizar: $a^3 + 3a^2b + 3ab^2 + b^3$
2. Factorizar: $x^3 + 6x^2 + 12x + 8$

🟡 **Nivel Medio (Signos intercalados y coeficientes mayores):**
3. Factorizar: $125 - 75x + 15x^2 - x^3$
4. Factorizar: $27a^3 - 108a^2b + 144ab^2 - 64b^3$

🔴 **Nivel Avanzado — Aplicación con $USD:**
5. El volumen proyectado de una bodega de almacenamiento de activos financieros en dólares está representado por la expresión: $64x^3 + 240x^2y^4 + 300xy^8 + 125y^{12}$. Encuentra el binomio al cubo que representa este volumen.
*(Recuerda: Para las letras, divide el exponente entre 3. El resultado esperado es $(4x + 5y^4)^3$).*
```

---

> [!tip] **Consejo de estudio**
> Para ser el más rápido de la clase, te recomiendo memorizar los cubos de los números del 1 al 7. Si reconoces estos números en los extremos, ¡ya tienes medio ejercicio resuelto!
> * $1^3 = 1$
> * $2^3 = 8$
> * $3^3 = 27$
> * $4^3 = 64$
> * $5^3 = 125$
> * $6^3 = 216$
> * $7^3 = 343$