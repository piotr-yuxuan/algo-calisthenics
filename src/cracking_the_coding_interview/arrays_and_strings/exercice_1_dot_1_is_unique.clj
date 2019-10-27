(ns cracking-the-coding-interview.arrays-and-strings.exercice-1-dot-1-is-unique
  (:require [clojure.test :refer [deftest is testing]]))

(defn is-unique?
  [seen? [i & s]]
  (cond (seen? i) false
        (empty? s) true
        (conj! seen? i) #(is-unique? seen? s)))

(def response #(trampoline is-unique? (transient #{}) %))

(deftest response-test
  (is (= (response "") true))
  (is (= (response "a") true))
  (is (= (response "aa") false))
  (is (= (response "ab") true))
  (is (= (response "aba") false))
  (is (= (response "abcbd") false)))

(defn merge-coll
  [f ret [left right]]
  (cond (< (count right) (count left)) #(merge-coll f ret [right left])
        (empty? left) (into ret right)
        (empty? right) (into left ret)
        (<= (f (first left)) (f (first right))) #(merge-coll f (conj ret (first left)) (vector (rest left) right))
        (<= (f (first right)) (f (first left))) #(merge-coll f (conj ret (first right)) (vector left (rest right)))))

(defn divide-coll
  [f c]
  (->> c
       (partition-all (/ (count c) 2))
       (map (partial divide-coll f))
       (trampoline merge-coll f [])
       lazy-seq
       (if (<= (count c) 1) c)))

(defn merge-sort
  ([c] (divide-coll int c))
  ([f c] (divide-coll f c)))

(deftest merge-sort-test
  (let [given (vector [0 0]
                      [3 3]
                      [1 2]
                      [3 1]
                      [4 4])
        f (comp int first)
        expected (vector [0 0]
                         [1 2]
                         [3 3]
                         [3 1]
                         [4 4])
        actual (merge-sort f given)]
    (is (not (realized? actual)))
    (is (= actual expected))
    (is (= actual (sort-by f given))))
  (let [expected (range 10)
        given (shuffle expected)
        actual (merge-sort given)]
    (is (not (realized? actual)))
    (is (= expected actual))
    (is (= actual (sort given)))))

(defn repeated
  [s]
  (->> (merge-sort s)
       (partition 2 1)
       (some #(apply = %))))

(def response-1 (complement repeated))

(deftest response-1-test
  (is (= (response-1 "") true))
  (is (= (response-1 "a") true))
  (is (= (response-1 "aa") false))
  (is (= (response-1 "ab") true))
  (is (= (response-1 "aba") false))
  (is (= (response-1 "abcbd") false)))
