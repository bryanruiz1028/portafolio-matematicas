# 📖 Guía de estudio — Clase 07: Razones Trigonométricas

> [!info] **📌 Conceptos clave**
> ¡Qué tal, amigos! Espero que estén muy bien. Hoy vamos a simplificar el mundo de las razones trigonométricas. Estas son herramientas que nos permiten relacionar los ángulos de un triángulo con la medida de sus lados. Pero, ¡pilas con esto!, para poder aplicarlas debemos cumplir con condiciones muy específicas:
> - **Condición indispensable:** Solo se aplican en **triángulos rectángulos**, es decir, aquellos que tienen un ángulo recto (90°). Si no hay ángulo de 90°, no hay razones trigonométricas básicas.
> - **Identificación de los lados:** 
>     - **Hipotenusa:** Es el lado más largo del triángulo y siempre está frente al ángulo de 90°.
>     - **Catetos:** Son los dos lados que forman la esquina del ángulo recto.
> - **Referencia del ángulo:** ¡Ojo aquí! Los nombres de los catetos cambian según el ángulo que elijas:
>     - **Cateto Opuesto:** El que está enfrente (lejano) al ángulo de referencia.
>     - **Cateto Adyacente:** El que está junto (pegado) al ángulo de referencia.
> - **Configuración técnica:** Antes de empezar, revisa tu calculadora. En la pantalla debe aparecer una **"D"** o la palabra **"DEG"** (Degrees). Si dice "RAD" o "GRA", ¡detente!, porque los resultados no serán correctos.

---

## 2. Fórmulas y definiciones importantes

Lo primero que haremos, como siempre, es tener nuestras fórmulas a la mano. Estas tres razones son la base de todo:

| Término | Definición / Fórmula |
| :--- | :--- |
| **Seno ($\sin$)** | $\frac{\text{Cateto Opuesto}}{\text{Hipotenusa}}$ |
| **Coseno ($\cos$)** | $\frac{\text{Cateto Adyacente}}{\text{Hipotenusa}}$ |
| **Tangente ($\tan$)** | $\frac{\text{Cateto Opuesto}}{\text{Cateto Adyacente}}$ |

> [!note]
> Recuerda: La elección entre opuesto y adyacente depende totalmente de la posición del ángulo que estés analizando.

---

## 3. Ejemplos resueltos adicionales

```ad-example
**Ejemplo A: Cálculo de un cateto (Caso Básico)**
**Problema:** En un triángulo rectángulo, tenemos un ángulo de 32° y la hipotenusa mide 10 metros. ¿Cuánto mide el cateto opuesto (X)?

1. **Identificar datos:** Ángulo = 32°; Hipotenusa = 10 m; Incógnita = Cateto Opuesto (X).
2. **Elegir fórmula:** Como tenemos ángulo, hipotenusa y buscamos el opuesto, usamos el Seno.
   $$\sin(32°) = \frac{X}{10}$$
3. **Despeje:** El 10 que está dividiendo pasa al otro lado a multiplicar.
   $$10 \cdot \sin(32°) = X$$
4. **Resultado:** Al operar en la calculadora obtenemos $5.2991...$ metros. Para ser prácticos, lo aproximamos a:
   **X ≈ 5.3 metros.**
```

```ad-example
**Ejemplo B: Aplicación real y sistema de igualación**
**Problema:** Un barco debe instalar fibra óptica desde su posición hasta la base de un risco que tiene un faro de 30 m encima. Desde el barco, el ángulo a la base del faro es $28° 19' 15"$ y a la punta del faro es $35° 40'$. Si el cable cuesta **$15 USD por metro**, ¿cuánto costará conectar el barco con la base del risco?

1. **Identificar variables:** Llamaremos $x$ a la altura del risco y $y$ a la distancia barco-base (nuestra incógnita).
2. **Plantear ecuaciones (Tangente):**
   - Triángulo 1 (Base): $\tan(28° 19' 15") = \frac{x}{y} \implies x = y \cdot \tan(28° 19' 15")$
   - Triángulo 2 (Cima): $\tan(35° 40') = \frac{x + 30}{y} \implies x = y \cdot \tan(35° 40') - 30$
3. **Igualación:** Como $x$ es igual a $x$, igualamos los lados derechos:
   $$y \cdot \tan(28° 19' 15") = y \cdot \tan(35° 40') - 30$$
4. **Despejar "y":** Pasamos los términos con $y$ a un lado y factorizamos:
   $$30 = y \cdot (\tan(35° 40') - \tan(28° 19' 15"))$$
   $$y = \frac{30}{\tan(35° 40') - \tan(28° 19' 15")}$$
5. **Cálculo final:** Operando con cuidado (usando paréntesis en el denominador), obtenemos que la distancia es **167.8 metros**.
6. **Presupuesto:** $167.8 \text{ m} \cdot \$15 \text{ USD/m} = \$2,517 \text{ USD}$.
**Resultado:** El costo total de la obra es de **$2,517 USD**.
```

---

## 4. Ejercicios de repaso

```ad-abstract
**🟢 Nivel Fácil: Hallar el lado**
Halla el valor del cateto adyacente (Y) en un triángulo rectángulo donde el ángulo de referencia es de 65° y la hipotenusa tiene una longitud de 13 metros.
*(Pista: Usa Coseno y recuerda que el valor debe ser menor que la hipotenusa).*
```

```ad-abstract
**🟡 Nivel Medio: Encontrar el ángulo**
Encuentra el valor del ángulo $\theta$ si el cateto opuesto mide 6 unidades y el cateto adyacente mide 8 unidades.
- **Paso 1:** Usa la función inversa $\arctan(6/8)$.
- **Paso 2:** Verifica visualmente. Al ser el opuesto (6) menor que el adyacente (8), el ángulo debe ser menor a 45°.
```

```ad-abstract
**🔴 Nivel Avanzado: Altura y Costo Operativo**
Dos personas separadas por 790 m observan un avión entre ellas con ángulos de elevación de 82° y 70° respectivamente. 
1. Calcula la altura exacta ($h$) del avión usando el método de igualación.
2. **Contexto económico:** Si el costo de combustible para mantener esa altura es de **$250 USD por cada 100 metros de altura**, ¿cuál es el costo operativo total en ese momento?

**Sección de comprobación:**
- Altura resultante: $1565.8 \text{ m}$.
- Costo operativo: $(1565.8 / 100) \cdot \$250 = \mathbf{\$3,914.50 \text{ USD}}$.
```

---

> [!tip] **💡 Consejo de estudio: El éxito está en la igualdad**
> Cuando tengas problemas con dos triángulos que comparten una pared (como el avión o el faro), la clave es el **Método de Igualación**. Despeja la misma incógnita en ambas ecuaciones (generalmente la altura o la distancia común).
> 
> **Punto crítico en la calculadora:** Para operaciones complejas en el denominador, ¡usa siempre paréntesis! Ejemplo: `Valor / (tan(A) - tan(B))`. Sin los paréntesis, la calculadora dividirá solo por el primer término y restará el segundo al final, dándote un error fatal. ¡Mucho éxito en tu práctica!