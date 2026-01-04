import requests, os
import numpy as np
from chromadb import HttpClient
from dotenv import load_dotenv
load_dotenv()

def search_chroma(query_text):
    query_emb = generate_embeddings_single(query_text)
    result = collection.query(query_embeddings=[query_emb], n_results=2, include=["documents"])
    print(result)

def generate_embeddings_single(text):
    url = "https://api.euron.one/api/v1/euri/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"{EURI_API_KEY}"
    }
    payload = {
        "input": text,
        "model": "text-embedding-3-small"
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    
    embedding = np.array(data['data'][0]['embedding'])
    # embeddings = [item["embedding"] for item in response.json()["data"]]
    
    return embedding

def generate_embeddings(text_list):
    url = "https://api.euron.one/api/v1/euri/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"{EURI_API_KEY}"
    }
    payload = {
        "input": text_list,
        "model": "text-embedding-3-small"
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    
    # embedding = np.array(data['data'][0]['embedding'])
    embeddings = [item["embedding"] for item in response.json()["data"]]
    
    return embeddings


if __name__ == "__main__":

    text = "The weather is sunny today."
    document = [
                "my name is sudhanshu kumar", 
                "i use to teach tech", 
                "sudhanshu kumar total years of experience as a techie is 11 as a mentor is 7 as a enterpenure is 1006", 
                "sudhanshu kumar love teaching core concepts and architecture", 
                "sudhanshu kumar love build tech which is  his fav by the way", 
                "sudhanshu kumar have started a new company called euron", 
                "Sudhanshu kumar was the founder of ineuron", 
                "Sudhanshu Kumar's life is a story of triumph over adversity, driven by the belief in the transformative power of education. Born in Jamshedpur, Jharkhand, India",
                "His surroundings offered little opportunity, and resources were limited, yet he understood from a young age that education could be his ticket out of poverty.",
                "While many would have been daunted by the lack of support and opportunity, Sudhanshu was relentless in his pursuit of knowledge",
                "He knew that education had the power to change lives, and he was determined to leverage it to create a better future for himself and his family.", 
                "Despite the numerous challenges along the way, Sudhanshu excelled academically, eventually earning a degree in Computer Science and Engineering (CSE)."
    ]

    EURI_API_KEY = os.getenv("EURI_API_KEY")

    client = HttpClient(host="localhost", port=8000)
    collection = client.get_or_create_collection("sudh_euron_data")

    print(f"Connect with Chroma client Successfully >>> {client} \n")

    # all_embedding = generate_embeddings(document)
    # print("EMBEDDINGS ARE >>>>>>>>>>>>>> \n")
    # print(f"Length of embeddings = {len(all_embedding[0])}  >>> {all_embedding[0]}")

    # for idx, (doc, emb) in enumerate(zip(document, all_embedding)):
    #     collection.add(
    #         documents= [doc], 
    #         embeddings= [emb],
    #         metadatas=[{"source":"sudh_euron_data"}],
    #         ids = [f"doc_{idx}"]
    #     )
    # print("All data stored successfully in chroma db!")

    # Fetching all data from the db
    # print(collection.get(include=["documents", "embeddings"]))

    # Searching from ChromaDB
    search_chroma("My name is sudhanshu kumar")
