![][image1]

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

[**DolyNation	1**](#heading=)

[**Índice	2**](#heading=)

[**1\. Título del proyecto	4**](#heading=)

[**2\. Planteamiento del problema	4**](#heading=)

[**3\. Justificación	5**](#heading=)

[**4\. Objetivo general	6**](#heading=)

[**5\. Objetivos específicos	6**](#heading=)

[**6\. Alcance del proyecto	7**](#heading=)

[**Registro y autenticación	7**](#heading=)

[**Selección de idioma	7**](#heading=)

[**Contenido por niveles	7**](#heading=)

[**Lecturas	7**](#heading=)

[**Comprensión lectora	7**](#heading=)

[**Análisis contextual de vocabulario mediante inteligencia artificial	8**](#heading=)

[Sistema de rachas	8](#sistema-de-rachas)

[**Seguimiento del progreso	8**](#heading=)

[**7\. Limitaciones	9**](#heading=)

[**8\. Producto Mínimo Viable (MVP).	10**](#8.-producto-mínimo-viable-\(mvp\).)

[**9\. Requerimientos funcionales y no funcionales	11**](#9.-requerimientos-funcionales-y-no-funcionales)

[9.1. Requerimientos funcionales	11](#9.1.-requerimientos-funcionales)

[RF-01. Registro y autenticación de usuarios	11](#rf-01.-registro-y-autenticación-de-usuarios)

[RF-02. Selección de idioma de aprendizaje	11](#rf-02.-selección-de-idioma-de-aprendizaje)

[RF-03. Selección de categorías de interés	12](#rf-03.-selección-de-categorías-de-interés)

[RF-04. Selección del nivel de dificultad	12](#rf-04.-selección-del-nivel-de-dificultad)

[RF-05. Generación de contenido educativo personalizado	12](#rf-05.-generación-de-contenido-educativo-personalizado)

[RF-06. Configuración de parámetros de generación	13](#rf-06.-configuración-de-parámetros-de-generación)

[RF-07. Evaluación de comprensión lectora mediante IA	13](#rf-07.-evaluación-de-comprensión-lectora-mediante-ia)

[RF-08. Consulta de vocabulario contextual	13](#rf-08.-consulta-de-vocabulario-contextual)

[RF-09. Registro de progreso e historial	14](#rf-09.-registro-de-progreso-e-historial)

[RF-10. Sistema de rachas de aprendizaje	14](#rf-10.-sistema-de-rachas-de-aprendizaje)

[RF-11. Perfil y preferencias del usuario	14](#rf-11.-perfil-y-preferencias-del-usuario)

[RF-12. Interfaz de navegación y visualización de contenidos	15](#rf-12.-interfaz-de-navegación-y-visualización-de-contenidos)

[RF-13. Soporte de idiomas	15](#rf-13.-soporte-de-idiomas)

[9.2. Requerimientos no funcionales	15](#9.2.-requerimientos-no-funcionales)

[9.2.1. Usabilidad y accesibilidad	15](#9.2.1.-usabilidad-y-accesibilidad)

[RNF-01. Interfaz responsiva	15](#rnf-01.-interfaz-responsiva)

[RNF-02. Facilidad de uso	16](#rnf-02.-facilidad-de-uso)

[RNF-03. Diseño centrado en la lectura	16](#rnf-03.-diseño-centrado-en-la-lectura)

[9.1.2. Rendimiento	16](#9.1.2.-rendimiento)

[RNF-04. Tiempo de respuesta	16](#rnf-04.-tiempo-de-respuesta)

[9.1.3. Seguridad	17](#9.1.3.-seguridad)

[RNF-05. Almacenamiento seguro de credenciales	17](#rnf-05.-almacenamiento-seguro-de-credenciales)

[RNF-06. Autenticación y autorización de API	17](#rnf-06.-autenticación-y-autorización-de-api)

[RNF-07. Protección de información	17](#rnf-07.-protección-de-información)

[9.1.4. Escalabilidad	17](#9.1.4.-escalabilidad)

[RNF-08. Arquitectura modular y desacoplada	17](#rnf-08.-arquitectura-modular-y-desacoplada)

[9.1.5. Mantenibilidad	18](#9.1.5.-mantenibilidad)

[RNF-09. Organización y mantenibilidad del código	18](#rnf-09.-organización-y-mantenibilidad-del-código)

[RNF-10. Manejo de errores y servicios externos	18](#rnf-10.-manejo-de-errores-y-servicios-externos)

[9.1.6. Disponibilidad y confiabilidad	18](#9.1.6.-disponibilidad-y-confiabilidad)

[RNF-11. Persistencia de información	18](#rnf-11.-persistencia-de-información)

[RNF-12. Integridad de la información	18](#rnf-12.-integridad-de-la-información)

[10\. Análisis de riesgo	19](#10.-análisis-de-riesgo)

[**11\. Elección de metodología y roles del equipo	24**](#11.-elección-de-metodología-y-roles-del-equipo)

[11.1. Metodología de trabajo	24](#11.1.-metodología-de-trabajo)

[11.2. Estructura de roles y responsabilidades	24](#11.2.-estructura-de-roles-y-responsabilidades)

[12\. Separación del proyecto en tareas	25](#12.-separación-del-proyecto-en-tareas)

[Resumen de distribución de tareas	25](#resumen-de-distribución-de-tareas)

[13\. Cronograma de actividades	27](#13.-cronograma-de-actividades)

[13.1. Hitos del proyecto	27](#13.1.-hitos-del-proyecto)

[13.2. Tabla de asignación de tareas y cronograma	27](#13.2.-tabla-de-asignación-de-tareas-y-cronograma)

[Sprint 1: Infraestructura, Autenticación y Perfil	27](#sprint-1:-infraestructura,-autenticación-y-perfil)

[Sprint 2: Configuración de Estudio y Lecturas con IA	28](#sprint-2:-configuración-de-estudio-y-lecturas-con-ia)

[Sprint 3: Vocabulario Contextual y Evaluación por PNL	29](#sprint-3:-vocabulario-contextual-y-evaluación-por-pnl)

[Sprint 4: Historial, Rachas y Panel Administrativo	31](#sprint-4:-historial,-rachas-y-panel-administrativo)

[/Sprint 5: Pruebas, Tagging v1.0.0 y Cierre del Proyecto	31](#sprint-5:-pruebas,-tagging-v1.0.0-y-cierre-del-proyecto)

[14\. Elección de estructura web y tecnologías.	33](#14.-elección-de-estructura-web-y-tecnologías.)

[**16\. Selección de patrones de diseño.	34**](#16.-selección-de-patrones-de-diseño.)

[Patrones de Diseño en el Backend (NestJS)	34](#patrones-de-diseño-en-el-backend-\(nestjs\))

[Patrones de Diseño en el Frontend (Next.js)	34](#patrones-de-diseño-en-el-frontend-\(next.js\))

[17\. Wireframes.	35](#17.-wireframes.)

[18\. Fuentes.	36](#18.-fuentes.)

# 

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

De esta manera, Dolynglish se posiciona como una **herramienta complementaria** orientada a usuarios que buscan superar las limitaciones de las aplicaciones tradicionales, integrando **vocabulario, gramática y comprensión lectora** en una sola propuesta de valor.

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

# 

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
* Selección de Ruta de Estudio: Al ingresar, el usuario selecciona el idioma que desea practicar entre las cuatro opciones iniciales (inglés o español).  
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
Las contraseñas de los usuarios no deberán almacenarse en texto plano. El sistema deberá utilizar mecanismos de hashing criptográfico seguros y adecuados para el almacenamiento de credenciales con el uso de bcrypt.

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

| ID | Tipo de problema | Probabilidad | Impacto | Puntuación | Nivel de riesgo | Consecuencia  | Respuesta ante el problema  | Estrategia de respuesta  |
| :---- | :---- | :---: | :---: | :---: | :---: | ----- | ----- | ----- |
| R1 | Costos elevados por consultas excesivas de IA (análisis por palabra o contexto en cada lectura) | 4 | 4 | 16 | Crítico | La aplicación podría presentar incomodidad a los usuarios ante limitaciones | Suspender temporalmente funciones no esenciales y avisar al equipo para priorizar el presupuesto restante |  MITIGAR  |
| R2 | Dependencia de servicios externos de IA (costos y disponibilidad) | 3 | 4 | 12 | Alto | La plataforma queda inutilizable si el proveedor cae o cambia condiciones | Activar un modo degradado (contenido pregenerado o funciones básicas sin IA) mientras se resuelve | MITIGAR  |
| R3 | Latencia en la generación y evaluación de contenido por IA | 4 | 3 | 12 | Alto | Mala experiencia de usuario, abandono de la sesión de estudio | Mostrar indicadores de carga y mensajes claros al usuario mientras se procesa | MITIGAR |
| R4 | Precisión de la calificación automática de comprensión lectora | 3 | 4 | 12 | Alto | Mala experiencia de usuario, abandono de la sesión de estudio | Permitir que el usuario reporte una calificación como incorrecta para revisión manual | MITIGAR |
| R5 | Explicaciones de vocabulario o contexto generadas por IA poco acertadas | 3 | 4 | 12 | Alto | Usuarios reciben calificaciones injustas o poco confiables, perdiendo confianza en la plataforma | Habilitar un botón de "reportar error" en cada explicación mostrada | MITIGAR |
| R6 | Abuso del sistema por usuarios no verificados mediante múltiples cuentas | 3 | 4 | 12 | Alto | El usuario aprende información incorrecta, afectando la calidad educativa | Suspender temporalmente cuentas sospechosas hasta verificación | MITIGAR |
| R7 | Crecimiento no controlado del alcance del proyecto (scope creep) | 4 | 3 | 12 | Alto | Retrasos en la entrega y funcionalidades del MVP incompletas | Mantener un backlog separado para ideas futuras y aplicar control de cambios formal en reuniones de equipo  | EVITAR |
| R8 | Alcance limitado por el tiempo disponible del equipo | 3 | 4 | 12 | Alto | Funcionalidades planeadas quedan fuera de la entrega final | Reevaluar el alcance en cada iteración y pausar nuevas ideas hasta cerrar el MVP | MITIGAR |
| R9 | Seguridad de la información del usuario (credenciales, progreso) | 2 | 5 | 10 | Medio | Filtración de datos personales o credenciales, pérdida de confianza y posibles implicaciones legales | Repriorizar el backlog dejando sólo lo esencial del MVP | TRANSFERIR |
| R10 | Calidad inconsistente del contenido generado por IA | 3 | 3 | 9 | Medio | Textos con errores gramaticales o poco naturales, afectando el aprendizaje | Notificar a los usuarios afectados y revocar/forzar cambio de credenciales de inmediato | MITIGAR |
| R11 | Baja adopción o retención de usuarios | 3 | 3 | 9 | Medio | Textos con errores gramaticales o poco naturales, afectando el aprendizaje | Filtrar o descartar contenido antes de mostrarlo si no pasa validaciones básicas | MITIGAR |
| R12 | Mezcla de idiomas en las lecturas generadas por IA | 2 | 4 | 8 | Medio | El proyecto no logra validar su propuesta de valor con usuarios reales | Recoger retroalimentación temprana y ajustar la propuesta de valor según hallazgos | MITIGAR |
| R13 | Rotación o salida de un integrante del equipo a mitad del proyecto | 2 | 4 | 8 | Medio | Confunde al usuario y reduce la calidad percibida del contenido | Descartar automáticamente el texto generado si se detecta mezcla de idiomas | ACEPTAR |
| R14 | Escalabilidad de la infraestructura ante crecimiento de usuarios | 2 | 3 | 6 | Medio | Pérdida de conocimiento técnico y retraso en tareas asignadas | Redistribuir tareas entre el resto del equipo de inmediato | MITIGAR |
| R15 | Cambios en políticas o precios de proveedores de IA | 2 | 3 | 6 | Medio | Caídas o lentitud del sistema al aumentar los usuarios | Escalar recursos manualmente de forma reactiva mientras se ajusta la arquitectura | ACEPTAR |
| R16 | Lecturas repetitivas o poco variadas en temática | 3 | 2 | 6 | Medio | El usuario pierde interés por falta de variedad en el contenido | Ampliar temporalmente las categorías o parámetros de generación disponibles | MITIGAR |

# **11\. Elección de metodología y roles del equipo** {#11.-elección-de-metodología-y-roles-del-equipo}

### **11.1. Metodología de trabajo** {#11.1.-metodología-de-trabajo}

Para el desarrollo del proyecto **DolyNation** se implementa el marco de trabajo **Scrum** combinado con un flujo de desarrollo guiado por tareas en GitHub (*Issue-Driven Development*). El proyecto se divide en 5 Sprints con fechas estrictas de entrega que abarcan desde el 05 de octubre hasta el 10 de diciembre de 2026\.

### **11.2. Estructura de roles y responsabilidades** {#11.2.-estructura-de-roles-y-responsabilidades}

* **Product Owner:** Sebastián  
  * **Responsabilidades:** Definición y validación de historias de usuario, priorización del backlog de productos, diseño de prompts para los modelos de Inteligencia Artificial y validación de criterios de aceptación de los entregables.  
* **Scrum Master / Lead Developer:** Jesús Alberto Villarreal Pérez  
  * **Responsabilidades:** Coordinación del flujo de trabajo en GitHub, configuración de políticas de integración continua (CI/CD), revisión de Pull Requests, tagging de releases y apoyo en desarrollo técnico estratégico (Frontend/Backend).  
* **Desarrollador Frontend:** Juan Antonio Deras Durón  
  * **Responsabilidades:** Maquetado responsivo en Next.js, integración de Tailwind CSS, diseño de componentes de interfaz (visor de lectura, pop-ups contextuales, dashboard de usuario).  
* **Desarrollador Backend (Principal):** Aozmar Azael García Candela  
  * **Responsabilidades:** Arquitectura de microservicios y módulos en NestJS, lógica de autenticación criptográfica, conector con APIs de IA (OpenAI/Gemini) y motor de evaluación de resúmenes.  
* **Desarrollador Backend (Soporte):** José Elías Galarza Pedroza  
  * **Responsabilidades:** Diseño de DTOs, controladores de base de datos (PostgreSQL/MongoDB), endpoints para perfiles, historial de actividades y módulo administrativo.

## **12\. Separación del proyecto en tareas** {#12.-separación-del-proyecto-en-tareas}

El proyecto contempla un total de **33 tareas técnicas** derivadas directamente de los requerimientos funcionales y del MVP. Las tareas están divididas por capas técnicas, donde los desarrolladores Backend y Frontend trabajan en sus áreas específicas y colaboran en tareas parejas para la integración de la API con la interfaz de usuario.

### **Resumen de distribución de tareas** {#resumen-de-distribución-de-tareas}

| Persona | Rol | Tareas Individuales | Tareas en Pareja | Total Tareas |
| :---- | :---- | :---- | :---- | :---- |
| **Sebastián** | Product Owner | — | — | *Supervisión y Validaciones* |
| **Jesús Alberto Villarreal Pérez** | Scrum Master / Dev | 6 | 3 | **9** |
| **Juan Antonio Deras Durón** | Desarrollador Frontend | 9 | 3 | **12** |
| **José Elías Galarza Pedroza** | Desarrollador Backend | 6 | 3 | **9** |
| **Aozmar Azael García Candela** | Desarrollador Backend | 5 | 3 | **8** |
| **Todo el equipo** | Trabajo colaborativo | 1 | — | **1** |

### 

## **13\. Cronograma de actividades** {#13.-cronograma-de-actividades}

[*Referencia visual*](https://github.com/orgs/DolyLanguagesORG/projects/1/views/3)

### **13.1. Hitos del proyecto** {#13.1.-hitos-del-proyecto}

* **Sprint 1 (05/Oct – 18/Oct/2026):** Infraestructura Base, Autenticación y Perfil.  
* **Sprint 2 (19/Oct – 01/Nov/2026):** Configuración de Estudio y Lecturas con IA.  
* **Sprint 3 (02/Nov – 15/Nov/2026):** Vocabulario Contextual e Integración de PNL.  
* **Sprint 4 (16/Nov – 29/Nov/2026):** Historial, Rachas y Panel Administrativo.  
* **Sprint 5 (30/Nov – 10/Dic/2026):** Pruebas, Tagging v1.0.0 y Release de Cierre.

### **13.2. Tabla de asignación de tareas y cronograma** {#13.2.-tabla-de-asignación-de-tareas-y-cronograma}

> **Referencia de issues.** Al separar el monorepo en cuatro repos, cada tarea es un issue en su repositorio. El identificador `back#N`, `front#N`, `infra#N` o `docs#N` indica el repo (`dolynation-atl-back`, `dolynation-tonatiuh-front`, `dolynation-tlalli-infra`, `dolynation-ehecatl-docs`) y el número del issue.

#### **Sprint 1: Infraestructura, Autenticación y Perfil** {#sprint-1:-infraestructura,-autenticación-y-perfil}

**Periodo:** 05 de Octubre al 18 de Octubre de 2026

| Issue | Tarea / Descripción | Responsable | Fecha Inicio | Fecha Entrega |
| :---- | :---- | :---- | :---- | :---- |
| **infra#2** | Configuración del repositorio: main/develop, branch protection, plantillas y CI/CD | Jesús (SM) | 05 oct 2026 | 06 oct 2026 |
| **back#2** | Setup de arquitectura NestJS, conexión a base de datos y entidad User | Azael | 05 oct 2026 | 08 oct 2026 |
| **front#2** | Setup de proyecto Next.js con Tailwind CSS, layout base y temas | Juan | 05 oct 2026 | 07 oct 2026 |
| **back#3** | Servicio de hash criptográfico (bcrypt/Argon2) y estrategia JWT | Azael | 09 oct 2026 | 12 oct 2026 |
| **back#4** | DTOs de validación de registro/login y endpoints de autenticación | Elías | 09 oct 2026 | 12 oct 2026 |
| **front#3** | Maquetado e integración de vistas de login y registro en Next.js | Juan | 08 oct 2026 | 12 oct 2026 |
| **back#5** | Endpoints para consultar y actualizar el perfil de usuario | Elías | 13 oct 2026 | 15 oct 2026 |
| **front#4** | Vista del perfil de usuario e integración con estado de sesión | Juan | 13 oct 2026 | 16 oct 2026 |
| **back#6** | Pruebas de integración del Sprint 1 y revisión de PRs hacia develop | Jesús (SM) | 16 oct 2026 | 18 oct 2026 |

#### 

#### 

#### 

#### 

#### 

#### 

#### **Sprint 2: Configuración de Estudio y Lecturas con IA** {#sprint-2:-configuración-de-estudio-y-lecturas-con-ia}

**Periodo:** 19 de Octubre al 01 de Noviembre de 2026

| Issue | Tarea / Descripción | Responsable | Fecha Inicio | Fecha Entrega |
| :---- | :---- | :---- | :---- | :---- |
| **back#7** | Módulo de servicios en NestJS para integración con API de IA y prompts | Azael | 19 oct 2026 | 23 oct 2026 |
| **back#8** | Endpoints para selección y guardado de categorías e idiomas |  |  | 22 oct 2026 |
| **front#5** | Formulario de selección de parámetros de estudio en Next.js | Juan | 19 oct 2026 | 23 oct 2026 |
| **back#9** | Servicio de caché para respuestas de lectura con parámetros equivalentes | Jesús (SM) | 22 oct 2026 | 26 oct 2026 |
| **front#6** | Visor inmersivo de lectura centrado en legibilidad en Next.js | Juan | 24 oct 2026 | 28 oct 2026 |
| **back#10** | Endpoint de generación de lectura basada en parámetros | Azael \+ Elías | 24 oct 2026 | 28 oct 2026 |
| **front#7** | Conexión del flujo completo: Formulario $\rightarrow$ IA $\rightarrow$ Visor | Jesús \+ Juan | 29 oct 2026 | 01 nov 2026 |

#### **Sprint 3: Vocabulario Contextual y Evaluación por PNL** {#sprint-3:-vocabulario-contextual-y-evaluación-por-pnl}

**Periodo:** 02 de Noviembre al 15 de Noviembre de 2026

| Issue | Tarea / Descripción | Responsable | Fecha Inicio | Fecha Entrega |
| :---- | :---- | :---- | :---- | :---- |
| **front#8** | Captura e interacción de selección de texto dentro del visor | Juan | 02 nov 2026 | 05 nov 2026 |
| **back#11** | Endpoint de consulta contextual de vocabulario a la IA | Azael | 02 nov 2026 | 06 nov 2026 |
| **front#9** | Pop-up de diccionario contextual e integración de audio corto (TTS) | Juan | 06 nov 2026 | 09 nov 2026 |
| **front#10** | Componente de área de redacción libre de resumen y envío | Juan \+ Elías | 07 nov 2026 | 10 nov 2026 |
| **back#12** | Servicio de evaluación y calificación por PNL en NestJS | Jesús \+ Azael | 06 nov 2026 | 11 nov 2026 |
| **back#13** | Endpoint de procesamiento y almacenamiento de la evaluación | Elías | 10 nov 2026 | 13 nov 2026 |
| **back#14** | Pruebas del módulo de vocabulario y evaluación por PNL | Jesús (SM) | 13 nov 2026 | 15 nov 2026 |

#### **Sprint 4: Historial, Rachas y Panel Administrativo** {#sprint-4:-historial,-rachas-y-panel-administrativo}

**Periodo:** 16 de Noviembre al 29 de Noviembre de 2026

| Issue | Tarea / Descripción | Responsable | Fecha Inicio | Fecha Entrega |
| :---- | :---- | :---- | :---- | :---- |
| **back#15** | Lógica de cálculo de racha diaria y asignación de puntos en NestJS | Azael | 16 nov 2026 | 19 nov 2026 |
| **back#16** | Endpoints de consulta de historial de actividades y calificaciones | Elías | 16 nov 2026 | 20 nov 2026 |
| **front#11** | Dashboard de usuario (métricas, racha, historial y puntos) | Juan | 19 nov 2026 | 24 nov 2026 |
| **back#17** | Endpoints para gestión administrativa de categorías globales | Elías | 21 nov 2026 | 25 nov 2026 |
| **front#12** | Vista del panel administrativo básico en Next.js | Juan \+ Jesús | 24 nov 2026 | 27 nov 2026 |
| **infra#3** | Revisión general de código, limpieza de endpoints y merge a develop | Jesús (SM) | 27 nov 2026 | 29 nov 2026 |

#### 

#### 

#### **Sprint 5: Pruebas, Tagging v1.0.0 y Cierre del Proyecto** {#sprint-5:-pruebas,-tagging-v1.0.0-y-cierre-del-proyecto}

**Periodo:** 30 de Noviembre al 10 de Diciembre de 2026

| Issue | Tarea / Descripción | Responsable | Fecha Inicio | Fecha Entrega |
| :---- | :---- | :---- | :---- | :---- |
| **front#13** | Pruebas de usabilidad y revisión de diseño responsivo | Juan | 30 nov 2026 | 03 dic 2026 |
| **back#18** | Pruebas de rendimiento, manejo de errores de IA y seguridad | Azael \+ Elías | 30 nov 2026 | 04 dic 2026 |
| **infra#4** | PR final develop $\rightarrow$ main, tagging v1.0.0 y verificación CI/CD | Jesús (SM) | 04 dic 2026 | 06 dic 2026 |
| **docs#3** | Documentación final, capturas del sistema y presentación | Todo el equipo | 06 dic 2026 |  |

## **14\. Elección de estructura web y tecnologías.** {#14.-elección-de-estructura-web-y-tecnologías.}

Para cumplir con la arquitectura cliente-servidor modular descrita en el proyecto, se ha seleccionado un stack tecnológico moderno, robusto y altamente tipado (TypeScript de extremo a extremo), optimizado para un entorno de despliegue propio (**Self-host**):

* **Frontend (Cliente Web):** **Next.js**  
  * *Justificación:* Permite construir una interfaz web responsiva y optimizada para la lectura, ofreciendo capacidades de renderizado avanzado (SSR/SSG) para mejorar el rendimiento y garantizar una experiencia de usuario limpia y sin distracciones.  
* **Backend (API y Lógica de Negocio):** **NestJS**  
  * *Justificación:* Framework de Node.js diseñado bajo una arquitectura fuertemente modular, ideal para separar responsabilidades (usuarios, contenidos, evaluaciones, etc.) y facilitar la integración escalable con servicios externos de inteligencia artificial.  
* **Capa de Acceso a Datos (ORM):** **Prisma ORM**  
  * *Justificación:* Proporciona seguridad de tipos e interactúa de manera eficiente con la base de datos, agilizando las migraciones y la estructuración de las consultas.  
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

[image1]: <data:image/png;base64,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>