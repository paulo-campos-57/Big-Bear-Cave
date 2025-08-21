CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS pgcrypto;

create table users (
	id UUID primary key default uuid_generate_v4(),
	name varchar(100) not null unique,
	email varchar(100) not null unique,
	password varchar(50) not null,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  	user_role integer not NULL,
  	profile_image_path varchar(300),
	teste varchar(100)
);

ALTER TABLE users ALTER COLUMN password TYPE varchar(255);

create table player_profile (
	user_id uuid references users(id) on delete cascade
);

ALTER TABLE player_profile
ADD CONSTRAINT player_profile_pkey PRIMARY KEY (user_id);

create table player_characters (
	player_id uuid references player_profile(user_id) on delete cascade,
	character_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	name varchar(100) not null,
	level integer,
	char_class varchar(100) not null,
	species varchar(100) not null,
	background varchar(100) not null,
	alignement varchar(100) not null,
	total_health integer default 0,
	current_health integer default 0,
	armor_class integer default 0,
	initiative integer default 0,
	speed integer default 0,
	-- attributes --
	strength integer default 0,
	dexterity integer default 0,
	constitution integer default 0,
	intelligence integer default 0,
	wisdom integer default 0,
	charisma integer default 0
);

create table inventory (
	inv_id uuid primary key default gen_random_uuid(),
	character_id uuid references player_characters(character_id) on delete cascade,
	weight integer default 0,
	item varchar(100),
	description text
);

create table languages (
	lang_id uuid primary key default gen_random_uuid(),
	character_id uuid references player_characters(character_id) on delete cascade,
	known_language varchar (100)
);

create table skills (
	skill_id uuid primary key default gen_random_uuid(),
	character_id uuid references player_characters(character_id) on delete cascade,
	title varchar(100) not null,
	description text
);

create table spells (
    spell_id uuid primary key default gen_random_uuid(),
    character_id uuid references player_characters(character_id) on delete cascade,
    title varchar(100) not null,
    description text
);

create table master_profile (
	player_id uuid references player_profile(user_id) on delete cascade,
	master_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
	began_at date not null
);

create table master_characters (
	master_id uuid references player_profile(user_id) on delete cascade,
	character_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	name varchar(100) not null,
	level integer,
	char_class varchar(100) not null,
	species varchar(100) not null,
	background varchar(100) not null,
	alignement varchar(100) not null,
	total_health integer default 0,
	current_health integer default 0,
	armor_class integer default 0,
	initiative integer default 0,
	speed integer default 0,
	-- attributes --
	strength integer default 0,
	dexterity integer default 0,
	constitution integer default 0,
	intelligence integer default 0,
	wisdom integer default 0,
	charisma integer default 0,
	boss integer default 0,
	experience integer default 0
);

-- Optional initial selects
-- select * from users;
-- select * from player_profile;
-- select * from player_characters;
-- select * from master_profile; 