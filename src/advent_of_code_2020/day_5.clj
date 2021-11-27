(ns advent-of-code-2020.day-5
  (:require [clojure.java.io :as io]
            [clojure.test :refer [is with-test]]
            [instaparse.core :as insta]))

(defn half-interval-length
  [lower upper]
  (-> upper
      (- lower)
      (/ 2)))

(with-test
  (defn interval-partitioning
    [[lower upper] direction]
    (let [pivot (->> upper
                     (half-interval-length lower)
                     (+ lower)
                     int)]
      (case direction
        (\F, \L) [lower pivot]
        (\B, \R) [(inc pivot) upper])))
  (is (= [16 20]
         (interval-partitioning [10 20] \B)
         (interval-partitioning [10 20] \R)))
  (is (= [10 15]
         (interval-partitioning [10 20] \F)
         (interval-partitioning [10 20] \L))))

(defn seat-id
  [[row column]]
  (+ (* 8 row) column))

(defn seat-coordinates
  [{:keys [row-directions column-directions]}]
  (let [[row _] (reduce interval-partitioning
                        [0 127]
                        row-directions)
        [column _] (reduce interval-partitioning
                           [0 7]
                           column-directions)]
    [row column]))

(def parser
  (insta/parser
    (slurp (io/resource "day-5-grammar.txt"))))

(with-test
  (defn answer
    []
    (->> (io/resource "day-5.txt")
         io/reader
         line-seq
         (map #(insta/parse parser %))
         (map #(into {} %))
         (map seat-coordinates)
         (map seat-id)
         (apply max)))
  (is (= (answer) 955)))
