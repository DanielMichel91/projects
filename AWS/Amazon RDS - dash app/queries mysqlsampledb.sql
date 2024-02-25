/* Distribution of orders */
SELECT DATE_FORMAT(orderDate, '%M %Y'), COUNT(orderNumber) from orders GROUP BY YEAR(orderDate), MONTH(orderDate);

/* Busy Sales Reps */
SELECT COUNT(customerNumber) as numberCustomers, employeeNumber, firstName, lastName FROM employees INNER JOIN customers on salesRepEmployeeNumber = employeeNumber GROUP BY employeeNumber ORDER BY numberCustomers DESC LIMIT 10;

/* Best Customers */
SELECT COUNT(orderNumber) as numberOrders, customerNumber, customerName FROM customers INNER JOIN orders using (customerNumber) GROUP BY customerNumber ORDER BY numberOrders DESC LIMIT 10;

/* Kunden pro Land */
SELECT COUNT(customerNumber) as numberCustomers, country FROM customers GROUP BY country ORDER BY numberCustomers DESC;