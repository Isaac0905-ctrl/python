from .db import DbHandler


def create_db(db_path: str = ':memory:') -> None:
    db = DbHandler(db_path)
    create_sql = """Create table if not exists users(
    id text primary key,
    name text,
    credit real default 0);
    
    Create table if not exists buses(
    id text primary key,
    total_seats integer not null,
    busy_seats integer not null default 0,
    check (total_seats>= 0),
    check (busy_seats>=0),
    check (total_seats >= busy_seats));
    
    Create table if not exists stops(
    id text primary key,
    name text not null,
    cost real default 0);
    
    create table if not exists trip(
    user_id text not null,
    bus_id text not null,
    stop_id text not null,
    moment datetime not null,
    status text not null,
    primary key (user_id, bus_id, moment),
    foreign key (user_id)references users(id),
    foreign key (bus_id) references buses(id),
    foreign key (stop_id) references stops(id));
    
    Create table if not exists route(
    bus_id text not null, 
    stop_id text not null,
    stop_order integer not null,
    primary key (bus_id, stop_id),
    foreign key (bus_id)references buses(id),
    foreign key (stop_id)references stops(id));"""

    db.cur.executescript(create_sql)
