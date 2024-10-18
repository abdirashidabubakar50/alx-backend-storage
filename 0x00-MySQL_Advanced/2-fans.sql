-- script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- column names are origin and nb_fans

SELECT origin AS origin,
    SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY Origin
    ORDER BY nb_fans DESC;