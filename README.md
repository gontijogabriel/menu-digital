
# Cardápio Eletrônico

O Cardápio Eletrônico é uma aplicação web e mobile que permite aos usuários visualizarem os cardápios dos restaurantes parceiros, fazerem pedidos e acompanharem o status de seus pedidos em tempo real. Além disso, oferece um blog de notícias dos restaurantes parceiros e um filtro de restaurantes para facilitar a busca.

## Funcionalidades Principais

### 1. Home
- Apresenta um blog de notícias dos restaurantes parceiros.
- Oferece um filtro de restaurantes para facilitar a busca.

### 2. Página Web Mobile
- Apresenta o cardápio do restaurante com categorias de produtos: bebidas, comidas, entradas e sobremesas.

### 3. Leitura de QR Code
- Ao escanear o QR Code, o usuário é direcionado para a página do restaurante.
- O usuário pode criar sua comanda fornecendo CPF, nome e telefone.

### 4. Pedido de Produtos
- O usuário tem acesso a todos os produtos e preços.
- Pode fazer pedidos pelo celular e acompanhar os produtos pedidos, bem como o valor total de sua conta.

### 5. Finalização do Atendimento
- Ao encerrar o atendimento, o usuário deve finalizá-lo no aplicativo.
- O cadastro do usuário é excluído e os dados do pedido são enviados para o caixa e armazenados no banco de dados.

### 6. Relatórios de Vendas
- Os dados armazenados no banco são utilizados para gerar relatórios de vendas.

## Instalação e Uso

1. Clone o repositório: ``
2. Navegue até o diretório do projeto: ``
3. Instale as dependências: `` ou ``
4. Inicie o servidor: `` ou ``
5. Acesse a aplicação no navegador ou no dispositivo móvel.

## Tecnologias Utilizadas

- Frontend: ReactJS, React Native
- Backend: Django REST Framework
- Banco de Dados: Postgres
- Autenticação: JWT
- QR Code: React Native QR Code Scanner