# Script para generar código ANTLR
source venv/bin/activate


# Limpiar archivos anteriores
rm -f gramaticas/RISCO*.py   
rm -rf generado

# Generar con ANTLR
java -jar /usr/local/lib/antlr-4.13.2-complete.jar \
    -Dlanguage=Python3 \
    -visitor \
    -no-listener \
    -o generado \
    gramaticas/RISCO.g4    

if [ $? -eq 0 ]; then
    echo "LEXER, PARSER Y VISITOR HECHO"
    
    # Mover archivos generados
    cp generado/gramaticas/*.py gramaticas/
    
    # Crear __init__.py
    touch gramaticas/__init__.py
    
    # Limpiar
    rm -rf generado
    
    ls -la gramaticas/RISCO*.py   # ← CAMBIADO
else
    echo "Error en generación"
    exit 1
fi