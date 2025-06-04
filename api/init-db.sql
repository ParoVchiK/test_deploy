CREATE TABLE IF NOT EXISTS user_(
    id serial,
    name varchar not null,
    primary key(id)
);

CREATE TABLE IF NOT EXISTS post(
    id serial,
    user_id integer not null,
    post_text varchar,
    primary key(id),
    foreign key(user_id) references user_(id)
)