import sys
import os

# Asegurar que podemos importar desde el directorio padre
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr4 import *
from gramaticas.RISCOLexer import RISCOLexer         
from gramaticas.RISCOParser import RISCOParser        
from src.visitante_evaluador import VisitanteEvaluador

class RISCO:
    """
    Intérprete principal del lenguaje RISCO
    """
    
    def __init__(self):
        self.visitante = VisitanteEvaluador()
        
    def ejecutar_archivo(self, ruta_archivo):
        """
        Ejecuta un archivo .risco
        """
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                codigo = f.read()
            self._ejecutar_codigo(codigo)
        except FileNotFoundError:
            print(f"Error: No se encuentra el archivo '{ruta_archivo}'")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    def _ejecutar_codigo(self, codigo):
        """
        Ejecuta código fuente directamente
        """
        # Asegurar que termina con newline
        if not codigo.endswith('\n'):
            codigo += '\n'
        
        # Configurar entrada
        entrada = InputStream(codigo)
        
        # Lexer
        lexer = RISCOLexer(entrada)                 
        
        # Token stream
        tokens = CommonTokenStream(lexer)
        
        # Parser
        parser = RISCOParser(tokens)                 
        
        # Parsear
        try:
            arbol = parser.programa()
        except Exception as e:
            print(f"Error durante el parseo: {e}")
            return
        
        # Evaluar
        try:
            self.visitante.visit(arbol)
        except Exception as e:
            print(f"Error en evaluación: {e}")
    
    def modo_interactivo(self):
        """
        Modo REPL interactivo
        """
        print("RISCO v1.0 - Modo interactivo")
        print("Escribe expresiones o 'salir' para terminar")
        print("-" * 50)
        
        while True:
            try:
                linea = input("risco> ").strip()  
                
                if not linea:
                    continue
                
                if linea.lower() in ('salir', 'exit', 'quit'):
                    break
                
                self._ejecutar_codigo(linea + '\n')
                
            except KeyboardInterrupt:
                print("\n¡Hasta luego!")
                break
            except Exception as e:
                print(f"Error: {e}")

def main():
    if len(sys.argv) > 1:
        lenguaje = RISCO()                          
        lenguaje.ejecutar_archivo(sys.argv[1])
    else:
        lenguaje = RISCO()                       
        lenguaje.modo_interactivo()

if __name__ == "__main__":
    main()