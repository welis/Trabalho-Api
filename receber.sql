create table itens(
    id serial primary key,
    descricao varchar(100),
    quantidade int,
    preco float
);

create table venda(
    id_num_venda serial primary key,
    data_venda varchar(10),
    cpf_cnpj varchar(11),
    nome varchar(100),
    cpf_vendedor varchar(11),
    itens_id int references itens(id)
    valor_entrada float,
    quantidade_parcelas int
);

create table contas_receber(
    id serial primary key,
    id_venda int references venda(id_num_venda),
    data_vencimento varchar(10),
    valor float,
);

insert into itens(descricao, quantidade, preco) values('Mouse', 10, 10.00);
insert into itens(descricao, quantidade, preco) values('Teclado', 10, 10.00);
insert into itens(descricao, quantidade, preco) values('Monitor', 10, 10.00);


insert into venda(data_venda, cpf_cnpj, nome, cpf_vendedor, itens_id, valor_entrada, quantidade_parcelas) values('01/01/2020', '12345678901', 'Joao da Silva', '12345678901', 1, 1000, 3);
insert into venda(data_venda, cpf_cnpj, nome, cpf_vendedor, itens_id, valor_entrada, quantidade_parcelas) values('01/01/2020', '12345678901', 'Maria da Silva', '12345678901', 2, 1000, 5);
insert into venda(data_venda, cpf_cnpj, nome, cpf_vendedor, itens_id, valor_entrada, quantidade_parcelas) values('01/02/2020', '12345678901', 'Jose da Silva', '12345678901', 3, 1000, 7);
insert into venda(data_venda, cpf_cnpj, nome, cpf_vendedor, itens_id, valor_entrada, quantidade_parcelas) values('01/02/2020', '12345655901', 'Carlos Souza', '12345678901', 1, 1000, 3);

insert into contas_receber(id_venda, data_vencimento, valor) values(1, '01/01/2020', 1000);
insert into contas_receber(id_venda, data_vencimento, valor) values(1, '14/02/2020', 500);
insert into contas_receber(id_venda, data_vencimento, valor) values(1, '17/03/2020', 560);
