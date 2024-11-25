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
- Usuarios No Registrados (si)
- Registro de cuenta. (si)
- Iniciar sesión en el sistema. (si)

## **Usuarios Registrados**
- Visualización del saldo de la cuenta. (si)
- Cambio de foto de perfil y edición de datos personales. (casi)
- Ingreso de dinero a la cuenta. (si)
- Transferencias de dinero a otros usuarios registrados, con selección de motivo desde una lista predefinida. (si)
- Visualización de comprobantes de transferencias desde la interfaz web. (si)
- Marcar usuarios como favoritos para agilizar futuras transferencias. (casi)
- Consulta del historial de movimientos, incluyendo ingresos y transferencias realizadas y recibidas. (casi)

## **Usuarios Administradores**
- Visualización de la lista completa de usuarios. (no)
- Activación o desactivación de cuentas de usuarios. (no)
- Edición de información de usuarios. (no)
- Revisión de detalles de cuentas y movimientos de cada usuario. (no)
- Gestión de motivos de transferencia (CRUD). (no)