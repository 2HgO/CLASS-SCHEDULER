create database DBMS;
use DBMS;

create Table Programs(
    Program ENUM('CT','CS-A','CS-B','CIS') not null unique
);

create Table Student(
    ID int(10) unsigned not null auto_increment Primary Key,
    Matric char(7) unique,
    FName varchar(20) not null default '',
    LName varchar(20) not null default '',
    Program ENUM('CT','CS-A','CS-B','CIS') not null,
    Foreign Key (Program) references Programs(Program)
);

create Table Lecturer(
    ID int(10) unsigned not null auto_increment Primary Key,
    LecturerID char(5) unique,
    FName varchar(20) not null default '',
    LName varchar(20) not null default ''
);

create Table Courses(
    CourseID char(7) not null unique,
    Code1 char(4) not null,
    Code2 char(3) not null,
    Units ENUM('1','2','3','6') not null,
    LecturerID char(5) not null,
    Foreign Key (LecturerID) references Lecturer(LecturerID)
);

create Table CourseTaken(
    CourseID char(7) not null,
    Program ENUM('CT','CS-A','CS-B','CIS') not null,
    Foreign Key (CourseID) references Courses(CourseID),
    Foreign Key (Program) references Programs(Program)
);

create Table Venues(
    Venue ENUM('CIT','OEL','E102','E202','F104','F204','NH') not null unique,
    Size int(10) unsigned not null
);

create Table Schedule(
    CourseID char(7) not null,
    Program ENUM('CT','CS-A','CS-B','CIS') not null,
    Venue ENUM('CIT','OEL','E102','E202','F104','F204','NH') not null,
    Day ENUM('Monday','Tuesday','Wednesday','Thursday','Friday') not null,
    StartTime Time not null,
    StopTime Time not null,
    Foreign Key (CourseID) references Courses(CourseID),
    Foreign Key (Program) references Programs(Program),
    Foreign Key (Venue) references Venues(Venue)
);

delimiter //

CREATE PROCEDURE GenMatric()
BEGIN
UPDATE Student SET Matric = concat("15","/","000",ID) where ID < 10;
UPDATE Student SET Matric = concat("15","/","00",ID) where ID >= 10;
END

//

CREATE PROCEDURE GenLecID()
BEGIN
UPDATE Lecturer SET LecturerID = concat("CS","-","0",ID) where ID < 10;
UPDATE Lecturer SET LecturerID = concat("CS","-",ID) where ID >= 10;
END

//

CREATE TRIGGER COU BEFORE INSERT ON Courses
FOR EACH ROW
BEGIN
SET NEW.CourseID = concat(NEW.Code1,NEW.Code2);
END

//
delimiter ;

INSERT into Programs values
('CT'),
('CS-A'),
('CS-B'),
('CIS');

INSERT into Student values

(NULL,NULL,'Oghogho','Odemwingie','CT'),
(NULL,NULL,'Airat','Anifowose','CT'),
(NULL,NULL,'Jessica','Iyorchir','CT'),
(NULL,NULL,'Mawuena','Hayes','CT'),
(NULL,NULL,'Diys','Oyetorola','CT'),
(NULL,NULL,'Osamola','Peter','CT'),
(NULL,NULL,'Atin','Tari','CT'),
(NULL,NULL,'Oyakhilome','Idialu','CT'),
(NULL,NULL,'Oduyomi','Damilare','CT'),
(NULL,NULL,'Odira','Daniel','CT'),
(NULL,NULL,'Paul','Sochi','CT'),
(NULL,NULL,'Alex','Kedi','CT'),
(NULL,NULL,'Ademeso','Olayide','CT'),
(NULL,NULL,'Papka','Dziram','CT'),
(NULL,NULL,'Chidebe','Justice','CT'),
(NULL,NULL,'Iyamu','Ilunose','CT'),
(NULL,NULL,'Iheme','Chiazam','CT'),
(NULL,NULL,'Adeh','Loveth','CT'),
(NULL,NULL,'Emir','Emmanuel','CT'),
(NULL,NULL,'Peter','Ebube','CT'),
(NULL,NULL,'Olasimbo','Temilorun','CT'),
(NULL,NULL,'Onamade','Okikioluwa','CT'),
(NULL,NULL,'Olagunju','Damilola','CT'),
(NULL,NULL,'James','Lucia','CT'),
(NULL,NULL,'Palmer','William','CT'),
(NULL,NULL,'Agboma','Festus','CT'),
(NULL,NULL,'Jibirin','Yaro','CT'),
(NULL,NULL,'Yohanna','Esther','CT'),
(NULL,NULL,'Dalamu','Daniella','CT'),
(NULL,NULL,'Eniayo','Adediran','CS-A'),
(NULL,NULL,'Eniayo','Adediran','CS-A'),
(NULL,NULL,'Kemi','Adekaiyaja','CS-A'),
(NULL,NULL,'Sharon','Adetomi','CS-A'),
(NULL,NULL,'Fola','Famuyiwa','CS-A'),
(NULL,NULL,'Funmi','Koyi','CS-A'),
(NULL,NULL,'Muyiwa','Adesanya','CS-A'),
(NULL,NULL,'Tobi','Nifemi','CS-A'),
(NULL,NULL,'Tito','Greene','CS-A'),
(NULL,NULL,'Jennifer','Ade','CS-A'),
(NULL,NULL,'Dami','Gbuyiro','CS-A'),
(NULL,NULL,'Anu','Adekaiyaja','CS-A'),
(NULL,NULL,'Joy','Ilenreh','CS-A'),
(NULL,NULL,'Solomon','Hayes','CS-A'),
(NULL,NULL,'Femi','Branch','CS-A'),
(NULL,NULL,'Tolu','Adekola','CS-A'),
(NULL,NULL,'Bola','Oyelowo','CS-A'),
(NULL,NULL,'Mide','Onasanya','CS-A'),
(NULL,NULL,'Sam','Arhore','CS-A'),
(NULL,NULL,'Pero','Adekunle','CS-A'),
(NULL,NULL,'Peace','Igwe','CS-A'),
(NULL,NULL,'Sam','Arhore','CS-A'),
(NULL,NULL,'Peter','Pan','CS-B'),
(NULL,NULL,'Femi','Oyebayo','CS-B'),
(NULL,NULL,'Kike','Tolufashe','CS-B'),
(NULL,NULL,'Fauziya','Shuaib','CS-B'),
(NULL,NULL,'Zara','Nnmadu','CS-B'),
(NULL,NULL,'David','Okaka','CS-B'),
(NULL,NULL,'Kamsy','Nnuabe','CS-B'),
(NULL,NULL,'Rita','Omozuafoh','CS-B'),
(NULL,NULL,'Ugo','Osinachi','CS-B'),
(NULL,NULL,'Sotonye','Johnson','CS-B'),
(NULL,NULL,'Ebuka','David','CS-B'),
(NULL,NULL,'Kelechi','Oriaku','CS-B'),
(NULL,NULL,'Chelsea','Hippolite','CS-B'),
(NULL,NULL,'Esther','Owens','CS-B'),
(NULL,NULL,'Hanifa','Suleiman','CS-B'),
(NULL,NULL,'Labra','Ambo','CS-B'),
(NULL,NULL,'Bakarat','Soaga','CS-B'),
(NULL,NULL,'Hafsat','Lamee','CS-B'),
(NULL,NULL,'Anita','Abiona','CS-B'),
(NULL,NULL,'Grace','Dara','CS-B'),
(NULL,NULL,'Racheal','Simi','CS-B'),
(NULL,NULL,'Daniel','Olarichy','CS-B'),
(NULL,NULL,'Dalton','Sirkay','CS-B'),
(NULL,NULL,'Taiwo','Ferrari','CS-B'),
(NULL,NULL,'Tony','Stark','CIS'),
(NULL,NULL,'Benjamin','Franklin','CIS'),
(NULL,NULL,'Bruce','Banner','CIS'),
(NULL,NULL,'Bruce','Wayne','CIS'),
(NULL,NULL,'Idowu','Ini','CIS'),
(NULL,NULL,'Shittu','Opeyemi','CIS'),
(NULL,NULL,'Ekeke','Paul','CIS'),
(NULL,NULL,'Nwakankwo','John','CIS'),
(NULL,NULL,'Alabi','Tope','CIS'),
(NULL,NULL,'Afolabi','Emmnauel','CIS'),
(NULL,NULL,'Ebo','Praise','CIS'),
(NULL,NULL,'Orijogo','Propsper','CIS'),
(NULL,NULL,'Akpoyibo','Emmanuel','CIS'),
(NULL,NULL,'Dan','Utibe','CIS'),
(NULL,NULL,'Akinsanya','Adeoluwa','CIS'),
(NULL,NULL,'Ejieji','Dozie','CIS'),
(NULL,NULL,'Agugua','Kene','CIS'),
(NULL,NULL,'Yomi','Dotun','CIS'),
(NULL,NULL,'Ayodele','Tobi','CIS'),
(NULL,NULL,'Okasor','Faruk','CIS');

INSERT into Lecturer values
(NULL,NULL,'Chloe','Bennet'),
(NULL,NULL,'Steve','Rogers'),
(NULL,NULL,'Maria','Hill'),
(NULL,NULL,'Nick','Fury'),
(NULL,NULL,'Sheldon','Cooper'),
(NULL,NULL,'Mutiu','Ayodele');

CALL GenMatric();
CALL GenLecID();

INSERT into Courses values
(NULL,'COSC','401','2','CS-01'),
(NULL,'COSC','403','3','CS-02'),
(NULL,'COSC','405','3','CS-05'),
(NULL,'COSC','409','2','CS-03'),
(NULL,'COSC','423','3','CS-02'),
(NULL,'COSC','431','3','CS-04'),
(NULL,'ELCT','405','2','CS-05'),
(NULL,'ELCT','409','3','CS-06'),
(NULL,'INSY','401','3','CS-03'),
(NULL,'INSY','405','3','CS-04');

INSERT into CourseTaken values
('ELCT405','CT'),
('INSY405','CT'),
('COSC403','CT'),
('COSC405','CT'),
('COSC423','CT'),
('COSC401','CT'),
('ELCT409','CT'),
('INSY401','CT'),
('INSY405','CS-A'),
('COSC403','CS-A'),
('COSC405','CS-A'),
('COSC423','CS-A'),
('COSC401','CS-A'),
('INSY401','CS-A'),
('COSC431','CS-A'),
('COSC409','CS-A'),
('INSY405','CS-B'),
('COSC403','CS-B'),
('COSC405','CS-B'),
('COSC423','CS-B'),
('COSC401','CS-B'),
('INSY401','CS-B'),
('COSC431','CS-B'),
('COSC409','CS-B'),
('INSY405','CIS'),
('COSC403','CIS'),
('COSC405','CIS'),
('COSC423','CIS'),
('COSC401','CIS'),
('INSY401','CIS');

INSERT into Venues values
('CIT',40),
('E202',30),
('E102',20),
('F104',25),
('OEL',30),
('NH',35),
('F204',20);

INSERT into Schedule values
('ELCT405','CT','OEL','Monday','07:00:00','09:00:00'),
('INSY405','CT','F204','Thursday','09:00:00','10:00:00'),
('COSC403','CS-A','E102','Tuesday','09:00:00','11:00:00'),
('INSY405','CS-B','CIT','Monday','10:00:00','11:00:00'),
('INSY405','CS-A','F104','Friday','11:00:00','13:00:00'),
('COSC403','CT','F204','Thursday','11:00:00','13:00:00'),
('INSY405','CIS','E102','Monday','07:00:00','09:00:00'),
('COSC405','CS-B','F104','Friday','14:00:00','16:00:00'),
('COSC409','CS-A','NH','Monday','14:00:00','16:00:00'),
('ELCT405','CT','OEL','Wednesday','16:00:00','18:00:00'),
('INSY401','CS-A','E102','Monday','16:00:00','18:00:00'),
('COSC401','CS-B','E202','Tuesday','07:00:00','09:00:00');

CREATE view CS_A_Schedule 
AS
select Student.Program,
Lecturer.LecturerID,
Courses.CourseID,
Schedule.Day,
Schedule.Venue,
Schedule.StartTime,
Schedule.StopTime 
from (((Lecturer 
inner join Courses on
Lecturer.LecturerID=Courses.LecturerID)
inner join Schedule on
Schedule.CourseID=Courses.CourseID)
right join Student on
Schedule.Program=Student.Program)
where Student.Program = 'CS-A'
group by Student.Program,Courses.CourseID,Schedule.Day,Schedule.StartTime
order by Schedule.StartTime;

CREATE view CS_B_Schedule 
AS
select Student.Program,
Lecturer.LecturerID,
Courses.CourseID,
Schedule.Day,
Schedule.Venue,
Schedule.StartTime,
Schedule.StopTime 
from (((Lecturer 
inner join Courses on
Lecturer.LecturerID=Courses.LecturerID)
inner join Schedule on
Schedule.CourseID=Courses.CourseID)
right join Student on
Schedule.Program=Student.Program)
where Student.Program = 'CS-B'
group by Student.Program,Courses.CourseID,Schedule.Day,Schedule.StartTime
order by Schedule.StartTime;

CREATE view CIS_Schedule 
AS
select Student.Program,
Lecturer.LecturerID,
Courses.CourseID,
Schedule.Day,
Schedule.Venue,
Schedule.StartTime,
Schedule.StopTime 
from (((Lecturer 
inner join Courses on
Lecturer.LecturerID=Courses.LecturerID)
inner join Schedule on
Schedule.CourseID=Courses.CourseID)
right join Student on
Schedule.Program=Student.Program)
where Student.Program = 'CIS'
group by Student.Program,Courses.CourseID,Schedule.Day,Schedule.StartTime
order by Schedule.StartTime;

CREATE view CT_Schedule 
AS
select Student.Program,
Lecturer.LecturerID,
Courses.CourseID,
Schedule.Day,
Schedule.Venue,
Schedule.StartTime,
Schedule.StopTime 
from (((Lecturer 
inner join Courses on
Lecturer.LecturerID=Courses.LecturerID)
inner join Schedule on
Schedule.CourseID=Courses.CourseID)
right join Student on
Schedule.Program=Student.Program)
where Student.Program = 'CT'
group by Student.Program,Courses.CourseID,Schedule.Day,Schedule.StartTime
order by Schedule.StartTime;