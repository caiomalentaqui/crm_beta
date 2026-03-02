#!/usr/bin/env python3
"""
CRUD simples para "Jogos de Videogame" usando MongoDB (PyMongo).
Cole em games_crud.py e rode: python games_crud.py
"""

import os
import sys
from typing import Optional, List, Dict, Any
from pymongo import MongoClient, errors
from bson.objectid import ObjectId

# CONFIG: pega URI do ambiente ou usa localhost
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGO_DB", "game_catalog")
COLLECTION_NAME = "games"

def get_client(uri: str = MONGO_URI) -> MongoClient:
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        # força a checagem de conexão
        client.server_info()
        return client
    except errors.ServerSelectionTimeoutError as e:
        print("Erro ao conectar no MongoDB:", e)
        sys.exit(1)

def get_collection() -> Any:
    client = get_client()
    db = client[DB_NAME]
    return db[COLLECTION_NAME]

# --- CRUD ---

def create_game(game: Dict[str, Any]) -> str:
    """
    Insere um documento de jogo.
    game exemplo: {"title": "Zelda", "platform": "Switch", "genre": "Adventure", "release_year": 2017}
    Retorna o id do documento inserido (string).
    """
    col = get_collection()
    result = col.insert_one(game)
    return str(result.inserted_id)

def get_game(game_id: str) -> Optional[Dict[str, Any]]:
    col = get_collection()
    try:
        oid = ObjectId(game_id)
    except Exception:
        print("ID inválido")
        return None
    doc = col.find_one({"_id": oid})
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc

def list_games(filter_q: Dict[str, Any] = None, limit: int = 100) -> List[Dict[str, Any]]:
    col = get_collection()
    filter_q = filter_q or {}
    cursor = col.find(filter_q).limit(limit)
    results = []
    for d in cursor:
        d["_id"] = str(d["_id"])
        results.append(d)
    return results

def update_game(game_id: str, updates: Dict[str, Any]) -> bool:
    col = get_collection()
    try:
        oid = ObjectId(game_id)
    except Exception:
        print("ID inválido")
        return False
    # apenas campos permitidos (simples validação)
    allowed = {"title", "platform", "genre", "release_year", "rating", "notes"}
    update_doc = {k: v for k, v in updates.items() if k in allowed}
    if not update_doc:
        print("Nada para atualizar (campos permitidos: title, platform, genre, release_year, rating, notes).")
        return False
    result = col.update_one({"_id": oid}, {"$set": update_doc})
    return result.modified_count > 0

def delete_game(game_id: str) -> bool:
    col = get_collection()
    try:
        oid = ObjectId(game_id)
    except Exception:
        print("ID inválido")
        return False
    result = col.delete_one({"_id": oid})
    return result.deleted_count > 0

# --- CLI simples para testar o CRUD ---
def input_game_data() -> Dict[str, Any]:
    title = input("Título: ").strip()
    platform = input("Plataforma: ").strip()
    genre = input("Gênero: ").strip()
    release_year = input("Ano de lançamento (opcional): ").strip()
    rating = input("Nota (0-10) opcional: ").strip()
    notes = input("Observações (opc): ").strip()

    doc = {"title": title, "platform": platform, "genre": genre}
    if release_year:
        try:
            doc["release_year"] = int(release_year)
        except ValueError:
            doc["release_year"] = release_year
    if rating:
        try:
            doc["rating"] = float(rating)
        except ValueError:
            doc["rating"] = rating
    if notes:
        doc["notes"] = notes
    return doc

def print_game(doc: Dict[str, Any]) -> None:
    print("-" * 40)
    for k, v in doc.items():
        print(f"{k}: {v}")
    print("-" * 40)

def main_menu():
    print("""
== Game Catalog (MongoDB) ==
1) Criar jogo
2) Listar jogos
3) Buscar jogo por ID
4) Atualizar jogo por ID
5) Deletar jogo por ID
6) Sair
""")
    choice = input("Escolha: ").strip()
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            print("== Criar jogo ==")
            doc = input_game_data()
            _id = create_game(doc)
            print("Inserido com _id =", _id)
        elif choice == "2":
            print("== Listar jogos ==")
            games = list_games()
            if not games:
                print("Nenhum jogo encontrado.")
            for g in games:
                print_game(g)
        elif choice == "3":
            game_id = input("Informe o ID do jogo: ").strip()
            g = get_game(game_id)
            if g:
                print_game(g)
            else:
                print("Jogo não encontrado.")
        elif choice == "4":
            game_id = input("ID do jogo para atualizar: ").strip()
            print("Insira somente os campos que quer atualizar; deixe vazio para pular.")
            updates = {}
            for field in ["title", "platform", "genre", "release_year", "rating", "notes"]:
                v = input(f"{field}: ").strip()
                if v:
                    if field in ("release_year",):
                        try:
                            updates[field] = int(v)
                        except:
                            updates[field] = v
                    elif field == "rating":
                        try:
                            updates[field] = float(v)
                        except:
                            updates[field] = v
                    else:
                        updates[field] = v
            ok = update_game(game_id, updates)
            print("Atualizado?" , ok)
        elif choice == "5":
            game_id = input("ID do jogo para deletar: ").strip()
            ok = delete_game(game_id)
            print("Deletado?" , ok)
        elif choice == "6":
            print("Saindo.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
