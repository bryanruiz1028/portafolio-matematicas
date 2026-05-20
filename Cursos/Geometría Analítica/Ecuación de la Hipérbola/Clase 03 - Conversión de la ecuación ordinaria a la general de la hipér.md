---
status: completo
dificultad: introductoria
tags: [#algebra, #convertingfromt]
prerrequisitos: [[Clase 02]], Binomios al cuadrado, Operaciones con fracciones
---

# Clase 03 — Conversión de la ecuación ordinaria a la general de la hipérbola

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | [[Clase 04|Clase 04 ➡]]

## 🌍 Relevancia y aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> El paso de la forma ordinaria a la general no es solo un ejercicio algebraico; es el lenguaje necesario para que las computadoras y el software de ingeniería procesen curvas.
> 
> 1.  **Arquitectura y Estructuras:** Las estructuras hiperbólicas (como torres de enfriamiento o techos de estadios) se calculan mediante sistemas de ecuaciones. La forma general igualada a cero permite integrar estas trayectorias en software de diseño estructural de forma unificada.
> 2.  **Fluctuaciones de Mercado ($USD):** En economía, la hipérbola modela la **elasticidad precio-demanda**. Sus asíntotas representan límites naturales, como un precio máximo que nadie pagaría o una oferta que no puede bajar más. La forma general facilita hallar estos "puntos críticos" financieros.
> 3.  **Localización por Señales:** El sistema GPS calcula tu posición mediante la intersección de hipérbolas. Convertir las señales a la forma general permite que los procesadores resuelvan rápidamente dónde estás comparando tiempos de llegada de señal.

## 📌 ¿Qué es la conversión a la forma general?

> [!note] 📌 ¿Qué es...
> Imagina que tienes las piezas de un rompecabezas (la forma ordinaria) y quieres guardarlas todas en una sola caja que debe quedar totalmente vacía al final (igualada a cero). Pasar de la forma ordinaria a la general es simplemente **reordenar** los términos de la ecuación. 
> 
> Movemos todo lo que está a la derecha del igual hacia la izquierda, siguiendo un orden específico ($x^2, y^2, x, y$ y el número solo), dejando el otro lado en cero.

> [!warning] ⚠️ Error común
> El signo **negativo** central es el mayor enemigo. En una hipérbola, las fracciones se restan. Al aplicar el "Método Mariposa", ese signo menos debe afectar a **todo** el numerador de la segunda fracción. Si lo ignoras, terminarás con una elipse o una ecuación errónea.

> [!tip] 💡 Truco para recordarlo
> 1. **La Carita Feliz:** Multiplica los denominadores (la sonrisa) y luego en cruz (los ojos).
> 2. **La Visita:** Al expandir binomios como $10(x-2)^2$, recuerda la **Propiedad Distributiva**: el número de afuera es un "visitante" que debe saludar (multiplicar) a cada integrante de la familia dentro de la casa (paréntesis).

## 🛠 Procedimiento Técnico

Para transformar la ecuación ordinaria $\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1$ a la forma general $Ax^2 + By^2 + Cx + Dy + E = 0$, sigue este algoritmo:

1.  **Multiplicación de denominadores:** Multiplica $a^2 \cdot b^2$ para obtener un común denominador.
2.  **Multiplicación en cruz:** Multiplica el primer numerador por el segundo denominador y viceversa. Mantén el signo menos central.
3.  **Eliminación de fracción:** El denominador común pasa al otro lado multiplicando al $1$ (se convierte en el valor constante inicial).
4.  **Expansión y Distribución:** Desarrolla los binomios al cuadrado $(x-h)^2 = x^2 - 2xh + h^2$ y distribuye los coeficientes.
5.  **Ordenamiento y Validación:** Agrupa términos e iguala a cero. 
    *   **Validación Profe Alex:** Verifica que los signos de $x^2$ y $y^2$ sean **diferentes**. Si son iguales, no es una hipérbola.

## 📝 Ejemplos Prácticos

> [!example] Ejemplo 1: Centro en el origen (0,0)
> **Ecuación:** $\frac{x^2}{4} - \frac{y^2}{9} = 1$
> 1. **Común denominador:** $4 \cdot 9 = 36$.
> 2. **Cruce:** $(x^2 \cdot 9) - (4 \cdot y^2) = 36 \cdot 1$.
> 3. **Simplificación:** $9x^2 - 4y^2 = 36$.
> 4. **Igualar a cero:** $9x^2 - 4y^2 - 36 = 0$.

> [!example] Ejemplo 2: Centro en $(h,k)$
> **Ecuación:** $\frac{(x-2)^2}{5} - \frac{(y+4)^2}{10} = 1$
> 1. **Común denominador:** $5 \cdot 10 = 50$.
> 2. **Planteamiento:** $10(x-2)^2 - 5(y+4)^2 = 50$.
> 3. **Binomios:** $10(x^2 - 4x + 4) - 5(y^2 + 8y + 16) = 50$.
> 4. **Distribución:** $10x^2 - 40x + 40 - 5y^2 - 40y - 80 = 50$.
> 5. **Orden:** $10x^2 - 5y^2 - 40x - 40y + 40 - 80 - 50 = 0$.
> **Resultado:** $10x^2 - 5y^2 - 40x - 40y - 90 = 0$.

> [!example] Ejemplo 3: Un denominador es la unidad ($1$)
> Basado en la lógica del Profe Alex para casos simplificados: $\frac{x^2}{12} - y^2 = 1$.
> 1. Ponemos un $1$ debajo: $\frac{x^2}{12} - \frac{y^2}{1} = 1$.
> 2. Común denominador: $12 \cdot 1 = 12$.
> 3. Cruce: $(x^2 \cdot 1) - (12 \cdot y^2) = 12$.
> **Resultado:** $x^2 - 12y^2 - 12 = 0$.

> [!example] Ejemplo 4: Aplicación Económica ($USD)
> Una curva de demanda en $USD sigue la trayectoria $\frac{x^2}{100} - \frac{y^2}{400} = 1$, donde $x$ es el precio del activo.
> 1. Común denominador: $100 \cdot 400 = 40000$.
> 2. Cruce: $400x^2 - 100y^2 = 40000$.
> 3. Simplificamos dividiendo entre $100$: $4x^2 - y^2 = 400$.
> **Forma General:** $4x^2 - y^2 - 400 = 0$.

## ✏️ Bloque de Ejercicios

### 🟢 Nivel Fácil (Centro 0,0)
1. $\frac{x^2}{9} - \frac{y^2}{16} = 1$
2. $\frac{y^2}{25} - \frac{x^2}{4} = 1$
3. $x^2 - \frac{y^2}{10} = 1$
4. $\frac{x^2}{3} - \frac{y^2}{5} = 1$

### 🟡 Nivel Medio (Centro h,k)
5. $\frac{(x-1)^2}{4} - \frac{(y+2)^2}{9} = 1$
6. $\frac{(y-3)^2}{16} - \frac{(x-5)^2}{4} = 1$
7. $\frac{(x+4)^2}{2} - \frac{y^2}{8} = 1$
8. $\frac{(y+1)^2}{12} - \frac{(x-1)^2}{10} = 1$

### 🔴 Nivel Avanzado (Contexto $USD)
9. Una hipérbola de elasticidad de producto entre $10 USD y $50 USD: $\frac{x^2}{10^2} - \frac{y^2}{50^2} = 1$.
10. Convierta la trayectoria de costo marginal: $\frac{(x-10)^2}{25} - \frac{(y-50)^2}{100} = 1$.
11. Elasticidad unitaria simplificada: $\frac{x^2}{1} - \frac{y^2}{0.5} = 1$.
12. Modelo de mercado bursátil: $\frac{(x-20)^2}{400} - \frac{(y-10)^2}{900} = 1$.

> [!success] ✅ Respuestas para el docente
> 1. $16x^2 - 9y^2 - 144 = 0$
> 2. $-25x^2 + 4y^2 - 100 = 0$ (u ordenado: $-25x^2 + 4y^2 - 100 = 0$)
> 3. $10x^2 - y^2 - 10 = 0$
> 4. $5x^2 - 3y^2 - 15 = 0$
> 5. $9x^2 - 4y^2 - 18x - 16y - 43 = 0$
> 6. **$-4x^2 + y^2 + 40x - 6y - 107 = 0$** (Simplificada)
> 7. $4x^2 - y^2 + 32x + 56 = 0$
> 8. **$-6x^2 + 5y^2 + 12x + 10y - 61 = 0$** (Simplificada)
> 9. $25x^2 - y^2 - 2500 = 0$
> 10. $4x^2 - y^2 - 80x + 100y - 2200 = 0$
> 11. $x^2 - 2y^2 - 1 = 0$
> 12. $9x^2 - 4y^2 - 360x + 80y - 400 = 0$

## 🧠 Autoevaluación

> [!question] Pregunta 1: Sobre los signos
> Si al llegar a la forma general obtienes $5x^2 + 2y^2 - 10 = 0$, ¿has convertido correctamente la hipérbola?
> **Respuesta:** No. En la hipérbola, los coeficientes de $x^2$ y $y^2$ deben tener **signos diferentes**. Si ambos son positivos, has calculado una elipse por error.

> [!question] Pregunta 2: Procedimental
> ¿Qué sucede con el denominador común (ej. 50) obtenido por el método mariposa?
> **Respuesta:** Pasa al otro lado de la igualdad multiplicando al $1$. Luego, ese resultado debe regresarse al lado izquierdo restando para igualar la ecuación a cero.

> [!question] Pregunta 3: Aplicación Económica
> Si una hipérbola de precios tiene centro en $(0,0)$, ¿cuántos términos tendrá su ecuación general?
> **Respuesta:** Tendrá 3 términos: el término con $x^2$, el término con $y^2$ y el término independiente ($E$). Los términos lineales ($x$ y $y$ simples) no aparecen cuando el centro es el origen.

## 🎓 Cierre y Próximos Pasos

Dominar la conversión a la forma general es el puente necesario para analizar cualquier hipérbola, sin importar cómo se presente en un plano técnico o financiero. En la **Clase 04**, realizaremos el proceso inverso: aprenderemos a extraer los elementos (vértices, focos y centro) partiendo únicamente de la ecuación general.

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | [[Clase 04|Clase 04 ➡]]