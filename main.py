from src.agent_logic import setup_agent

def main():
    print(" Agente Hive-IA conectado al clúster EMR")
    agent_executor = setup_agent()
    
    while True:
        user_input = input("\nPregunta sobre el Titanic (o 'salir'): ")
        if user_input.lower() == 'salir': break
        
        response = agent_executor.invoke({"input": user_input})
        print(f"\nRespuesta: {response['output']}")

if __name__ == "__main__":
    main()