# Money Exchange Between User$ (M.E.B.U.)
## app-mebu-bootcamp-ecom
Sistema de intercambio de dinero ficticio entre usuarios, desarrollada para cumplir con el desafío final en el bootcamp de python de ECOM en 2024

## **Descripción del Proyecto**
Money Exchange es un sistema web diseñado para facilitar el intercambio de dinero entre usuarios registrados. A través de esta plataforma, los usuarios pueden visualizar su saldo, realizar transferencias a otros usuarios, mantener un historial de movimientos y marcar usuarios frecuentes para agilizar futuras transacciones. Además, los administradores tienen acceso a herramientas de gestión para la administración de usuarios y motivos de transferencia.

## **Instrucciones para Configurar y Ejecutar el Proyecto**

### **Requisitos Previos**
- **Python 3.12+**
- **Django 5.0**
- **PostgreSQL**
- **Git**

### **Estructura de Variables de Entorno**
Crea una carpeta **env** que contenga un archivo **.env** en la raíz del proyecto siguiendo con la estructura del archivo que se encuentra dentro de la carpeta **env_guia**.

### **Instalación de Dependencias**
En la carpeta **requirements** se encuentra el archivo con las dependecias necesarias para ejecutar el proyecto.


## **Funcionalidades Desarrolladas**
- :heavy_check_mark: Usuarios No Registrados.
- :heavy_check_mark: Registro de cuenta.
- :heavy_check_mark: Iniciar sesión en el sistema.

## **Usuarios Registrados**
- :heavy_check_mark: Visualización del saldo de la cuenta.
- :heavy_check_mark: Cambio de foto de perfil y edición de datos personales.
- :heavy_check_mark: Ingreso de dinero a la cuenta.
- :heavy_check_mark: Transferencias de dinero a otros usuarios registrados, con selección de motivo desde una lista predefinida.
- :heavy_check_mark: Visualización de comprobantes de transferencias desde la interfaz web.
- :heavy_check_mark: Marcar usuarios como favoritos para agilizar futuras transferencias.
- :heavy_check_mark: Consulta del historial de movimientos, incluyendo ingresos y transferencias realizadas y recibidas.

## **Usuarios Administradores**
- :heavy_check_mark: Visualización de la lista completa de usuarios.
- :heavy_check_mark: Buscador por nombre o apellido en la lista de usuarios.
- :heavy_check_mark: Activación o desactivación de cuentas de usuarios.
- :heavy_check_mark: Edición de información de usuarios.
- :heavy_check_mark: Revisión de detalles de cuentas y movimientos de cada usuario.
- :x: Gestión de motivos de transferencia (CRUD).