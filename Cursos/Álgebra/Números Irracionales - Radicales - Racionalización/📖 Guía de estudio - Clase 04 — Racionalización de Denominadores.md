# 📖 Guía de estudio — Clase 04: Racionalización de Denominadores

### 1. Bloque de Información: Conceptos Clave

> [!info] 📌 Conceptos clave
> - **¿Qué es la Racionalización?:** Es el proceso de transformar una fracción que tiene raíces en su denominador en una fracción equivalente donde el denominador sea un número racional (sin raíces).
> - **El poder de la Amplificación:** Para no alterar el valor de la fracción, multiplicamos el numerador y el denominador por la misma expresión. Matemáticamente, es como multiplicar por $1$.
> - **Monomios vs. Binomios:** Si el denominador es un **monomio**, buscamos completar el exponente para que coincida con el índice de la raíz. Si es un **binomio**, usamos el "conjugado" para crear una diferencia de cuadrados.
> - **El objetivo final:** No buscamos "desaparecer" las raíces del número, sino "mudarlas" al numerador para facilitar operaciones futuras.

---

### 2. Tabla de Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Racionalización de Monomio Cuadrado** | Se multiplica por la misma raíz cuadrada para que el radicando quede elevado al cuadrado: $\frac{1}{\sqrt{a}} \cdot \frac{\sqrt{a}}{\sqrt{a}} = \frac{\sqrt{a}}{\sqrt{a^2}} = \frac{\sqrt{a}}{a}$. |
| **Racionalización de Monomio de Índice $n$** | Se busca completar lo que le falta al exponente $m$ para llegar al índice $n$: $\sqrt[n]{a^m} \cdot \sqrt[n]{a^{n-m}} = \sqrt[n]{a^{m + (n - m)}} = \sqrt[n]{a^n} = a$. |
| **Binomio Conjugado** | Es la misma expresión del denominador pero con el signo central opuesto. Al multiplicarlos, aplicamos: $(a+b)(a-b) = a^2 - b^2$. El objetivo es elevar cada término al cuadrado para "cancelar" las raíces. |

---

### 3. Sección de Ejemplos Resueltos

```ad-example
**Ejemplo A — Caso Básico (Monomio de índice n)**
**Enunciado:** Racionalizar la expresión $\frac{2}{\sqrt[3]{5}}$

- **Paso 1 (Identificar el factor):** El denominador es $\sqrt[3]{5^1}$. Para que el exponente sea $3$, nos faltan $2$ unidades. Por tanto, nuestro factor es $\sqrt[3]{5^2}$.
- **Paso 2 (Multiplicación y simplificación):**
$$\frac{2}{\sqrt[3]{5}} \cdot \frac{\sqrt[3]{5^2}}{\sqrt[3]{5^2}} = \frac{2\sqrt[3]{25}}{\sqrt[3]{5^{1+2}}} = \frac{2\sqrt[3]{25}}{\sqrt[3]{5^3}}$$
$$\frac{2\sqrt[3]{25}}{5}$$

✅ **Resultado:** $\frac{2\sqrt[3]{25}}{5}$
```

```ad-example
**Ejemplo B — Aplicación con Contexto Económico ($USD)**
**Enunciado:** Tenemos un presupuesto de $\$5$ USD que debe dividirse entre un factor de ajuste irracional de $\sqrt{7} - \sqrt{2}$. ¿Cuál es el valor racionalizado?

- **Paso 1 (Multiplicación por el conjugado):** El conjugado de $\sqrt{7} - \sqrt{2}$ es $\sqrt{7} + \sqrt{2}$. Multiplicamos arriba y abajo:
$$\frac{5}{\sqrt{7} - \sqrt{2}} \cdot \frac{\sqrt{7} + \sqrt{2}}{\sqrt{7} + \sqrt{2}}$$
- **Paso 2 (Aplicar diferencia de cuadrados):** Dejamos el numerador indicado y resolvemos el denominador:
$$\frac{5(\sqrt{7} + \sqrt{2})}{(\sqrt{7})^2 - (\sqrt{2})^2} = \frac{5(\sqrt{7} + \sqrt{2})}{7 - 2}$$
- **Paso 3 (Simplificación de factores):**
$$\frac{5(\sqrt{7} + \sqrt{2})}{5}$$
**Nota pedagógica:** Aquí podemos simplificar los $5$ porque el del numerador es un factor (multiplica a todo) y el del denominador es el divisor. Al ser iguales, se cancelan.

✅ **Resultado:** $(\sqrt{7} + \sqrt{2})$ USD
```

---

### 4. Ejercicios de Repaso

```ad-abstract
**🟢 Nivel Fácil: Monomios con raíces cuadradas**
1. $\frac{5}{\sqrt{3}}$
2. $\frac{2}{\sqrt{2}}$ (¡Ojo! Aquí puedes simplificar el resultado final).
3. $\frac{10}{\sqrt{5}}$
```

```ad-abstract
**🟡 Nivel Medio: Índices superiores y simplificación**
1. $\frac{2}{\sqrt[4]{a}}$ (Considera que dentro de la raíz tienes $a^1$).
2. $\frac{3}{\sqrt[5]{3^2}}$
3. $\frac{2}{\sqrt[4]{8}}$ (Pista: Transforma el $8$ en potencia de $2$ antes de empezar).
```

```ad-abstract
**🔴 Nivel Avanzado: Aplicación con $USD**
Un fondo de reserva de $\$13$ USD debe distribuirse proporcionalmente según el índice $(4 + \sqrt{3})$. Racionaliza la expresión para hallar el costo unitario exacto:
- Ejercicio: $\frac{13}{4 + \sqrt{3}}$
*(Recuerda: Usa el binomio conjugado y verifica si el denominador final permite simplificar el $13$ del numerador).*
```

---

### 5. Bloque de Consejo de Estudio

> [!tip] 💡 Consejo de estudio
> ¡No te apresures a multiplicar! Un error clásico es intentar simplificar números que están "atrapados" dentro de una raíz con números que están afuera; **esto es matemáticamente imposible**. Mi consejo de oro: mantén las multiplicaciones del numerador "indicadas" (con paréntesis) hasta el final. Como vimos en el ejemplo de los $\$5$ USD, es muy probable que el número que obtengas en el denominador se pueda simplificar directamente con el factor de afuera, ahorrándote mucho trabajo sucio. ¡Siempre verifica si el denominador se volvió un número entero antes de dar el ejercicio por terminado!