use aiweb;


create table if not exists `member` (
     `member_id`   int  NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `identity_type` varchar(20) default'member',
    `account` varchar(100), 
    `password` varchar(100),
    `username` varchar(100),
    `email` varchar(100),
	`date` datetime);
)
select*from member;