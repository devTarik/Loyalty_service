FROM postgres:13.2-alpine

COPY ./compose/postgres/create_database.sql /docker-entrypoint-initdb.d
RUN echo "host  all  all  0.0.0.0/0  md5" >> /var/lib/postgresql/data/pg_hba.conf