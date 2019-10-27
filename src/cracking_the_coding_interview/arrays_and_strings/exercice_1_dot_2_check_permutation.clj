(ns cracking-the-coding-interview.arrays-and-strings.exercice-1-dot-2-check-permutation
  (:require [clojure.test :refer [deftest is]]))

(defn inc-count
  [[i & s] seen?]
  (or (and i #(inc-count s (assoc! seen? i (inc (get seen? i 0))))) seen?))

(defn dec-count
  [[i & s] seen?]
  (let [c (get seen? i)]
    (or (nil? i) (and (not (#{0 nil} c)) #(dec-count s (assoc! seen? i (dec c)))))))

(defn check-permutation
  [left right]
  (->> (transient {})
       (trampoline inc-count left)
       (trampoline dec-count right)
       (and (= (count left) (count right)))))

(def response check-permutation)

(deftest response-test
  (is (response "" ""))
  (is (not (response "a" "")))
  (is (not (response "" "a")))
  (is (not (response "aesd" "assd")))
  (is (response "yolo" "yolo")))
