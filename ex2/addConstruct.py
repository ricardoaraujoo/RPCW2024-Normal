from flask import Flask, jsonify, render_template, request, url_for
from datetime import datetime
import requests
import _json
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph
app = Flask(__name__)


def parse_rdf_data(rdf_data):
    g = Graph()
    g.parse(data=rdf_data, format='application/rdf+xml')

    triples = []
    for subj, pred, obj in g:
        triples.append(f"<{subj}> <{pred}> <{obj}> .")

    return "\n".join(triples)


graphDB_endpoint = "http://localhost:7200/repositories/ex2"

@app.route('/')
def index():
    sparql_query = """
PREFIX : <http://www.example.org/disease-ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

CONSTRUCT {
  ?patient :hasDisease ?disease .
}
WHERE {
  ?patient rdf:type :Patient .
  ?disease rdf:type :Disease .

  ?disease :hasSymptom ?symptom .

  FILTER NOT EXISTS {
    ?disease :hasSymptom ?diseaseSymptom .
    FILTER NOT EXISTS {
      ?patient :exhibitsSymptom ?diseaseSymptom .
    }
  }
}
"""

    resposta = requests.get(graphDB_endpoint, 
                            params = {'query': sparql_query}, 
                            headers = {'Accept': 'application/rdf+xml'})
    if resposta.status_code == 200:
        # parse_rdf_data(resposta.text)
        triples = parse_rdf_data(resposta.text)

        insert_query = f"""
        PREFIX : <http://www.example.org/disease-ontology#>
        INSERT DATA {{
            {triples}
        }}
        """
        execute_sparql_query(insert_query)
        return "Triples inserted successfully", 200

    else:
        return jsonify({"message": "Query failed", "error": resposta.text})


def execute_sparql_query(query):
    sparql = SPARQLWrapper("http://localhost:7200/repositories/ex2/statements")
    sparql.setMethod('POST')
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


if __name__ == '__main__':
    app.run(debug=True)