source venv/bin/activate

echo "Generando lexer, parser y visitor"

# Verificar que existe el JAR de ANTLR
JAR_PATH="/usr/local/lib/antlr-4.13.2-complete.jar"
if [[ ! -f "$JAR_PATH" ]]; then
    echo "📥 Descargando ANTLR 4.13.2..."
    sudo curl -L -o "$JAR_PATH" \
        "https://www.antlr.org/download/antlr-4.13.2-complete.jar"
fi

# Limpiar archivos anteriores
rm -f gramaticas/RISCO*.py
rm -rf generado

# Generar con ANTLR
java -jar "$JAR_PATH" \
    -Dlanguage=Python3 \
    -visitor \
    -no-listener \
    -o generado \
    gramaticas/RISCO.g4

if [[ $? -eq 0 ]]; then
    
    # Mover archivos generados
    cp generado/gramaticas/*.py gramaticas/
    
    # Crear __init__.py
    touch gramaticas/__init__.py
    
    # Limpiar
    rm -rf generado
    
    echo "Archivos generados:"
    ls -la gramaticas/RISCO*.py
else
    echo "❌ Error en generación"
    exit 1
fi
