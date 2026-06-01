# Clase 06 — Teorema del Coseno: Hallar un Lado

tags: #algebra #cosinetheorem
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 6 de 9

[!info] 🧭 Navegación
« [[Clase 05 — Ley del Seno]] | [[00 - Índice del curso]] | [[Clase 07 — Teorema del Coseno: Hallar un Ángulo]] »

---

[!info] 🌍 Relevancia y aplicaciones
El Teorema del Coseno es una de las herramientas más potentes de la trigonometría. Se utiliza para resolver **triángulos oblicuángulos**, que es simplemente el nombre técnico para los triángulos que no tienen un ángulo de 90° (no son rectángulos).

*   **💵 [Aplicación USD]:** Determinar el costo exacto de cercar un terreno con forma de "rebanada de pizza" donde conoces el largo de dos lados y la apertura del ángulo entre ellos.
*   **🏗️ [Aplicación Práctica]:** En arquitectura, permite calcular la longitud de vigas de soporte en techos inclinados donde los ángulos no son rectos.
*   **📊 [Situación Cotidiana]:** En navegación, si dos aviones parten de un mismo aeropuerto y conoces sus rumbos y distancias recorridas, el Teorema del Coseno te da la distancia exacta que los separa.

---

[!note] 📌 ¿Qué es el Teorema del Coseno?
Es una fórmula que permite encontrar un lado desconocido cuando tenemos un "sándwich" de información: conocemos un lado, el ángulo, y el otro lado (**Caso LAL**). También es la herramienta clave cuando conocemos los tres lados y queremos encontrar los ángulos (**Caso LLL**).

[!warning] ⚠️ El "Atrapa-Errores" del Experto
1.  **La trampa de la calculadora:** Para que el resultado sea correcto, tu calculadora DEBE estar en modo **DEG** (grados). Además, al calcular la raíz cuadrada de toda la fórmula, **debes abrir un paréntesis al inicio y cerrarlo al final**; de lo contrario, la calculadora solo aplicará la raíz al primer número. 
    *   ❌ `sqrt 12^2 + 7^2...`
    *   ✅ `sqrt(12^2 + 7^2 - 2*12*7*cos(40))`
2.  **Uso incorrecto:** No lo uses si tienes una "pareja" conocida (un lado y su ángulo opuesto). Para eso, la Ley del Seno es mucho más rápida.

[!tip] 💡 El "Hermano Mayor" de Pitágoras
Si te fijas bien, la fórmula empieza igual que el Teorema de Pitágoras ($a^2 = b^2 + c^2$). El resto de la fórmula ($- 2bc \cos A$) es simplemente un "ajuste" matemático que hacemos porque el triángulo no tiene un ángulo de 90°.

---

### Procedimiento para hallar un lado

Para resolver estos ejercicios de forma profesional y sin errores, sigue estos pasos:

```yaml
PASO 1: Identificar y nombrar. Ángulos en MAYÚSCULAS (A, B, C) y 
        lados opuestos en minúsculas (a, b, c).
PASO 2: Verificar el caso LAL (Lado-Ángulo-Lado). El ángulo debe 
        estar entre los dos lados conocidos.
PASO 3: Plantear la fórmula maestra:
        a² = b² + c² - 2bc * cos(A)
PASO 4: Despejar usando raíz cuadrada. No olvides los paréntesis 
        globales en la calculadora y verificar el modo "DEG".
```

---

### Ejemplos Prácticos

[!example] Ejemplo 1: Aplicación Básica (LAL)
**Problema:** En un triángulo, el lado $b = 12m$, $c = 7m$ y el ángulo comprendido $A = 40^\circ$. Halla el lado $a$.
1.  **Fórmula:** $a = \sqrt{12^2 + 7^2 - 2(12)(7) \cdot \cos(40^\circ)}$
2.  **Cálculo:** $a = \sqrt{144 + 49 - 168 \cdot \cos(40^\circ)}$
3.  **Resultado:** $a \approx 8.01m$

[!example] Ejemplo 2: Precisión en Lado Desconocido
**Problema:** Un triángulo tiene lados de $19m$ y $9m$ con un ángulo intermedio de $65^\circ$.
1.  **Fórmula:** $x = \sqrt{19^2 + 9^2 - 2(19)(9) \cdot \cos(65^\circ)}$
2.  **Cálculo:** $x = \sqrt{361 + 81 - 342 \cdot \cos(65^\circ)}$
3.  **Resultado:** $x \approx 17.25m$
*(Nota pedagógica: El resultado es lógico, ya que 17.25m es menor que el lado más largo de 19m en este tipo de apertura).*

[!example] Ejemplo 3: Hallar un Ángulo (Check de Seguridad)
**Problema:** Dados los lados $a = 6, b = 14, c = 11$, halla el ángulo $A$.
1.  **Fórmula inversa:** $A = \arccos\left(\frac{a^2 - b^2 - c^2}{-2bc}\right)$
2.  **Sustitución:** $A = \arccos\left(\frac{6^2 - 14^2 - 11^2}{-2 \cdot 14 \cdot 11}\right)$
3.  **Resultado:** $A \approx 24.17^\circ$
4.  **Check de Seguridad:** Como $a=6$ es el lado más pequeño, el ángulo $A$ debe ser el más pequeño del triángulo. Este paso es vital para confirmar que nuestra solución es coherente.

[!example] Ejemplo 4: Presupuesto USD (Caso Real)
**Problema:** Se requiere un cable tensor para unir dos postes. Los cables de apoyo miden $15m$ y $20m$ con un ángulo de $50^\circ$ entre ellos. Si el cable cuesta $\$5.50$ USD por metro, ¿cuál es el costo total?
1.  **Hallar lado:** $x = \sqrt{15^2 + 20^2 - 2(15)(20) \cdot \cos(50^\circ)} \approx 15.47m$
2.  **Presupuesto:** $15.47 \times 5.50 = 85.085$
3.  **Resultado:** El costo total es de **$\$85.09$ USD**.

---

### Ejercicios de Práctica

**🟢 Fácil (LAL)**
1. $b=5, c=8, A=60^\circ$. Hallar $a$.
2. $a=10, b=10, C=60^\circ$. Hallar $c$. (Pista: ¡Mira el ángulo!)
3. $a=7, c=4, B=45^\circ$. Hallar $b$.
4. $b=12, c=15, A=30^\circ$. Hallar $a$.

**🟡 Medio (Contextual)**
5. Dos barcos salen de un puerto; uno recorre $12km$ y otro $18km$ con un ángulo de $100^\circ$ entre ellos. ¿Qué distancia hay entre los barcos?
6. En un triángulo con lados de $25cm$ y $30cm$ y un ángulo de $40^\circ$ entre ellos, halla el tercer lado.
7. $a=50m, b=60m, C=20^\circ$. Hallar $c$.
8. $b=100, c=150, A=120^\circ$. Hallar $a$.

**🔴 Avanzado (Presupuestos USD)**
9. Se cerca un jardín con lados de $20m$ y $30m$ y un ángulo de $70^\circ$. Si la valla cuesta $\$12$ USD/metro, ¿cuánto cuesta el tercer lado?
10. Se fabrica un panel triangular de metal con lados de $4m$ y $6m$ y un ángulo de $50^\circ$. Hallar el perímetro total para cotizar materiales.
11. Un cable de alta tensión conecta dos torres; los brazos miden $80m$ y $120m$ con un ángulo de $45^\circ$. Si el cable cuesta $\$2.50$ USD/metro, halla el costo del cableado.
12. Un terreno agrícola tiene lados de $15m$ y $25m$ con un ángulo de $80^\circ$. El cerramiento cuesta $\$15$ USD por metro. ¿Cuál es el presupuesto para el lado faltante?

#### ✅ Respuestas
*   **Fácil:** 1) 7 | 2) 10 | 3) 4.97 | 4) 7.52
*   **Medio:** 5) 23.23 km | 6) 19.34 cm | 7) 21.41 m | 8) 217.94
*   **Avanzado:** 9) $352.44 USD | 10) Perímetro $\approx 14.60m$ | 11) $212.50 USD ($a \approx 85.00m$) | 12) $402.45 USD ($a \approx 26.83m$)

---

### Autoevaluación y Cierre

[!question] ¿Cuándo es estrictamente necesario usar el Teorema del Coseno?
> **Respuesta:** Cuando el triángulo es oblicuángulo (no tiene ángulos de 90°) y conocemos los casos LAL (Lado-Ángulo-Lado) o LLL (Tres lados). Si hay un ángulo recto, Pitágoras es más eficiente.

[!question] Intuición Geométrica: Si $a=10, b=10$ y el ángulo $C=60^\circ$, ¿cuánto vale $c$ sin usar la calculadora?
> **Respuesta:** Vale 10. Al tener dos lados iguales y un ángulo de $60^\circ$ entre ellos, los otros ángulos también deben ser de $60^\circ$, formando un triángulo **equilátero**.

[!question] Un lado calculado mide $15.5m$ y el costo del material es de $\$10.00$ USD por metro. ¿Cuál es el presupuesto?
> **Respuesta:** $\$155.00$ USD. Simplemente multiplicamos la longitud por el precio unitario.

**Tip para la próxima clase:** Veremos la **Ley del Seno**. Recuerda esta regla de oro: Si el problema te da una "pareja" (un lado y su ángulo opuesto), usa la Ley del Seno. Si te da un "sándwich" (Lado-Ángulo-Lado), el Coseno es tu mejor amigo.

[!info] 🧭 Navegación
« [[Clase 05 — Ley del Seno]] | [[00 - Índice del curso]] | [[Clase 07 — Teorema del Coseno: Hallar un Ángulo]] »