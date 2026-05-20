# 📖 Guía de estudio — Clase 04: Logaritmos y Ecuaciones Logarítmicas

> [!info] 📌 Conceptos clave
> - **El logaritmo como búsqueda de un exponente:** Resolver un logaritmo es encontrar a qué exponente hay que elevar la base para obtener el argumento. Por ejemplo: $\log_{2}(8) = 3$ porque $2^{3} = 8$.
> - **Convención de Base 10:** Cuando veas un logaritmo sin base escrita (ej. $\log(100)$), se sobreentiende que la base es $10$. Es el estándar en calculadoras científicas (tecla `log`).
> - **Logaritmos Naturales ($\ln$):** Son logaritmos cuya base es el número irracional $e$ ($\approx 2,718$). Son la operación inversa de la función exponencial $e^{x}$; por ello, $\ln(e^{x}) = x$.
> - **Restricción de negativos:** No existen logaritmos de números negativos. **Pro-tip de Profe Alex:** Al probar esto en la calculadora, usa la tecla de signo negativo `(-)` o `±` y no la tecla de resta `-` para evitar errores de sintaxis antes del "Math Error".

---

## 2. Tabla de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Logaritmo común ($\log_{10}$)** | Logaritmo en base $10$. En calculadoras se representa simplemente como la tecla `log`. |
| **Cambio de base** | Técnica para calcular cualquier logaritmo: $\frac{\log(\text{argumento})}{\log(\text{base})}$. |
| **Logaritmo Natural ($\ln$)** | Logaritmo en base $e$. Es la función inversa de la exponencial: $\ln(e^x) = x$. |
| **Conversión a potencia** | Método para **"quitar el logaritmo"** en una ecuación: Si $\log_{b}(x) = a \Rightarrow b^{a} = x$. |
| **Propiedades de suma/resta** | Resta se vuelve división: $\log(A) - \log(B) = \log\left(\frac{A}{B}\right)$. Suma se vuelve multiplicación. |

---

## 3. Ejemplos Resueltos Adicionales

```ad-example
**Ejemplo A: Cálculo con cambio de base**
**Problema:** Calcular el valor de $\log_{4}(16)$ usando una calculadora que solo tiene la tecla `log`.

1. **Identificar elementos:** El argumento es $16$ (está más arriba) y la base es $4$ (está más abajo).
2. **Aplicar la fórmula:** Dividimos el logaritmo del de arriba entre el logaritmo del de abajo:
   $$\frac{\log(16)}{\log(4)}$$
3. **Uso de la calculadora:**
   - Presiona `log`, escribe `16` y cierra paréntesis `)`.
   - Presiona la tecla de división `÷`.
   - Presiona `log`, escribe `4` y cierra paréntesis `)`.
4. **Resultado:** El visor mostrará $2$. Esto es exacto porque $4^{2} = 16$.
```

```ad-example
**Ejemplo B: Aplicación en Finanzas ($USD)**
**Problema:** Un modelo de inversión en dólares sigue la ecuación $\log_{2}(17x - 15) - \log_{2}(2x) = 3$. Hallar el valor de la variable $x$.

1. **Agrupar en un solo logaritmo:** Aplicamos la propiedad de la resta (división de argumentos):
   $$\log_{2} \left( \frac{17x - 15}{2x} \right) = 3$$
2. **Convertir a potencia (Quitar el logaritmo):** La base $2$ pasa al otro lado y eleva al número $3$:
   $$\frac{17x - 15}{2x} = 2^{3}$$
   *(Sabemos que $2 \cdot 2 \cdot 2 = 8$)*.
3. **Despejar la variable:**
   - Pasamos el $2x$ multiplicando: $17x - 15 = 8(2x)$
   - Multiplicamos: $17x - 15 = 16x$
   - Agrupamos las $x$: $17x - 16x = 15$
4. **Resultado:** $x = 15$.
5. **Verificación:** Al sustituir $x=15$ en los argumentos originales ($17(15)-15$ y $2(15)$), ambos dan resultados positivos, por lo que la solución es válida.
```

---

## 4. Sección de Ejercicios de Repaso

```ad-abstract
**🟢 Nivel Fácil: Cálculo Directo**
Usa la fórmula de cambio de base en tu calculadora (redondea a dos decimales si es necesario):
1. $\log_{3}(27)$ 
2. $\log_{5}(625)$ 
3. $\log_{2}(20)$ 
*(Respuestas: 1. [3]; 2. [4]; 3. [4.32])*
```

```ad-abstract
**🟡 Nivel Medio: Ecuaciones Simples**
Despeja la $x$ convirtiendo el logaritmo en potencia:
1. $\log_{6}(2x - 4) = 1$
2. $\log_{2}(x + 5) = 3$
3. $\log_{10}(5x) = 2$
*(Respuestas: 1. [x=5]; 2. [x=3]; 3. [x=20])*
```

```ad-abstract
**🔴 Nivel Avanzado: Aplicación con $USD**
Resuelve aplicando propiedades de resta y división para hallar el valor de $x$:
1. Un presupuesto contable se rige por: $\log_{5}(x + 10) - \log_{5}(2) = 1$. Halla $x$.
2. Determina el valor de $x$ en el siguiente balance: $\log_{2}(17x - 15) - \log_{2}(2x) = 3$.
*(Respuestas: 1. [x=0]; 2. [x=15])*
```

---

## 5. Consejo de Estudio

> [!tip] 💡 Estrategia para el cambio de base
> Para no confundir qué número va arriba y cuál va abajo en la división de la calculadora, usa la **regla de la posición visual** de Profe Alex:
> - El **argumento** está escrito físicamente más arriba.
> - La **base** está escrita físicamente más abajo (como subíndice).
> 
> En la fórmula: $\frac{\log(\text{el que está arriba})}{\log(\text{el que está abajo})}$. ¡Así nunca te equivocarás!