Instruções de como correr:

No ex2 modifiquei o json com o programa decode.py, para tratar dos erros de encoding do JSON nos campos name. Além disso, também substitui qualquer " " por "_" usando o vscode.

Para fazer o ex2, basta executar o script "l.py" para gerar todos os ttls necessários(Ele gere 1 a mais chamado updated_ontology.ttl)
-----

No ex1, fui criando as classes, propriedades... ao longo que lia e revia a historia, depois importei a ontologia para o graphdb e criei as queries.
-----

No ex2, carrguei a ontologia já existente, adicionei as propriedades data necessárias(name,id,hasDescription todas como data properties) no script,e fui dando parse do csv e json enquanto criava os triples para povoar a BD.

Para a 12. usei o programa addConstruct.py, que é um servidor que na rota "/" executa a query construct e de seguida envia os triples para a BD. Demora uns minutos a executar.

Para a 13. dei import da construct query da pergunta 12 para me ajudar.