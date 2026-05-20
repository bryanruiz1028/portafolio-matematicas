# 📖 Guía de estudio — Clase 07: Jerarquía de Operaciones

> [!info] 📌 Conceptos clave
> ¡Bienvenido, estudiante! Resolver operaciones combinadas es como seguir una receta de cocina: si alteras el orden de los pasos, el resultado final no será el esperado. Para dominar este tema, debemos basarnos en tres pilares fundamentales:
> 
> 1.  **Orden Jerárquico Estricto:** Nunca resuelvas simplemente de izquierda a derecha. Sigue siempre este camino:
>     *   **1.°** Operaciones dentro de **Signos de Agrupación**.
>     *   **2.°** **Potencias y Raíces**.
>     *   **3.°** **Multiplicaciones y Divisiones**.
>     *   **4.°** **Sumas y Restas**.
> 2.  **Separar en términos:** Es el "secreto profesional" para no perderse. Los signos $+$ y $-$ que están **fuera** de paréntesis o raíces actúan como muros que dividen el ejercicio en "mini-problemas" independientes.
> 3.  **Lógica de Signos (¡Atención aquí!):**
>     *   **En Multiplicación/División:** Aplicamos la ley: signos iguales dan positivo $(+)$; signos diferentes dan negativo $(-)$.
>     *   **En Suma/Resta:** Olvida la ley anterior. Usamos la lógica financiera de **"debo y tengo"**. Si debo $10$ ($-10$) y tengo $2$ ($+2$), mi saldo es deudor: $-8$.
> 4.  **Multiplicación "Invisible":** Recuerda que un número o un signo pegado a un paréntesis (sin un $+$ o $-$ de por medio) indica que debes multiplicar lo de afuera por lo de adentro. Ejemplo: $4(2) = 8$.

## 📋 Fórmulas y definiciones importantes

| Concepto | Definición y Regla de Oro |
| :--- | :--- |
| **Signos de Agrupación** | Orden de eliminación: se resuelve de adentro hacia afuera, empezando por Paréntesis $()$, luego Corchetes $[]$ y finalmente Llaves $\{\}$. |
| **Jerarquía de Operaciones** | $1^\circ$ Paréntesis, $2^\circ$ Potencias/Raíces, $3^\circ$ Multiplicación/División, $4^\circ$ Suma/Resta. |
| **Regla de Signos (Mult/Div)** | **Signos iguales:** resultado $(+)$. **Signos diferentes:** resultado $(-)$. |
| **La Regla del "Pegado"** | Un número o signo inmediatamente a la izquierda de un paréntesis indica multiplicación. |

## 💡 Ejemplos resueltos adicionales

> [!example] **Ejemplo A: Caso con potencias y raíces**
> **Ejercicio:** $3 + 2^2 \cdot 3^2 - \sqrt{16}$
> 
> ¡No te apresures! Primero identifiquemos los términos. Tenemos tres bloques separados por los signos $+$ y $-$. Resolvemos cada bloque respetando la jerarquía interna:
> 
> 1.  **Potencias y Raíces:**
>     $3 + \mathbf{4 \cdot 9} - \mathbf{4}$
> 2.  **Multiplicaciones:**
>     $3 + \mathbf{36} - 4$
> 3.  **Sumas y Restas finales:**
>     $\mathbf{39} - 4 = \mathbf{35}$
> 
> ✅ **Resultado final:** $35$.

> [!example] **Ejemplo B: Aplicación financiera ($USD)**
> **Contexto:** Imagina que tienes una deuda acumulada de $12$ cuotas mensuales y cada una tiene un valor de $\$49$ USD. ¿Cuál es tu situación financiera actual?
> 
> **Planteamiento:** $(-12) \cdot 49$
> 
> **Paso a paso:**
> 1.  **Análisis de signos:** Representamos la deuda como $-12$ (lo que debo) y el valor como $49$ (lo que se descuenta por cada cuota).
> 2.  **Multiplicación de signos:** El $12$ es negativo y el $49$ es positivo. Según la regla, signos diferentes dan negativo $(- \cdot + = -)$.
> 3.  **Cálculo numérico:** $12 \cdot 49 = 588$.
> 
> ✅ **Resultado final:** $-\$588$ USD. Esto significa que tienes un saldo negativo o deuda de $588$ dólares.

## ✍️ Ejercicios de repaso

> [!abstract] **🟢 Nivel Fácil: Jerarquía básica**
> 1. Calcule el resultado de: $3 + 5 \cdot 2$
> 2. Resuelva la siguiente operación con potencias: $10 + 2^3$
> 3. Determine el valor de: $3 \cdot 2^2$

> [!abstract] **🟡 Nivel Medio: Paréntesis y raíces**
> 1. Resuelva aplicando jerarquía: $-5 \cdot (-2) + 5^2$
> 2. Calcule: $15 + \sqrt{25} - 2 \cdot 3$
> 3. Elimine el paréntesis y resuelva: $2 \cdot (18 - 16) + 4$

> [!abstract] **🔴 Nivel Avanzado: Aplicación con $USD**
> 1. **Saldo final:** Tienes un crédito inicial de $\$15$ y restas los siguientes gastos agrupados: $-( -10 + 2 \cdot 5 )$. *(Pista: resuelve primero la multiplicación interna y recuerda que un signo pegado al paréntesis cambia los signos de adentro).*
> 2. **Cálculo de deuda:** Determina el valor final de la expresión: $-( -4 \cdot 6 ) + (-20)$.
> 3. **Operación financiera compleja:** Resuelve el saldo final aplicando el orden de eliminación de signos de agrupación: $-1 \cdot \{ -7 + [ 24 + 5 + 12 ] + 15 \}$.

> [!tip] 💡 Consejo de estudio
> La estrategia más poderosa para no confundirse es **"Separar en términos"**. Antes de escribir cualquier número, marca con un color los signos $+$ y $-$ que no estén atrapados dentro de paréntesis. Trata cada término como un mini-ejercicio independiente. Resuelve todo dentro de cada término hasta que solo quede un número, y solo entonces realiza las sumas y restas finales. ¡El orden es tu mejor aliado!