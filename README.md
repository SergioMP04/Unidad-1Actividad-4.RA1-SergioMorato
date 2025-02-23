# Informe de Prueba en Entorno Controlado

# Índice

- [Informe de Prueba en Entorno Controlado](#informe-de-prueba-en-entorno-controlado)
- [Índice](#índice)
  - [**Introducción**](#introducción)
  - [Consideraciones previas](#consideraciones-previas)
    - [1. Windows Sandbox](#1-windows-sandbox)
    - [2. Sandboxie Plus](#2-sandboxie-plus)
    - [3. Máquinas Virtuales](#3-máquinas-virtuales)
  - [Sandboxie Plus](#sandboxie-plus)
    - [**1. Descargar e instalar Sandboxie Plus**](#1-descargar-e-instalar-sandboxie-plus)
    - [**2. Ejecutar la aplicación en Sandboxie Plus**](#2-ejecutar-la-aplicación-en-sandboxie-plus)
    - [**3. Verificar y cerrar el entorno aislado**](#3-verificar-y-cerrar-el-entorno-aislado)
  - [**Resultados y Observaciones**](#resultados-y-observaciones)
  - [**Conclusión**](#conclusión)

## **Introducción**

En este informe se documenta la prueba de la aplicación de calculadora en un entorno controlado utilizando Sandboxie Plus. El objetivo es verificar su funcionamiento en un entorno aislado sin afectar el sistema principal.

## Consideraciones previas

Para probar aplicaciones en un entorno seguro y aislado, dispones de varias alternativas que te permiten ejecutar programas sin riesgo para tu sistema principal. A continuación, se detallan algunas de las opciones más destacadas:

### 1. Windows Sandbox

Windows Sandbox es una característica integrada en las ediciones Pro y Enterprise de Windows 10 y Windows 11. Proporciona un entorno de escritorio ligero y temporal donde puedes ejecutar aplicaciones de forma aislada.
Al cerrar el Sandbox, todo el contenido se elimina permanentemente, asegurando que no queden rastros en el sistema principal. Para activarlo, debes acceder a las "Características de Windows" y habilitar "Espacio aislado de Windows".
Es importante destacar que esta función no está disponible en la edición Home de Windows.

### 2. Sandboxie Plus

Sandboxie Plus es una herramienta gratuita y de código abierto que crea un entorno operativo aislado en Windows. Permite ejecutar o instalar aplicaciones sin que estas modifiquen permanentemente el sistema local. Originalmente lanzado en 2004, Sandboxie ha evolucionado y, tras ser liberado como software libre, ha dado lugar a Sandboxie Plus, que ofrece una interfaz más moderna y funcionalidades adicionales. Es compatible con diversas versiones de Windows y es ideal para probar aplicaciones de manera segura.

### 3. Máquinas Virtuales

Otra alternativa es utilizar software de virtualización como VirtualBox o VMware. Estas herramientas permiten crear máquinas virtuales en las que puedes instalar un sistema operativo completo y probar aplicaciones en un entorno completamente aislado. Aunque consumen más recursos que las opciones anteriores, ofrecen un alto nivel de seguridad y flexibilidad.

## Sandboxie Plus

Para esta práctica yo he decidido usar Sandboxie por su simplicidad y comodidad, a continuaci´on se describe la realización de la práctica.

### **1. Descargar e instalar Sandboxie Plus**

1. Ir a la página oficial de [Sandboxie Plus](https://sandboxie-plus.com/downloads/).
2. Descargar la versión más reciente e instalarla.
3. Seguir los pasos del asistente de instalación.

<p align="center">
    <img src="Imagenes\Instalacion1.png" alt="Config Nano">
    <img src="Imagenes\Instalacion2.png" alt="Config Nano">
</p>

### **2. Ejecutar la aplicación en Sandboxie Plus**

1. Abrir **Sandboxie Plus**.

<p align="center">
    <img src="Imagenes\Sand1.png" alt="Config Nano">
</p>
Aqui podemos ver que sandboxie nos tendrá creada una sandbox por defecto.

1. En la interfaz principal, hacer clic en **Ejecutar programa > Ejecutar en Sandboxie**.

<p align="center">
    <img src="Imagenes\Sand2.png" alt="Config Nano">
</p>

2. Seleccionar el ejecutable de la calculadora, adjuntaremos la ruta al archivo que queremos ejecutar.

```bash
python -u "c:\Users\Sergio\Desktop\CECETI\PPS\Tema2\Unidad 1Actividad 4.RA1-SergioMorato\source\pruebas.py"
```

<p align="center">
    <img src="Imagenes\Sand3.png" alt="Config Nano">
</p>

### **3. Verificar y cerrar el entorno aislado**

1. Usar la aplicación y comprobar su correcto funcionamiento.
2. Al finalizar, cerrar la aplicación y borrar los contenidos del sandbox desde Sandboxie Plus.

<p align="center">
    <img src="Imagenes\Sand5.png" alt="Config Nano">
</p>

---

## **Resultados y Observaciones**

Durante la ejecución de la prueba, la calculadora funcionó correctamente dentro del entorno aislado sin afectar el sistema principal. Se pudo realizar operaciones matemáticas básicas y la interfaz respondió sin errores.

La funcionalidad de aislamiento de Sandboxie Plus garantizó que no quedaran rastros de la aplicación una vez finalizada la prueba y eliminados los datos del entorno sandbox.

---

## **Conclusión**

Se ha demostrado que Sandboxie Plus es una herramienta efectiva para ejecutar aplicaciones en un entorno controlado. La prueba de la calculadora se realizó con éxito, asegurando su funcionamiento sin comprometer la seguridad del sistema anfitrión.

---
**Autor**
Sergio Morato Prieto
