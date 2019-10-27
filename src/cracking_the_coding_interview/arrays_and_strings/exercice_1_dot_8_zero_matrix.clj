(ns cracking-the-coding-interview.arrays-and-strings.exercice-1-dot-8-zero-matrix
  (:require [clojure.test :refer [deftest is]]))

(defn zero-i
  [matrix m i]
  (assoc matrix i (vec (repeat (inc m) 0))))

(defn zero-j
  [matrix m j]
  (reduce (fn [acc i]
            (assoc-in acc [i j] 0))
          matrix
          (range m)))

(defn zero-matrix-recur-fn
  [matrix m]
  (fn zero-matrix-recur [{:keys [output-matrix sites zeroed-i? zeroed-j?] :as args}]
    (let [[[i j]] sites]
      (cond (nil? sites) output-matrix

            (and (not (zeroed-i? i))
                 (zero? (get-in matrix [i j])))
            #(zero-matrix-recur (assoc args
                                  :output-matrix (zero-i output-matrix m i)
                                  :zeroed-i? (conj zeroed-i? i)))

            (and (not (zeroed-j? j))
                 (zero? (get-in matrix [i j])))
            #(zero-matrix-recur (assoc args
                                  :output-matrix (zero-j output-matrix m j)
                                  :zeroed-j? (conj zeroed-j? j)))

            :default
            #(zero-matrix-recur (assoc args :sites (next sites)))))))

(defn zero-matrix
  [matrix m n]
  (trampoline (zero-matrix-recur-fn matrix m)
              {:output-matrix matrix
               :sites (for [i (range m), j (range n)] [i j]) ;; lazy sequence
               :zeroed-i? #{}
               :zeroed-j? #{}}))

(deftest zero-matrix-test
  (let [object [[1 2 3 4]
                [5 6 7 8]
                [9 1 2 3]]]
    (is (= object (zero-matrix object 3 4))))
  (is (= (zero-matrix [[1 2 0 4]
                       [5 6 7 8]
                       [9 1 2 3]]
                      3
                      4)
         [[0 0 0 0]
          [5 6 0 8]
          [9 1 0 3]]))
  (is (= (zero-matrix [[1 0 3 4]
                       [5 6 0 8]
                       [9 1 2 3]]
                      3
                      4)
         [[0 0 0 0]
          [0 0 0 0]
          [9 0 0 3]])))
