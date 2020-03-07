USE web_ise;
CREATE TABLE users(
uname VARCHAR(30) PRIMARY KEY,
pword VARCHAR(30) NOT NULL,
firstname VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL,
email VARCHAR(50) NOT NULL,
address VARCHAR(200) NOT NULL,
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) 
SELECT * FROM users;
insert into users(uname,pword,firstname,lastname,email,address)
values('1','11','mony','Sebin','M@o.com','tdpa'),('2','22','Sony','Bastian','S@o.com','mltm'),('3','33','Rony','Binu','R@o.com','ekm');




