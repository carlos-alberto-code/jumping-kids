# Inicio Rápido

## Requisitos

Para comenzar con el proyecto, asegúrate de tener instalado Visual Studio Code (VSCode) y las siguientes extensiones, ya que estamos utilizando GitHub Codespaces:

- [GitHub Codespaces](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces)

## Configuración del Entorno

Este contenedor está configurado para instalar las siguientes herramientas:

- Python 3.11
- Poetry 1.8
- SQLite3

## Instalación de Dependencias

Una vez que tengas el Codespace inicializado en tu máquina, sigue estos pasos para instalar las dependencias internas gestionadas con Poetry:

1. Abre una terminal en VSCode.
2. Ejecuta el siguiente comando para activar el entorno de Poetry:
    ```sh
    poetry shell
    ```
3. Una vez activado el entorno, instala las dependencias con:
    ```sh
    poetry install
    ```

Con estos pasos, tendrás todas las dependencias necesarias para trabajar en el proyecto.