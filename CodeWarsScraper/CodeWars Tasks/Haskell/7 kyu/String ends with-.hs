module StringsEndsWith (solution) where

solution :: String -> String -> Bool
solution str1 str2 = str2 == drop ((length str1) - (length str2)) str1