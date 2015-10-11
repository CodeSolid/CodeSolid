use test;
DROP PROCEDURE if exists salesperson_by_city;
DELIMITER //
CREATE PROCEDURE salesperson_by_city
(IN City CHAR(20))
BEGIN  
  SELECT * from salespeople where city = City;
END //
DELIMITER ;

CALL salesperson_by_city('London')