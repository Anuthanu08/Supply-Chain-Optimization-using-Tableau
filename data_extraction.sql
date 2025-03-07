-- Extract inventory data
SELECT product_id, product_name, category, stock_level, reorder_level, last_restocked_date 
FROM inventory;

-- Extract sales data
SELECT product_id, sales_date, units_sold, revenue 
FROM sales
WHERE sales_date BETWEEN '2024-01-01' AND '2024-12-31';

-- Join inventory and sales data
SELECT i.product_id, i.product_name, s.sales_date, s.units_sold, i.stock_level
FROM inventory i
JOIN sales s ON i.product_id = s.product_id;
