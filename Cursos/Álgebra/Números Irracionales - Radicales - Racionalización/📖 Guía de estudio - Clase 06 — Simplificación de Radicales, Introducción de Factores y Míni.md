# 📖 Guía de estudio — Clase 06: Simplificación de Radicales y Operaciones Básicas

> [!info] 📌 Conceptos clave
> - **Relación Índice-Exponente:** Si el exponente de la cantidad subradical es igual al índice de la raíz, se cancelan (ej. $\sqrt[n]{a^n} = a$). Esto ocurre porque el exponente se divide por el índice ($n/n = 1$).
> - **Introducción de factores:** Para meter un factor dentro de una raíz, este debe elevarse al índice del radical. Solo funciona con **factores** (multiplicación), nunca con sumas.
> - **Mínimo Común Índice (MCI):** Se usa para igualar los índices de raíces distintas mediante el MCM. **¿Por qué?** Porque solo podemos multiplicar o dividir radicales si tienen el mismo índice.
> - **Condición para simplificar:** Un radical se puede simplificar solo si el exponente es mayor o igual al índice.
> - **El "Secreto" de los Signos Negativos:** Si el índice es **impar**, puedes trabajar con negativos libremente. Pero si el índice es **par**, los negativos **no deben entrar** a la raíz, ya que cambiarías la naturaleza de la expresión (un resultado negativo se volvería positivo al elevarse a potencia par), alterando el ejercicio original.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Simplificación básica** | Propiedad de cancelación directa: $\sqrt[n]{a^n} = a$. |
| **Introducción de factores** | El factor "paga el peaje" elevándose al índice: $x \cdot \sqrt[n]{y} = \sqrt[n]{x^n \cdot y}$. |
| **Mínimo Común Índice** | **¡Pilas!** Si multiplicas el índice por un número $k$, **debes** multiplicar el exponente interno por el mismo número $k$: $\sqrt[n]{a^m} = \sqrt[n \cdot k]{a^{m \cdot k}}$. |
| **Radicales como potencias** | El índice pasa a ser el denominador: $\sqrt[n]{a^m} = a^{m/n}$. |

```ad-example
title: Ejemplo A — Simplificación por división de exponentes
**Ejercicio:** Simplificar $\sqrt[3]{3^4}$

1. **Descomponer el exponente:** Como 4 no es divisible exactamente entre 3, buscamos el múltiplo de 3 más cercano y menor a 4 (que es 3). Escribimos $3^4$ como $3^3 \cdot 3^1$.
   $$\sqrt[3]{3^3 \cdot 3^1}$$
2. **Separar las raíces:** Aplicamos la propiedad de separación de factores.
   $$\sqrt[3]{3^3} \cdot \sqrt[3]{3^1}$$
3. **Cancelar índice y exponente:** El primer factor tiene índice 3 y exponente 3, así que se liberan de la raíz.
   $$3 \cdot \sqrt[3]{3^1}$$
4. **Resultado final:** $3\sqrt[3]{3}$
```

```ad-example
title: Ejemplo B — Cálculo de dimensiones de inversión
**Escenario:** Tienes un terreno cuadrado cuyo lado mide $\sqrt{18}$ metros. Quieres poner una cerca en todo el **perímetro** y cada metro de malla cuesta $10 USD.

1. **Simplificar el lado del terreno:**
   $$\sqrt{18} = \sqrt{9 \cdot 2} = \sqrt{3^2 \cdot 2} = 3\sqrt{2} \text{ metros.}$$
2. **Calcular el costo de UN lado:**
   Multiplicamos la medida por el costo unitario: $10 \cdot (3\sqrt{2}) = 30\sqrt{2}$ USD.
3. **Calcular el costo PERIMETRAL total:**
   Un cuadrado tiene 4 lados iguales. Multiplicamos el costo de un lado por 4:
   $$4 \cdot (30\sqrt{2}) = 120\sqrt{2} \text{ USD.}$$
**Resultado:** El costo total de la cerca perimetral es de $120\sqrt{2}$ USD.
```

## Ejercicios de Repaso

```ad-abstract
title: Nivel 🟢 Fácil
1. Simplifica cancelando índice y exponente:
   - $\sqrt[5]{x^5}$
   - $\sqrt[3]{(-4)^3}$ (¿Es posible? Sí, porque el índice es impar).
2. Introduce el número entero en la raíz cuadrada aplicando el "peaje":
   - $2\sqrt{5}$
```

```ad-abstract
title: Nivel 🟡 Medio
1. **Pilas con el MCI:** Reduce a Mínimo Común Índice los siguientes radicales para que puedan multiplicarse:
   - $\sqrt[3]{m}$ y $\sqrt[4]{m}$
   - *Pista: El MCM de 3 y 4 es 12. Recuerda multiplicar el exponente por el mismo factor que el índice.*
2. Simplifica descomponiendo el exponente:
   - $\sqrt[3]{x^7}$
```

```ad-abstract
title: Nivel 🔴 Avanzado (Aplicación $USD)
**Problema de Presupuesto:**
Un proyecto financiero tiene un costo base de $\sqrt{5y}$. Debes aplicar un factor de ajuste de $2x$ introduciéndolo en la raíz. 
**Reto:** Escribe la expresión final dentro de un solo radical.
*Pista: Al introducir $(2x)$ en una raíz cuadrada, debes elevar TODO el factor al cuadrado: $(2x)^2 = 4x^2$.*
```

> [!tip] 💡 Consejo de estudio
> **La estrategia del peaje:** Imagina que el índice de la raíz es el "precio" que un factor debe pagar para entrar. Si quieres entrar a una raíz cuadrada, pagas elevándote al cuadrado; si es raíz cúbica, al cubo. 
> 
> **¡El Secreto del Profe Alex!** Nunca metas un signo negativo dentro de una raíz de índice par. Si tienes $-3\sqrt{2}$, deja el menos afuera y solo mete el 3. Esto evita que cambies el signo original del problema por accidente.