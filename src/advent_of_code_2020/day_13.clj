(ns advent-of-code-2020.day-13
  (:require [clojure.test :refer [is with-test]]
            [clojure.java.io :as io]))

(def answer-part-1
  (->> [17 41 643 23 13 29 433 37 19]
       (map (juxt #(- % (mod 1014511 %)) identity))
       (sort-by first)
       first
       (apply *)))
