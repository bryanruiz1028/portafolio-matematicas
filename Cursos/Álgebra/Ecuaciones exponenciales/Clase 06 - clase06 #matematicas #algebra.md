#clase06 #matematicas #algebra

# Clase 06 — Resolución de ecuaciones exponenciales con logaritmos

[Anterior: Clase 05 — Ecuaciones con bases iguales] | [Siguiente: Clase 07 — Ecuaciones con bases distintas en ambos lados]

## Relevancia y aplicaciones
Cuando nos encontramos ante una ecuación donde las bases no pueden igualarse de forma exacta (como intentar convertir un 7 en potencia de 2), el uso de logaritmos es el único camino para despejar el **Exponente**.

*   💵 **Crecimiento de inversión ($USD):** Permite calcular con exactitud el tiempo ($x$ en años) necesario para duplicar un capital o alcanzar una meta de ahorro con interés compuesto.
*   🏗️ **Modelos científicos:** Esencial para calcular la antigüedad de fósiles mediante la desintegración de materiales o proyectar el crecimiento de poblaciones.
*   📊 **Situaciones cotidianas:** Útil para determinar en cuánto tiempo una cuenta de redes sociales alcanzará cierto número de seguidores si mantiene un ritmo de crecimiento constante.

---

## Concepto clave

> [!note] Definición
> La resolución con logaritmos se aplica cuando no existe un exponente entero que iguale las bases de la ecuación. Al aplicar un logaritmo a ambos lados de la igualdad, convertimos una ecuación exponencial en una ecuación lineal, aprovechando las propiedades que permiten transformar potencias en multiplicaciones.

> [!warning] Error común
> Nunca intentes aplicar logaritmos si hay términos sumando o restando fuera de la potencia (ejemplo: $3^x + 5 = 20$). Primero debes realizar el despeje para que la potencia quede aislada: $3^x = 15$. Solo entonces puedes aplicar el logaritmo.

> [!tip] Regla mnemotécnica: El logaritmo es el "ascensor"
> Imagina que el logaritmo abre las puertas de un ascensor para que el **Exponente** pueda bajar del piso superior y caminar por la planta baja como un factor multiplicador normal.

---

## Procedimiento paso a paso

```text
1. Aislar la potencia (si existen raíces, convertirlas primero a potencia fraccionaria).
2. Aplicar logaritmo (ln o log) a ambos miembros de la ecuación.
3. "Bajar" el exponente multiplicando al logaritmo (Propiedad de la potencia).
4. Despejar la variable "x" (usar Factorización si la "x" aparece en varios términos).
```

---

## Ejemplos de clase

### Ejemplo 1: Caso Básico
**Ecuación:** $2^x = 7$
1. Aplicamos **Logaritmo Natural** ($\ln$) a ambos lados: $\ln(2^x) = \ln(7)$.
2. Bajamos el **Exponente**: $x \cdot \ln(2) = \ln(7)$.
3. Despejamos $x$: $x = \frac{\ln(7)}{\ln(2)}$.
4. Resultado aproximado: **$x \approx 2,81$**.

✅ **Comprobación:** Si elevamos $2^{2,81}$ en la calculadora, obtenemos $\approx 7,01$, lo cual valida nuestro resultado.

### Ejemplo 2: Caso con Binomio
**Ecuación:** $3^{x+2} = 10$
1. Aplicamos $\ln$ en ambos miembros: $\ln(3^{x+2}) = \ln(10)$.
2. Bajamos el binomio (usando paréntesis): $(x+2) \cdot \ln(3) = \ln(10)$.
3. Pasamos el número $\ln(3)$ dividiendo: $x+2 = \frac{\ln(10)}{\ln(3)}$.
4. Despejamos restando 2: $x = \frac{\ln(10)}{\ln(3)} - 2$.
5. Resultado aproximado: **$x \approx 0,0959$**.

### Ejemplo 3: Caso Avanzado (Raíces y Factorización)
**Ecuación:** $3^{x+2} = \sqrt{5^x}$
1. Transformamos la raíz en **Exponente** fraccionario: $3^{x+2} = 5^{x/2}$.
2. Aplicamos **Logaritmo Común** ($\log$): $\log(3^{x+2}) = \log(5^{x/2})$.
3. Bajamos los exponentes: $(x+2)\log(3) = \frac{x}{2}\log(5)$.
4. Multiplicamos toda la ecuación por 2 para eliminar la fracción: $2(x+2)\log(3) = x\log(5)$.
5. **Distribución:** Multiplicamos el $2\log(3)$ por los términos del paréntesis: $2x\log(3) + 4\log(3) = x\log(5)$.
6. **Agrupación:** Pasamos los términos con $x$ a un lado: $2x\log(3) - x\log(5) = -4\log(3)$.
7. **Factorización:** Extraemos el factor común $x$: $x(2\log(3) - \log(5)) = -4\log(3)$.
8. Despeje final: $x = \frac{-4\log(3)}{2\log(3) - \log(5)}$.
9. Resultado aproximado: **$x \approx -7,476$**.

### Ejemplo 4: Aplicación financiera ($USD)
**Problema:** ¿Cuánto tiempo ($x$ en años) tarda una inversión en duplicarse si crece a una tasa del 5% anual, siguiendo la ecuación $1,05^x = 2$?
1. Aplicamos logaritmos: $\log(1,05^x) = \log(2)$.
2. Bajamos la incógnita: $x \cdot \log(1,05) = \log(2)$.
3. Despejamos: $x = \frac{\log(2)}{\log(1,05)}$.
4. Resultado: **$x \approx 14,2$ años**.

---

## Ejercicios para el estudiante

```ad-abstract
title: Nivel Verde (Fácil)
1. $5^x = 12$
   
2. $4^x = 10$
```

```ad-abstract
title: Nivel Amarillo (Medio)
3. $2^{x+3} = 15$
```

```ad-abstract
title: Nivel Rojo (Avanzado)
4. $3^{2x+1} - 5 = 16$ 
*(Pista: Primero suma 5 a ambos lados para aislar la potencia).*
```

```ad-success
title: Respuestas
1. $x \approx 1,544$
2. $x \approx 1,661$
3. $x \approx 0,907$
4. $x \approx 0,8856$
```

---

## Mini-prueba de autoevaluación

1. **¿Qué propiedad fundamental permite resolver ecuaciones donde las bases no se pueden igualar?**
   - a) Logaritmo de un producto.
   - b) Propiedad de la potencia ($\log(a^n) = n \cdot \log a$).
   - c) Logaritmo de la unidad.
   - d) Suma de logaritmos.

2. **Ante la ecuación $7^x = \sqrt{2}$, ¿por qué el primer paso debe ser convertir la raíz en potencia ($2^{1/2}$)?**
   - a) Porque los logaritmos no pueden calcular raíces.
   - b) Para "hablar el mismo lenguaje" de potencias y poder aplicar la propiedad de bajar el exponente.
   - c) Para eliminar el número 7.
   - d) Es un paso opcional que no afecta el resultado.

3. **Si una inversión sigue la ecuación $1,10^x = 2$, ¿cuál es el tiempo de duplicación?**
   - a) 5 años.
   - b) 10 años.
   - c) 7,27 años.
   - d) 20 años.

**Clave de respuestas:** 
1: **b** (Es la esencia del método: bajar la $x$).
2: **b** (Convertir a potencia fraccionaria es el requisito técnico para que el logaritmo actúe sobre el exponente).
3: **c** ($\frac{\log 2}{\log 1,10} \approx 7,27$). *Dato experto: No importa si usas log o ln, el cociente será siempre el mismo.*

---

> [!tip] Próxima clase
> En la Clase 07 aprenderemos a resolver el reto máximo: ecuaciones donde la incógnita aparece en ambos lados con bases distintas y potencias que requieren **Factorización** avanzada.

[Anterior: Clase 05 — Ecuaciones con bases iguales] | [Siguiente: Clase 07 — Ecuaciones con bases distintas en ambos lados]