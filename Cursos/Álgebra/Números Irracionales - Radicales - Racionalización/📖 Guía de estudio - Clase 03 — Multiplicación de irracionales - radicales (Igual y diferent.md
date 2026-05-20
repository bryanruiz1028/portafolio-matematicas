# 📖 Guía de estudio — Clase 03: Multiplicación de Irracionales (Radicales)

> [!info] 📌 Conceptos clave
> Para dominar la multiplicación de números irracionales, es fundamental tener claros los siguientes puntos:
> - **Propiedad fundamental:** Se utiliza la regla $\sqrt[n]{a} \cdot \sqrt[n]{b} = \sqrt[n]{a \cdot b}$. Los radicales se pueden unir en una sola raíz siempre que tengan el mismo índice.
> - **Índices diferentes:** No se pueden multiplicar de forma directa. Primero se deben transformar en raíces equivalentes con un índice común mediante el Mínimo Común Múltiplo (MCM).
> - **Multiplicación de coeficientes:** Si existen números fuera de la raíz (coeficientes), estos se multiplican entre sí, de forma independiente a lo que sucede dentro de los radicales.
> - **Nota conceptual importante:** A diferencia de la suma y la resta, **no es necesario** que los radicandos sean iguales para multiplicar; solo requerimos que los índices coincidan o se igualen.
> - **Simplificación final:** Siempre intentaremos descomponer en factores primos para extraer términos y presentar la respuesta más sencilla posible.

## 2. Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Índice** | El número que indica el grado de la raíz (ej. $2$ para cuadrada, $3$ para cúbica). |
| **Radicando** | La cantidad o expresión que se encuentra dentro del símbolo de la raíz. |
| **Mínimo Común Múltiplo (MCM)** | Herramienta utilizada para hallar un "índice común" cuando las raíces tienen grados distintos, permitiéndonos hablar el mismo "idioma" matemático. |
| **Propiedad de Amplificación** | Permite obtener raíces equivalentes: $\sqrt[n]{a^m} = \sqrt[n \cdot p]{a^{m \cdot p}}$, multiplicando índice y exponente por un mismo número $p$. |

## 3. Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A (El "Método Alex": Descomponer antes de multiplicar)
**Operación:** $\sqrt{6} \cdot \sqrt{15}$

1. **Identificar índices:** Ambos son raíz cuadrada (índice $2$).
2. **Descomposición previa:** En lugar de multiplicar $6 \cdot 15$, descomponemos cada número en factores primos:
   - $6 = 2 \cdot 3$
   - $15 = 3 \cdot 5$
3. **Unión en una sola raíz:** $\sqrt{2 \cdot 3 \cdot 3 \cdot 5}$
4. **Agrupar potencias:** Observamos que el $3$ aparece dos veces: $\sqrt{2 \cdot 3^2 \cdot 5}$
5. **Extracción y resultado:** Como el exponente del $3$ coincide con el índice, el $3$ sale de la raíz:
   $3 \cdot \sqrt{2 \cdot 5} = 3\sqrt{10}$

*¡Evitamos trabajar con el número 90 y simplificamos directamente!*
```

```ad-example
title: Ejemplo B (Aplicación Real en Terrenos)
**Enunciado:** Un terreno rectangular mide $\sqrt{5} \text{ m}$ de ancho y $\sqrt{10} \text{ m}$ de largo. Si el costo de mantenimiento es de $10 \text{ USD}$ por cada metro cuadrado, ¿cuál es el costo total?

1. **Cálculo del área:**
   $\text{Área} = \sqrt{5} \cdot \sqrt{10} = \sqrt{5 \cdot (5 \cdot 2)} = \sqrt{5^2 \cdot 2}$
2. **Simplificación del área:**
   $\text{Área} = 5\sqrt{2} \text{ m}^2$
3. **Cálculo del costo total:**
   $\text{Costo} = 10 \cdot (5\sqrt{2}) \text{ USD} = 50\sqrt{2} \text{ USD}$

**Resultado:** El área es $5\sqrt{2} \text{ m}^2$ y el costo de mantenimiento es $50\sqrt{2} \text{ USD}$ (aproximadamente $70.71 \text{ USD}$).
```

## 4. Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel: Fácil (Multiplicación directa)
Resuelve las siguientes operaciones manteniendo el mismo índice:
1. $\sqrt{2} \cdot \sqrt{3}$
2. $\sqrt{7} \cdot \sqrt{5}$
3. $\sqrt[3]{4} \cdot \sqrt[3]{2}$
```

```ad-abstract
title: 🟡 Nivel: Medio (Simplificación y Coeficientes)
Aplica la multiplicación de coeficientes y simplifica el radical final:
1. $2\sqrt{5} \cdot 5\sqrt{10}$
2. $3\sqrt{6} \cdot 2\sqrt{2}$
3. $\sqrt[3]{9} \cdot \sqrt[3]{6}$
```

```ad-abstract
title: 🔴 Nivel: Avanzado (Índices Diferentes y Aplicación Económica)
**Problema:** Una pieza de arte metálica tiene una base de $\sqrt[3]{2} \text{ m}$ y una altura de $\sqrt{3} \text{ m}$. 
1. Calcula el área exacta de la pieza igualando los índices (MCM de $2$ y $3$ es $6$).
2. Si el material especial cuesta $100 \text{ USD}$ por cada unidad de área resultante, calcula el costo total multiplicando $100$ por la expresión radical hallada.
*Pista: Recuerda amplificar tanto el índice como el exponente interno.*
```

## 5. Consejo de Estudio

> [!tip] 💡 Estrategia de los factores primos
> Cuando te enfrentes a números grandes dentro de las raíces, no te apresures a multiplicarlos para obtener un resultado gigante. Sigue la estrategia del **"Profe Alex"**: **descompón cada número en sus factores primos antes de unirlos**. Esto te permitirá identificar "parejas" (en raíces cuadradas) o "tríos" (en raíces cúbicas) de forma mucho más rápida y visual. ¡La organización de factores es la clave para que el álgebra sea sencilla y sin errores!