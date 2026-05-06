INCLUDE PERFETTO MODULE slices.with_context;
INCLUDE PERFETTO MODULE viz.slices;





CREATE PERFETTO VIEW fcp AS
WITH shared_sq_24 AS (
  SELECT *
  FROM thread_or_process_slice
),
sq_25 AS (
  SELECT *
  FROM shared_sq_24
  WHERE name = 'firstContentfulPaint'
),
sq_6899 AS (
  SELECT *
  FROM (
    SELECT id, ts, dur, category, name, utid, thread_91utid_93_46tid, thread_91utid_93_46name, upid, process_91upid_93_46pid, process_91upid_93_46name, track_id, track_91track_id_93_46name, print_args_40arg_set_id_41, arg_set_id
    FROM (
      SELECT
            _viz_slices_for_ui_table_0.id AS id,
        _viz_slices_for_ui_table_0.ts AS ts,
        _viz_slices_for_ui_table_0.dur AS dur,
        _viz_slices_for_ui_table_0.category AS category,
        _viz_slices_for_ui_table_0.name AS name,
        _viz_slices_for_ui_table_0.utid AS utid,
        thread_1.tid AS thread_91utid_93_46tid,
        thread_1.name AS thread_91utid_93_46name,
        _viz_slices_for_ui_table_0.upid AS upid,
        process_2.pid AS process_91upid_93_46pid,
        process_2.name AS process_91upid_93_46name,
        _viz_slices_for_ui_table_0.track_id AS track_id,
        track_3.name AS track_91track_id_93_46name,
        __intrinsic_arg_set_to_json(_viz_slices_for_ui_table_0.arg_set_id) AS print_args_40arg_set_id_41,
        _viz_slices_for_ui_table_0.arg_set_id AS arg_set_id
          FROM _viz_slices_for_ui_table AS _viz_slices_for_ui_table_0
          LEFT JOIN thread AS thread_1 ON thread_1.id = _viz_slices_for_ui_table_0.utid
      LEFT JOIN process AS process_2 ON process_2.id = _viz_slices_for_ui_table_0.upid
      LEFT JOIN track AS track_3 ON track_3.id = _viz_slices_for_ui_table_0.track_id
          WHERE
       _viz_slices_for_ui_table_0.name LIKE 'Navigation: %' AND
      _viz_slices_for_ui_table_0.name NOT LIKE 'Navigation: chrome%' AND
      _viz_slices_for_ui_table_0.name NOT LIKE 'Navigation: about:blank' AND
      _viz_slices_for_ui_table_0.name NOT LIKE 'Navigation: data%' AND
      _viz_slices_for_ui_table_0.name NOT LIKE 'Navigation: https://example.com/' AND
      _viz_slices_for_ui_table_0.name NOT LIKE 'Navigation: https://static.ddg.local/Application/NewTabPage/Html/index.html'
    ))
),
sq_6895 AS (
  SELECT *
  FROM
  (WITH starts AS (SELECT * FROM sq_6899),
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
SELECT *
FROM sq_6895
