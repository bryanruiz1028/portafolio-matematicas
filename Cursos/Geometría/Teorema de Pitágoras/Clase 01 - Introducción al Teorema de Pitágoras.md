# Clase 01 — Pythagorean Theorem Introduction + Cómo saber si un triángulo es rectángulo | Teorema de Pitágoras

#algebra #pythagoreantheo

[[00 - Índice del curso]] | [[Clase 02]]

---

¡Qué tal amigos! Espero que estén muy bien. Hoy vamos a viajar miles de años atrás para descubrir un secreto de la geometría que nos ha permitido construir desde pirámides hasta las pantallas de nuestros celulares.

> [!info] **Relevancia y Aplicaciones**
> Aunque lleva el nombre de Pitágoras (filósofo griego del siglo VI a.C.), este conocimiento es mucho más antiguo. Civilizaciones en **Babilonia (1800 a.C.)** y **China (500 a.C.)** ya conocían estas relaciones, y la primera demostración escrita aparece en la obra "Los Elementos" de **Euclides (300 a.C.)**.
> 
> **¿Cómo lo hacían sin tecnología?**
> Los antiguos egipcios usaban cuerdas con nudos a distancias iguales para formar el "Triángulo Sagrado" de medidas 3, 4 y 5. Al tensar la cuerda, obtenían un ángulo recto perfecto (90°) para alinear escaleras y muros sin necesidad de escuadras o niveles modernos.
> 
> **Aplicaciones actuales:**
> - 💵 **Comercio:** Calcular el precio de un televisor basado en las pulgadas de su diagonal (que es la hipotenusa).
> - 🏗️ **Construcción:** Asegurar que las paredes y techos estén perfectamente alineados.
> - 📊 **Tecnología:** El GPS utiliza este teorema para calcular la distancia más corta en línea recta entre dos puntos.

---

> [!note] **Concepto Clave**
> El Teorema de Pitágoras es una "regla mágica" que **solo funciona en triángulos rectángulos** (aquellos que tienen un ángulo de 90°).
> 
> - **Hipotenusa ($h$):** Es el lado más largo del triángulo y siempre está frente al ángulo recto.
> - **Catetos ($a$ y $b$):** Son los dos lados que forman el ángulo de 90°.
> 
> **La Fórmula Maestra:**
> $$h^2 = a^2 + b^2$$
> *Donde el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos.*

> [!warning] **¡Pilas con esto!**
> - ❌ **No es un triángulo:** Antes de aplicar nada, recuerda que la suma de los dos lados menores debe ser mayor al tercero, si no, ¡el triángulo no existe!
> - ❌ **Error típico:** Sumar los lados antes de elevarlos al cuadrado (ej. $3+4=7$ y luego $7^2=49$ ❌). ¡Primero elevamos, luego sumamos!
> - ✅ **Lo correcto:** $3^2 + 4^2 \rightarrow 9 + 16 = 25$ ✅.

> [!tip] **Truco Mnemotécnico**
> Para que nunca se te olvide: *"El cuadrado de la **H**ipotenusa es igual a la suma de los cuadrados de sus amigos los **Catetos** ($a$ y $b$)"*.

---

### Procedimiento: ¿Cómo saber si un triángulo es rectángulo?

```text
PASO 0: Verificar existencia (Lado A + Lado B debe ser > Lado C).
PASO 1: Identificar el lado más largo (Hipotenusa potencial).
PASO 2: Elevar la hipotenusa al cuadrado.
PASO 3: Elevar los dos catetos al cuadrado y sumar sus resultados.
PASO 4: Comparar:
        - Si h² = a² + b² —> ¡SÍ es un triángulo rectángulo! (90°)
        - Si h² ≠ a² + b² —> NO es un triángulo rectángulo.
```

---

> [!example] **Ejemplos Prácticos**
> 
> **Ejemplo 1: El Triángulo Sagrado (3, 4, 5)**
> 1. Lado largo: $5$.
> 2. $5^2 = 25$
> 3. $3^2 + 4^2 = 9 + 16 = 25$
> *Resultado:* $25 = 25$. **¡Sí es un triángulo rectángulo!**
> 
> **Ejemplo 2: Comprobación de terna (5, 12, 13)**
> 1. Lado largo: $13$.
> 2. $13^2 = 169$
> 3. $12^2 + 5^2 = 144 + 25 = 169$
> *Pilas:* Primero elevamos $12 \times 12$ y $5 \times 5$. **¡Sí es un triángulo rectángulo!**
> 
> **Ejemplo 3: Caso Negativo (5, 6, 8)**
> 1. Lado largo: $8$.
> 2. $8^2 = 64$
> 3. $5^2 + 6^2 = 25 + 36 = 61$
> *Resultado:* $64 \neq 61$. **No es un triángulo rectángulo.**
> 
> **Ejemplo 4: Aplicación Económica ($USD)**
> Un técnico cobra $10 USD por cada pulgada de diagonal de una pantalla. Si mide 30" de base y 40" de altura:
> 1. Hipotenusa: $30^2 + 40^2 = 900 + 1600 = 2500$.
> 2. $\sqrt{2500} = 50$ pulgadas.
> 3. Precio: $50 \times 10 = \mathbf{500 \text{ USD}}$.

---

> [!abstract] **Ejercicios para el Estudiante**
> 
> **🟢 Nivel Verde (Fácil) - Verifica si son rectángulos:**
> 1. Lados: $6, 8, 10$
> 2. Lados: $9, 12, 15$
> 3. Lados: $8, 15, 17$
> 4. Lados: $12, 16, 20$
> 
> **🟡 Nivel Amarillo (Medio) - Cifras mayores o decimales:**
> 5. Lados: $7, 24, 25$
> 6. Lados: $20, 21, 29$
> 7. Lados: $10, 24, 26$
> 8. Lados: $1.5, 2, 2.5$
> 
> **🔴 Nivel Rojo (Avanzado) - Problemas aplicados ($USD):**
> 9. Una antena de $12m$ de alto usa un cable hasta un anclaje a $5m$ de la base. Si el metro de cable cuesta $\$15$ USD, ¿cuánto cuesta el cable?
> 10. Un terreno rectangular de $30m \times 40m$ se divide con una valla diagonal. Si el metro cuesta $\$20$ USD, ¿cuál es el costo?
> 11. Un dron vuela desde el suelo a la cima de una torre de $24m$. Despegó a $7m$ de la base. Si cobran $\$2$ USD por metro de vuelo, ¿cuánto cuesta el envío?
> 12. Verifica si un triángulo de lados $10, 11$ y $14$ es rectángulo. Si no lo es, justifica usando el símbolo $\neq$.

---

> [!success] **Respuestas**
> 1. Sí ($100 = 100$) | 2. Sí ($225 = 225$) | 3. Sí ($289 = 289$) | 4. Sí ($400 = 400$)
> 5. Sí ($625 = 625$) | 6. Sí ($841 = 841$) | 7. Sí ($676 = 676$) | 8. Sí ($6.25 = 6.25$)
> 9. **$195 USD** (Longitud: $13m$)
> 10. **$1,000 USD** (Longitud: $50m$)
> 11. **$50 USD** (Recorrido: $25m$)
> 12. **No es rectángulo** ($196 \neq 221$).

> [!question] **Mini-prueba de Autoevaluación**
> 1. **¿Cuál es el nombre del lado que siempre está frente al ángulo de 90°?**
> 2. **¿Es un triángulo rectángulo uno cuyos lados miden 5, 10 y 12?**
> 3. **Si una pantalla triangular tiene una base de 3 pulgadas y una altura de 4 pulgadas, y cada pulgada de diagonal cuesta $2 USD, ¿cuál es el precio total?**

---

**Próximo tema:** ¡Superfácil! En la siguiente clase aprenderemos a despejar la fórmula para encontrar un lado faltante cuando ya estamos seguros de que el triángulo es rectángulo. ¡No te lo pierdas!

[[00 - Índice del curso]] | [[Clase 02]]