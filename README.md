# Baozi Store — API REST

Trabalho de Desenvolvimento Web Back-End (Uninter).
API REST para controle de clientes, produtos e pedidos da Baozi Store, uma loja de pão chinês.

**Aluno:** Tiago Santana Palmeira — RU 5258014

## Tecnologias

- Java 21
- Spring Boot 4 (Spring Web MVC)
- Spring Data JPA (Hibernate)
- Banco relacional H2 (em arquivo)
- Maven (via Maven Wrapper, não precisa instalar)

## Estrutura (padrão MVC)

```
src/main/java/br/com/baozistore
├── model/        Cliente, Produto, Pedido (entidades JPA)
├── repository/   ClienteRepository, ProdutoRepository, PedidoRepository
└── controller/   ClienteController, ProdutoController, PedidoController
```

## Como rodar

Requisito: Java 21 ou superior.

```bash
# Windows
mvnw.cmd spring-boot:run

# Linux / macOS
./mvnw spring-boot:run
```

A API sobe em `http://localhost:8081`.
Console do banco H2: `http://localhost:8081/h2-console` (JDBC URL `jdbc:h2:file:./data/baozistore`, usuário `sa`, sem senha).

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| POST | `/clientes` | Cria um cliente |
| GET | `/clientes` | Lista todos os clientes |
| GET | `/clientes/{id}` | Consulta um cliente por ID |
| PUT | `/clientes/{id}` | Atualiza um cliente (opcional) |
| DELETE | `/clientes/{id}` | Apaga um cliente |
| POST | `/produtos` | Cria um produto |
| GET | `/produtos` | Lista todos os produtos |
| GET | `/produtos/{id}` | Consulta um produto por ID |
| PUT | `/produtos/{id}` | Atualiza um produto (opcional) |
| DELETE | `/produtos/{id}` | Apaga um produto |
| POST | `/pedidos` | Cria um pedido (valida se cliente e produto existem) |
| GET | `/pedidos` | Lista todos os pedidos |
| GET | `/pedidos/{id}` | Consulta um pedido por ID |
| PUT | `/pedidos/{id}` | Atualiza um pedido (opcional) |
| DELETE | `/pedidos/{id}` | Apaga um pedido |

## Exemplos de JSON

```json
// POST /clientes
{ "nome": "TiagoSantanaPalmeira5258014", "clienteDesde": "2026-10-10" }

// POST /produtos
{ "nome": "Baozi de Porco", "preco": 8.50, "estoque": true }

// POST /pedidos
{ "clienteId": 1, "produtoId": 1, "quantidade": 6 }
```

## Postman

Importe `postman/BaoziStore.postman_collection.json` no Postman.
