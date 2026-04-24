import anthropic
import os
import sys

# Intenta obtener la API KEY de una variable de entorno
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY", "TU_CLAVE_AQUI")
)

def probar_modelo(model_name, prompt):
    print(f"\n--- Probando modelo: {model_name} ---")
    try:
        message = client.messages.create(
            model=model_name,
            max_tokens=1000,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        )
        print(f"Respuesta:\n{message.content[0].text}")
    except Exception as e:
        print(f"Error al llamar a {model_name}: {e}")

if __name__ == "__main__":
    test_prompt = "¿Cuáles son las 3 leyes de la robótica?"
    
    # Modelos de Anthropic
    models = [
        "claude-3-5-sonnet-20240620",  # Sonnet 3.5 (el más rápido y actual)
        "claude-3-opus-20240229"       # Opus (el más inteligente de la serie 3)
    ]
    
    if os.environ.get("ANTHROPIC_API_KEY") is None:
        print("AVISO: No detecto la variable ANTHROPIC_API_KEY.")
        print("Por favor, ejecuta: export ANTHROPIC_API_KEY='tu_clave_aqui'")
        sys.exit(1)

    for m in models:
        probar_modelo(m, test_prompt)
