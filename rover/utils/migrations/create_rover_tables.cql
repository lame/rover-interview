use rover
create table if not exists sitter_profile(
    id int,
    image text,
    profile_text text,
    PRIMARY KEY (id)
);

create table if not exists owner_profile(
    id int,
    image text,
    profile_text text,
    dogs set<text>,
    PRIMARY KEY (id)
);

create table if not exists sitter_by_owner(
    owner_id int,
    sitter_id int,
    start_date timestamp,
    end_date timestamp,
    dogs_handles set<text>,
    primary key((owner_id), sitter_id)
);

create table if not exists owner_by_sitter(
    sitter_id int,
    owner_id int,
    start_date timestamp,
    end_date timestamp,
    PRIMARY KEY((sitter_id), owner_id)
);
