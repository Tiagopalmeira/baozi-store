# Trabalho de Desenvolvimento Web Back-End — API REST Baozi Store

**Aluno:** Tiago Santana Palmeira — **RU:** 5258014

---

## 1. Descrição da situação fictícia (estudo de caso)

A **Baozi Store** é uma pequena loja que vende **pão chinês**.
Para melhorar a organização do negócio, foi criado um sistema simples para controlar clientes, produtos e pedidos.

Um cliente chamado **TiagoSantanaPalmeira5258014** realizou seu cadastro no sistema em 10/10/2026.

O produto vendido pela loja chama-se **Baozi de Porco** e é vendido por unidade, ao preço de **R$ 8,50**, e está disponível em estoque.

Em um determinado momento, o cliente realizou um pedido de **6 unidades** do produto.

O sistema registra o cliente, o produto comprado e a quantidade solicitada, facilitando o controle da loja.

---

## 2. Diagrama de Caso de Uso

*(Inserir a imagem `docs/diagrama-caso-de-uso.png`)*

O ator principal é o **Usuário da API**, que pode cadastrar, listar, consultar por ID, atualizar (opcional) e apagar clientes, produtos e pedidos. O caso de uso **Cadastrar Pedido** inclui (**«include»**) a validação de que o cliente e o produto informados existem.

---

## 3. Especificação da API desenvolvida

**Tecnologias:** Java 21, Spring Boot 4, Spring Data JPA (Hibernate), banco relacional H2 (salvo em arquivo, conforme permitido nos requisitos técnicos), JSON e arquitetura MVC do Spring (pacotes `model`, `repository` e `controller`).

**Endereço base:** `http://localhost:8081`

### 3.1 Entidades criadas e seus campos

**Cliente** (tabela `cliente`)

| Campo | Tipo | Descrição |
|---|---|---|
| id | Long | Identificador (gerado automaticamente) |
| nome | String | Nome do cliente |
| clienteDesde | LocalDate | Data de cadastro do cliente |

**Produto** (tabela `produto`)

| Campo | Tipo | Descrição |
|---|---|---|
| id | Long | Identificador (gerado automaticamente) |
| nome | String | Nome do produto |
| preco | BigDecimal | Preço por unidade |
| estoque | Boolean | Indica se há o produto em estoque |

**Pedido** (tabela `pedido`)

| Campo | Tipo | Descrição |
|---|---|---|
| id | Long | Identificador (gerado automaticamente) |
| clienteId | Long | ID do cliente que comprou |
| produtoId | Long | ID do produto comprado |
| quantidade | Integer | Quantidade comprada |

### 3.2 Endpoints implementados

| Método | Rota | Descrição | Resposta de sucesso |
|---|---|---|---|
| POST | /clientes | Cria um cliente | 201 Created |
| GET | /clientes | Lista todos os clientes | 200 OK |
| GET | /clientes/{id} | Consulta cliente por ID | 200 OK (404 se não existir) |
| PUT | /clientes/{id} | Atualiza cliente (opcional) | 200 OK |
| DELETE | /clientes/{id} | Apaga cliente | 204 No Content |
| POST | /produtos | Cria um produto | 201 Created |
| GET | /produtos | Lista todos os produtos | 200 OK |
| GET | /produtos/{id} | Consulta produto por ID | 200 OK (404 se não existir) |
| PUT | /produtos/{id} | Atualiza produto (opcional) | 200 OK |
| DELETE | /produtos/{id} | Apaga produto | 204 No Content |
| POST | /pedidos | Cria um pedido (valida cliente e produto) | 201 Created (400 se inválido) |
| GET | /pedidos | Lista todos os pedidos | 200 OK |
| GET | /pedidos/{id} | Consulta pedido por ID | 200 OK (404 se não existir) |
| PUT | /pedidos/{id} | Atualiza pedido (opcional) | 200 OK |
| DELETE | /pedidos/{id} | Apaga pedido | 204 No Content |

### 3.3 Exemplos de JSON

```json
POST /clientes
{ "nome": "TiagoSantanaPalmeira5258014", "clienteDesde": "2026-10-10" }

POST /produtos
{ "nome": "Baozi de Porco", "preco": 8.50, "estoque": true }

POST /pedidos
{ "clienteId": 1, "produtoId": 1, "quantidade": 6 }
```

---

## 4. Prints do Postman

*(Colar os prints na ordem abaixo, cada um com um título curto)*

1. POST /clientes — criar o cliente TiagoSantanaPalmeira5258014
2. POST /produtos — criar o produto Baozi de Porco
3. POST /pedidos — criar o pedido de 6 unidades
4. GET /clientes — listagem geral de clientes
5. GET /produtos — listagem geral de produtos
6. GET /pedidos — listagem geral de pedidos
7. GET /clientes/1 — consulta por ID (fazer também /produtos/1 e /pedidos/1 se quiser)
8. DELETE /pedidos/1 — apagar (status 204)
9. *(Opcional)* GET /pedidos/1 depois do DELETE, mostrando 404

---

## 5. Link do repositório

https://github.com/SEU-USUARIO/baozi-store
