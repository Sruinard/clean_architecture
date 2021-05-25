CREATE TABLE Cabcenter (
    CabID INT,
    City VARCHAR(255),
    IsAvailable BIT,
	PRIMARY KEY (CabID)
);

INSERT INTO Cabcenter (CabId, City, IsAvailable) VALUES (1, 'Amsterdam', 1);
INSERT INTO Cabcenter (CabId, City, IsAvailable) VALUES (2, 'Amsterdam', 0);
INSERT INTO Cabcenter (CabId, City, IsAvailable) VALUES (3, 'Utrecht', 1);
