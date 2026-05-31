# 📖 Guía de estudio — Clase 04: Regla de la Suma y Unión de Sucesos

¡Qué tal amigas y amigos! Espero que estén muy bien. En esta guía vamos a dominar la **Regla de la Suma**, que es el truco maestro para calcular probabilidades cuando un evento **O** el otro pueden ocurrir, ¡sin caer en la trampa de contar dos veces lo mismo!

> [!info] 📌 Conceptos clave
> - **Unión de sucesos:** Se identifica cuando buscamos la probabilidad de que ocurra un evento "A" **O** un evento "B". La conectiva **"O"** es tu señal de alarma para saber que debes usar la unión.
> - **Excluyentes vs. No excluyentes:** 
> 	- **Excluyentes:** No pueden pasar al mismo tiempo (como que un número sea par e impar a la vez). 
> 	- **No excluyentes:** Tienen "elementos que juegan en los dos equipos" (hay una intersección).
> - **Evitar el doble conteo:** ¡Cuidado con este punto! Si los sucesos tienen elementos en común, al sumarlos individualmente estarás contando la intersección dos veces. Por eso, la fórmula general nos pide restarla una vez.
> - **Tres formas de representar el resultado:** Recuerda que una probabilidad se puede escribir como **Fracción** (9/10), **Decimal** (0.9) o **Porcentaje** (90%). ¡Cualquiera de las tres es válida!

## 2. Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Sucesos mutuamente excluyentes** | Aquellos donde la ocurrencia de uno imposibilita la del otro (intersección vacía). |
| **Sucesos NO excluyentes** | Aquellos que tienen elementos en común. Decimos que su intersección no es vacía. |
| **Regla de la suma (General)** | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| **Regla de la suma (Excluyentes)** | $P(A \cup B) = P(A) + P(B)$ |

## 3. Ejemplos Resueltos Adicionales

````ad-example
**Ejemplo A — Café y Revistas**
En la sala de espera de un consultorio, el 60% de los pacientes toma café, el 50% lee revistas y el 20% hace ambas cosas. ¿Cuál es la probabilidad de que un paciente tome café **O** lea revistas?

**Paso a paso:**
1. **Identificar datos:** $P(C) = 60\%$, $P(R) = 50\%$.
2. **Identificar la intersección:** El 20% hace ambas cosas ($P(C \cap R) = 20\%$).
3. **Aplicar la fórmula:** 
   - $P = 60\% + 50\% - 20\%$
   - $P = 110\% - 20\% = 90\%$

**Resultado:** La probabilidad es del **90%** (o 0.9 en decimal).
````

````ad-example
**Ejemplo B — Presupuesto de Transporte**
Una empresa analiza el uso de transporte para sus empleados: el 70% usa servicio público ($P$), el 55% usa transporte particular ($M$) y el 40% alterna entre ambos.

**Resolución siguiendo la lógica de la Regla de la Suma:**
Para saber qué porcentaje de empleados usa al menos un medio de transporte, aplicamos la fórmula general:
- $P(P \cup M) = P(P) + P(M) - P(P \cap M)$
- $P(P \cup M) = 70\% + 55\% - 40\%$
- $P(P \cup M) = 125\% - 40\% = 85\%$

**Resultado:** El **85%** de los empleados utiliza algún transporte.
````

## 4. Ejercicios de Repaso

````ad-abstract
**🟢 Fácil — El Dado Matemático**
Considerando el lanzamiento de un dado estándar de 6 caras:
1. ¿Cuál es la probabilidad de obtener un número **par O impar**?
2. ¿Cuál es la probabilidad de obtener un número **menor a 3 O mayor a 5**?
3. ¿Cuál es la probabilidad de obtener un **2 O un número par**? (¡Ojo! El 2 ya es par, identifica la intersección).
````

````ad-abstract
**🟡 Medio — La Tienda de Mascotas**
En una tienda hay un total de **13 mascotas**. Según el conteo del Profe Alex, tenemos: **7 gatos** (2 de ellos blancos) y **4 perros** (2 de ellos blancos). El resto son otros animales.
1. ¿Cuál es la probabilidad de elegir un animal que sea **gato O blanco**?
2. ¿Cuál es la probabilidad de elegir un animal que sea **perro O blanco**?
3. ¿Cuál es la probabilidad de elegir un animal que sea **gato O perro**? 
*Nota: Si notas que 7 gatos + 4 perros no suman 13, es porque hay 2 animales de otra especie que no entran en estas categorías.*
````

````ad-abstract
**🔴 Avanzado — Decisión Financiera ($USD)**
Imagina que eres el administrador de la comunidad del Ejemplo B (Transporte). La población total es de **1,000 personas**. El gobierno decide otorgar un bono de transporte de **$100 USD** a cada ciudadano que utilice transporte público **O** particular.
1. Basándote en la probabilidad de la unión calculada (85%), ¿cuántas personas se estima que recibirán el bono?
2. ¿Cuál debe ser el presupuesto total en dólares ($USD) que el gobierno debe asegurar para cubrir exactamente a esa población?
3. ¿Sería correcto asignar un presupuesto para el 100% de la población? Justifica usando la probabilidad de la unión.
````

## 5. Consejo de Estudio

> [!tip] 💡 El "Tip de Oro": Empieza por el centro
> Como dice el Profe Alex, para no equivocarte nunca, usa un **Diagramas de Venn** y sigue este secreto: **¡Pon siempre el número de la intersección primero!**
> 1. Dibuja los dos círculos.
> 2. Escribe el valor de los que cumplen ambas condiciones en el centro (la intersección).
> 3. Para completar el resto de cada círculo, resta ese valor central de los totales individuales. 
> Visualizarlo así te hará entender por qué la fórmula resta la intersección: ¡para que no cuentes a las mismas personas dos veces!