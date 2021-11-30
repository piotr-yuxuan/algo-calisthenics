(ns advent-of-code-2020.day-9
  (:require [clojure.java.io :as io]
            [clojure.test :refer [is with-test]]))

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

(def input
  (->> (io/resource "day-9.txt")
       io/reader
       line-seq
       (map #(Long/parseLong %))))

(with-test
  (defn answer-part-1
    [input]
    (some (fn [window] (let [[items [result]] (split-at 25 window)] (when-not (->> (any-2-combinations items) (map (fn* [p1__891700#] (apply + p1__891700#))) (some (fn* [p1__891702#] (when (= result p1__891702#) p1__891702#)))) result))) (partition 26 1 input)))
  (is (= 22477624 (answer-part-1 input))))

(def invalid-number 22477624)

(defn largest-subvec-of-sum
  [v target-sum]
  (loop [left 0
         right (+ left 2)
         window-sum (reduce + (subvec v left right))]
    (cond (= window-sum target-sum)
          (subvec v left right)

          (< window-sum target-sum)
          (recur left
                 (inc right)
                 (+ window-sum (nth v right)))

          (> window-sum target-sum)
          (recur (inc left)
                 right
                 (- window-sum (nth v left))))))

(with-test
  (defn answer-part-2
    [input]
    (let [v (largest-subvec-of-sum (vec input) invalid-number)]
      (+ (apply min v)
         (apply max v))))
  (is (= 2980044 (answer-part-2 input))))
