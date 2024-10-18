-- lists all bands with Glam rock as their main style,
-- ranked by their longevity
-- column names 
--    - band_name
--    - lifespan

SELECT band_name AS band_name,
    COALESCE(
    CASE
        WHEN split IS NULL THEN 2022 - formed
        ELSE split - formed
    END, 0) AS lifespan
    FROM 
        metal_bands
    WHERE
        style = 'Glam rock'
    ORDER BY
        lifespan DESC