from mem import Memory
import os


config={
    "version":"v1.1",
    "embedder":{
        "provider":"openai",
        "config":{
            "api_key":"your_openai_api_key_here", "model":"text-embedding-3-small"
        },
        "llm":{
            "provider":"openai",
            "config":{
                "api_key":"your_openai_api_key_here", "model":"gpt-4o"
            }
        },
        "graph_store":{
            "provider":"neo4j",
            "config":{
                "connection_uri":"your_neo4j_connection_uri_here", 
                "username":"your_neo4j_username_here", 
                "password":"your_neo4j_password_here"
            }
        },
        "vector_store":{
            "provider":"qdrant",
            "config":{
                "host":"localhost", 
                "port":6333
            }
        }

    }
}

mem_client = Memory.from_config(config)
while True:

    user_query = input (">")
    search_memory = mem_client.search(query= user_query, user_id="user_1", top_k=3)
    memories = [
        f"ID:{mem.get("id")} \n Memory:{mem.get("memory")}"
        for mem in search_memory.get("results")
    ]
    print("Found Memories:",memories)

    SYSTEM_PROMPT = f"""
You are a helpful assistant that retrieves relevant memories from a memory graph and provides answers based on those memories.
{json.dumps(memories, indent=2)}
"""
 