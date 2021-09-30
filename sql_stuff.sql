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
-- BASIC SGGREGATION
SELECT (salary*months) AS earnings, COUNT(*)
FROM Employee
GROUP BY 1 
ORDER BY earnings DESC
LIMIT 1; 

Welcome to Facebook!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you would like to use for your interview,
simply choose it from the dropdown in the top bar.

----------
This table has 1 row per unique call.
(i.e. Assume it only includes calls between 2 individuals)

Table name: video_calls
+-----------------+---------------+---------------------------------------+
|  column         |  data_type    |  description                          |
+-----------------+---------------+---------------------------------------+
|  caller         |  BIGINT       |  FB ID of person who made the call    |
|  recipient      |  BIGINT       |  FB ID of person who was called       |
|  ds             |  STRING       |  date of the call                     |
|  call_id        |  BIGINT       |  each call has a unique ID            |
|  duration       |  DOUBLE       |  length of time of call, in seconds   |
+-----------------+---------------+---------------------------------------+

SAMPLE ROWS
caller   | recipient   | ds         | call_id | duration        
123      | 456         | 2019-01-01 | 4325    |  864.4   
032      | 789         | 2019-01-01 | 9395    |  263.7             
456      | 032         | 2019-01-01 | 0879    |  22.0
*/

Identify the 10 users who initiated / started the most video calls over the past 30 days

SELECT caller, count(*) as cnt
FROM video_calls
GROUP BY caller
WHERE ds INTERVAL(30)
ORDER BY cnt DESC
LIMIT 10;
Table name: dim_all_users
+------------------+---------------+---------------------------------------+
|  column          |  data_type    |  description                          |
+------------------+---------------+---------------------------------------+
|  user_id         |  BIGINT       |  user's FB ID                         |
|  age_bucket      |  STRING       |  user's age category                  |
|  country         |  STRING       |  country where the user is based      |
|  primary_os      |  STRING       |  main device operating system         |
|  dau_flag        |  TINYINT      |  1 for daily active users, else 0     |
|  ds              |  STRING       |  date of the record                   |
+------------------+---------------+---------------------------------------+

SAMPLE ROWS
user_id  | age_bucket  | country       | primary_os   | dau_flag   | ds     
123      | 25-34       | us            | android      |   1        | 2019-07-01
456      | 65+         | gb            | ios          |   1        | 2019-07-01
789      | 13-17       | fr            | ios          |   0        | 2019-07-01
032      | 45-54       | eg            | android      |   1        | 2019-07-01

What % of daily active users from France were on a video call yesterday?

SELECT caller
FROM video_calls
WHERE caller in (SELECT user_id as caller
FROM dim_all_users
WHERE country = 'fr' and dau_flag = 1)

