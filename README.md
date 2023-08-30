# ponderada2_m7

Uso de Flask como servidor, ele lida de uma forma mais amigável pra renderizar arquivos estáticos, como o CSS, do que o FastAPI, que eu estava utlizando mais ultimamente. Banco de dados contruído com Postgres e SQLAlchemy, já que estava sendo mais comentado em sala de aula. Temos duas tabelas, uma de usuários, com seu user e senha, e uma de tasks, com o conteúdo da task.
Duas imagens são utilizadas, um criada por meio do Dockerfile que vai possuir tudo relacionado a frontend e backend, enquanto a outra imagem é a oficial do Postgres para que ele seja utilizado com Docker.

## Pastas
|
|- static
    |
    |- styles.css
 |- templates
    |
    |- addTodo.html
    |- login.html
    |- signup.html
    |- todo.html
    |
 |
 |- auth.py
 |- docker-compose.yml
 |- Dockerfile
 |- main.py
 |- models.py
 |- requirements.txt
|


## Como rodar

Na root do projeto, rode "docker-compose up", assim, o Docker consegue colocar todos os serviços para trabalharem em conjunto e tudo funcionar belezinha. Aproveite a minha todo list rosa!

 
