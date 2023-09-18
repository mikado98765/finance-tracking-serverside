PRAGMA foreign_keys = ON;

CREATE TABLE transactions(
    id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    paymentID INT NOT NULL,
    purchaseID INT NOT NULL,
    companyID INT NOT NULL,
    notes VARCHAR(50),
    PRIMARY KEY(id)
);

CREATE TABLE payments(
    id INT NOT NULL,
    name VARCHAR(20)
    PRIMARY KEY(id)
);

CREATE TABLE purchase_types(
    id INT NOT NULL,
    name VARCHAR(20)
    PRIMARY KEY(id)
);

CREATE TABLE companies(
    id INT NOT NULL,
    name VARCHAR(20)
    PRIMARY KEY(id)
);