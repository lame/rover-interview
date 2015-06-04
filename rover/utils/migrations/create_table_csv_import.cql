//Temporary table for use in data recovery, should be depricated after scrape upload

use rover;
create table if not exists csv_import(
    id uuid,
    sitter_id int,
    rating int,
    sitter_image text,
    start_date timestamp,
    end_date timestamp,
    profile_text text,
    owner_image text,
    dogs set<text>,
    sitter text,
    owner text,
    owner_id int,
    PRIMARY KEY (id)
);
