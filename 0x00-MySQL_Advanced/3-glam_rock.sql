-- lists all bands with Glam rock as their main style,
-- ranked by their longevity
-- column names 
--    - band_name
--    - lifespan

SELECT band_name,
    CASE
        WHEN formed > 2022 THEN 0
        WHEN split IS NULL THEN 2022 - formed
        ELSE GREATEST(split - formed, 0)
    END  AS lifespan
FROM 
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;