create table if not exists flask_blogly.table_name
(
	id serial not null
		constraint table_name_pk
			primary key,
	first_name varchar(20) not null,
	last_name varchar(50) not null
);

alter table flask_blogly.table_name owner to acampos;

create unique index if not exists table_name_id_uindex
	on flask_blogly.table_name (id);

