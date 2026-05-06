INCLUDE PERFETTO MODULE slices.with_context;

CREATE PERFETTO VIEW fcp AS
WITH shared_sq_24 AS (
  SELECT *
  FROM thread_or_process_slice
),
shared_sq_8 AS (
  SELECT *
  FROM thread_or_process_slice
),
sq_25 AS (
  SELECT *
  FROM shared_sq_24
  WHERE name = 'firstContentfulPaint'
),
sq_12 AS (
  SELECT *
  FROM shared_sq_8
  WHERE category = 'blink.user_timing' AND name = 'TextInput'
),
sq_6823 AS (
  SELECT *
  FROM
  (WITH starts AS (SELECT * FROM sq_12),
       ends AS (SELECT * FROM sq_25),
       matched AS (
         SELECT
           starts.ts AS start_ts,
           (SELECT MIN(ends.ts) FROM ends WHERE ends.ts > starts.ts) AS end_ts
         FROM starts
       )
  SELECT
    start_ts AS ts,
    end_ts - start_ts AS dur
  FROM matched
  WHERE end_ts IS NOT NULL)

)

SELECT dur
FROM sq_6823
