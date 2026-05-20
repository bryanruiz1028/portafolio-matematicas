# 📖 Guía de estudio — Clase 06: Regla de 3 compuesta

¡Hola! En esta guía vamos a dominar la **regla de 3 compuesta**. No te dejes intimidar por el número de datos; verás que, siguiendo un orden lógico y analizando cómo se relacionan las variables, cualquier problema se vuelve sencillo. ¡La clave está en la organización!

> [!info] 📌 Conceptos clave
> - **Definición:** Se utiliza cuando intervienen **más de dos variables** relacionadas proporcionalmente.
> - **Identificación de variables:** Busca las palabras que siguen a los números (ej. 15 **obreros**, 7 **horas**, 8 **casas**). Si una cantidad no cambia en todo el problema, no es necesario tratarla como variable.
> - **Relación Directa:** Si una variable aumenta, la otra también (ej. a más unidades que fabricar, más días se necesitan).
> - **Relación Inversa:** Si una variable aumenta, la otra disminuye (ej. a más obreros trabajando, menos días tardarán).
> - **Simplificación:** ¡Tu mejor amiga! Simplificar las fracciones antes del cálculo final evita errores con números gigantes.

---

### 2. Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Variable** | Lo que cambia en el problema (obreros, horas, días, unidades, raciones). |
| **Relación Directa** | Cuando ambas variables se mueven en la misma dirección (Ejemplo: Unidades y Días). **Se mantiene la fracción igual.** |
| **Relación Inversa** | Cuando las variables se mueven en direcciones opuestas (Ejemplo: Obreros y Días). **Se debe invertir (voltear) la fracción.** |

---

### 3. Ejemplos Resueltos Adicionales

```ad-example
**Ejemplo A: Caso de Construcción**
**Problema:** Si 15 obreros trabajando 7 horas diarias construyen 1 casa en 40 días, ¿cuántos obreros serán necesarios para construir 8 casas en 60 días trabajando 8 horas diarias?

**1. Planteamiento:**
- Obreros (X): 15 → **x**
- Horas/día: 7 → 8 (¿Más horas, menos obreros? Sí. **Inversa**)
- Casas: 1 → 8 (¿Más casas, más obreros? Sí. **Directa**)
- Días: 40 → 60 (¿Más días, menos obreros? Sí. **Inversa**)

**2. Procedimiento:**
Escribimos la relación de la incógnita e igualamos a las demás variables. Como hay variables inversas, **aplicamos el "flip" (giro)** a sus fracciones:
$\frac{x}{15} = (\frac{7}{8}) \cdot (\frac{8}{1}) \cdot (\frac{40}{60})$
*Nota: Horas y Días se invirtieron porque son inversas.*

**3. Simplificación paso a paso:**
- El **15** que divide a la $x$ pasa a multiplicar: $x = 15 \cdot \frac{7}{8} \cdot \frac{8}{1} \cdot \frac{40}{60}$
- Cancelamos el **8** que está arriba con el **8** de abajo.
- Simplificamos **40/60**: eliminamos los ceros ($\frac{4}{6}$) y sacamos mitad, quedando $\frac{2}{3}$.
- Ahora tenemos: $x = 15 \cdot 7 \cdot \frac{2}{3}$.
- Simplificamos el **15** con el **3** ($15 \div 3 = 5$).
- Multiplicamos lo que queda: $5 \cdot 7 \cdot 2 = 70$.

**✅ Resultado: 70 obreros**
```

```ad-example
**Ejemplo B: Aplicación Real - Gestión de Recursos**
**Problema:** Un granjero tiene 1800 ovejas y alimento para 20 días con una ración completa (100%). Si vende algunas ovejas y decide darles el 80% de la ración para que el alimento dure 10 días más (30 días en total), ¿cuántas ovejas vendió?

**1. Planteamiento:**
- Ovejas (X): 1800 → **x**
- Días: 20 → 30 (¿Más días, menos ovejas? Sí. **Inversa**)
- Ración: 100% → 80% (¿Menos ración, alcanza para más ovejas? Sí. **Inversa**)

**2. Cálculo de ovejas que quedan (x):**
$\frac{x}{1800} = \frac{20}{30} \cdot \frac{100}{80}$ *(Invertimos ambas porque son inversas)*
$x = 1800 \cdot (\frac{2}{3}) \cdot (\frac{10}{8}) = 1500$

**3. Análisis final:**
El problema pregunta cuántas **vendió**. Si le quedan 1500:
$1800 - 1500 = 300$

**✅ Resultado: Vendió 300 ovejas**
```

---

### 4. Ejercicios de Repaso

```ad-abstract
**🟢 Fácil (Nivel 1)**
Utilizando los datos del Ejemplo A: Si 15 obreros construyen una casa en 40 días trabajando 7 horas diarias, ¿cuántos obreros se necesitan para construir la misma casa en solo 20 días trabajando las mismas 7 horas?
*(Pista: Como las casas y las horas no cambian, solo tienes una relación entre obreros y días).*
```

```ad-abstract
**🟡 Medio (Nivel 2)**
**El Reto del Profe Alex:** Tomando como base los datos iniciales (15 obreros, 7 horas/día, 1 casa, 40 días), calcula cuántos días tardarán 5 obreros en construir 3 casas trabajando 6 horas diarias.
**Instrucción:** Compara cada variable con los "Días" para saber si debes invertir las fracciones.
```

```ad-abstract
**🔴 Avanzado (Desafío Lógico)**
En una fábrica, 10 máquinas empacan un pedido de 1,000,000 de unidades. Se sabe que trabajando 8 horas diarias, las 10 máquinas empacan 400,000 unidades en 5 días. Sin embargo, al iniciar el quinto día (tras 4 días de trabajo normal), se averían 3 máquinas. El resto debe trabajar 10 horas diarias para terminar el pedido.

**Sigue estos pasos:**
1. **Paso 1:** Calcula cuántas unidades se hicieron en los primeros 4 días (si en 5 días hacen 400k, ¿cuántas hacen en 4?).
2. **Paso 2:** Resta eso al total (1,000,000) para saber cuánto falta.
3. **Paso 3:** Calcula los días necesarios para terminar lo que falta con 7 máquinas a 10 horas/día.
```

---

### 5. Estrategia de Dominio (Consejo de Estudio)

> [!tip] 💡 El secreto de "Preguntar a la X"
> Para no confundirte con los números al decidir si una relación es directa o inversa, utiliza la técnica del **profe Alex**: Olvida las cifras por un momento e imagina la situación.
> 
> Hazte esta pregunta mágica: **"Si tengo MÁS de la Variable A, ¿necesitaré MÁS o MENOS de mi Variable X?"** 
> 
> - Si la respuesta es **MÁS**, la relación es **Directa** (dejas la fracción igual).
> - Si la respuesta es **MENOS**, la relación es **Inversa** (volteas la fracción). 
> 
> ¡La lógica siempre debe ir antes que el cálculo!