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
