main :: IO ()
main = do
  input <- map (map (read :: String -> Int) . words) . lines <$> readFile "input.txt"
  (print . sum . map (fromEnum . safe)) input
  (print . sum . map (fromEnum . safe_p2)) input

safe :: [Int] -> Bool
safe report@(n1 : n2 : _) = all (`elem` vals) (zipWith (-) (drop 1 report) report)
  where
    vals = if n2 > n1 then [1, 2, 3] else [-1, -2, -3]

safe_p2 :: [Int] -> Bool
safe_p2 report = any safe possible
  where
    possible = [take i report ++ drop (i + 1) report | i <- [0 .. length report - 1]]
