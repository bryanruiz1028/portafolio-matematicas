# 📖 Guía de estudio — Clase 04: Propiedades de la potenciación combinadas

> [!info] **¿Cuándo sabemos que un ejercicio está terminado?**
> ¡Hola, futuro experto en álgebra! A veces, lo más difícil no es empezar, sino saber cuándo hemos llegado a la meta. Para que tu ejercicio esté perfecto, debe cumplir estas tres reglas de oro:
> 1. **No puede haber bases repetidas:** Si ves la misma letra o número varias veces, ¡únelos en una sola!
> 2. **No puede haber paréntesis:** Debes usar tus propiedades para "limpiar" el camino y eliminar signos de agrupación.
> 3. **No puede haber exponentes negativos:** Un resultado profesional siempre usa exponentes positivos. 
> 
> ¡Sigue estos pasos y verás cómo los ejercicios más complejos se vuelven sencillos!

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Producto de bases iguales** | Se mantiene la base y se suman los exponentes: $a^m \cdot a^n = a^{m+n}$. |
| **Potencia de una potencia** | Se multiplican los exponentes: $(a^m)^n = a^{m \cdot n}$. **¡Cuidado!** No es lo mismo $(x^3)^2 = x^6$ que $x^{3^2} = x^9$ (en el segundo caso, elevas el 3 al cuadrado). |
| **Potencia de un producto** | El exponente se distribuye. **Truco de experto:** Si la base ya tiene exponente, multiplícalos: $(a^m \cdot b^p)^n = a^{m \cdot n} \cdot b^{p \cdot n}$. |
| **Exponentes negativos** | Representan un "cambio de lado". Para positivizar, mueve la base del numerador al denominador (o viceversa): $x^{-n} = \frac{1}{x^n}$. |
| **Exponente cero** | Cualquier base (excepto el 0) elevada a cero es igual a 1 ($x^0 = 1$). Esto ocurre porque al dividir algo por sí mismo ($x^n / x^n$), todo se "cancela" y queda la unidad. |

---

## Ejemplos resueltos adicionales

````ad-example
**Ejemplo A: Limpieza de paréntesis paso a paso**
Simplifica la expresión: $(m^2)^3 \cdot (m^4)^2 \cdot m^3$

**¡Paso a paso llegarás a la meta!:**
1.  **Quitar paréntesis:** Aplicamos potencia de una potencia multiplicando los exponentes.
    *   $(m^2)^3 = m^{2 \cdot 3} = m^6$
    *   $(m^4)^2 = m^{4 \cdot 2} = m^8$
    *   Ahora nuestra expresión es: $m^6 \cdot m^8 \cdot m^3$
2.  **Unir bases iguales:** Como es una multiplicación, sumamos los exponentes.
    *   $m^{6 + 8 + 3} = m^{17}$

**Resultado final:** $m^{17}$ (¡Misión cumplida! Una sola base, sin paréntesis y exponente positivo).
````

````ad-example
**Ejemplo B: Multiplicadores de Crecimiento ($USD)**
Imagina que un factor de crecimiento financiero se duplica cada año ($2^t$). Si un proyecto tiene tres fases de crecimiento con distintos tiempos acumulados ($2^2, 2^3, 2^4$), queremos hallar el **factor de crecimiento total** resultante de multiplicar estas fases.

**Procedimiento:**
*   **Planteamiento:** Multiplicamos los factores: $2^2 \cdot 2^3 \cdot 2^4$
*   **Suma de exponentes:** Al ser la misma base (2), sumamos: $2^{2+3+4} = 2^9$
*   **Valor final:** $2^9 = 512$. 
*   **Contexto real:** Si la inversión inicial fuera de 1 USD, el valor final tras consolidar estos factores de crecimiento sería de **$512 USD**.
````

---

## Ejercicios de repaso

````ad-abstract
**🟢 Nivel: Fácil (Para calentar motores)**
1. $(x^3)^2$
2. $(a^5)^4$
3. $(y^2)^5$
````

````ad-abstract
**🟡 Nivel: Medio (¡Tú puedes con esto!)**
1. $x^2 \cdot (x^3)^4$
2. $m^5 \cdot (m^2)^3 \cdot m$
3. $(a^4)^2 \cdot (a^3)^2$
````

````ad-abstract
**🔴 Nivel: Avanzado (Aplicación financiera)**
Un fondo de inversión de $2^{10}$ dólares debe repartirse entre $2^3$ personas, pero antes se aplica un ajuste por gastos administrativos de $2^{-2}$ que multiplica al fondo inicial. 

**Simplifica la expresión:** $\frac{2^{10} \cdot 2^{-2}}{2^3}$

**Solución paso a paso:**
1.  **Positivizar:** El $2^{-2}$ que está arriba "está mal puesto". Lo bajamos al denominador como $2^2$.
    *   Queda: $\frac{2^{10}}{2^3 \cdot 2^2}$
2.  **Unir abajo:** Sumamos exponentes en el denominador: $2^{3+2} = 2^5$.
    *   Queda: $\frac{2^{10}}{2^5}$
3.  **Restar para dividir:** $2^{10-5} = 2^5$.
4.  **Resultado:** $2^5 = 32$. Cada persona recibe **$32 USD**.
````

---

> [!tip] **Consejo de estudio: El orden ideal para no confundirse**
> Para resolver ejercicios de forma organizada y evitar errores de signos, aplica esta estrategia que usan los expertos:
> 1. **Elimina signos de agrupación:** Primero quita paréntesis y corchetes multiplicando exponentes internos por externos.
> 2. **Positivizar:** Si ves exponentes negativos, ¡muévelos de lado! Lo que está arriba pasa abajo y lo que está abajo pasa arriba.
> 3. **Unir bases iguales:** Finalmente, simplifica sumando exponentes (si multiplican) o restando (si dividen). 
> 
> ¡Sigue este 1-2-3 y el álgebra será pan comido!