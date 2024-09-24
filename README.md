# Gerador de QR Code Personalizado

Este projeto oferece um gerador de QR Code flexível e personalizável que permite aos usuários criar códigos QR únicos com vários estilos para marcadores, bordas e módulos de dados.

## Características

- Gera códigos QR com estilos personalizáveis
- Múltiplos estilos de marcadores (Quadrado, Arredondado, Círculo, Quarto de Círculo, Estrela, Diamante, Cruz)
- Vários estilos de borda (Quadrado, Arredondado, Círculo, Quarto de Círculo, Quarto de Círculo Suave, Quarto Circular, Circular, Quadrado Arredondado)
- Diferentes estilos de linha para módulos de dados (Quadrado, Quadrado com Espaço, Círculo, Arredondado, Barras Verticais, Barras Horizontais)
- Opção para adicionar uma imagem central ao código QR

## Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/nathanvsn/gerador-qr-code-personalizado.git
   cd gerador-qr-code-personalizado
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
   ```

## Uso

Aqui está um exemplo básico de como usar o Gerador de QR Code Personalizado:

```python
from qr_code_generator.generator import QRCodeGenerator
from qr_code_generator.styles.marker_styles import MarkerStyle
from qr_code_generator.styles.border_styles import BorderStyle
from qr_code_generator.styles.line_styles import LineStyle

qr_generator = QRCodeGenerator()
qr_img = qr_generator.create_custom_qr(
    "https://www.exemplo.com.br",
    size=10,
    border=4,
    marker_style=MarkerStyle.PLUS,
    border_style=BorderStyle.CIRCLE,
    line_style=LineStyle.ROUNDED,
    center_image="caminho/para/imagem_central.png"
)
qr_img.save("qr_code_personalizado.png")
qr_img.show()
```

## Opções de Personalização

## Opções de Personalização

### Estilos de Marcadores

| Estilo | Código | Visualização |
|--------|--------|--------------|
| Quadrado | `MarkerStyle.SQUARE` | <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 6 6"><rect width="6" height="6"/></svg> |
| Arredondado | `MarkerStyle.ROUNDED` | <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 6 6"><path d="M6,1.7v2.7C6,5.2,5.2,6,4.3,6H1.7C0.7,6,0,5.3,0,4.3V1.7C0,0.8,0.8,0,1.7,0h2.7C5.3,0,6,0.7,6,1.7z"/></svg> |
| Círculo | `MarkerStyle.CIRCLE` | <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 6 6"><circle cx="3" cy="3" r="3"/></svg> |
| Quarto de Círculo | `MarkerStyle.QUARTER_CIRCLE` | <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 6 6"><path d="M3,6L3,6C1.3,6,0,4.7,0,3l0-3l3,0c1.7,0,3,1.3,3,3v0C6,4.7,4.7,6,3,6z"/></svg> |
| Estrela | `MarkerStyle.STAR` | <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 6 6"><path d="M3.2,0.3l0.6,1.3C4,1.8,4.1,1.9,4.3,1.9l1.4,0.2c0.2,0,0.3,0.3,0.2,0.5l-1,1C4.7,3.7,4.7,3.9,4.7,4.1L5,5.5 c0,0.2-0.2,0.4-0.4,0.3L3.3,5.2c-0.2-0.1-0.4-0.1-0.6,0L1.4,5.8C1.2,5.9,1,5.8,1,5.5l0.2-1.4c0-0.2,0-0.4-0.2-0.5l-1-1 C-0.1,2.4,0,2.2,0.2,2.1l1.4-0.2c0.2,0,0.4-0.2,0.5-0.3l0.6-1.3C2.9,0.1,3.1,0.1,3.2,0.3z"/></svg> |
| Diamante | `MarkerStyle.DIAMOND` | <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 6 6"><rect x="0.9" y="0.9" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -1.2426 3)" width="4.2" height="4.2"/></svg> |
| Cruz | `MarkerStyle.PLUS` | <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 6 6"><polygon points="6,1.5 4.5,1.5 4.5,0 1.5,0 1.5,1.5 0,1.5 0,4.5 1.5,4.5 1.5,6 4.5,6 4.5,4.5 6,4.5"/></svg> |

### Estilos de Borda

| Estilo | Código | Visualização |
|--------|--------|--------------|
| Quadrado | `BorderStyle.SQUARE` | <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 14 14"><rect width="14" height="14" fill="white"/><path d="M0,0v14h14V0H0z M12,12H2V2h10V12z"/></svg> |
| Arredondado | `BorderStyle.ROUNDED` | <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 14 14"><rect width="14" height="14" fill="white"/><path d="M4.5,14h5.1C12,14,14,12,14,9.6V4.5C14,2,12,0,9.5,0H4.4C2,0,0,2,0,4.4v5.1C0,12,2,14,4.5,14z M12,4.8v4.4 c0,1.5-1.3,2.8-2.8,2.8H4.8C3.2,12,2,10.8,2,9.2V4.8C2,3.3,3.3,2,4.8,2h4.4C10.8,2,12,3.2,12,4.8z"/></svg> |
| Círculo | `BorderStyle.CIRCLE` | <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 14 14"><rect width="14" height="14" fill="white"/><path d="M0,7L0,7c0,3.9,3.1,7,7,7h0c3.9,0,7-3.1,7-7v0c0-3.9-3.1-7-7-7h0C3.1,0,0,3.1,0,7z M7,12L7,12c-2.8,0-5-2.2-5-5v0 c0-2.8,2.2-5,5-5h0c2.8,0,5,2.2,5,5v0C12,9.8,9.8,12,7,12z"/></svg> |
| Quarto de Círculo | `BorderStyle.QUARTER_CIRCLE` | <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 14 14"><rect width="14" height="14" fill="white"/><path d="M0,0l0,7c0,3.9,3.1,7,7,7h0c3.9,0,7-3.1,7-7v0c0-3.9-3.1-7-7-7H0z M7,12L7,12c-2.8,0-5-2.2-5-5V2h5c2.8,0,5,2.2,5,5v0 C12,9.8,9.8,12,7,12z"/></svg> |
| Quarto de Círculo Suave | `BorderStyle.SMOOTH_QUARTER_CIRCLE` | <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 14 14"><rect width="14" height="14" fill="white"/><path d="M0,0l0,7c0,3.9,3.1,7,7,7h7V7c0-3.9-3.1-7-7-7H0z M12,12H7c-2.8,0-5-2.2-5-5v0c0-2.8,2.2-5,5-5h0c2.8,0,5,2.2,5,5V12z"/></svg> |
| Quarto Circular | `BorderStyle.CIRCULAR_QUARTER` | <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 14 14"><rect width="14" height="14" fill="white"/><path d="M0,0l0,7c0,3.9,3.1,7,7,7h7V7c0-3.9-3.1-7-7-7H0z M7,12L7,12c-2.8,0-5-2.2-5-5v0c0-2.8,2.2-5,5-5h0c2.8,0,5,2.2,5,5v0 C12,9.8,9.8,12,7,12z"/></svg> |
| Circular | `BorderStyle.CIRCULAR` | <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 14 14"><rect width="14" height="14" fill="white"/><path d="M0,0l0,14h14V0H0z M7,12L7,12c-2.8,0-5-2.2-5-5v0c0-2.8,2.2-5,5-5h0c2.8,0,5,2.2,5,5v0C12,9.8,9.8,12,7,12z"/></svg> |
| Quadrado Arredondado | `BorderStyle.ROUNDED_SQUARE` | <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 14 14"><rect width="14" height="14" fill="white"/><path d="M0,0v9.6C0,12,2,14,4.4,14h5.1C12,14,14,12,14,9.6V4.4C14,2,12,0,9.6,0H0z M9.2,12H4.8C3.3,12,2,10.7,2,9.2V2h7.2 C10.7,2,12,3.3,12,4.8v4.4C12,10.7,10.7,12,9.2,12z"/></svg> |

### Estilos de Linha
- `LineStyle.SQUARE` (Quadrado)
- `LineStyle.GAPPED_SQUARE` (Quadrado com Espaço)
- `LineStyle.CIRCLE` (Círculo)
- `LineStyle.ROUNDED` (Arredondado)
- `LineStyle.VERTICAL_BARS` (Barras Verticais)
- `LineStyle.HORIZONTAL_BARS` (Barras Horizontais)

## Exemplos

Aqui estão alguns exemplos de diferentes estilos de códigos QR que você pode criar:

1. Estilo circular com módulos de dados arredondados:
   ```python
   qr_img = qr_generator.create_custom_qr(
       "https://www.exemplo.com.br",
       marker_style=MarkerStyle.CIRCLE,
       border_style=BorderStyle.CIRCLE,
       line_style=LineStyle.ROUNDED
   )
   ```

2. Marcadores em estrela com borda quadrada:
   ```python
   qr_img = qr_generator.create_custom_qr(
       "https://www.exemplo.com.br",
       marker_style=MarkerStyle.STAR,
       border_style=BorderStyle.SQUARE,
       line_style=LineStyle.SQUARE
   )
   ```

3. Marcadores em diamante com barras verticais para módulos de dados:
   ```python
   qr_img = qr_generator.create_custom_qr(
       "https://www.exemplo.com.br",
       marker_style=MarkerStyle.DIAMOND,
       border_style=BorderStyle.ROUNDED_SQUARE,
       line_style=LineStyle.VERTICAL_BARS
   )
   ```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request.

1. Faça um fork do repositório
2. Crie sua branch de feature (`git checkout -b feature/NovaFuncionalidade`)
3. Faça commit de suas mudanças (`git commit -m 'Adiciona alguma NovaFuncionalidade'`)
4. Faça push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Agradecimentos

- [qrcode](https://github.com/lincolnloop/python-qrcode) - A biblioteca base para geração de QR Code
- [Pillow](https://python-pillow.org/) - Para processamento de imagens
- [cairosvg](https://cairosvg.org/) - Para conversão de SVG para PNG

## Contato

Nathan Nóbrega - nathanitau@gmail.com

Link do Projeto: [https://github.com/nathanvsn/gerador-qr-code-personalizado](https://github.com/nathanvsn/gerador-qr-code-personalizado)