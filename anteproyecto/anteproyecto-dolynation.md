![DolyNation](assets/logo-dolynation.png)

**Ingeniería en Desarrollo y Gestión de Software — 9° A TN**

# **DolyNation**

*Desarrollo de una plataforma web para el aprendizaje contextual de idiomas mediante inteligencia artificial, evaluación de comprensión por IA y análisis de vocabulario y gramática*

**Integrantes**  
Jesús Alberto Villarreal Pérez  
Juan Antonio Deras Durón  
Sebastián Rodríguez Contreras  
Aozmar Azael García Candela  
José Elías Galarza Pedroza

*Torreón, Coahuila — 07/09/202*

# **Índice**

- [1. Título del proyecto](#1-t%C3%ADtulo-del-proyecto)
- [2. Planteamiento del problema](#2-planteamiento-del-problema)
- [3. Justificación](#3-justificaci%C3%B3n)
- [4. Objetivo general](#4-objetivo-general)
- [5. Objetivos específicos](#5-objetivos-espec%C3%ADficos)
- [6. Alcance del proyecto](#6-alcance-del-proyecto)
  - [Registro y autenticación](#registro-y-autenticaci%C3%B3n)
  - [Selección de idioma](#selecci%C3%B3n-de-idioma)
  - [Contenido por niveles](#contenido-por-niveles)
  - [Lecturas](#lecturas)
  - [Comprensión lectora](#comprensi%C3%B3n-lectora)
  - [Análisis contextual de vocabulario mediante inteligencia artificial](#an%C3%A1lisis-contextual-de-vocabulario-mediante-inteligencia-artificial)
  - [Sistema de rachas](#sistema-de-rachas)
  - [Seguimiento del progreso](#seguimiento-del-progreso)
- [7. Limitaciones](#7-limitaciones)
- [8. Producto Mínimo Viable (MVP).](#8.-producto-m%C3%ADnimo-viable-(mvp).)
- [9. Requerimientos funcionales y no funcionales](#9.-requerimientos-funcionales-y-no-funcionales)
  - [9.1. Requerimientos funcionales](#9.1.-requerimientos-funcionales)
  - [9.2. Requerimientos no funcionales](#9.2.-requerimientos-no-funcionales)
  - [10. Análisis de riesgo](#10.-an%C3%A1lisis-de-riesgo)
- [11. Elección de metodología y roles del equipo](#11.-elecci%C3%B3n-de-metodolog%C3%ADa-y-roles-del-equipo)
  - [12. Separación del proyecto en tareas](#12.-separaci%C3%B3n-del-proyecto-en-tareas)
- [14. Elección de estructura web y tecnologías.](#14.-elecci%C3%B3n-de-estructura-web-y-tecnolog%C3%ADas.)
- [16. Selección de patrones de diseño.](#16.-selecci%C3%B3n-de-patrones-de-dise%C3%B1o.)
  - [17. Wireframes.](#17.-wireframes.)
  - [18. Fuentes.](#18.-fuentes.)

# **1\. Título del proyecto**

DolyNation: desarrollo de una plataforma web para el aprendizaje de idiomas mediante contenido contextual asistido por inteligencia artificial, evaluación de comprensión mediante resúmenes calificados por IA y análisis de vocabulario y gramática.

# **2\. Planteamiento del problema**

En los últimos años, las plataformas digitales para el aprendizaje de idiomas se han consolidado como una de las principales alternativas de estudio, apoyándose predominantemente en mecánicas de gamificación, como puntos, niveles, rachas y recompensas, para sostener la motivación del usuario.

Sin embargo, al concentrar su metodología en dinámicas de juego, estas plataformas relegan a segundo plano el **desarrollo real del vocabulario y la comprensión del idioma**. Este enfoque resulta funcional en etapas iniciales, pero insuficiente para usuarios con conocimientos previos o nivel intermedio.

Una limitación central es la **enseñanza del vocabulario de forma descontextualizada**: aprender una palabra de manera aislada no garantiza su uso correcto, ya que su significado varía según la oración, el contexto y la estructura gramatical en la que se emplea.

A esto se suma la naturaleza efímera del contenido, como lecciones breves y ejercicios repetitivos, que limita la profundidad del aprendizaje. Los usuarios con mayor tiempo de práctica tienden a alcanzar un **techo de aprendizaje**, donde los ejercicios disponibles dejan de representar un desafío, generando estancamiento.

# **3\. Justificación**

El dominio de un idioma requiere el desarrollo integrado de **comprensión lectora, vocabulario, gramática y capacidad de interpretación contextual**.

Los métodos tradicionales, basados en ejercicios independientes, permiten memorizar reglas y palabras sin garantizar su aplicación correcta en situaciones reales, generando un **techo de aprendizaje** que un segmento considerable de usuarios de nivel básico-intermedio no logra superar pese a una práctica prolongada.

DolyNation aborda esta limitación utilizando **el texto como unidad central de aprendizaje**. El usuario selecciona manualmente su nivel sin examen de diagnóstico y accede a **contenido generado por IA** que vincula vocabulario y gramática a su contexto real de uso.

La comprensión se evalúa mediante **resúmenes redactados por el usuario y calificados por inteligencia artificial**, en lugar de preguntas estructuradas, lo que ofrece una evaluación más fiel a su nivel real.

Como complemento, el sistema incorpora un esquema de **puntuación, progreso y rachas de uso** que aporta un componente de motivación sin desplazar al contenido educativo como eje central de la experiencia.

De esta manera, DolyNation se posiciona como una **herramienta complementaria** orientada a usuarios que buscan superar las limitaciones de las aplicaciones tradicionales, integrando **vocabulario, gramática y comprensión lectora** en una sola propuesta de valor.

# 

# 

# **4\. Objetivo general**

Desarrollar DolyNation, una plataforma web de aprendizaje inmersivo que garantice la adquisición progresiva del inglés, francés, español e italiano a través de niveles modulares personalizables, contenido situado generado con asistencia de IA, evaluación automática de la comprensión lectora basada en resúmenes puntuados por procesamiento de lenguaje natural, análisis morfosintáctico y semántico, y un tablero integral de métricas de rendimiento y trazabilidad formativa.

# **5\. Objetivos específicos**

1. Implementar un sistema de registro y autenticación de usuarios que permita gestionar de forma segura el acceso a la plataforma y la información asociada a cada usuario.  
2. Desarrollar un sistema de personalización del aprendizaje que permita al usuario establecer el idioma, temas de interés y nivel de dificultad —bajo, medio y alto— de acuerdo con sus preferencias y necesidades.  
3. Desarrollar un sistema de generación de contenido educativo personalizado que utilice las preferencias configuradas por el usuario para producir contenidos acordes con su proceso de aprendizaje.  
4. Incorporar mecanismos de retroalimentación durante el proceso de aprendizaje, proporcionando información sobre el desempeño del usuario y elementos que contribuyan a reforzar la comprensión de los contenidos.  
5. Implementar un sistema de seguimiento del aprendizaje que permita registrar y consultar el progreso, resultados e historial de actividades realizadas por el usuario.  
6. Incorporar un sistema de continuidad y motivación del aprendizaje mediante el registro de rachas de actividad, con el propósito de visualizar y reforzar la constancia del usuario dentro de la plataforma.  
7. Diseñar e implementar una interfaz web intuitiva y accesible que facilite la navegación entre las funcionalidades, contenidos educativos, resultados y herramientas disponibles en la plataforma.

# **6\. Alcance del proyecto**

El proyecto contempla el desarrollo de una aplicación web orientada al aprendizaje de idiomas. La primera versión contará con los siguientes componentes principales:

## **Registro y autenticación**

El usuario podrá crear una cuenta e iniciar sesión para conservar su progreso y resultados.

## **Selección de idioma**

El usuario podrá seleccionar el idioma que desea estudiar. La primera versión contempla:

> * Inglés.  
> * Francés.  
> * Español.  
> * Italiano.

## **Contenido por niveles**

Los textos están clasificados con tres diferentes niveles de dificultad. La implementación inicial podrá concentrarse en los niveles que resulten más viables durante el desarrollo y posteriormente ampliarse.

## **Lecturas**

Las lecturas se van a generar en base a 3 variables principales:

1. Dificultad de la lectura (BAJO, MEDIO, ALTO)  
2. Categoría (Una de las previamente creadas por el usuario)  
3. Longitud (CORTO, MEDIO, LARGO)

Esto permitirá proporcionar variedad y evitar que el aprendizaje se limite a frases aisladas.

## **Comprensión lectora**

Después de leer o escuchar un texto, el usuario podrá redactar un resumen o explicación general de lo que entendió del contenido.  
No se generarán preguntas sobre el texto. En su lugar, la inteligencia artificial analizará el resumen redactado por el usuario y calificará qué tan acertada fue su comprensión, con base en distintos parámetros de evaluación que el equipo definirá durante el desarrollo del proyecto (por ejemplo, cobertura de las ideas principales, precisión y coherencia). El sistema proporcionará retroalimentación sobre el resumen del usuario y asignará una calificación, registrando el resultado en su historial.

## 

## **Análisis contextual de vocabulario mediante inteligencia artificial**

Una de las funciones principales de la aplicación será permitir que el usuario interactúe con palabras u oraciones presentes en los textos. Al seleccionarlos, el sistema, apoyado en inteligencia artificial, podrá mostrar:

> * Significado.  
> * Definición.  
> * Ejemplos de utilización.  
> * Oración original.

Esto permitirá que el estudiante comprenda no solamente qué significa una palabra, sino cómo funciona dentro de una oración.  
Además, dentro del diccionario el usuario podrá reproducir en audio la pronunciación de la palabra o de la oración seleccionada. Para controlar los costos de los servicios de texto a voz y mantener tiempos de respuesta adecuados, la generación de audio estará limitada a palabras u oraciones cortas seleccionadas por el usuario, evitando la generación completa de audio para textos extensos.

## 

## **Sistema de rachas** {#sistema-de-rachas}

Para incentivar el uso constante de la aplicación, el sistema incluirá un sistema de rachas diarias que funcionará como mecanismo de motivación y seguimiento, reconociendo la constancia del usuario al utilizar la plataforma día con día. 

## **Seguimiento del progreso**

El usuario podrá consultar información relacionada con su aprendizaje. Por ejemplo:

> * Textos completados.  
> * Palabras estudiadas.  
> * Historial de actividades.  
> * Métricas sobre las lecturas y audios respondidos.

# 

# 

# **7\. Limitaciones**

El proyecto tendrá determinadas limitaciones durante su primera versión.

> * La primera versión estará limitada a cuatro idiomas: inglés, francés, español e italiano.  
> * El sistema estará principalmente orientado a comprensión lectora, vocabulario y gramática. Funciones avanzadas relacionadas con reconocimiento de voz, pronunciación automática, conversación mediante inteligencia artificial o evaluación completa de expresión oral podrán considerarse como futuras ampliaciones.  
> * La calidad y variedad del contenido dependerán de la cantidad de material educativo disponible y de los recursos utilizados para su elaboración.  
> * La selección de nivel es definida manualmente por el usuario y no constituye una certificación oficial del dominio de un idioma.  
> * La generación de audio mediante inteligencia artificial estará limitada a la pronunciación de palabras y frases cortas seleccionadas por el usuario, y no a la generación completa de audio de textos extensos, con el fin de controlar costos de los servicios de texto a voz y mantener tiempos de respuesta adecuados.  
> * La evaluación de comprensión se basa en la calificación por IA de resúmenes redactados por el usuario, y no en preguntas estructuradas (opción múltiple, verdadero/falso, etc.), debido a la naturaleza dinámica del contenido generado.  
> * Las fechas de entrega pueden verse comprometidas por falta de tokens para la IA que generara los textos

# **8\. Producto Mínimo Viable (MVP).** {#8.-producto-mínimo-viable-(mvp).}

El MVP de DolyNation consiste en una plataforma web de aprendizaje de idiomas centrada en la lectura contextualizada y asistida por inteligencia artificial. Está diseñada para ofrecer una experiencia directa donde el usuario rompe con las limitaciones de las aplicaciones tradicionales basadas en ejercicios aislados o de opción múltiple.   

1\. Acceso y Personalización Inicial.

* Gestión de Usuario: El usuario puede registrarse e iniciar sesión de forma segura para que posteriormente su progreso, historial y preferencias queden guardados permanentemente.     
* Selección de Ruta de Estudio: Al ingresar, el usuario selecciona el idioma que desea practicar entre las cuatro opciones iniciales (inglés, francés, español e italiano).  
* Perfil y Parámetros: Define sus categorías de interés y el nivel de dificultad con el que desea trabajar (bajo, medio o alto), configurando a su medida la experiencia de estudio.   

2\. Núcleo de Aprendizaje. 

* Lecturas y Contexto Generación de Contenido por IA: Utilizando las preferencias del usuario (idioma, categoría y dificultad) junto con la longitud deseada del texto, el sistema genera lecturas educativas enfocadas en situaciones reales y de interés.    

3\. Evaluación de Comprensión Lectora. 

* En lugar de los cuestionarios tradicionales de opción múltiple, la comprensión se evalúa mediante la redacción de resúmenes libres.     
* El usuario escribe con sus propias palabras lo que entendió del texto y lo envía. La inteligencia artificial analiza el escrito evaluando la cobertura de ideas principales, coherencia y precisión.     
* Como resultado, el usuario recibe una calificación cuantitativa inmediata, junto con observaciones y retroalimentación constructiva para mejorar su desempeño.   

# **9\. Requerimientos funcionales y no funcionales** {#9.-requerimientos-funcionales-y-no-funcionales}

## **9.1. Requerimientos funcionales** {#9.1.-requerimientos-funcionales}

#### **RF-01. Registro y autenticación de usuarios** {#rf-01.-registro-y-autenticación-de-usuarios}

**Descripción:**  
El sistema debe permitir a los usuarios registrarse e iniciar sesión mediante un mecanismo de autenticación que permita identificar de forma única a cada usuario y gestionar de manera segura el acceso a la plataforma.

**Funcionalidades:**

* Crear una cuenta de usuario.  
* Iniciar sesión.  
* Cerrar sesión.  
* Validar las credenciales proporcionadas.  
* Mantener asociadas las actividades y preferencias a la cuenta correspondiente.

#### **RF-02. Selección de idioma de aprendizaje** {#rf-02.-selección-de-idioma-de-aprendizaje}

**Descripción:**  
El sistema debe proporcionar una interfaz que permita al usuario seleccionar manualmente el idioma que desea estudiar entre los idiomas disponibles.

**Idiomas iniciales:**

* Inglés.  
* Francés.  
* Español.  
* Italiano.

El idioma seleccionado deberá utilizarse como parámetro para la generación y presentación del contenido educativo.

#### 

#### 

#### **RF-03. Selección de categorías de interés** {#rf-03.-selección-de-categorías-de-interés}

**Descripción:**  
El sistema debe permitir al usuario seleccionar o agregar categorías de interés para personalizar las temáticas utilizadas en la generación de contenidos educativos.

Las categorías seleccionadas deberán almacenarse como preferencias del usuario y podrán ser modificadas posteriormente.

#### **RF-04. Selección del nivel de dificultad** {#rf-04.-selección-del-nivel-de-dificultad}

Descripción:  
El sistema debe permitir al usuario seleccionar el nivel de dificultad con el que desea trabajar durante su aprendizaje.

Niveles disponibles:

* Bajo.  
* Medio.  
* Alto.

El nivel seleccionado deberá utilizarse como parámetro para determinar la complejidad del contenido generado.

#### **RF-05. Generación de contenido educativo personalizado** {#rf-05.-generación-de-contenido-educativo-personalizado}

**Descripción:**  
El sistema debe integrar un módulo de inteligencia artificial capaz de generar contenido educativo personalizado de acuerdo con las preferencias y parámetros establecidos por el usuario.

**Parámetros considerados:**

* Idioma de aprendizaje.  
* Categorías de interés.  
* Nivel de dificultad.  
* Longitud del contenido.

#### 

#### 

#### **RF-06. Configuración de parámetros de generación** {#rf-06.-configuración-de-parámetros-de-generación}

**Descripción:**  
El sistema debe proporcionar una interfaz que permita configurar los parámetros utilizados para generar una lectura educativa.

**Parámetros obligatorios:**

* Categorías de interés.  
* Nivel de dificultad (Bajo, Medio, Alto).  
* Longitud del texto (Corto, Medio, Largo).

El sistema deberá utilizar estos parámetros como entrada para el proceso de generación mediante inteligencia artificial.

#### **RF-07. Evaluación de comprensión lectora mediante IA** {#rf-07.-evaluación-de-comprensión-lectora-mediante-ia}

**Descripción:**  
El sistema debe permitir al usuario redactar un resumen o explicación libre sobre una lectura realizada y enviarlo para su evaluación mediante inteligencia artificial.

**Criterios de evaluación:**

* Cobertura de las ideas principales.  
* Precisión.  
* Coherencia.

**Resultados proporcionados:**

* Una calificación.  
* Retroalimentación sobre el desempeño.  
* Observaciones que ayuden al usuario a identificar aspectos que puede mejorar.

#### **RF-08. Consulta de vocabulario contextual** {#rf-08.-consulta-de-vocabulario-contextual}

**Descripción:**  
El sistema debe permitir al usuario seleccionar palabras u oraciones dentro de una lectura para consultar información relacionada con ellas mediante inteligencia artificial.

**Información proporcionada:**

* Significado.  
* Definición.  
* Ejemplos de uso.  
* Oración original dentro de la lectura.

El sistema también deberá permitir reproducir mediante audio la pronunciación de la palabra o frase seleccionada.

#### **RF-09. Registro de progreso e historial** {#rf-09.-registro-de-progreso-e-historial}

**Descripción:**  
El sistema debe registrar y almacenar de forma persistente las actividades realizadas por cada usuario para permitir el seguimiento de su proceso de aprendizaje.

**Elementos registrados:**

* Lecturas realizadas.  
* Contenidos completados.  
* Palabras consultadas o estudiadas.  
* Evaluaciones realizadas.  
* Calificaciones obtenidas.  
* Fecha de realización de las actividades.

#### **RF-10. Sistema de rachas de aprendizaje** {#rf-10.-sistema-de-rachas-de-aprendizaje}

**Descripción:**  
El sistema debe registrar la actividad diaria del usuario y calcular su racha de aprendizaje con base en los días consecutivos en los que haya realizado actividades dentro de la plataforma.

**Información mostrada:**

* Racha actual.  
* Registro de actividad.  
* Días consecutivos de aprendizaje.

#### **RF-11. Perfil y preferencias del usuario** {#rf-11.-perfil-y-preferencias-del-usuario}

**Descripción:**  
El sistema debe proporcionar un módulo de perfil que permita al usuario consultar y administrar la información asociada a su cuenta.

**Opciones de gestión:**

* Información personal.  
* Idioma de aprendizaje.  
* Categorías de interés.  
* Nivel de dificultad.  
* Preferencias de estudio.  
* Configuración de la cuenta.

#### 

#### **RF-12. Interfaz de navegación y visualización de contenidos** {#rf-12.-interfaz-de-navegación-y-visualización-de-contenidos}

**Descripción:**  
El sistema debe proporcionar una interfaz web que permita al usuario navegar entre las diferentes funcionalidades de la plataforma y acceder a los contenidos educativos generados.

**Secciones accesibles:**

* Contenidos educativos.  
* Actividades de comprensión.  
* Consultas de vocabulario.  
* Resultados.  
* Progreso e historial.  
* Perfil y preferencias.

#### **RF-13. Soporte de idiomas** {#rf-13.-soporte-de-idiomas}

**Descripción:**  
El sistema debe proporcionar soporte funcional para los idiomas definidos para la primera versión de la plataforma.

**Idiomas soportados:**

* Inglés.  
* Francés.  
* Español.  
* Italiano.

El soporte deberá contemplar la generación y presentación de contenidos educativos correspondientes al idioma seleccionado.

## **9.2. Requerimientos no funcionales** {#9.2.-requerimientos-no-funcionales}

### **9.2.1. Usabilidad y accesibilidad** {#9.2.1.-usabilidad-y-accesibilidad}

#### **RNF-01. Interfaz responsiva** {#rnf-01.-interfaz-responsiva}

**Descripción:**  
La aplicación web debe adaptarse correctamente a diferentes tamaños de pantalla, permitiendo su utilización desde computadoras de escritorio, tabletas y dispositivos móviles.

#### 

#### 

#### **RNF-02. Facilidad de uso** {#rnf-02.-facilidad-de-uso}

**Descripción:**  
La interfaz debe permitir que un usuario pueda utilizar las funciones principales de la plataforma sin requerir conocimientos técnicos o capacitación previa.  
Las principales acciones deberán encontrarse claramente identificadas y ser accesibles mediante una navegación consistente.

#### **RNF-03. Diseño centrado en la lectura** {#rnf-03.-diseño-centrado-en-la-lectura}

**Descripción:**  
La interfaz destinada a la visualización de contenidos educativos debe priorizar la legibilidad y reducir elementos visuales innecesarios que puedan distraer al usuario durante la lectura.  
**Aspectos clave:**

* Tipografías legibles.  
* Contraste adecuado.  
* Espaciado suficiente.  
* Jerarquía visual clara.  
* Presentación diferenciada de títulos, párrafos y elementos interactivos.

### **9.1.2. Rendimiento** {#9.1.2.-rendimiento}

#### **RNF-04. Tiempo de respuesta** {#rnf-04.-tiempo-de-respuesta}

**Descripción:**  
El sistema deberá proporcionar una respuesta visual inmediata ante las acciones del usuario y mostrar indicadores de carga durante operaciones que dependan de servicios externos, especialmente aquellas relacionadas con la generación y evaluación mediante inteligencia artificial.  
Para las operaciones de IA, se deberá establecer posteriormente un tiempo objetivo de respuesta de acuerdo con las capacidades y proveedores seleccionados.

### 

### 

### 

### 

### **9.1.3. Seguridad** {#9.1.3.-seguridad}

#### **RNF-05. Almacenamiento seguro de credenciales** {#rnf-05.-almacenamiento-seguro-de-credenciales}

**Descripción:**  
Las contraseñas de los usuarios no deberán almacenarse en texto plano. El sistema deberá utilizar mecanismos de hashing criptográfico seguros y adecuados para el almacenamiento de credenciales con el uso de **Argon2id**.

#### **RNF-06. Autenticación y autorización de API** {#rnf-06.-autenticación-y-autorización-de-api}

**Descripción:**  
Los endpoints de la API que proporcionen acceso a información privada deberán requerir autenticación y autorización.  
El sistema deberá garantizar que cada usuario únicamente pueda consultar o modificar la información correspondiente a su propia cuenta, de acuerdo con los permisos establecidos.

#### **RNF-07. Protección de información** {#rnf-07.-protección-de-información}

**Descripción:**  
La información sensible transmitida entre el cliente y el servidor deberá protegerse mediante protocolos de comunicación seguros, como HTTPS/TLS.

### **9.1.4. Escalabilidad** {#9.1.4.-escalabilidad}

#### **RNF-08. Arquitectura modular y desacoplada** {#rnf-08.-arquitectura-modular-y-desacoplada}

**Descripción:**  
El sistema deberá utilizar una arquitectura modular que permita separar las responsabilidades principales de la aplicación y facilite la incorporación de nuevas funcionalidades.  
**Posibilidades futuras:**

* Incorporar nuevos idiomas.  
* Agregar nuevos tipos de actividades.  
* Integrar nuevos proveedores de inteligencia artificial.  
* Incorporar clientes móviles.  
* Ampliar las funcionalidades de aprendizaje.

### 

### 

### 

### 

### **9.1.5. Mantenibilidad** {#9.1.5.-mantenibilidad}

#### **RNF-09. Organización y mantenibilidad del código** {#rnf-09.-organización-y-mantenibilidad-del-código}

**Descripción:**  
El código fuente deberá organizarse de manera modular y mantener una separación clara de responsabilidades entre las diferentes capas o componentes del sistema.  
**Aspectos facilitados:**

* Mantenimiento.  
* Corrección de errores.  
* Pruebas.  
* Incorporación de nuevas funcionalidades.  
* Comprensión del código por parte de otros desarrolladores.

#### **RNF-10. Manejo de errores y servicios externos** {#rnf-10.-manejo-de-errores-y-servicios-externos}

**Descripción:**  
El sistema deberá implementar mecanismos de manejo de errores para situaciones relacionadas con servicios externos.

* Fallos de conexión.  
* Tiempo de espera.  
* Disponibilidad del proveedor.  
* Límites de consumo (rate limits).  
* Respuestas inválidas o incompletas.

El sistema deberá informar al usuario cuando una operación no pueda completarse y evitar que un fallo de un servicio externo provoque el bloqueo o la interrupción completa de la aplicación.

### **9.1.6. Disponibilidad y confiabilidad** {#9.1.6.-disponibilidad-y-confiabilidad}

#### **RNF-11. Persistencia de información** {#rnf-11.-persistencia-de-información}

**Descripción:**  
La información relacionada con usuarios, preferencias, actividades, resultados, progreso e historial deberá almacenarse de manera persistente para evitar su pérdida durante reinicios o interrupciones del sistema.

#### **RNF-12. Integridad de la información** {#rnf-12.-integridad-de-la-información}

**Descripción:**  
El sistema deberá garantizar la consistencia e integridad de la información almacenada, evitando registros duplicados o inconsistentes y manteniendo las relaciones entre usuarios, actividades, contenidos y resultados.

## 

## **10\. Análisis de riesgo** {#10.-análisis-de-riesgo}

*Escala: Probabilidad e Impacto se califican de 1 (muy bajo) a 5 (muy alto). Puntuación \= Probabilidad × Impacto. Nivel de riesgo: Bajo (1–5), Medio (6–10), Alto (11–15), Crítico (16–25).*

| ID | Tipo de problema | Probabilidad | Impacto | Puntuación | Nivel de riesgo | Consecuencia | Respuesta ante el problema | Estrategia |
| :---- | :---- | :---: | :---: | :---: | :---: | :---- | :---- | :---- |
| R1 | Costos elevados por consultas excesivas de IA | 4 | 4 | 16 | Crítico | Los costos de la API de IA se disparan y el proyecto queda sin presupuesto para el resto del ciclo | Limitar la generación con caché por `prompt_hash`, acotar el audio a palabras y frases cortas y vigilar el gasto por usuario | MITIGAR |
| R2 | Dependencia de servicios externos de IA (costos y disponibilidad) | 3 | 4 | 12 | Alto | La plataforma queda inutilizable si el proveedor cae o cambia sus condiciones | Proveedor adaptable con timeouts, reintentos, *circuit breaker* y modo degradado con funciones básicas sin IA | MITIGAR |
| R3 | Latencia en la generación y evaluación de contenido por IA | 4 | 3 | 12 | Alto | Mala experiencia de usuario y abandono de la sesión de estudio | Indicadores de carga y mensajes claros mientras se procesa, con límite de lecturas pendientes | MITIGAR |
| R4 | Precisión de la calificación automática de comprensión lectora | 3 | 4 | 12 | Alto | El usuario recibe calificaciones poco fiables y deja de confiar en la plataforma | Rúbrica explícita con cobertura, precisión y coherencia, feedback explicativo y opción de reportar una calificación para revisión | MITIGAR |
| R5 | Explicaciones de vocabulario o contexto generadas por IA poco acertadas | 3 | 4 | 12 | Alto | El usuario estudia un significado incorrecto y su comprensión se deteriora | Mostrar siempre la oración original junto a la definición y habilitar el reporte de error | MITIGAR |
| R6 | Abuso del sistema mediante múltiples cuentas o llamadas automatizadas | 3 | 4 | 12 | Alto | Los costos y el contenido se explotan y los resultados se contaminan | Rate limiting en registro, login, generación y chat, y registro de las llamadas en `prompt_logs` | MITIGAR |
| R7 | Crecimiento no controlado del alcance (scope creep) | 4 | 3 | 12 | Alto | Retrasos en la entrega y funcionalidades del MVP incompletas | Backlog separado para ideas futuras, control de cambios en la planeación y alcance de la entrega declarado | EVITAR |
| R8 | Alcance limitado por el tiempo disponible del equipo | 3 | 4 | 12 | Alto | Funcionalidades planeadas quedan fuera de la entrega final | Reparto de carga equilibrado por sprint, Definition of Done estricto y recorte explícito documentado | MITIGAR |
| R9 | Seguridad de la información del usuario (credenciales y progreso) | 2 | 5 | 10 | Medio | Filtración de datos personales o credenciales, con pérdida de confianza y posibles implicaciones legales | Argon2id, JWT con secreto fail-fast, CORS con lista blanca, refresh tokens rotados y revocados, y canal privado de reporte en `SECURITY.md` | MITIGAR |
| R10 | Calidad inconsistente del contenido generado por IA | 3 | 3 | 9 | Medio | Textos con errores gramaticales o poco naturales que afectan el aprendizaje | Validación básica antes de mostrar el texto, descarte de contenido mixto entre idiomas y aviso al usuario | MITIGAR |
| R11 | Baja adopción o retención de usuarios | 3 | 3 | 9 | Medio | El proyecto no valida su propuesta de valor con usuarios reales | Retroalimentación temprana en las pruebas de usabilidad y ajuste de la propuesta según hallazgos | MITIGAR |
| R12 | Mezcla de idiomas en las lecturas generadas por IA | 2 | 4 | 8 | Medio | El usuario recibe material en un idioma distinto al elegido y no puede practicar | Validación de idioma en la generación, prompts por idioma y descarte del texto que no coincide | MITIGAR |
| R13 | Rotación o salida de un integrante del equipo a mitad del proyecto | 2 | 4 | 8 | Medio | Pérdida de conocimiento técnico y retraso en las tareas asignadas | CODEOWNERS con dos responsables por ruta, documentación actualizada en cada PR y redistribución inmediata de tareas | ACEPTAR |
| R14 | Escalabilidad de la infraestructura ante el crecimiento de usuarios | 2 | 3 | 6 | Medio | Caídas o lentitud del sistema al aumentar los usuarios | Recursos asignados con límites por servicio, healthchecks y despliegue escalable por imagen y SHA | ACEPTAR |
| R15 | Cambios en políticas o precios de proveedores de IA | 2 | 3 | 6 | Medio | El costo o el acceso al proveedor deja de ser viable para el proyecto | Interfaz de proveedor adaptable, caché por `prompt_hash` y seguimiento del gasto por usuario | ACEPTAR |
| R16 | Lecturas repetitivas o poco variadas en temática | 3 | 2 | 6 | Medio | El usuario pierde interés por falta de variedad en el contenido | Categorías, dificultades y longitudes configurables, con ampliación temporal de los parámetros disponibles | MITIGAR |

# **11\. Elección de metodología y roles del equipo** {#11.-elección-de-metodología-y-roles-del-equipo}

### **11.1. Metodología de trabajo** {#11.1.-metodología-de-trabajo}

Para el desarrollo del proyecto **DolyNation** se implementa el marco de trabajo **Scrum** combinado con un flujo de desarrollo guiado por tareas en GitHub (*Issue-Driven Development*). El proyecto se divide en 5 Sprints con fechas estrictas de entrega que abarcan desde el **19 de octubre** hasta el **10 de diciembre** de 2026\. El Sprint 1 se reprogramó al 19 de octubre tras detectarse que su entrega se retrasó, y los sprints 4 y 5 se acortaron para sostener la fecha de entrega de la 1 a 10 de diciembre.

**Plataforma de trabajo.** Toda la coordinación vive en **GitHub**: los repositorios de código, la documentación, las issues con sus entregables y dependencias, el tablero del proyecto, la revisión de código por *code owners*, la integración continua, los entornos de despliegue y los releases. La justificación de esa decisión, con los criterios, las alternativas descartadas y sus límites, está en
[`operations/JUSTIFICACION-GITHUB.md`](../operations/JUSTIFICACION-GITHUB.md) y en el
[ADR-009](../decisions/README.md).

### **11.2. Estructura de roles y responsabilidades** {#11.2.-estructura-de-roles-y-responsabilidades}

* **Product Owner:** Sebastián  
  * **Responsabilidades:** Definición y validación de historias de usuario, priorización del backlog de productos, diseño de prompts para los modelos de Inteligencia Artificial y validación de criterios de aceptación de los entregables.  
* **Scrum Master / Lead Developer:** Jesús Alberto Villarreal Pérez  
  * **Responsabilidades:** Coordinación del flujo de trabajo en GitHub, configuración de políticas de integración continua (CI/CD), revisión de Pull Requests, tagging de releases y apoyo en desarrollo técnico estratégico (Frontend/Backend).  
* **Desarrollador Frontend:** Juan Antonio Deras Durón  
  * **Responsabilidades:** Maquetado responsivo en Next.js, integración de Tailwind CSS, diseño de componentes de interfaz (visor de lectura, pop-ups contextuales, dashboard de usuario).  
* **Desarrollador Backend (Principal):** Aozmar Azael García Candela  
  * **Responsabilidades:** Arquitectura de microservicios y módulos en NestJS, lógica de autenticación criptográfica, conector con APIs de IA (MiniMax-M3 adaptable) y motor de evaluación de resúmenes.  
* **Desarrollador Backend (Soporte):** José Elías Galarza Pedroza  
  * **Responsabilidades:** Diseño de DTOs, controladores de base de datos (PostgreSQL), endpoints para perfiles, historial de actividades y módulo administrativo.

## **12\. Separación del proyecto en tareas** {#12.-separación-del-proyecto-en-tareas}

El proyecto se gestiona como un conjunto de **issues en GitHub**, uno por entregable, y esa lista es la fuente de verdad. En total hay **70 issues abiertas** repartidas en cuatro repositorios: 33 entregables de producto derivados de los requerimientos funcionales y del MVP, 12 sub-issues que descomponen los entregables grandes, 5 tareas de plataforma de CI/CD y entornos, 3 migraciones de schema y 17 issues de saneamiento creadas en la auditoría del proyecto.

Las tareas están divididas por capas técnicas: los desarrolladores backend y frontend trabajan en sus áreas específicas y colaboran en tareas en pareja para la integración de la API con la interfaz de usuario. **Cada issue tiene estado actual, entregables, criterios de aceptación, dependencias, evidencia esperada y fecha objetivo**; el avance se mide en los sub-issues, no en los padres, para no contarlo dos veces.

### **Resumen de distribución de tareas** {#resumen-de-distribución-de-tareas}

La columna «Asignaciones» cuenta una vez por persona cada issue que tiene asignada, de modo que una tarea en pareja aparece en las dos. Las 70 issues abiertos suman 85 asignaciones.

| Persona | Rol | Issues asignadas | En pareja con | Total |
| :---- | :---- | ---: | :---- | ---: |
| **Jesús Alberto Villarreal Pérez** | Scrum Master / Dev | 27 | 9 | **27** |
| **Aozmar Azael García Candela** | Desarrollador Backend | 20 | 7 | **20** |
| **Juan Antonio Deras Durón** | Desarrollador Frontend | 19 | 6 | **19** |
| **José Elías Galarza Pedroza** | Desarrollador Backend | 18 | 5 | **18** |
| **Sebastián Rodríguez** | Product Owner | 1 | — | *Supervisión y validaciones* |

*Nota de reparto:* Jesús concentra la coordinación, las tareas de QA y las de infraestructura, y además las 5 issues de saneamiento de la documentación (`docs#11`-`#15`), que se cierran en la primera semana y no son carga sostenida.

### 

## **13\. Cronograma de actividades** {#13.-cronograma-de-actividades}

[*Referencia visual*](https://github.com/orgs/DolyLanguagesORG/projects/1/views/3)

### **13.1. Hitos del proyecto** {#13.1.-hitos-del-proyecto}

* **Sprint 1 (05/Oct – 18/Oct/2026):** Configuración del repositorio y cimientos. *Cerrado con retraso: se completó el 19/Oct/2026.*  
* **Sprint 2 (19/Oct – 01/Nov/2026):** Fundamentos: autenticación, perfil y base del frontend.  
* **Sprint 3 (02/Nov – 15/Nov/2026):** Lecturas con IA.  
* **Sprint 4 (16/Nov – 29/Nov/2026):** Vocabulario, TTS, evaluación y progreso.  
* **Sprint 5 (30/Nov – 06/Dic/2026):** Calidad, integración y release v1.0.0. Del **07 al 10/Dic/2026**: entrega del *release*, capturas y presentación del proyecto.

### **13.2. Tabla de asignación de tareas y cronograma** {#13.2.-tabla-de-asignación-de-tareas-y-cronograma}

> **Referencia de issues.** Al separar el monorepo en cuatro repos, cada tarea es un issue en su repositorio. El identificador `back#N`, `front#N`, `infra#N` o `docs#N` indica el repo (`dolynation-atl-back`, `dolynation-tonatiuh-front`, `dolynation-tlalli-infra`, `dolynation-ehecatl-docs`) y el número del issue.

> **Referencia de issues.** Al separar el monorepo en cuatro repositorios, cada tarea es un issue en su repositorio. El identificador `back#N`, `front#N`, `infra#N` o `docs#N` indica el repo (`dolynation-atl-back`, `dolynation-tonatiuh-front`, `dolynation-tlalli-infra`, `dolynation-ehecatl-docs`) y el número del issue. El tablero con el estado, las fechas y los responsables en vivo está en [el Project de la organización](https://github.com/orgs/DolyLanguagesORG/projects/1/views/3).

> **Referencia de issues.** Al separar el monorepo en cuatro repositorios, cada tarea es un issue en su repositorio. El identificador `back#N`, `front#N`, `infra#N` o `docs#N` indica el repo (`dolynation-atl-back`, `dolynation-tonatiuh-front`, `dolynation-tlalli-infra`, `dolynation-ehecatl-docs`) y el número del issue. El tablero con el estado, las fechas y los responsables en vivo está en [el Project de la organización](https://github.com/orgs/DolyLanguagesORG/projects/1/views/3).

> **Alcance de la entrega.** El desarrollo termina el **06 de diciembre de 2026**; del **07 al 10 de diciembre** se reserva para el *release* `v1.0.0`, las capturas y la presentación.

#### **Sprint 1: Configuración del repositorio y cimientos**

**Periodo:** 05 al 18 de octubre de 2026 (cerrado con retraso el 19 de octubre)

| Issue | Tarea / Descripción | Responsable | Fecha Inicio | Fecha Entrega |
| :---- | :---- | :---- | :---- | :---- |
| **back#2** | Setup de arquitectura NestJS, conexión a PostgreSQL (Drizzle ORM) y entidad User | Azael | 5 Oct 2026 2026 | 8 Oct 2026 2026 |
| **back#3** | Servicio de hash criptográfico (Argon2id) y estrategia de autenticación JWT en NestJS | Azael | 9 Oct 2026 2026 | 12 Oct 2026 2026 |
| **docs#6** | docs(repo): onboarding de Elías, CODEOWNERS y reglas de revisión | Sebastián | 12 Oct 2026 2026 | 15 Oct 2026 2026 |
| **docs#11** | Sanear el anteproyecto: corregir contradicciones con el código y desajustes de formato | Jesús | 19 Oct 2026 2026 | 19 Oct 2026 2026 |
| **docs#12** | Revisar los diagramas y corregir los que contradicen el código | Jesús | 19 Oct 2026 2026 | 20 Oct 2026 2026 |
| **docs#13** | Completar el registro de decisiones (ADR) y documentar las decisiones pendientes | Jesús | 20 Oct 2026 2026 | 20 Oct 2026 2026 |
| **docs#14** | Unificar el contrato API y alinear las convenciones al código real | Jesús | 20 Oct 2026 2026 | 20 Oct 2026 2026 |
| **docs#15** | Saneamiento de la configuración de GitHub: milestones, tablero, rulesets e higiene de los repos | Jesús | 20 Oct 2026 2026 | 20 Oct 2026 2026 |

#### **Sprint 2: Fundamentos: autenticación, perfil y base del frontend**

**Periodo:** 19 de octubre al 01 de noviembre de 2026

| Issue | Tarea / Descripción | Responsable | Fecha Inicio | Fecha Entrega |
| :---- | :---- | :---- | :---- | :---- |
| **back#4** | DTOs de validación y endpoints de autenticación (/auth/register, /auth/login, /auth/refresh, /auth/logout, /auth/me) | Azael | 19 Oct 2026 2026 | 21 Oct 2026 2026 |
| **front#2** | Setup de proyecto Next.js con Tailwind CSS, layout base y temas de la interfaz | Juan | 19 Oct 2026 2026 | 24 Oct 2026 2026 |
| **infra#24** | Runner de migraciones con tabla schema_migrations | Jesús | 19 Oct 2026 2026 | 21 Oct 2026 2026 |
| **back#19** | Cliente IA: adaptador MiniMax-M3 configurable (interfaz para otros proveedores) | Elías | 21 Oct 2026 2026 | 22 Oct 2026 2026 |
| **back#7** | Módulo de servicios en NestJS para integración con la API de IA (MiniMax-M3) y arquitectura de prompts | Azael | 22 Oct 2026 2026 | 24 Oct 2026 2026 |
| **infra#20** | Migración S2: preferencias, categorías, idioma y caché de lecturas | Jesús | 22 Oct 2026 2026 | 24 Oct 2026 2026 |
| **back#5** | Endpoints para consultar y actualizar el perfil de usuario (/user/profile) | Elías | 23 Oct 2026 2026 | 25 Oct 2026 2026 |
| **back#20** | Arquitectura de prompts versionados por idioma, categoría, dificultad y longitud | Azael | 25 Oct 2026 2026 | 27 Oct 2026 2026 |
| **front#22** | Base de i18n con next-intl y diccionarios en inglés, francés, español e italiano | Juan | 25 Oct 2026 2026 | 26 Oct 2026 2026 |
| **infra#6** | Definir entornos (dev/staging/prod), secretos y acceso SSH | Jesús | 25 Oct 2026 2026 | 26 Oct 2026 2026 |
| **back#6** | Pruebas de integración del Sprint 1, corrección de bugs y revisión de PRs hacia develop | Elías + Sebastián | 26 Oct 2026 2026 | 28 Oct 2026 2026 |
| **front#24** | Sistema de diseño: tokens de marca, componentes base y Flowbite | Juan | 27 Oct 2026 2026 | 29 Oct 2026 2026 |
| **back#8** | Endpoints para selección y guardado de categorías e idiomas (/settings/categories, /settings/languages) | Azael | 28 Oct 2026 2026 | 30 Oct 2026 2026 |
| **back#46** | /health/ready debe validar la conexión real con PostgreSQL | Elías | 29 Oct 2026 2026 | 29 Oct 2026 2026 |
| **back#47** | Separar test:unit de test:e2e para que npm run verify no exija base de datos | Elías | 30 Oct 2026 2026 | 30 Oct 2026 2026 |
| **front#3** | Maquetado e integración de vistas de login y registro en Next.js | Juan | 30 Oct 2026 2026 | 1 Nov 2026 2026 |
| **back#41** | Verificar y completar la documentación OpenAPI/Scalar del Sprint 1 | Azael | 31 Oct 2026 2026 | 31 Oct 2026 2026 |

#### **Sprint 3: Lecturas con IA**

**Periodo:** 02 al 15 de noviembre de 2026

| Issue | Tarea / Descripción | Responsable | Fecha Inicio | Fecha Entrega |
| :---- | :---- | :---- | :---- | :---- |
| **back#9** | Servicio de caché para respuestas de lectura con parámetros equivalentes (RNF-04) | Elías | 2 Nov 2026 2026 | 4 Nov 2026 2026 |
| **front#4** | Vista del perfil de usuario e integración con el estado de sesión en Next.js | Juan | 2 Nov 2026 2026 | 3 Nov 2026 2026 |
| **front#5** | Formulario de selección de parámetros de estudio (idioma, categoría, dificultad, longitud) en Next.js | Juan | 4 Nov 2026 2026 | 6 Nov 2026 2026 |
| **back#21** | Manejo de errores, timeouts y modo degradado del proveedor IA (implementación) | Azael | 5 Nov 2026 2026 | 6 Nov 2026 2026 |
| **back#43** | Adaptador de TTS con MiniMax y sus variables de entorno | Azael | 7 Nov 2026 2026 | 8 Nov 2026 2026 |
| **front#6** | Visor inmersivo de lectura (diseño enfocado en la legibilidad) en Next.js | Juan | 7 Nov 2026 2026 | 10 Nov 2026 2026 |
| **back#10** | Endpoint de generación de lectura (POST /readings) basado en parámetros | Elías + Azael | 9 Nov 2026 2026 | 11 Nov 2026 2026 |
| **back#45** | Protección contra prompt injection en generación y evaluación | Azael | 12 Nov 2026 2026 | 13 Nov 2026 2026 |
| **front#7** | Conexión del flujo completo: formulario de parámetros → generación IA → visor | Elías + Sebastián + Juan | 12 Nov 2026 2026 | 14 Nov 2026 2026 |
| **front#23** | Base de pruebas del frontend: Vitest, Playwright y jobs de CI | Juan | 15 Nov 2026 2026 | 15 Nov 2026 2026 |

#### **Sprint 4: Vocabulario, TTS, evaluación y progreso**

**Periodo:** 16 al 29 de noviembre de 2026

| Issue | Tarea / Descripción | Responsable | Fecha Inicio | Fecha Entrega |
| :---- | :---- | :---- | :---- | :---- |
| **back#11** | Endpoint de vocabulario contextual (significado, definición, ejemplos, oración original) y TTS | Azael | 16 Nov 2026 2026 | 17 Nov 2026 2026 |
| **front#8** | Captura e interacción de selección de texto dentro del visor de lectura en Next.js | Juan | 16 Nov 2026 2026 | 18 Nov 2026 2026 |
| **infra#21** | Migración S3: evaluaciones y vocabulario contextual | Jesús | 16 Nov 2026 2026 | 18 Nov 2026 2026 |
| **back#12** | Servicio de evaluación y calificación por PNL en NestJS (cobertura, precisión, coherencia) con feedback | Azael | 18 Nov 2026 2026 | 20 Nov 2026 2026 |
| **infra#22** | Migración S4: rol de administrador en users | Jesús | 19 Nov 2026 2026 | 20 Nov 2026 2026 |
| **back#13** | Endpoint de evaluación de resumen (POST /readings/{id}/evaluate) | Azael | 21 Nov 2026 2026 | 22 Nov 2026 2026 |
| **infra#26** | Endurecer docker-compose.prod.yml: red interna, healthchecks, proxy TLS y límites | Jesús | 21 Nov 2026 2026 | 23 Nov 2026 2026 |
| **back#17** | Endpoints administrativos de categorías globales y supervisión de usuarios (/admin/categories, /admin/users) | Elías | 23 Nov 2026 2026 | 24 Nov 2026 2026 |
| **back#22** | Motor de puntuación por cobertura y precisión semántica | Azael | 23 Nov 2026 2026 | 24 Nov 2026 2026 |
| **front#10** | Componente de área de redacción libre de resumen y envío de evaluación en Next.js | Elías + Sebastián + Juan | 23 Nov 2026 2026 | 25 Nov 2026 2026 |
| **infra#27** | Pipeline de build de imágenes y despliegue por SHA con rollback | Jesús | 24 Nov 2026 2026 | 26 Nov 2026 2026 |
| **back#15** | Lógica de cálculo de racha diaria (días consecutivos de actividad) y asignación de puntos en NestJS | Elías | 25 Nov 2026 2026 | 26 Nov 2026 2026 |
| **back#23** | Cálculo de coherencia y construcción del feedback | Elías | 25 Nov 2026 2026 | 25 Nov 2026 2026 |
| **back#44** | Endpoint de TTS: audio corto de palabra o frase seleccionada | Azael | 26 Nov 2026 2026 | 27 Nov 2026 2026 |
| **front#12** | Vista del panel administrativo básico en Next.js | Elías + Sebastián + Juan | 26 Nov 2026 2026 | 27 Nov 2026 2026 |
| **back#16** | Endpoints de consulta de historial de actividades (lecturas, palabras consultadas, calificaciones) | Elías | 27 Nov 2026 2026 | 28 Nov 2026 2026 |
| **front#9** | Componente emergente (pop-up) de diccionario contextual e integración de audio corto (TTS) | Juan | 28 Nov 2026 2026 | 29 Nov 2026 2026 |

#### **Sprint 5: Calidad, integración y release v1.0.0**

**Periodo:** 30 de noviembre al 06 de diciembre de 2026 (desarrollo) y del 07 al 10 de diciembre de 2026 (entrega)

| Issue | Tarea / Descripción | Responsable | Fecha Inicio | Fecha Entrega |
| :---- | :---- | :---- | :---- | :---- |
| **back#14** | Pruebas del módulo de vocabulario y evaluación de resúmenes por PNL | Elías + Sebastián | 30 Nov 2026 2026 | 1 Dic 2026 2026 |
| **infra#9** | Auditoría de seguridad: dependencias, secretos y protección de ramas | Sebastián + Jesús | 30 Nov 2026 2026 | 1 Dic 2026 2026 |
| **back#18** | Pruebas de rendimiento, manejo de errores de la API de IA (modo degradado) y validación de seguridad | Elías + Sebastián | 2 Dic 2026 2026 | 3 Dic 2026 2026 |
| **back#24** | Pruebas unitarias del motor de evaluación PNL | Elías + Sebastián | 2 Dic 2026 2026 | 2 Dic 2026 2026 |
| **front#11** | Dashboard de usuario en Next.js (métricas, contador de racha, historial y gráfica de puntos) | Juan | 2 Dic 2026 2026 | 3 Dic 2026 2026 |
| **infra#25** | Test de paridad entre el schema de Drizzle y el SQL de PostgreSQL | Jesús | 2 Dic 2026 2026 | 2 Dic 2026 2026 |
| **back#27** | Validación de seguridad (auth, validación de entrada, rate limiting) | Elías + Sebastián | 4 Dic 2026 2026 | 5 Dic 2026 2026 |
| **front#13** | Pruebas de usabilidad y revisión de diseño responsivo (móvil/desktop) | Sebastián + Juan | 4 Dic 2026 2026 | 4 Dic 2026 2026 |
| **front#14** | Tarjetas de métricas y contador de racha en el dashboard | Juan | 4 Dic 2026 2026 | 4 Dic 2026 2026 |
| **infra#3** | Revisión general de código, limpieza de endpoints y merge a develop | Sebastián + Jesús | 4 Dic 2026 2026 | 5 Dic 2026 2026 |
| **front#15** | Gráfica de puntos por día | Juan | 5 Dic 2026 2026 | 5 Dic 2026 2026 |
| **back#25** | Pruebas de carga y latencia de endpoints críticos | Elías + Jesús | 6 Dic 2026 2026 | 6 Dic 2026 2026 |
| **back#26** | Verificación E2E del modo degradado ante fallos de la API de IA | Elías + Azael | 6 Dic 2026 2026 | 6 Dic 2026 2026 |
| **front#16** | Tabla de historial de actividad con paginación | Juan | 6 Dic 2026 2026 | 6 Dic 2026 2026 |
| **infra#4** | Creación del pull request final de develop hacia main, tagging v1.0.0 y verificación de CI/CD | Sebastián + Jesús | 7 Dic 2026 2026 | 7 Dic 2026 2026 |
| **docs#3** | Preparación de la documentación final del repositorio, capturas del sistema y presentación del proyecto | Sebastián | 8 Dic 2026 2026 | 10 Dic 2026 2026 |

# **14\. Elección de estructura web y tecnologías.** {#14.-elección-de-estructura-web-y-tecnologías.}

Para cumplir con la arquitectura cliente-servidor modular descrita en el proyecto, se ha seleccionado un stack tecnológico moderno, robusto y altamente tipado (TypeScript de extremo a extremo), optimizado para un entorno de despliegue propio (**Self-host**):

* **Frontend (Cliente Web):** **Next.js**  
  * *Justificación:* Permite construir una interfaz web responsiva y optimizada para la lectura, ofreciendo capacidades de renderizado avanzado (SSR/SSG) para mejorar el rendimiento y garantizar una experiencia de usuario limpia y sin distracciones.  
* **Backend (API y Lógica de Negocio):** **NestJS**  
  * *Justificación:* Framework de Node.js diseñado bajo una arquitectura fuertemente modular, ideal para separar responsabilidades (usuarios, contenidos, evaluaciones, etc.) y facilitar la integración escalable con servicios externos de inteligencia artificial.  
* **Capa de Acceso a Datos (ORM):** **Drizzle ORM**  
  * *Justificación:* Proporciona tipado extremo a extremo sobre SQL, sin ocultar la consulta ni el esquema, y mantiene el SQL de PostgreSQL como fuente de verdad en el repositorio de infraestructura.  
* **Base de Datos:** **PostgreSQL**  
  * *Justificación:* Sistema de gestión de bases de datos relacional que garantiza la integridad, consistencia y persistencia segura de la información de los usuarios, historiales y contenidos.  
* **Infraestructura de Despliegue:** **Self-host**  
  * *Justificación:* Entorno autohospedado (mediante contenedores y un servidor dedicado) que otorga control total sobre la seguridad, el rendimiento y la optimización de los costos operativos del sistema..

# **16\. Selección de patrones de diseño.** {#16.-selección-de-patrones-de-diseño.}

Para garantizar la mantenibilidad, escalabilidad y una correcta separación de responsabilidades a nivel de código, el desarrollo del sistema se apoyará en los patrones de diseño nativos implementados por los frameworks seleccionados (NestJS y Next.js):

#### **Patrones de Diseño en el Backend (NestJS)** {#patrones-de-diseño-en-el-backend-(nestjs)}

NestJS implementa de forma nativa patrones de diseño orientados a la arquitectura de software empresarial y modular:

* **Inyección de Dependencias (Dependency Injection \- DI):** Permite desacoplar los componentes del sistema (servicios y controladores), facilitando la reutilización de código, el mantenimiento y la realización de pruebas unitarias.  
* **Patrón Módulo (Module Pattern):** Organiza el código fuente en bloques lógicos autónomos (como el módulo de usuarios, contenidos y evaluaciones), encapsulando sus respectivos controladores y proveedores de forma independiente.  
* **Patrón Controlador-Servicio (Controller-Service / Arquitectura en Capas):** Separa claramente las responsabilidades donde los *Controllers* manejan exclusivamente el flujo de peticiones HTTP y los *Services* concentran la lógica de negocio y las reglas de procesamiento.

#### **Patrones de Diseño en el Frontend (Next.js)** {#patrones-de-diseño-en-el-frontend-(next.js)}

Next.js estructura la interfaz de usuario bajo patrones modernos de desarrollo web basados en componentes de React:

* **Patrón de Componentes Reutilizables y Composición:** Divide la interfaz visual en piezas modulares, independientes y jerárquicas (botones, tarjetas, vistas de lectura), promoviendo la reutilización del código.  
* **Patrón de Renderizado Híbrido (Server / Client Components):** Separa la lógica de renderizado en el servidor (para optimizar la carga inicial y el rendimiento) de la interactividad en el cliente (para acciones dinámicas como la selección de texto o envíos de formularios).

## 

## **17\. Wireframes.** {#17.-wireframes.}

[DolyNation – Figma](https://www.figma.com/design/NpeSJlQsZhpa0233xNcYkP/DolyNation?node-id=0-1&p=f&t=sNXZOHJbsUWWNBUK-0)

## **18\. Fuentes.** {#18.-fuentes.}

* *Amazon Web Services. (s. f.). Precios de Amazon Polly. [https\://aws.amazon.com/polly/pricing/](https://aws.amazon.com/polly/pricing/)*  
* *AssemblyAI. (s. f.). AssemblyAI pricing. [https\://www\.assemblyai.com/pricing](https://www.assemblyai.com/pricing)*  
* *Cartesia. (s. f.). Cartesia pricing. [https\://cartesia.ai/pricing](https://cartesia.ai/pricing)*  
* *Cloudflare. (s. f.). Add a self-hosted application. Cloudflare One Docs. [https\://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/)*  
* *Deepgram. (s. f.-a). Deepgram pricing. [https\://deepgram.com/pricing](https://deepgram.com/pricing)*  
* *Deepgram. (s. f.-b). Voice agent API. [https\://deepgram.com/product/voice-agent-api](https://deepgram.com/product/voice-agent-api)*  
* *ElevenLabs. (s. f.-a). API reference: Text to speech. [https\://elevenlabs.io/docs/api-reference/text-to-speech](https://elevenlabs.io/docs/api-reference/text-to-speech)*  
* *ElevenLabs. (s. f.-b). ElevenLabs pricing. [https\://elevenlabs.io/pricing](https://elevenlabs.io/pricing)*  
* *ElevenLabs. (s. f.-c). Sound effects. [https\://elevenlabs.io/sound-effects](https://elevenlabs.io/sound-effects)*  
* *Figma. (s. f.). Wireframe kits and templates. [https\://www\.figma.com/templates/wireframe-kits/](https://www.figma.com/templates/wireframe-kits/)*  
* *Google Cloud. (s. f.). Precios de Cloud Text-to-Speech. [https\://cloud.google.com/text-to-speech/pricing](https://cloud.google.com/text-to-speech/pricing)*  
* *IA University. (2025, 8 de abril). Cursos de IA gratis: Aprende inteligencia artificial sin costo. [https\://ia.university/inicio/cursos%20de%20inteligencia%20artificial/cursos%20de%20ia%20en%20miami/](https://ia.university/inicio/cursos%20de%20inteligencia%20artificial/cursos%20de%20ia%20en%20miami/)*  
* *La Nación. (2025, 30 de octubre). 10 herramientas para que la inteligencia artificial te ayude a aprender un idioma nuevo. [https\://www\.lanacion.com.ar/tecnologia/10-herramientas-para-que-la-inteligencia-artificial-te-ayude-a-aprender-un-idioma-nuevo-nid30102025/](https://www.lanacion.com.ar/tecnologia/10-herramientas-para-que-la-inteligencia-artificial-te-ayude-a-aprender-un-idioma-nuevo-nid30102025/)*  
* *MiniMax. (s. f.). MiniMax. [https\://www\.minimax.io/](https://www.minimax.io/)*  
* *NestJS. (s. f.). NestJS: A progressive Node.js framework. [https\://nestjs.com/](https://nestjs.com/)*  
* *OpenAI. (s. f.-a). API pricing. [https\://openai.com/api/pricing/](https://openai.com/api/pricing/)*  
* *OpenAI. (s. f.-b). Speech to text. OpenAI Platform Documentation. [https\://platform.openai.com/docs/guides/speech-to-text](https://platform.openai.com/docs/guides/speech-to-text)*  
* *OpenAI. (s. f.-c). Text to speech. OpenAI Platform Documentation. [https\://platform.openai.com/docs/guides/text-to-speech](https://platform.openai.com/docs/guides/text-to-speech)*  
* *Platzi. (s. f.-a). Curso de inteligencia artificial gratis desde cero. [https\://platzi.com/cursos/intro-ai/](https://platzi.com/cursos/intro-ai/)*  
* *Platzi. (s. f.-b). Cursos online de programación, IA, marketing, inglés. [https\://platzi.com/cursos/](https://platzi.com/cursos/)*  
* *Platzi. (s. f.-c). Escuela de AI Academy. [https\://platzi.com/escuela/ai-academy/](https://platzi.com/escuela/ai-academy/)*  
* *Platzi. (s. f.-d). Escuela de Inteligencia Artificial y Data Science. [https\://platzi.com/escuela/datos/](https://platzi.com/escuela/datos/)*  
* *Platzi. (s. f.-e). Platzi: Cursos de programación, IA, inglés. [https\://platzi.com/](https://platzi.com/)*  
* *Refactoring.Guru. (s. f.). Patrones de diseño. [https\://refactoring.guru/es/design-patterns](https://refactoring.guru/es/design-patterns)*  
* *Suno. (s. f.). Suno pricing. [https\://suno.com/pricing](https://suno.com/pricing)*  
* *Udio. (s. f.). Udio pricing. [https\://www\.udio.com/pricing](https://www.udio.com/pricing)*  
* *Vercel. (s. f.). Next.js: The React framework for the web. [https\://nextjs.org/](https://nextjs.org/)*

