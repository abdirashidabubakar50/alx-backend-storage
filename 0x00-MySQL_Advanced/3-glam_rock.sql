-- lists all bands with Glam rock as their main style,
-- ranked by their longevity
-- column names 
--    - band_name
--    - lifespan

SELECT 
    band_name,
        CASE 
            WHEN formed IS NULL THEN 0 -- No formation year available
            WHEN split IS NULL THEN 2022 - formed -- Band still active
            ELSE split - formed -- Band split
        END AS lifespan
FROM
    metal_bands
WHERE 
    style LIKE '%Glam rock%'
ORDER BY 
    lifespan DESC;
