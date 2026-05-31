# 📋 Planificación Didáctica — Axiomas de Probabilidad y Regla de Laplace

## 1. Tema
**Axiomas de Probabilidad y Regla de Laplace**  
Esta sesión tiene como objetivo fundamental la transición del pensamiento intuitivo hacia el rigor estadístico. A través de la axiomatización, el estudiante comprenderá que la probabilidad no es un cálculo aislado, sino una estructura lógica que define eventos imposibles ($P=0$), probables ($0 < P < 1$) y seguros ($P=1$), basándose en el análisis sistemático del espacio muestral.

## 2. Metodología
**Aprendizaje Colaborativo Formal**  
Los estudiantes se organizan en grupos pequeños con roles específicos que dinamizan la tarea matemática:
- **Facilitador:** Valida que los eventos analizados cumplan con las condiciones de los axiomas (ej. verificar si son mutuamente excluyentes).
- **Secretario:** Registra formalmente las fracciones y cálculos empleando la notación de Laplace.
- **Gestor de Materiales:** Manipula los dados y "caramelos" para garantizar que la simulación física sea fiel al espacio muestral.
- **Portavoz:** Expone la lógica detrás de la resolución ante el pleno.

## 3. Secuencia Didáctica

### 🔵 ANTICIPACIÓN — 20 min
> [!abstract] Actividad de inicio: El Dado de la Certeza
> Se presenta un dado estándar de seis caras ($S = \{1, 2, 3, 4, 5, 6\}$). Los grupos deben predecir resultados para introducir formalmente los primeros pilares de la probabilidad:
> 1. **Axioma de Positividad:** Se solicita la probabilidad de obtener un 10. Al ser un evento imposible ($0/6$), se define que $P(A) \geq 0$; nunca existen probabilidades negativas.
> 2. **Axioma de Certidumbre:** Se solicita la probabilidad de obtener un número menor a 7. Al coincidir con todo el espacio muestral ($6/6$), se define que $P(S) = 1$.
> 3. **Escala de Probabilidad:** Se discute por qué cualquier resultado probable debe ser una fracción propia donde el numerador nunca supera al denominador.

> [!note] Enfoque DUA
> - **Qué:** Activación de conocimientos previos sobre la escala de 0 a 1.
> - **Cómo:** Discusión dirigida y anotación en pizarra de predicciones grupales.
> - **Por qué:** Proporcionar una base lógica y visual antes de la abstracción algebraica.

---

### 🟡 CONSTRUCCIÓN — 40 min
> [!example] Actividades centrales: Estaciones de Experimentación
> **Estación 1: Laplace y Axioma de Aditividad**
> Utilizando dados, los estudiantes calculan probabilidades simples mediante la Regla de Laplace: $P(A) = \frac{\text{Casos favorables}}{\text{Casos posibles}}$.
> - **Reto de Aditividad:** Deben calcular $P(\text{Par} \cup \text{Impar})$. Al ser eventos mutuamente excluyentes (un número no puede ser ambos), deben demostrar que $P(A \cup B) = P(A) + P(B) = 3/6 + 3/6 = 1$.
> 
> **Estación 2: Probabilidad Condicional y Urna Física**
> El **Gestor de Materiales** organiza una urna con 10 esferas (caramelos): **6 azules** y **4 rojas**. Dentro de las azules, **4 tienen números pares** y **2 impares**.
> - **Reto:** "Se extrae una esfera y se sabe que es **azul**. ¿Cuál es la probabilidad de que sea **par**?".
> - **Lógica Pedagógica:** Los estudiantes deben primero "reducir el espacio muestral" (ignorar las rojas y trabajar solo con las 6 azules).
> - **Formalización:** El **Secretario** aplica la fórmula $P(\text{Par}|\text{Azul}) = \frac{P(\text{Par} \cap \text{Azul})}{P(\text{Azul})} = \frac{4/10}{6/10} = 4/6$. Se comparará la reducción lógica visual con el resultado de la fórmula.

> [!note] Enfoque DUA
> - **Qué:** Aplicación de la Regla de Laplace y comprensión de la dependencia de eventos.
> - **Cómo:** Uso de material concreto (caramelos) para representar físicamente la reducción del espacio muestral.
> - **Por qué:** Ofrecer múltiples medios de representación (el objeto físico frente a la fórmula general).

---

### 🟢 CONSOLIDACIÓN — 20 min
> [!success] Actividad de cierre: El Reto de la Intersección (No Excluyente)
> Se plantea un problema de encuesta escolar basado en datos del Source Context:
> - **Datos:** El **40%** de estudiantes practica fútbol ($P(F)=0.40$), el **50%** baloncesto ($P(B)=0.50$) y el **15%** practica ambos ($P(F \cap B)=0.15$).
> - **Tarea:** Calcular la probabilidad de que un estudiante practique fútbol **o** baloncesto ($P(F \cup B)$).
> - **Requisito Visual:** Los grupos deben construir un **Diagrama de Venn** y una **Tabla de Contingencia** para visualizar por qué se resta la intersección ($0.40 + 0.50 - 0.15 = 0.75$). Deben identificar que sin la resta, se estaría cometiendo un error de "doble conteo" de los 15 estudiantes que integran ambos conjuntos.

> [!note] Enfoque DUA
> - **Qué:** Síntesis de los Axiomas (Suma y Complemento).
> - **Cómo:** Socialización mediante la creación de diagramas en la pizarra.
> - **Por qué:** Fomentar la expresión y comunicación mediante organizadores gráficos.

---

## 4. Recursos

| Recurso | Tipo | Uso en la clase |
| :--- | :--- | :--- |
| **Pizarra y Marcadores** | Físico | Modelado de Diagramas de Venn y resolución de tablas de contingencia. |
| **Fichas Impresas** | Material | Guías con problemas de Laplace y axiomas para el trabajo en estaciones. |
| **Dados** | Físico | Demostración de los axiomas de positividad, certidumbre y eventos excluyentes. |
| **Caramelos de colores** | Físico | Representación de la urna (6 azules/4 rojas) para la probabilidad condicional. El **Gestor de Materiales** los utiliza para simular la extracción y reducción del espacio muestral. |
| **Calculadora** | Tecnológico | Verificación de conversiones de fracciones a decimales y porcentajes. |