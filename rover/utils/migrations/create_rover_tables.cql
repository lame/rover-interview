// The following code is to be used in creating the schema in Cassandra
// Another option is CQLEngines management class sync_table, however it
// does not allow full flexability.

use rover
create table if not exists sitter_profile(
    id int,
    name text,
    image text,
    owner_review_text text,
    rating double,
    score double,
    PRIMARY KEY (id)
);

CREATE INDEX ON rover.sitter_profile(score);

create table if not exists owner_profile(
    id int,
    name text,
    image text,
    owner_review_text text,
    dogs set<text>,
    PRIMARY KEY (id)
);

create table if not exists sitter_by_owner(
    owner_id int,
    sitter_id int,
    start_date timestamp,
    end_date timestamp,
    dogs_handled set<text>,
    rating int,
    primary key((owner_id), sitter_id)
);

create table if not exists owner_by_sitter(
    sitter_id int,
    owner_id int,
    start_date timestamp,
    end_date timestamp,
    PRIMARY KEY((sitter_id), owner_id)
);

create table if not exists sitter_name_by_id(
    sitter_id int,
    sitter_name text,
    PRIMARY KEY(sitter_id)
);

create table if not exists owner_name_by_id(
    owner_id int,
    owner_name text,
    PRIMARY KEY(owner_id)
);

create table if not exists rating_by_sitter(
    sitter_id int,
    rating double,
    id uuid,
    PRIMARY KEY(sitter_id)
);

create table if not exists sitters_by_rating(
    overall_rank int,
    rating double,
    sitter_id int,
    PRIMARY KEY(overall_rank)
);
