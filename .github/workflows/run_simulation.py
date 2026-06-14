name: Ejecutar Simulación de Ruleta

on:
  push:
    branches: [ main, master ]  # Se ejecuta cada vez que subes código
  workflow_dispatch:            # Te permite ejecutarlo manualmente con un botón desde la web de GitHub

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Descargar el repositorio
      uses: actions/checkout@v4

    - name: Configurar Python 3.13
      uses: actions/setup-python@v5
      with:
        python-version: '3.13'

    - name: Ejecutar Script de la Ruleta
      run: python ruleta.py
