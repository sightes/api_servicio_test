CREATE TABLE beneficiaries (
    id serial PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    gender CHAR(1) NOT NULL,
    birth_date DATE NULL,
    rut_number BIGINT NULL,
    program VARCHAR(100) NULL,
    process_date DATE NULL
);
