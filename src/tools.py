from langchain.tools import tool
from src.connector import run_query

@tool
def query_hive_tool(sql_query: str) -> str:
    """
    Útil para consultar el Data Lake en Hive. 
    Recibe una sentencia SQL válida para HiveQL y devuelve los resultados.
    """
    try:
        data, columns = run_query(sql_query)
        return f"Columnas: {columns}\nDatos: {data[:10]}" # Limitamos para no saturar el prompt
    except Exception as e:
        return f"Error ejecutando SQL: {str(e)}"