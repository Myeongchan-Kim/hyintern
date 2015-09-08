drop table if exists phone_num_list;
create table phone_num_list (
	id		integer primary key autoincrement,
	title	string not null,
	text	string not null default '',
	location string not null default 'seoul',
	phone_num	string not null
);