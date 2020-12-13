(ns advent-of-code-2020.main
  (:require
    [advent-of-code-2020.day-1 :as day-1]
    [advent-of-code-2020.day-2 :as day-2]
    [advent-of-code-2020.day-3 :as day-3]
    [advent-of-code-2020.day-4 :as day-4]
    [advent-of-code-2020.day-5 :as day-5]
    [advent-of-code-2020.day-6 :as day-6]
    [advent-of-code-2020.day-7 :as day-7]))

(defn -main
  []
  (println :day-1 (day-1/answer))
  (println :day-2 (day-2/answer))
  (println :day-3 (day-3/answer))
  (println :day-4 (day-4/answer))
  (println :day-5 (day-5/answer))
  (println :day-6 (day-6/answer))
  (println :day-7/part-1 (day-7/answer-part-1))
  (println :day-7/part-2 (day-7/answer-part-2)))
