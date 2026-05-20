# 📖 Guía de estudio — Clase 07: Resolución de ecuaciones exponenciales con logaritmos

> [!info] 📌 Conceptos clave
> ¡Hola, estudiante! En esta sesión aprenderemos a resolver ecuaciones donde la incógnita se encuentra en el exponente y no existe una forma directa de igualar las bases.
> - **Uso de logaritmos:** Se emplean como herramienta principal cuando las bases (por ejemplo, $3$ y $2$) no pueden transformarse en una base común.
> - **Función del logaritmo:** Ya sea natural ($\ln$) o decimal ($\log$), su función es "bajar" el exponente para transformarlo en un factor multiplicativo.
> - **Álgebra esencial:** Para despejar $x$, es vital aplicar correctamente la **propiedad distributiva** y el **factor común**.
> - **Resultados decimales:** Debido a la naturaleza de los logaritmos, la respuesta suele ser un número irracional que expresamos como un valor aproximado ($\approx$).

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Propiedad de la Potencia** | Permite bajar el exponente: $\log(a^n) = n \cdot \log(a)$. El exponente pasa al frente a multiplicar. |
| **Propiedad del Producto** | Útil para separar multiplicaciones: $\ln(a \cdot b) = \ln(a) + \ln(b)$. Facilita el aislamiento de términos. |
| **Bases Iguales (Atajo)** | Si elegimos una base de logaritmo igual a la de la potencia, el término se simplifica: $\log_b(b) = 1$. Este es el "Método 2" para obtener resultados más directos. |
| **Logaritmo Natural ($\ln$)** | Logaritmo en base $e$. Es el preferido por el "Profe Alex" por su rapidez de escritura (solo dos letras). |

---

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Caso con exponentes en ambos lados
**Ecuación:** $3^{x+1} = 2^x$

1. **Aplicar logaritmos:** Usamos logaritmo natural en ambos lados:
   $\ln(3^{x+1}) = \ln(2^x)$

2. **Bajar exponentes:** Aplicamos la propiedad de la potencia. 
   > [!warning] **¡Pilas aquí!**
   > Como el exponente $x+1$ tiene dos términos, **debe ir obligatoriamente entre paréntesis** para que el logaritmo multiplique a toda la expresión:
   > $(x + 1)\ln(3) = x \ln(2)$

3. **Propiedad distributiva:** Multiplicamos $\ln(3)$ por cada término:
   $x \ln(3) + \ln(3) = x \ln(2)$

4. **Agrupar términos con $x$:** Movemos las $x$ a la izquierda y los constantes a la derecha. 
   *(Nota: El signo negativo surge al trasponer términos).*
   $x \ln(3) - x \ln(2) = -\ln(3)$

5. **Factorizar y despejar:** Extraemos factor común $x$:
   $x(\ln(3) - \ln(2)) = -\ln(3)$
   $x = \frac{-\ln(3)}{\ln(3) - \ln(2)}$

6. **Resultado final:** ✅ $x \approx -2.7092$
```

```ad-example
title: Ejemplo B — Aplicación de crecimiento financiero ($USD)
**Enunciado:** Una cuenta de inversión crece a razón de $5^x$, mientras que un fondo competidor inicia con 3 USD y crece a $2^x$. ¿En qué momento exacto se igualan ambos montos?
**Ecuación:** $5^x = 3 \cdot 2^x$

1. **Aplicar logaritmos:** $\ln(5^x) = \ln(3 \cdot 2^x)$.
2. **Propiedad del producto:** Separamos la multiplicación en el lado derecho:
   $\ln(5^x) = \ln(3) + \ln(2^x)$
3. **Bajar exponentes:** Aplicamos la propiedad de potencia para liberar las $x$:
   $x \ln(5) = \ln(3) + x \ln(2)$
4. **Agrupar y factorizar:**
   $x \ln(5) - x \ln(2) = \ln(3)$
   $x(\ln(5) - \ln(2)) = \ln(3)$
5. **Despeje:** $x = \frac{\ln(3)}{\ln(5) - \ln(2)}$
6. **Resultado final:** ✅ $x \approx 1.1989$
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
Practique la aplicación directa de logaritmos y el uso de la calculadora:
1. $5^x = 10$
2. $2^x = 7$
*Consejo: Aplique $\ln$ en ambos lados y despeje $x$ dividiendo los logaritmos.*
```

```ad-abstract
title: 🟡 Medio
Resuelva aplicando la distribución y el factor común:
1. $2^{2x} = 5^{1-2x}$

**Instrucciones clave:**
- No olvide los paréntesis al bajar $(1-2x)$.
- Agrupe todos los términos con $x$ en un solo lado antes de factorizar.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
Contexto: Determine el valor de $x$ para que la siguiente igualdad financiera se cumpla:
1. $3 \cdot 2^x = 5 \cdot 3^x$

**Pasos sugeridos:**
1. Aplique $\ln$ y separe los productos iniciales usando la suma de logaritmos.
2. Baje los exponentes $x$.
3. Organice la ecuación para que los términos con $x$ queden juntos y factorice.
```

> [!tip] 💡 Consejo de estudio
> **¡La verificación es tu mejor amiga!** Como recomienda el "Profe Alex", siempre reemplaza tu resultado decimal en la ecuación original usando tu calculadora. Si ambos lados de la igualdad dan resultados casi idénticos (por ejemplo, en el Ejemplo B verás que $6.88 \approx 6.88$), ¡puedes estar seguro de que tu proceso es excelente! Ten en cuenta que pequeñas variaciones en los últimos decimales son normales por el redondeo.