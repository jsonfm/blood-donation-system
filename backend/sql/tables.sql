CREATE TYPE blood_type_enum AS ENUM ('A+', 'A-', 'O+', 'O-', 'B+', 'B-', 'AB+', 'AB-');
CREATE TYPE gender_type_enum AS ENUM('F', 'M');


CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    birthday DATE,
    email VARCHAR(100),
    phone_number VARCHAR(20),
    gender gender_type_enum NOT NULL,
    blood_type blood_type_enum NOT NULL
);

CREATE TABLE IF NOT EXISTS banks (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS donations (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    donation_date TIMESTAMPTZ DEFAULT NOW(),
    comments TEXT,
    valid BOOLEAN,
    patient_id INT REFERENCES patients(id),
    bank_id INT REFERENCES banks(id)
);
