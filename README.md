# Prediccion-del-riesgo-cardiovascular
Proyecto de Machine Learning para desarrollar un modelo que prediga la probabilidad de sufrir una patología cardíaca, a partir de los datos recogidos en la encuesta de salud anual realizada por Behavioral Risk Factor Surveillance System (BRFSS).

# 1.-. Introducción

Hoy en día las encuestas de salud son una parte fundamental del sistema de salud de cualquier país, y ayudan a la toma de decisiones relativas a las políticas de salud. La información que proporcionan se divide en dos grandes apartados:
- Estado de salud
Se refiere a la autovaloración de la salud, restricción de la actividad, discapacidad y dependencia, salud mental, calidad de vida relacionada con la salud, y enfermedades crónicas.
- Determinantes de salud
En este apartado se recogen las condiciones socioeconómicas de vida y de trabajo, ingresos, situación económica, trabajo doméstico y de cuidado, entorno de la vivienda, discriminación o factores psicosociales. 

### 1.1.- Objetivos y alcance del proyecto

Este proyecto se basa en los datos extraídos de la encuesta de salud que elabora anualmente el Behavioral Risk Factor Surveillance System (BRFSS), para recopilar datos sobre la salud de los residentes en EE.UU.

Según  CDC (Centers for Disease Control and Prevention), las cardiopatías son una de las principales causas de muerte en la mayoría de las razas de EE.UU. (afroamericanos, indios americanos y nativos de Alaska, y blancos). Aproximadamente la mitad de los estadounidenses (47%) presentan al menos 1 de los 3 factores de riesgo clave de las cardiopatías: hipertensión, colesterol alto y tabaquismo. Otros indicadores clave son la diabetes, la obesidad (IMC elevado), no realizar suficiente actividad física o la ingesta de alcohol. Detectar y prevenir los factores que más influyen en las cardiopatías es muy importante en la asistencia sanitaria. 

Los avances informáticos permiten aplicar métodos de Machine Learning, para detectar patrones a partir de los datos recogidos en las encuestas de salud, que pueden predecir el estado de un paciente. En este caso, el objetivo del proyecto es diseñar un modelo de Machine Learning que pueda predecir la probabilidad de sufrir una afección cardíaca, por medio de modelos supervisados de Machine Learning, ya que tenemos una variable target para cada muestra, denominada *HeartDisease*.

# 2.- Dataset

### 2.1.- Dataset utilizado

El dataset que se estudia en este proyecto corresponde a la encuesta realizada por el BRFSS en 2020. Tiene en total 320.000 filas y 18 columnas, que corresponden a las respuestas dadas por los ciudadanos a las preguntas efectuadas. Las variables consideradas son:
- *HeartDisease*: Variable categórica con valor Sí/No. Se refiere a sufrir o haber sufrido una enfermedad coronaria o un infarto de miocardio. Esta es la variable target que hay que predecir en el estudio.
- *BMI*. Indice de masa corporal. Variable continua, se obtiene dividiendo el peso de la persona, en kg, entre su estatura, expresada en metros, elevada al cuadrado. 
- *Smoking*: Variable categórica, con valor Sí/No, respondiendo a la pregunta: ¿Ha fumado al menos 100 cigarrillos a lo largo de su vida?
- *AlcoholDrinking*: Variable categórica, con valor Sí/No, para detectar a los "Heavy Drinkers", hombres que toman más de 14 bebidas alcohólicas a la semana o 7 en el caso de las mujeres.
- *Stroke*: Variable categórica con valor Sí/No respondiendo a ¿Ha sufrido alguna vez un accidente cerebrovascular?
- PhysicalHealth: Respuesta con valor numérico a la pregunta:¿Durante cuantos días de los últimos 30 no ha tenido buena salud física?
- *MentalHealth*: Respuesta con valor numérico a la pregunta:¿Durante cuantos días de los últimos 30 no ha tenido buena salud mental?
- *DiffWalking*: Variable categórica con valor Sí/No, cuya pregunta era: ¿Tiene dificultades para andar o subir escaleras?
- *Sex*. Variable nominal, con valor Hombre/Mujer.
- *AgeCategory*: Variable ordinal referida a un intervalo de edad.
- *Race*: Variable nominal, referida al grupo étnico del encuestado.
- *Diabetic*: Variable categórica con valor Sí/No respondiendo a: ¿Ha tenido alguna vez diabetes?
- *PhysicalActivity*: Respuesta SÍ/No a la pregunta ¿Ha realizado algún ejercicio físico aparte del trabajo en los últimos 30 días?
- *GenHealth*: Variable ordinal como respuesta a: Diría que su salud en general es... 
- *SleepTime*: Variable numérica, para expresar el número de horas diarias de sueño
- *Asthma*: Variable categórica con valor Sí/No respondiendo a: ¿Es asmático?
- *KidneyDisease*: Variable categórica con valor Sí/No respondiendo a: Sin incluir cálculos renales, infección de vejiga o incontinencia, ¿le han diagnosticado alguna vez una enfermedad renal?
- *SkinCancer*: Variable categórica con valor Sí/No respondiendo a: ¿Ha tenido o tiene cáncer de piel?
