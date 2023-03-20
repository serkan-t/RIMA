from neo4j import GraphDatabase

uri = "bolt://localhost:7687"

userName = "neo4j"

password = "1234qweR"

graphDB_Driver = GraphDatabase.driver(uri, auth=(
    userName, password))
