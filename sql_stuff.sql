SELECT t.vendor_id, t.invoice_number, max(t.invoice_total) AS mx
FROM (
SELECT vendor_id, invoice_number, invoice_total
FROM invoices
order by invoice_number, invoice_total desc) t
GROUP BY vendor_id, invoice_number
LIMIT 10;


ROW_NUMBER() OVER (PARTITION BY DocumentID ORDER BY DateCreated DESC) AS rn



SELECT *
FROM ( 
    SELECT *,
    RANK() OVER (PARTITION BY vendor_id ORDER BY invoice_total DESC) AS rn
    FROM invoices) ranks
WHERE rn = 1;


-- Bike Sharing 
/*
SELECT start_terminal,
       duration_seconds,
       SUM(duration_seconds) OVER
         (PARTITION BY start_terminal) AS sum_terminal_total,
YOU CAN DO MATH ON A PARTITION BUT YOU CAN'T USE THE RESULTS OF ONE IN THE SAME QUERY
      duration_seconds/SUM(duration_seconds) OVER 
        (PARTITION BY start_terminal)*100 AS percent_terminal_total 

  FROM tutorial.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'
 ORDER BY 1, 4 DESC # Notice how they use the indeces to name columns
*/
 