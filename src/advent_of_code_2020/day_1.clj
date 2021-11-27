(ns advent-of-code-2020.day-1
  (:require [clojure.java.io :as io]
            [clojure.test :refer [deftest is testing with-test]]
            [malli.core :as m]
            [malli.transform :as transform]))

(def Entry
  int?)

(with-test
  (defn any-2-combinations
    "All the ways of taking 2 different elements from items."
    [[x & items]]
    (when (seq items)
      (lazy-cat (map #(do [x %])
                     items)
                (any-2-combinations items))))
  (is (= [[1 2] [1 3] [1 4] [2 3] [2 4] [3 4]]
         (any-2-combinations [1 2 3 4]))))

(def target-value 2020)

(with-test
  (defn answer
    []
    (->> (io/resource "day-1.txt")
         io/reader
         line-seq
         shuffle
         (map (m/decoder Entry (transform/string-transformer)))
         any-2-combinations
         (some #(when (= target-value
                         (reduce + %))
                  %))
         (apply *)))
  (is (= 618144 (answer))))
