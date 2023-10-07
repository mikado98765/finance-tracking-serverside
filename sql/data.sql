PRAGMA foreign_keys = ON;

INSERT INTO transactions(id, amount, paymentID, purchaseID, companyID, notes)
VALUES (0, -1000, 0, 0, 0, "Initial balance");

INSERT INTO payments(id, name)
VALUES(0, "ADMIN");

INSERT INTO purchase_types(id, name)
VALUES(0, "ADMIN");

INSERT INTO companies(id, name)
VALUES(0, "ADMIN");

