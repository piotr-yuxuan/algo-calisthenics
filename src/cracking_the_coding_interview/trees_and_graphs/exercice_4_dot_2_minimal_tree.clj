(ns cracking-the-coding-interview.trees-and-graphs.exercice-4-dot-2-minimal-tree
  (:require [clojure.string :as str]
            [clojure.test :refer [deftest is]]))

(defn increasing-order
  [a]
  (cond (< 2 (count a)) (vector (increasing-order (subvec a 0 (/ (count a) 2)))
                                (nth a (/ (count a) 2))
                                (increasing-order (subvec a (inc (/ (count a) 2)) (count a))))
        (= 2 (count a)) a
        (= 1 (count a)) (first a)))

(deftest increasing-order-test
  (is (= [[1 2 3] 4 [5 6]]
         (increasing-order [1 2 3 4 5 6]))))
