# 📖 Guía de estudio — Clase 02: Convertir Porcentaje a Fracción

> [!info] 📌 Conceptos clave
> - **Porcentaje como fracción:** Todo porcentaje representa una parte de un total de 100. Se puede expresar como una fracción con denominador 100 (por ejemplo, 25% es 25 de cada 100).
> - **Simplificación:** Para que una respuesta sea matemáticamente elegante y profesional, debemos reducir la fracción a su forma irreducible, dividiendo tanto el numerador como el denominador por el mismo número.
> - **Porcentajes con decimales:** Si el porcentaje tiene coma decimal, utilizamos potencias de 10 (10, 100, 1000) para eliminarla antes de empezar a simplificar.
> - **Razón vs. Fracción:** ¡Ojo con este detalle técnico! Una expresión como $12,5/100$ se llama **razón** porque contiene un decimal. Se convierte en **fracción** propiamente dicha solo cuando logramos que ambos números sean enteros.

## Tabla de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Porcentaje** | Representación de una cantidad como una fracción de 100 partes iguales ("de cada 100"). |
| **Simplificación** | El arte de reducir una fracción dividiendo numerador y denominador por un divisor común. |
| **Amplificación** | Multiplicar numerador y denominador por potencias de 10 (10, 100, 1000...) según la cantidad de decimales que deseamos eliminar para obtener números enteros. |

## Sección de Ejemplos Resueltos

````ad-example
title: Ejemplo A — Caso básico
**Problema:** Convertir 25% a fracción simplificada.

1. **Paso 1:** Escribimos el porcentaje sobre 100.
   $$25\% = \frac{25}{100}$$
2. **Paso 2:** Simplificamos. Aplicamos el criterio de divisibilidad (terminan en 5 y 0), así que dividimos entre 5:
   $$\frac{25 \div 5}{100 \div 5} = \frac{5}{20}$$
3. **Paso 3:** Volvemos a dividir entre 5 para llegar a la irreducible:
   $$\frac{5 \div 5}{20 \div 5} = \frac{1}{4}$$

**Resultado final:** $1/4$
````

````ad-example
title: Ejemplo B — Aplicación con decimales y $USD
**Problema:** Un producto tiene un descuento del 12,5%. ¿A qué fracción equivale?

1. **Paso 1:** Planteamos la razón inicial: $\frac{12,5}{100}$. (Recuerda que es razón por el decimal).
2. **Paso 2:** Amplificamos para eliminar la coma. Como hay **un** lugar decimal, multiplicamos por $10/10$:
   $$\frac{12,5 \times 10}{100 \times 10} = \frac{125}{1000}$$
3. **Paso 3:** Simplificamos la fracción dividiendo sucesivamente entre 5:
   - $\frac{125 \div 5}{1000 \div 5} = \frac{25}{200}$
   - $\frac{25 \div 5}{200 \div 5} = \frac{5}{40}$
   - $\frac{5 \div 5}{40 \div 5} = \frac{1}{8}$

**Utilidad práctica:** Saber que 12,5% es $1/8$ te permite calcular descuentos rápido: ¡solo divide el precio entre 8!
````

## Ejercicios de Repaso

````ad-abstract
title: 🟢 Nivel Fácil
Expresa las siguientes cifras como fracción irreducible:
1. **50%** (Pista: es la mitad de algo).
2. **10%** (Pista: termina en cero, puedes simplificar por 10).
3. **70%**
````

````ad-abstract
title: 🟡 Nivel Medio
Convierte a fracción simplificada y analiza los resultados:
1. **140%**: Nota que al ser mayor a 100, obtendrás una *fracción impropia* (donde el numerador es más grande que el denominador).
2. **15%**
3. **13%**: ¿Es posible simplificar esta fracción? 
   *Ayuda pedagógica:* Observa que el 13 es un **número primo** y no divide exactamente al 100; por lo tanto, la fracción ya es irreducible.
````

````ad-abstract
title: 🔴 Nivel Avanzado — Aplicación con $USD
Pon a prueba tu lógica con estos retos:
1. **Conversión técnica:** Convierte **2,25%** a fracción. Al tener **dos** cifras decimales, debes amplificar multiplicando por $100/100$ para desplazar la coma dos lugares hacia la derecha antes de simplificar.
2. **Problema de verificación:** Si **45 USD** representa el **20%** del costo de un producto:
   - Expresa ese 20% como fracción simplificada (obtendrás $1/5$).
   - **Verificación:** Si el 20% es "una de cinco partes", multiplica esos 45 USD por 5 para comprobar que el precio total es, efectivamente, **225 USD**.
````

> [!tip] 💡 Consejo de estudio
> ¡No te desesperes si la simplificación parece larga! Ir paso a paso te asegura el éxito. Para ser más veloz, domina los **criterios de divisibilidad** y ten siempre presentes tus tablas de multiplicar. 
> - Si termina en **0 o 5**, usa el **5**.
> - Si son **pares**, saca **mitad**. 
> - Si ambos terminan en **0**, ¡elimina un cero en cada uno y habrás dividido entre 10 al instante!