FASE 1: LOCAL (Docker Compose) ⏱️ 1-2 semanas
Passo 1: Estrutura de pastas
Crie a estrutura básica do projeto:
- Pasta raiz
- Pasta para aplicação
- Pasta para configs do Nginx
- Pasta para scripts de banco
- Arquivos na raiz (docker-compose, gitignore, readme, makefile)
Perguntas para você responder:

Como organizar de forma que fique fácil navegar?
Quais arquivos vão na raiz vs dentro de pastas?


Passo 2: Aplicação CRUD
Escolha sua linguagem (Go ou Python)
Desafios:

Como conectar com banco de dados?
Como ler variáveis de ambiente?
Quais endpoints preciso? (pense em CRUD completo)
Como estruturar os handlers/routes?
Preciso de um health check endpoint?

O que implementar:

 Conexão com banco
 Endpoint de health check
 GET /recurso (listar todos)
 GET /recurso/:id (buscar um)
 POST /recurso (criar)
 PUT /recurso/:id (atualizar)
 DELETE /recurso/:id (deletar)

Perguntas:

Como testar sem Docker primeiro?
Que biblioteca usar para HTTP server?
Como fazer parsing de JSON?
Como lidar com erros?


Passo 3: Banco de dados
Desafios:

Qual banco usar? (Postgres, MySQL, etc)
Como criar schema inicial?
Onde colocar o SQL de inicialização?
Como seed inicial de dados?

Pense em:

 Tabela(s) necessária(s)
 Campos e tipos
 Primary keys, indexes
 Dados iniciais para teste


Passo 4: Dockerfile da aplicação
Desafios:

Qual imagem base usar?
Multi-stage build? Por quê?
Como copiar apenas o necessário?
Qual porta expor?
Qual comando rodar?

Otimizações para pensar:

Cache de dependências
Tamanho da imagem final
Segurança (não rodar como root?)


Passo 5: Docker Compose
Desafios:

Quais services preciso definir? (banco, app, nginx)
Como fazer app esperar o banco estar pronto?
Como passar variáveis de ambiente?
Volumes: o que precisa persistir?
Networks: precisam conversar entre si?
Portas: quais expor para host?

Ordem de inicialização:

Banco primeiro, depois app, depois nginx?
Como garantir isso?

Health checks:

Como saber se cada service está realmente pronto?


Passo 6: Nginx
Desafios:

Configuração básica: o que é essencial?
Como fazer proxy para aplicação?
Que headers passar/adicionar?
Porta 80 ou 443? Ou ambas?
Logs: onde e como?

Pense em:

 Upstream definition
 Server block
 Location blocks
 Proxy headers
 Health check endpoint


Passo 7: Variáveis de ambiente
Desafios:

Quais variáveis a app precisa?
Como organizar (.env)?
Valores diferentes para dev vs prod?
O que NÃO commitar no git?

Lista para pensar:

Credenciais de banco
URL de conexão
Porta da aplicação
Ambiente (dev/prod)


Passo 8: Makefile (opcional mas útil)
Comandos úteis que você gostaria de ter:

Subir ambiente
Derrubar ambiente
Ver logs
Rebuild
Limpar tudo
Rodar testes

Como implementar cada um?

Passo 9: Scripts SQL
O que criar:

Schema do banco (CREATE TABLE)
Dados iniciais (INSERT)
Como fazer rodar automaticamente na inicialização?


Passo 10: Testes
Como validar que funciona:

 curl para health check
 curl para criar recurso
 curl para listar
 curl para buscar um específico
 curl para atualizar
 curl para deletar

Você consegue fazer isso manualmente primeiro?