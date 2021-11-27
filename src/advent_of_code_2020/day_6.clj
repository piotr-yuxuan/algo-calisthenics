(ns advent-of-code-2020.day-6
  (:require [clojure.java.io :as io]
            [clojure.set :as set]
            [clojure.test :refer [is with-test]]))

(with-test
  (defn group-lines-paragraph
    [coll]
    (->> coll
         (partition-by #{""})
         (remove #{'("")})))
  (is (= ['("abc") '("a" "b" "c") '("ab" "ac") '("a" "a" "a" "a") '("b")]
         (->> (io/resource "day-6-example.txt")
              io/reader
              line-seq
              group-lines-paragraph))))

(with-test
  (defn answer
    []
    (->> (line-seq (io/reader (io/resource "day-6.txt")))
         group-lines-paragraph
         (map #(map set %))
         (map #(apply set/union %))
         (map count)
         (reduce +)))
  (is (= (answer) 6885)))
