🎯 Checkpoints - Você deve conseguir:
Checkpoint 1:
[ ] App roda localmente (fora do Docker)
[ ] Conecta no banco
[ ] CRUD funciona
Checkpoint 2:
[ ] Dockerfile da app buildando
[ ] Imagem rodando sozinha
[ ] Conecta em banco local
Checkpoint 3:
[ ] docker-compose up funciona
[ ] Todos os services sobem
[ ] App conecta no banco do compose
Checkpoint 4:
[ ] Nginx proxying para app
[ ] Acesso via http://localhost funciona
[ ] CRUD completo funcionando via Nginx

🤔 Perguntas para reflexão:
Sobre Docker:

Por que usar multi-stage build?
Diferença entre COPY e ADD?
CMD vs ENTRYPOINT?
Por que --no-cache-dir no pip?
O que é .dockerignore e por que usar?

Sobre Docker Compose:

Diferença entre depends_on e healthcheck?
Por que networks são importantes?
Quando usar volumes named vs bind mounts?
O que é service discovery no Docker?

Sobre Nginx:

Por que usar Nginx e não acessar app direto?
O que são proxy headers e por que passar?
Diferença entre proxy_pass com / no final vs sem?

Sobre a aplicação:

Como fazer graceful shutdown?
Por que logs estruturados (JSON) são melhores?
Como lidar com secrets/senhas?
Connection pooling no banco: precisa?

