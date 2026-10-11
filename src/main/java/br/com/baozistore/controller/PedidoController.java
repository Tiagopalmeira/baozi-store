package br.com.baozistore.controller;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.com.baozistore.model.Pedido;
import br.com.baozistore.repository.ClienteRepository;
import br.com.baozistore.repository.PedidoRepository;
import br.com.baozistore.repository.ProdutoRepository;

@RestController
@RequestMapping("/pedidos")
public class PedidoController {

	private final PedidoRepository repository;
	private final ClienteRepository clienteRepository;
	private final ProdutoRepository produtoRepository;

	public PedidoController(PedidoRepository repository, ClienteRepository clienteRepository,
			ProdutoRepository produtoRepository) {
		this.repository = repository;
		this.clienteRepository = clienteRepository;
		this.produtoRepository = produtoRepository;
	}

	@PostMapping
	public ResponseEntity<?> criar(@RequestBody Pedido pedido) {
		String erro = validar(pedido);
		if (erro != null) {
			return ResponseEntity.badRequest().body(erro);
		}
		pedido.setId(null);
		return ResponseEntity.status(HttpStatus.CREATED).body(repository.save(pedido));
	}

	@GetMapping
	public List<Pedido> listar() {
		return repository.findAll();
	}

	@GetMapping("/{id}")
	public ResponseEntity<Pedido> buscarPorId(@PathVariable Long id) {
		return repository.findById(id)
				.map(ResponseEntity::ok)
				.orElse(ResponseEntity.notFound().build());
	}

	@PutMapping("/{id}")
	public ResponseEntity<?> atualizar(@PathVariable Long id, @RequestBody Pedido pedido) {
		if (!repository.existsById(id)) {
			return ResponseEntity.notFound().build();
		}
		String erro = validar(pedido);
		if (erro != null) {
			return ResponseEntity.badRequest().body(erro);
		}
		pedido.setId(id);
		return ResponseEntity.ok(repository.save(pedido));
	}

	@DeleteMapping("/{id}")
	public ResponseEntity<Void> apagar(@PathVariable Long id) {
		if (!repository.existsById(id)) {
			return ResponseEntity.notFound().build();
		}
		repository.deleteById(id);
		return ResponseEntity.noContent().build();
	}

	// Garante que o pedido aponta para um cliente e um produto que existem
	private String validar(Pedido pedido) {
		if (pedido.getClienteId() == null || !clienteRepository.existsById(pedido.getClienteId())) {
			return "Cliente não encontrado: " + pedido.getClienteId();
		}
		if (pedido.getProdutoId() == null || !produtoRepository.existsById(pedido.getProdutoId())) {
			return "Produto não encontrado: " + pedido.getProdutoId();
		}
		if (pedido.getQuantidade() == null || pedido.getQuantidade() <= 0) {
			return "Quantidade deve ser maior que zero";
		}
		return null;
	}

}
